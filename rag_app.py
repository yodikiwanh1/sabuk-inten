"""
rag_app.py
----------
Chat RAG dengan UI Chainlit di atas tabel `knowledge_rag` (Supabase pgvector).

    Embedding pertanyaan : Gemini (gemini-embedding-2) - sama dengan saat ingest
    LLM penjawab         : OpenRouter (API kompatibel OpenAI)

Jalankan (satu folder dengan ingest_pdf.py):
    chainlit run rag_app.py -w
"""
from __future__ import annotations

import os
from pathlib import Path

import chainlit as cl
from openai import APIError, AsyncOpenAI
from psycopg_pool import ConnectionPool

# Import ini juga memanggil load_dotenv(), jadi harus sebelum os.getenv di bawah.
from ingest.ingest_pdf import DB_URL, embed_query, vec_literal

# ------------------------------- Konfigurasi -------------------------------
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")
TOP_K = int(os.getenv("TOP_K", "6"))                       # jumlah chunk yang diambil
MIN_SIMILARITY = float(os.getenv("MIN_SIMILARITY", "0.0"))  # buang chunk di bawah skor ini
MAX_HISTORY = 6                                             # jumlah pesan riwayat yang dikirim ke LLM

llm = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY") or "missing",
)

SYSTEM_PROMPT = """Kamu adalah asisten yang menjawab pertanyaan berdasarkan KONTEKS dokumen yang diberikan.

Jika user bertanya tidak dalam bahasa inggris

Aturan:
- Jawab hanya berdasarkan konteks. Jika jawabannya tidak ada di konteks, katakan dengan jelas bahwa informasinya tidak ditemukan di dokumen. Jangan mengarang.
- Sebutkan sumber dengan format [1], [2], dst. sesuai nomor pada konteks.
- Konteks bisa berupa teks, tabel markdown, atau deskripsi gambar. Untuk tabel, baca baris dan kolom dengan teliti dan jangan menebak angka.
- Jawab dalam bahasa yang sama dengan pertanyaan pengguna (default Bahasa Indonesia), ringkas dan jelas."""

REWRITE_PROMPT = """Ubah pertanyaan lanjutan pengguna menjadi satu pertanyaan mandiri yang bisa dipahami tanpa riwayat percakapan, \
berdasarkan riwayat yang diberikan. Jika pertanyaan sudah mandiri, kembalikan apa adanya. \
Balas HANYA dengan pertanyaannya, tanpa penjelasan."""

SQL = """
select source, page, chunk_type, content, metadata,
       1 - (embedding <=> %s::vector) as similarity
  from knowledge_rag
 order by embedding <=> %s::vector
 limit %s
"""
COLUMNS = ("source", "page", "chunk_type", "content", "metadata", "similarity")


# ------------------------------- Database / retrieval -------------------------------
_pool: ConnectionPool | None = None


def get_pool() -> ConnectionPool:
    global _pool
    if _pool is None:
        if not DB_URL:
            raise RuntimeError("SUPABASE_DB_URL belum diset di .env")
        _pool = ConnectionPool(
            DB_URL,
            min_size=1,
            max_size=5,
            kwargs={"autocommit": True, "prepare_threshold": None},  # kompatibel dengan pooler Supabase
            check=ConnectionPool.check_connection,                   # buang koneksi yang sudah diputus server
            open=False,
        )
        _pool.open()
    return _pool


def retrieve(query: str, k: int = TOP_K) -> list[dict]:
    """Pencarian semantik (sinkron; dipanggil lewat cl.make_async agar tidak memblokir UI)."""
    lit = vec_literal(embed_query(query))
    with get_pool().connection() as conn:
        rows = conn.execute(SQL, (lit, lit, k)).fetchall()
    hits = [dict(zip(COLUMNS, row)) for row in rows]
    return [h for h in hits if h["similarity"] >= MIN_SIMILARITY]


# ------------------------------- Format konteks & sumber -------------------------------
def build_context(hits: list[dict]) -> str:
    return "\n\n".join(
        f"[{i}] (sumber: {h['source']}, hal. {h['page']}, tipe: {h['chunk_type']})\n{h['content']}"
        for i, h in enumerate(hits, 1)
    )


