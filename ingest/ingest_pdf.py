#!/usr/bin/env python3
"""
ingest_pdf.py
-------------
Ingest PDF (teks + tabel + gambar) -> embedding Google Gemini -> Supabase Postgres (pgvector).

Pemakaian:
    Ubah PDF_PATH / QUERY di bagian paling bawah file ini, lalu jalankan:
        python ingest_pdf.py
    atau impor dari kode lain:
        from ingest_pdf import ingest, search
        ingest("dokumen.pdf")
        search("berapa total pendapatan tahun 2025?", k=5)

Alur:
    1. Teks   : diambil per blok (di luar area tabel), lalu dipecah jadi chunk ber-overlap.
    2. Tabel  : dideteksi PyMuPDF, diubah ke markdown, tabel besar dipecah per baris
                (header diulang di tiap chunk).
    3. Gambar : diekstrak, di-caption oleh model Gemini (grafik/diagram/foto -> teks),
                lalu di-embed bersama gambarnya (multimodal) agar bisa dicari lewat teks.
    4. Semua chunk di-embed dengan gemini-embedding-2 dan disimpan ke tabel `document_chunks`.
"""
from __future__ import annotations

import hashlib
import os
import re
import sys
import time
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import psycopg
import pymupdf  # PyMuPDF
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types
from psycopg.types.json import Jsonb

load_dotenv()

# ------------------------------- Konfigurasi -------------------------------
EMBED_MODEL = os.getenv("EMBED_MODEL", "gemini-embedding-2")
EMBED_DIM = int(os.getenv("EMBED_DIM", "1536"))  # 768 / 1536 / 3072. Index HNSW pgvector maks 2000 dim.
CAPTION_MODEL = os.getenv("CAPTION_MODEL", "gemini-3.5-flash-lite")  # untuk mendeskripsikan gambar
DB_URL = os.getenv("SUPABASE_DB_URL")
IMAGE_DIR = Path(os.getenv("IMAGE_DIR", "extracted_images"))  # gambar hasil ekstraksi disimpan di sini

CHUNK_MAX_CHARS = 1200
CHUNK_OVERLAP = 200
TABLE_MAX_CHARS = 3000
TEXT_BATCH_SIZE = 50          # jumlah chunk teks per request embedding
MIN_IMAGE_SIDE = 100          # px; lebih kecil dianggap ikon/dekorasi
MIN_IMAGE_BYTES = 3_000
MAX_IMAGE_SIDE = 2000         # gambar lebih besar akan diperkecil

CAPTION_PROMPT = (
    "Kamu sedang menyiapkan knowledge base untuk sistem RAG. "
    "Deskripsikan gambar dari dokumen PDF ini dalam Bahasa Indonesia agar bisa dicari lewat teks:\n"
    "- Grafik/diagram: sebutkan jenis, judul, sumbu, tren, dan angka penting.\n"
    "- Tabel dalam bentuk gambar: tulis ulang isinya sebagai tabel markdown.\n"
    "- Tulis semua teks penting yang terlihat pada gambar.\n"
    "- Foto/ilustrasi: jelaskan objek dan konteksnya secara ringkas.\n"
    "- Jika gambar hanya dekorasi (logo, ikon, garis, latar belakang), jawab persis: DEKORASI\n"
    "Langsung ke isi, tanpa kalimat pembuka."
)

DDL = f"""
create extension if not exists vector with schema extensions;

create table if not exists document_chunks (
    id          bigint generated always as identity primary key,
    source      text    not null,                 -- nama file PDF
    doc_hash    text    not null,                 -- sha256 file (deteksi perubahan)
    page        int     not null,
    chunk_index int     not null,
    chunk_type  text    not null check (chunk_type in ('text', 'table', 'image')),
    content     text    not null,                 -- teks asli / markdown tabel / caption gambar
    metadata    jsonb   not null default '{{}}'::jsonb,
    embedding   vector({EMBED_DIM}) not null,
    created_at  timestamptz not null default now()
);

-- Supabase mengekspos schema public lewat REST API: aktifkan RLS tanpa policy
-- supaya data hanya bisa diakses lewat koneksi Postgres langsung / service role.
alter table document_chunks enable row level security;

create index if not exists document_chunks_embedding_idx
    on document_chunks using hnsw (embedding vector_cosine_ops);
create index if not exists document_chunks_source_idx
    on document_chunks (source);
"""


@dataclass
class Chunk:
    page: int
    chunk_type: str                      # 'text' | 'table' | 'image'
    content: str                         # teks yang disimpan & nanti dikirim ke LLM
    metadata: dict = field(default_factory=dict)
    image_png: bytes | None = None       # hanya untuk chunk gambar (tidak disimpan di DB)


