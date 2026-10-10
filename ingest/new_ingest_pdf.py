"""
Baca file markdown hasil chunking -> buat tabel (DDL) -> embed dengan gemini-embedding-2
-> simpan ke Supabase Postgres (tabel: knowledge_rag).

Install : pip install google-genai "psycopg[binary]"
Env     : GEMINI_API_KEY
          SUPABASE_DB_URL  (Supabase > Project Settings > Database > Connection string,
                            format: postgresql://postgres.xxxx:PASSWORD@host:5432/postgres)
Jalankan: python ingest_chunks.py --print-ddl   (tampilkan DDL saja)
          python ingest_chunks.py --dry-run     (cek parsing saja, tanpa API/DB)
          python ingest_chunks.py               (buat tabel + embed + insert)
"""
import hashlib
import math
import os
import re
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SOURCE = ("SJ-20250722111610-002-ZXEPS E6N1 R01M201 DC Power System "
          "Quick Installation Guide (Sinar Mas Group&XL).pdf")
DOC_HASH = hashlib.sha256(SOURCE.encode("utf-8")).hexdigest()

MD_PATH = Path(os.getenv("CHUNKS_MD", "ingest/ZXEPS_E6N1_chunks.md"))
TABLE = "knowledge_rag"
MODEL = os.getenv("EMBED_MODEL", "gemini-embedding-2")
DIM = int(os.getenv("EMBED_DIM", "1536"))      # dipakai juga untuk vector(N) di DDL
EMBED_WITH_HEADING = True                      # heading ikut di-embed, content tetap isi chunk saja
BATCH_INSERT = 20


# ----------------------------------------------------------------------------
# DDL
# ----------------------------------------------------------------------------
def build_ddl(table: str = TABLE, dim: int = DIM) -> str:
    assert re.fullmatch(r"[a-z_][a-z0-9_]*", table), "nama tabel tidak valid"
    return f"""
create extension if not exists vector with schema extensions;

create table if not exists public.{table} (
  id          bigint generated always as identity primary key,
  source      text        not null,
  doc_hash    text        not null,
  page        int,
  chunk_index int         not null,
  chunk_type  text        check (chunk_type in ('text', 'tabel', 'image')),
  content     text        not null,
  metadata    jsonb       not null default '{{}}'::jsonb,
  embedding   vector({dim}),
  created_at  timestamptz not null default now(),
  unique (doc_hash, chunk_index)
);

create index if not exists {table}_embedding_idx
  on public.{table} using hnsw (embedding vector_cosine_ops);
"""


def ensure_schema(conn):
    with conn.cursor() as cur:
        cur.execute(build_ddl())
    conn.commit()
    print(f"Tabel public.{TABLE} siap (vector({DIM})).")


# ----------------------------------------------------------------------------
# Parsing markdown
# ----------------------------------------------------------------------------
CHUNK_RE = re.compile(
    r"^## Chunk (\d+)\n"
    r"- \*\*Dokumen:\*\* ([^\n]*)\n"
    r"- \*\*Halaman:\*\* ([^\n]*)\n"
    r"- \*\*Tipe:\*\* ([^\n]*)\n"
    r"- \*\*Heading:\*\* ([^\n]*)\n\n"
    r"(.*?)\n\n---\n",
    re.M | re.S,
)


def map_chunk_type(tipe: str) -> str:
    """teks / teks+gambar / teks+tabel ... -> text ; diawali tabel -> tabel ; hanya gambar -> image"""
    parts = [p.strip() for p in tipe.split("+")]
    if parts[0] == "tabel":
        return "tabel"
    if parts == ["gambar"]:
        return "image"
    return "text"


def parse_chunks(md_text: str):
    rows = []
    for m in CHUNK_RE.finditer(md_text):
        num, dokumen, halaman, tipe, heading, body = m.groups()
        pages = [int(x) for x in re.findall(r"\d+", halaman)]
        rows.append({
            "chunk_index": int(num),
            "page": pages[0],
            "chunk_type": map_chunk_type(tipe),
            "content": body.strip(),
            "metadata": {
                "heading": heading.strip(),
                "page_start": pages[0],
                "page_end": pages[-1],
                "page_label": halaman.strip(),
                "tipe_asli": tipe.strip(),
                "has_table": "tabel" in tipe,
                "has_image": "gambar" in tipe,
                "file_name": dokumen.strip(),
            },
        })
    return rows


