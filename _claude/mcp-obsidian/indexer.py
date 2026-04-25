"""Scan the vault, chunk markdown, embed via OpenAI, store in sqlite-vec.

Incremental: skips files whose mtime hasn't changed. Removes chunks for
deleted files. Run with `python indexer.py` or `python indexer.py --full`.
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from common import (
    VAULT_ROOT, open_db, get_client, embed_batch, vec_to_bytes,
    iter_markdown_files, chunk_markdown,
)

BATCH_SIZE = 64


def current_mtimes() -> dict[str, float]:
    return {p.relative_to(VAULT_ROOT).as_posix(): p.stat().st_mtime
            for p in iter_markdown_files(VAULT_ROOT)}


def indexed_mtimes(conn) -> dict[str, float]:
    rows = conn.execute("SELECT path, MAX(mtime) FROM chunks GROUP BY path").fetchall()
    return {r[0]: r[1] for r in rows}


def delete_path(conn, path: str):
    ids = [r[0] for r in conn.execute("SELECT id FROM chunks WHERE path = ?", (path,))]
    if not ids:
        return
    placeholders = ",".join("?" * len(ids))
    conn.execute(f"DELETE FROM vec_chunks WHERE chunk_id IN ({placeholders})", ids)
    conn.execute("DELETE FROM chunks WHERE path = ?", (path,))


def index_file(conn, client, rel_path: str, abs_path: Path) -> int:
    text = abs_path.read_text(encoding="utf-8", errors="replace")
    chunks = chunk_markdown(text, rel_path)
    if not chunks:
        delete_path(conn, rel_path)
        return 0

    delete_path(conn, rel_path)
    mtime = abs_path.stat().st_mtime

    to_embed = [f"{h}\n\n{c}" for h, c in chunks]
    embeddings: list[list[float]] = []
    for i in range(0, len(to_embed), BATCH_SIZE):
        batch = to_embed[i:i + BATCH_SIZE]
        embeddings.extend(embed_batch(client, batch))

    for idx, ((header, content), emb) in enumerate(zip(chunks, embeddings)):
        cur = conn.execute(
            "INSERT INTO chunks(path, chunk_idx, header_trail, content, mtime) VALUES (?,?,?,?,?)",
            (rel_path, idx, header, content, mtime),
        )
        chunk_id = cur.lastrowid
        conn.execute(
            "INSERT INTO vec_chunks(chunk_id, embedding) VALUES (?, ?)",
            (chunk_id, vec_to_bytes(emb)),
        )
    return len(chunks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="Reindex everything, not just changed files")
    args = ap.parse_args()

    conn = open_db()
    client = get_client()

    current = current_mtimes()
    indexed = indexed_mtimes(conn)

    removed = [p for p in indexed if p not in current]
    for p in removed:
        print(f"remove {p}")
        delete_path(conn, p)

    to_index = []
    for rel, mt in current.items():
        if args.full or rel not in indexed or indexed[rel] < mt:
            to_index.append(rel)

    if not to_index and not removed:
        print("up to date")
        conn.commit()
        return

    start = time.time()
    total_chunks = 0
    for i, rel in enumerate(to_index, 1):
        abs_path = VAULT_ROOT / rel
        try:
            n = index_file(conn, client, rel, abs_path)
        except Exception as e:
            print(f"  FAIL {rel}: {e}", file=sys.stderr)
            continue
        total_chunks += n
        print(f"[{i}/{len(to_index)}] {rel} ({n} chunks)")
        if i % 10 == 0:
            conn.commit()

    conn.commit()
    elapsed = time.time() - start
    print(f"done: {len(to_index)} files, {total_chunks} chunks, {elapsed:.1f}s")


if __name__ == "__main__":
    main()