# ------------------------------ Gemini helpers ------------------------------
@lru_cache(maxsize=1)
def gemini() -> genai.Client:
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY belum diset (lihat .env.example).")
    return genai.Client(api_key=key)


def with_retry(fn, tries: int = 6):
    """Retry dengan exponential backoff untuk rate limit (429) / error server (5xx)."""
    delay = 2.0
    for attempt in range(1, tries + 1):
        try:
            return fn()
        except errors.APIError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < tries:
                print(f"  ! API {e.code}, mengulang ({attempt}/{tries - 1}) dalam {delay:.0f}s ...")
                time.sleep(delay)
                delay = min(delay * 2, 60)
            else:
                raise


def embed_contents(contents: list[types.Content]) -> list[list[float]]:
    """Satu embedding per objek Content (dibungkus Content => hasilnya terpisah, bukan agregat)."""
    res = with_retry(
        lambda: gemini().models.embed_content(
            model=EMBED_MODEL,
            contents=contents,
            config=types.EmbedContentConfig(output_dimensionality=EMBED_DIM),
        )
    )
    vectors = [e.values for e in res.embeddings]
    if len(vectors) != len(contents):
        raise RuntimeError(f"Jumlah embedding ({len(vectors)}) != jumlah input ({len(contents)})")
    return vectors


def text_content(text: str) -> types.Content:
    return types.Content(parts=[types.Part.from_text(text=text)])


def embed_query(query: str) -> list[float]:
    """Embedding untuk pertanyaan pengguna. Dipakai juga oleh aplikasi RAG (rag_app.py).
    Format query gemini-embedding-2; ganti ke "task: search result | query: ..." bila perlu."""
    return embed_contents([text_content(f"task: question answering | query: {query}")])[0]


def caption_image(png: bytes) -> str:
    resp = with_retry(
        lambda: gemini().models.generate_content(
            model=CAPTION_MODEL,
            contents=[types.Part.from_bytes(data=png, mime_type="image/png"), CAPTION_PROMPT],
        )
    )
    return (resp.text or "").strip()


# ------------------------------ Chunking teks/tabel ------------------------------
def clean_block(text: str) -> str:
    text = text.replace("\x00", "")  # Postgres menolak karakter NUL
    text = re.sub(r"\s*\n\s*", " ", text)
    return re.sub(r"[ \t]+", " ", text).strip()


def _split_long(paragraph: str, max_chars: int) -> list[str]:
    if len(paragraph) <= max_chars:
        return [paragraph]
    parts, cur = [], ""
    for sentence in re.split(r"(?<=[.!?])\s+", paragraph):
        if len(cur) + len(sentence) + 1 <= max_chars:
            cur = f"{cur} {sentence}".strip()
            continue
        if cur:
            parts.append(cur)
        while len(sentence) > max_chars:  # kalimat super panjang: potong paksa
            parts.append(sentence[:max_chars])
            sentence = sentence[max_chars:]
        cur = sentence
    if cur:
        parts.append(cur)
    return parts


def chunk_text(text: str, max_chars: int = CHUNK_MAX_CHARS, overlap: int = CHUNK_OVERLAP) -> list[str]:
    pieces: list[str] = []
    for para in (p.strip() for p in text.split("\n\n")):
        if para:
            pieces.extend(_split_long(para, max_chars))

    chunks, cur = [], ""
    for piece in pieces:
        if cur and len(cur) + len(piece) + 2 > max_chars:
            chunks.append(cur)
            tail = cur[-overlap:]
            tail = tail[tail.find(" ") + 1:] if " " in tail else ""  # potong di batas kata
            cur = f"{tail}\n\n{piece}" if tail else piece
        else:
            cur = f"{cur}\n\n{piece}" if cur else piece
    if cur.strip():
        chunks.append(cur)
    return chunks


def split_table_markdown(md: str, max_chars: int = TABLE_MAX_CHARS) -> list[str]:
    lines = [ln for ln in md.strip().splitlines() if ln.strip()]
    if len(md) <= max_chars or len(lines) <= 3:
        return [md.strip()]
    header, rows = "\n".join(lines[:2]), lines[2:]  # baris header + pemisah |---|
    parts, cur, size = [], [], len(header)
    for row in rows:
        if cur and size + len(row) > max_chars:
            parts.append(header + "\n" + "\n".join(cur))
            cur, size = [], len(header)
        cur.append(row)
        size += len(row) + 1
    if cur:
        parts.append(header + "\n" + "\n".join(cur))
    return parts


def overlap_ratio(rect: pymupdf.Rect, table_rects: list[pymupdf.Rect]) -> float:
    area = rect.get_area()
    if area <= 0:
        return 0.0
    best = 0.0
    for t in table_rects:
        if rect.intersects(t):
            best = max(best, (rect & t).get_area() / area)
    return best