def format_hits(hits: list[dict]) -> str:
    return "\n".join(
        f"[{i}] skor {h['similarity']:.3f} - {h['source']} hal. {h['page']} ({h['chunk_type']})"
        for i, h in enumerate(hits, 1)
    )


def resolve_image(path_str: str | None) -> Path | None:
    """image_path disimpan relatif terhadap folder tempat ingest dijalankan."""
    if not path_str:
        return None
    p = Path(path_str)
    for candidate in (p, Path(__file__).parent / p):
        if candidate.is_file():
            return candidate
    return None


def build_elements(hits: list[dict]) -> tuple[list, str]:
    """Elemen UI: teks sumber (panel samping, klik namanya) + gambar yang ikut ter-retrieve."""
    elements, names = [], []
    for i, h in enumerate(hits, 1):
        name = f"Sumber {i} (hal. {h['page']})"
        names.append(name)
        elements.append(cl.Text(
            name=name,
            content=f"**{h['source']}** - hal. {h['page']} - {h['chunk_type']} - skor {h['similarity']:.2f}\n\n{h['content']}",
            display="side",
        ))
        img = resolve_image((h.get("metadata") or {}).get("image_path"))
        if img:
            elements.append(cl.Image(name=f"Gambar sumber {i}", path=str(img), display="inline", size="medium"))
    # Nama elemen harus muncul di teks pesan agar menjadi tautan yang bisa diklik.
    return elements, "\n\n**Sumber:** " + " | ".join(names)


# ------------------------------- LLM -------------------------------
async def standalone_question(history: list[dict], question: str) -> str:
    """Ubah pertanyaan lanjutan ("kalau tahun lalu?") menjadi pertanyaan mandiri untuk pencarian."""
    if not history:
        return question
    transcript = "\n".join(f"{m['role']}: {m['content']}" for m in history[-MAX_HISTORY:])
    try:
        resp = await llm.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "system", "content": REWRITE_PROMPT},
                {"role": "user", "content": f"Riwayat:\n{transcript}\n\nPertanyaan lanjutan: {question}"},
            ],
        )
        return (resp.choices[0].message.content or "").strip() or question
    except Exception:  # noqa: BLE001 - kegagalan rewrite tidak boleh menghentikan chat
        return question


# ------------------------------- Chainlit -------------------------------
@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    if not os.getenv("OPENROUTER_API_KEY"):
        await cl.Message("OPENROUTER_API_KEY belum diset di file .env.").send()
    await cl.Message("Halo! Tanyakan apa saja tentang dokumen yang sudah di-ingest.").send()


@cl.on_message
async def on_message(message: cl.Message):
    history: list[dict] = cl.user_session.get("history")
    question = message.content.strip()
    if not question:
        return

    # 1) Retrieval
    try:
        search_query = await standalone_question(history, question)
        async with cl.Step(name="Mencari di dokumen", type="tool") as step:
            step.input = search_query
            hits = await cl.make_async(retrieve)(search_query)
            step.output = format_hits(hits) or "Tidak ada hasil."
    except Exception as e:  # noqa: BLE001
        await cl.Message(f"Gagal mengambil konteks dari database: {e}").send()
        return

    if not hits:
        await cl.Message("Saya tidak menemukan bagian dokumen yang relevan dengan pertanyaan itu.").send()
        return

    # 2) Generate jawaban (streaming)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *history[-MAX_HISTORY:],
        {"role": "user", "content": f"KONTEKS:\n{build_context(hits)}\n\nPERTANYAAN: {question}"},
    ]
    msg = cl.Message(content="")
    answer = ""
    try:
        stream = await llm.chat.completions.create(model=OPENROUTER_MODEL, messages=messages, stream=True)
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                answer += token
                await msg.stream_token(token)
    except APIError as e:
        await cl.Message(f"Error dari OpenRouter: {e}").send()
        return

    # 3) Sumber (teks di panel samping + gambar)
    elements, footer = build_elements(hits)
    await msg.stream_token(footer)
    msg.elements = elements
    await msg.send()

    history += [{"role": "user", "content": question}, {"role": "assistant", "content": answer}]
    history[:] = history[-MAX_HISTORY:]
