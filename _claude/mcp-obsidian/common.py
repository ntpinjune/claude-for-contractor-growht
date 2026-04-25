"""Shared db, embedding, and chunking helpers."""
from __future__ import annotations

import os
import re
import sqlite3
import struct
from pathlib import Path

import sqlite_vec
from openai import OpenAI

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = Path(__file__).resolve().parent / "index.db"
EMBED_MODEL = "text-embedding-3-small"
EMBED_DIM = 1536
CHUNK_TARGET_CHARS = 1800
CHUNK_MAX_CHARS = 6000
CHUNK_MIN_CHARS = 200

EXCLUDE_DIRS = {
    ".git", ".obsidian", ".trash", "node_modules",
    "_archive/fathom-meta",
    "_claude/mcp-obsidian",
    "_claude/mempalace",
}


def open_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    conn.executescript(f"""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY,
            path TEXT NOT NULL,
            chunk_idx INTEGER NOT NULL,
            header_trail TEXT,
            content TEXT NOT NULL,
            mtime REAL NOT NULL,
            UNIQUE(path, chunk_idx)
        );
        CREATE INDEX IF NOT EXISTS idx_chunks_path ON chunks(path);
        CREATE VIRTUAL TABLE IF NOT EXISTS vec_chunks USING vec0(
            chunk_id INTEGER PRIMARY KEY,
            embedding float[{EMBED_DIM}]
        );
    """)
    return conn


def get_client() -> OpenAI:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / ".env")
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set (check _claude/mcp-obsidian/.env)")
    return OpenAI(api_key=key)


def embed_batch(client: OpenAI, texts: list[str]) -> list[list[float]]:
    resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]


def vec_to_bytes(vec: list[float]) -> bytes:
    return struct.pack(f"{len(vec)}f", *vec)


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        if any(rel == ex or rel.startswith(ex + "/") for ex in EXCLUDE_DIRS):
            continue
        yield path


HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def chunk_markdown(text: str, path_label: str) -> list[tuple[str, str]]:
    """Split markdown by headers, then size. Returns list of (header_trail, content)."""
    if not text.strip():
        return []

    sections: list[tuple[list[str], str]] = []
    current_trail: list[str] = []
    buf: list[str] = []
    pos = 0

    def flush():
        body = "\n".join(buf).strip()
        if body:
            sections.append((current_trail[:], body))

    for m in HEADER_RE.finditer(text):
        pre = text[pos:m.start()]
        if pre.strip():
            buf.append(pre.rstrip())
        flush()
        buf.clear()

        level = len(m.group(1))
        title = m.group(2).strip()
        current_trail = current_trail[:level - 1]
        while len(current_trail) < level - 1:
            current_trail.append("")
        current_trail.append(title)
        pos = m.end()

    tail = text[pos:]
    if tail.strip():
        buf.append(tail.rstrip())
    flush()

    if not sections:
        sections = [([], text.strip())]

    chunks: list[tuple[str, str]] = []
    for trail, body in sections:
        trail_str = " > ".join([t for t in trail if t]) or "(top)"
        header_trail = f"{path_label} > {trail_str}"
        for piece in _split_to_size(body, CHUNK_TARGET_CHARS):
            chunks.append((header_trail, piece))

    return [(h, c) for h, c in chunks if len(c) >= CHUNK_MIN_CHARS or len(chunks) == 1]


def _split_to_size(text: str, target: int) -> list[str]:
    """Split text into pieces <= target chars, trying paragraph then line then char boundaries."""
    text = text.strip()
    if not text:
        return []
    if len(text) <= target:
        return [text]

    # 1) paragraph split
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    out: list[str] = []
    cur = ""
    for p in paras:
        # if a single paragraph is itself too big, recurse via line split
        if len(p) > target:
            if cur:
                out.append(cur)
                cur = ""
            out.extend(_split_lines(p, target))
            continue
        if cur and len(cur) + len(p) + 2 > target:
            out.append(cur)
            cur = p
        else:
            cur = f"{cur}\n\n{p}" if cur else p
    if cur:
        out.append(cur)
    return out


def _split_lines(text: str, target: int) -> list[str]:
    lines = text.split("\n")
    out: list[str] = []
    cur = ""
    for ln in lines:
        if len(ln) > target:
            if cur:
                out.append(cur)
                cur = ""
            # hard character split as last resort
            for i in range(0, len(ln), target):
                out.append(ln[i:i + target])
            continue
        if cur and len(cur) + len(ln) + 1 > target:
            out.append(cur)
            cur = ln
        else:
            cur = f"{cur}\n{ln}" if cur else ln
    if cur:
        out.append(cur)
    return out