# ------------------------------ Ekstraksi gambar ------------------------------
def image_to_png(doc: pymupdf.Document, xref: int) -> bytes | None:
    """Ubah gambar embedded ke PNG RGB (Gemini Embedding 2 hanya menerima PNG/JPEG)."""
    try:
        pix = pymupdf.Pixmap(doc, xref)
        if pix.width < MIN_IMAGE_SIDE or pix.height < MIN_IMAGE_SIDE:
            return None
        if pix.alpha:
            pix = pymupdf.Pixmap(pix, 0)  # buang alpha channel
        if pix.colorspace is None or pix.colorspace.n != 3:  # gray/CMYK -> RGB
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        while max(pix.width, pix.height) > MAX_IMAGE_SIDE:
            pix.shrink(1)  # perkecil 2x
        data = pix.tobytes("png")
        return data if len(data) >= MIN_IMAGE_BYTES else None
    except Exception as e:  # noqa: BLE001 - gambar rusak/mask tidak boleh menghentikan ingest
        print(f"  ! gambar xref={xref} dilewati: {e}")
        return None


# ------------------------------ Pipeline ekstraksi ------------------------------
def extract_chunks(pdf_path: Path) -> list[Chunk]:
    doc = pymupdf.open(pdf_path)
    chunks: list[Chunk] = []
    seen_xrefs: set[int] = set()  # logo/header yang berulang di banyak halaman hanya diproses sekali

    for page in doc:
        pno = page.number + 1

        # 1) Tabel -> markdown
        table_rects: list[pymupdf.Rect] = []
        for ti, tab in enumerate(page.find_tables().tables):
            md = tab.to_markdown().replace("\x00", "")
            if not md.strip() or tab.row_count < 2:
                continue
            table_rects.append(pymupdf.Rect(tab.bbox))
            for part_i, part in enumerate(split_table_markdown(md)):
                chunks.append(Chunk(
                    page=pno,
                    chunk_type="table",
                    content=f"Tabel (halaman {pno}):\n{part}",
                    metadata={"table_index": ti, "part": part_i, "rows": tab.row_count, "cols": tab.col_count},
                ))

        # 2) Teks di luar area tabel (supaya isi tabel tidak terduplikasi)
        paragraphs = []
        for b in page.get_text("blocks", sort=True):
            if b[6] != 0:  # 0 = blok teks, 1 = blok gambar
                continue
            if overlap_ratio(pymupdf.Rect(b[:4]), table_rects) > 0.5:
                continue
            txt = clean_block(b[4])
            if txt:
                paragraphs.append(txt)
        for piece in chunk_text("\n\n".join(paragraphs)):
            chunks.append(Chunk(page=pno, chunk_type="text", content=piece))

        # 3) Gambar (caption dibuat belakangan)
        for img in page.get_images(full=True):
            xref = img[0]
            if xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)
            png = image_to_png(doc, xref)
            if png:
                chunks.append(Chunk(page=pno, chunk_type="image", content="", metadata={"xref": xref}, image_png=png))

    doc.close()
    return chunks


def caption_images(chunks: list[Chunk], source_stem: str) -> list[Chunk]:
    """Isi caption untuk chunk gambar; buang gambar dekoratif."""
    out: list[Chunk] = []
    img_dir = IMAGE_DIR / source_stem
    for c in chunks:
        if c.chunk_type != "image":
            out.append(c)
            continue
        caption = caption_image(c.image_png).replace("\x00", "")
        if not caption or caption.strip().upper().startswith("DEKORASI"):
            print(f"  - hal. {c.page}: gambar dekoratif, dilewati")
            continue
        img_dir.mkdir(parents=True, exist_ok=True)
        path = img_dir / f"p{c.page}_x{c.metadata['xref']}.png"
        path.write_bytes(c.image_png)
        c.content = f"Gambar (halaman {c.page}): {caption}"
        c.metadata["image_path"] = str(path)
        out.append(c)
    return out


