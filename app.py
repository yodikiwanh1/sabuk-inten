"""
Sabuk Inten — chat AI bergaya WhatsApp dengan memori percakapan.
Stack: Chainlit + OpenRouter (API kompatibel OpenAI).
"""
import json
import os
from pathlib import Path

import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

# ----------------------------------------------------------------------------
# Konfigurasi
# ----------------------------------------------------------------------------
APP_NAME = "Sabuk Inten"
MODEL = os.getenv("OPENROUTER_MODEL", "nvidia/nemotron-3-ultra-550b-a55b:free")

KEEP_RECENT = 12       # jumlah pesan terakhir yang selalu dikirim utuh
SUMMARIZE_AT = 24      # kalau riwayat > ini, pesan lama diringkas
MEMORY_DIR = Path("data/memory")
MEMORY_DIR.mkdir(parents=True, exist_ok=True)

SYSTEM_PROMPT = (
    f"Kamu adalah {APP_NAME}, asisten AI yang ramah, hangat, dan to the point. "
    "Balas dalam bahasa yang dipakai pengguna (default Bahasa Indonesia). "
    "Gunakan gaya santai seperti chat WhatsApp: ringkas, jelas, boleh pakai "
    "emoji secukupnya. Gunakan format markdown hanya bila memang membantu "
    "(misalnya kode atau daftar)."
)

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    default_headers={
        "HTTP-Referer": os.getenv("APP_URL", "http://localhost:8000"),
        "X-Title": APP_NAME,
    },
)

# ----------------------------------------------------------------------------
# Login opsional (aktif jika AUTH_USERNAME & AUTH_PASSWORD diisi)
# ----------------------------------------------------------------------------
if os.getenv("AUTH_USERNAME") and os.getenv("AUTH_PASSWORD"):

    @cl.password_auth_callback
    def auth_callback(username: str, password: str):
        if username == os.getenv("AUTH_USERNAME") and password == os.getenv("AUTH_PASSWORD"):
            return cl.User(identifier=username, metadata={"role": "user"})
        return None


# ----------------------------------------------------------------------------
# Memori: riwayat + ringkasan, disimpan permanen bila user login
# ----------------------------------------------------------------------------
def _memory_path() -> Path | None:
    user = cl.user_session.get("user")
    if not user:
        return None
    safe = "".join(c for c in user.identifier if c.isalnum() or c in "-_")
    return MEMORY_DIR / f"{safe}.json"


def load_memory() -> None:
    history, summary = [], ""
    path = _memory_path()
    if path and path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            history = data.get("history", [])
            summary = data.get("summary", "")
        except Exception:
            pass
    cl.user_session.set("history", history)
    cl.user_session.set("summary", summary)


def save_memory() -> None:
    path = _memory_path()
    if not path:
        return
    data = {
        "history": cl.user_session.get("history", []),
        "summary": cl.user_session.get("summary", ""),
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def clear_memory() -> None:
    cl.user_session.set("history", [])
    cl.user_session.set("summary", "")
    path = _memory_path()
    if path and path.exists():
        path.unlink()


async def compress_memory() -> None:
    """Ringkas pesan lama agar konteks tetap ringan tapi ingatan tidak hilang."""
    history = cl.user_session.get("history", [])
    if len(history) <= SUMMARIZE_AT:
        return

    old, recent = history[:-KEEP_RECENT], history[-KEEP_RECENT:]
    previous = cl.user_session.get("summary", "")
    transcript = "\n".join(
        f"{'Pengguna' if m['role'] == 'user' else APP_NAME}: {m['content']}" for m in old
    )
    try:
        res = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ringkas percakapan berikut menjadi catatan memori singkat "
                        "(maks 200 kata) dalam Bahasa Indonesia. Simpan fakta penting "
                        "tentang pengguna, preferensi, keputusan, dan topik yang "
                        "sedang dibahas."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Ringkasan sebelumnya:\n{previous or '-'}\n\nPercakapan baru:\n{transcript}",
                },
            ],
            temperature=0.3,
        )
        cl.user_session.set("summary", res.choices[0].message.content.strip())
        cl.user_session.set("history", recent)
    except Exception:
        # Jika gagal meringkas, biarkan riwayat apa adanya.
        pass


def build_messages() -> list[dict]:
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
    summary = cl.user_session.get("summary", "")
    if summary:
        msgs.append(
            {
                "role": "system",
                "content": f"Memori dari percakapan sebelumnya dengan pengguna ini:\n{summary}",
            }
        )
    msgs.extend(cl.user_session.get("history", []))
    return msgs


# ----------------------------------------------------------------------------
# Event Chainlit
# ----------------------------------------------------------------------------
@cl.on_chat_start
async def on_chat_start():
    load_memory()

    if not os.getenv("OPENROUTER_API_KEY"):
        await cl.Message(
            content="⚠️ `OPENROUTER_API_KEY` belum diisi. Salin `.env.example` menjadi `.env` lalu isi API key-nya."
        ).send()
        return

    returning = bool(cl.user_session.get("history") or cl.user_session.get("summary"))
    greeting = (
        "Halo lagi! 👋 Aku masih ingat obrolan kita sebelumnya. Mau lanjut apa hari ini?"
        if returning
        else f"Halo! Aku **{APP_NAME}** ✨\nAku bisa ngobrol, bantu nulis, coding, atau brainstorming — dan aku ingat percakapan kita.\n\nKetik `/lupa` kapan saja untuk menghapus memoriku."
    )
    await cl.Message(content=greeting).send()


@cl.on_message
async def on_message(message: cl.Message):
    text = message.content.strip()

    # Perintah hapus memori
    if text.lower() in {"/lupa", "/reset", "/clear"}:
        clear_memory()
        await cl.Message(content="Oke, memori percakapan sudah dihapus 🧹 Kita mulai dari awal ya.").send()
        return

    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": text})
    cl.user_session.set("history", history)

    reply = cl.Message(content="")
    try:
        stream = await client.chat.completions.create(
            model=MODEL,
            messages=build_messages(),
            stream=True,
            temperature=0.7,
        )
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                await reply.stream_token(chunk.choices[0].delta.content)
    except Exception as e:
        # Batalkan pesan user terakhir supaya riwayat tetap konsisten
        history.pop()
        cl.user_session.set("history", history)
        await cl.Message(content=f"⚠️ Gagal menghubungi OpenRouter:\n\n`{e}`").send()
        return

    await reply.send()

    history.append({"role": "assistant", "content": reply.content})
    cl.user_session.set("history", history)

    await compress_memory()
    save_memory()