# ----------------------------------------------------------------------------
# Embedding
# ----------------------------------------------------------------------------
def l2_normalize(v):
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def embed_one(client, types, text, retries=5):
    # 1 chunk per request supaya satu teks = satu vektor (tidak digabung)
    for attempt in range(retries):
        try:
            res = client.models.embed_content(
                model=MODEL,
                contents=text,
                config=types.EmbedContentConfig(output_dimensionality=DIM),
            )
            assert len(res.embeddings) == 1, "Jumlah embedding tidak sesuai"
            vec = list(res.embeddings[0].values)
            assert len(vec) == DIM, f"Dimensi {len(vec)} != {DIM}"
            # vektor hasil pemotongan dimensi (MRL) perlu dinormalisasi
            return l2_normalize(vec) if DIM != 3072 else vec
        except Exception as e:
            wait = 2 ** attempt
            print(f"  gagal ({e}); coba lagi dalam {wait}s")
            time.sleep(wait)
    raise RuntimeError("Embedding gagal setelah beberapa percobaan")


# ----------------------------------------------------------------------------
# Insert
# ----------------------------------------------------------------------------
def upsert_rows(conn, rows):
    from psycopg.types.json import Jsonb
    sql = f"""
        insert into public.{TABLE}
          (source, doc_hash, page, chunk_index, chunk_type, content, metadata, embedding)
        values (%s, %s, %s, %s, %s, %s, %s, %s::vector)
        on conflict (doc_hash, chunk_index) do update set
          source = excluded.source,
          page = excluded.page,
          chunk_type = excluded.chunk_type,
          content = excluded.content,
          metadata = excluded.metadata,
          embedding = excluded.embedding
    """
    with conn.cursor() as cur:
        for i in range(0, len(rows), BATCH_INSERT):
            batch = rows[i:i + BATCH_INSERT]
            cur.executemany(sql, [
                (r["source"], r["doc_hash"], r["page"], r["chunk_index"], r["chunk_type"],
                 r["content"], Jsonb(r["metadata"]),
                 "[" + ",".join(repr(x) for x in r["embedding"]) + "]")
                for r in batch
            ])
            print(f"insert {min(i + BATCH_INSERT, len(rows))}/{len(rows)}")
    conn.commit()


def main():
    flags = set(sys.argv[1:])
    dry_run = "--dry-run" in flags       # hanya parsing, tanpa embed/DB
    print_ddl = "--print-ddl" in flags   # tampilkan DDL lalu keluar
    unknown = flags - {"--dry-run", "--print-ddl"}
    if unknown:
        sys.exit(f"Argumen tidak dikenal: {', '.join(sorted(unknown))}")

    if print_ddl:
        print(build_ddl())
        return

    rows = parse_chunks(MD_PATH.read_text(encoding="utf-8"))
    print(f"{len(rows)} chunk terbaca dari {MD_PATH}")
    print(f"doc_hash (sha256 dari source): {DOC_HASH}")
    if dry_run:
        from collections import Counter
        print(Counter(r["chunk_type"] for r in rows))
        for r in rows[:3]:
            print(r["chunk_index"], r["page"], r["chunk_type"], r["metadata"]["heading"])
        return

    import psycopg
    from google import genai
    from google.genai import types

    gclient = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    with psycopg.connect(os.environ["SUPABASE_DB_URL"]) as conn:
        ensure_schema(conn)

        out = []
        for i, r in enumerate(rows, 1):
            text = f'{r["metadata"]["heading"]}\n\n{r["content"]}' if EMBED_WITH_HEADING else r["content"]
            vec = embed_one(gclient, types, text)
            out.append({**r, "source": SOURCE, "doc_hash": DOC_HASH, "embedding": vec})
            print(f"[{i}/{len(rows)}] chunk {r['chunk_index']} di-embed")

        upsert_rows(conn, out)
    print("Selesai.")


if __name__ == "__main__":
    main()