# ------------------------------ Embedding ------------------------------
def embed_chunks(chunks: list[Chunk], title: str) -> list[list[float]]:
    vectors: list[list[float] | None] = [None] * len(chunks)

    # Teks & tabel: format dokumen yang direkomendasikan untuk gemini-embedding-2.
    # (gemini-embedding-2 tidak punya parameter task_type; instruksi task ada di teks.)
    text_idx = [i for i, c in enumerate(chunks) if c.chunk_type != "image"]
    for s in range(0, len(text_idx), TEXT_BATCH_SIZE):
        idxs = text_idx[s:s + TEXT_BATCH_SIZE]
        contents = [text_content(f"title: {title} | text: {chunks[i].content}") for i in idxs]
        for i, vec in zip(idxs, embed_contents(contents)):
            vectors[i] = vec
        print(f"  embedding teks/tabel: {min(s + TEXT_BATCH_SIZE, len(text_idx))}/{len(text_idx)}")

    # Gambar: caption + gambar dalam satu Content => satu embedding multimodal (agregat).
    # Satu gambar per request agar aman dari batas jumlah gambar per request.
    img_idx = [i for i, c in enumerate(chunks) if c.chunk_type == "image"]
    for n, i in enumerate(img_idx, 1):
        c = chunks[i]
        content = types.Content(parts=[
            types.Part.from_text(text=c.content),  # untuk input multimodal, tanpa prefix task
            types.Part.from_bytes(data=c.image_png, mime_type="image/png"),
        ])
        vectors[i] = embed_contents([content])[0]
        print(f"  embedding gambar: {n}/{len(img_idx)}")

    return vectors  # type: ignore[return-value]


# ------------------------------ Database ------------------------------
def connect() -> psycopg.Connection:
    if not DB_URL:
        sys.exit("SUPABASE_DB_URL belum diset (lihat .env.example).")
    # prepare_threshold=None: kompatibel dengan Supabase pooler mode transaction (port 6543)
    return psycopg.connect(DB_URL, autocommit=True, prepare_threshold=None)


def vec_literal(vec: list[float]) -> str:
    return "[" + ",".join(f"{x:.8g}" for x in vec) + "]"


def save(conn: psycopg.Connection, source: str, doc_hash: str,
         chunks: list[Chunk], vectors: list[list[float]]) -> None:
    rows = [
        (source, doc_hash, c.page, i, c.chunk_type, c.content, Jsonb(c.metadata), vec_literal(v))
        for i, (c, v) in enumerate(zip(chunks, vectors))
    ]
    with conn.transaction():
        # Idempotent: ingest ulang file yang sama menggantikan data lamanya
        conn.execute("delete from document_chunks where source = %s", (source,))
        with conn.cursor() as cur:
            cur.executemany(
                """insert into document_chunks
                       (source, doc_hash, page, chunk_index, chunk_type, content, metadata, embedding)
                   values (%s, %s, %s, %s, %s, %s, %s, %s::vector)""",
                rows,
            )


# ------------------------------ Fungsi utama ------------------------------
def ingest(pdf_path: str) -> None:
    """Proses satu PDF: ekstraksi -> caption gambar -> embedding -> simpan ke Supabase."""
    path = Path(pdf_path)
    if not path.is_file():
        sys.exit(f"File tidak ditemukan: {path}")
    doc_hash = hashlib.sha256(path.read_bytes()).hexdigest()

    print("[1/4] Ekstraksi teks, tabel, dan gambar ...")
    chunks = extract_chunks(path)
    n_img = sum(c.chunk_type == "image" for c in chunks)
    print(f"      {len(chunks) - n_img} chunk teks/tabel, {n_img} gambar kandidat")

    print("[2/4] Membuat caption gambar ...")
    chunks = caption_images(chunks, path.stem)
    if not chunks:
        sys.exit("Tidak ada konten yang bisa diambil dari PDF ini.")

    print("[3/4] Membuat embedding ...")
    vectors = embed_chunks(chunks, title=path.stem)

    print("[4/4] Menyimpan ke Supabase ...")
    with connect() as conn:
        conn.execute(DDL)
        save(conn, path.name, doc_hash, chunks, vectors)

    by_type = {t: sum(c.chunk_type == t for c in chunks) for t in ("text", "table", "image")}
    print(f"Selesai: {len(chunks)} chunk tersimpan untuk '{path.name}' {by_type}")


def search(query: str, k: int = 5) -> None:
    """Uji pencarian semantik: tampilkan k chunk paling mirip dengan pertanyaan."""
    lit = vec_literal(embed_query(query))

    with connect() as conn:
        rows = conn.execute(
            """select source, page, chunk_type, content, metadata,
                      1 - (embedding <=> %s::vector) as similarity
                 from document_chunks
                order by embedding <=> %s::vector
                limit %s""",
            (lit, lit, k),
        ).fetchall()

    for source, page, ctype, content, meta, sim in rows:
        preview = content[:300].replace("\n", " ")
        print(f"\n[{sim:.3f}] {source} - hal. {page} ({ctype})")
        if meta.get("image_path"):
            print(f"        gambar: {meta['image_path']}")
        print(f"        {preview}{'...' if len(content) > 300 else ''}")


if __name__ == "__main__":
    PDF_PATH = "dokumen.pdf"  # <- ganti dengan path PDF Anda
    QUERY = ""                # <- isi pertanyaan untuk menguji pencarian (kosongkan untuk melewati)

    ingest(PDF_PATH)
    if QUERY:
        search(QUERY, k=5)
