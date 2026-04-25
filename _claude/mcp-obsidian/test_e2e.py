"""End-to-end check: verifies the index, the MCP server, and the file watcher.

Run directly: `.venv/bin/python test_e2e.py`

Checks (in order):
  1. DB exists and has chunks
  2. Library-level semantic search returns sensible results
  3. MCP server: spawn it, list tools, call search_notes, call read_note
  4. Watcher: touch a throwaway file, confirm log shows a reindex within N seconds
"""
from __future__ import annotations

import asyncio
import os
import sys
import time
from pathlib import Path

from common import VAULT_ROOT, open_db, get_client, embed_batch, vec_to_bytes

HERE = Path(__file__).resolve().parent
VENV_PY = HERE / ".venv" / "bin" / "python"
SERVER = HERE / "server.py"
LOG = HERE / "watcher.log"

PASS = "✅"
FAIL = "❌"
results: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    mark = PASS if ok else FAIL
    print(f"{mark} {name}" + (f" — {detail}" if detail else ""))
    results.append((name, ok, detail))


def check_index() -> None:
    try:
        conn = open_db()
        n = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        v = conn.execute("SELECT COUNT(*) FROM vec_chunks").fetchone()[0]
        ok = n > 0 and v == n
        record("index has chunks", ok, f"{n} chunks, {v} vectors")
    except Exception as e:
        record("index has chunks", False, repr(e))


def check_library_search() -> None:
    try:
        client = get_client()
        qvec = embed_batch(client, ["price anchoring in ads"])[0]
        conn = open_db()
        rows = conn.execute(
            """SELECT c.path FROM vec_chunks v JOIN chunks c ON c.id = v.chunk_id
               WHERE v.embedding MATCH ? AND k = 5 ORDER BY v.distance""",
            (vec_to_bytes(qvec),),
        ).fetchall()
        ok = len(rows) >= 1
        record("library search returns results", ok, f"{len(rows)} hits, top: {rows[0][0] if rows else '-'}")
    except Exception as e:
        record("library search returns results", False, repr(e))


async def check_mcp_server() -> None:
    try:
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        params = StdioServerParameters(command=str(VENV_PY), args=[str(SERVER)])
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                tool_names = sorted(t.name for t in tools.tools)
                record(
                    "MCP server exposes tools",
                    tool_names == ["list_notes", "read_note", "search_notes"],
                    f"got {tool_names}",
                )

                r = await session.call_tool("search_notes", {"query": "setter hiring", "limit": 3})
                text = r.content[0].text if r.content else ""
                record(
                    "MCP search_notes returns content",
                    "results for" in text.lower() or "no results" in text.lower(),
                    f"{len(text)} chars",
                )

                r = await session.call_tool("read_note", {"path": "calls/consulting-calls.md"})
                text = r.content[0].text if r.content else ""
                record(
                    "MCP read_note returns markdown",
                    "Consulting Calls" in text,
                    f"{len(text)} chars",
                )

                r = await session.call_tool("list_notes", {"folder": "calls"})
                text = r.content[0].text if r.content else ""
                record(
                    "MCP list_notes returns paths",
                    "calls/2026-03-08-consulting-call.md" in text,
                    f"{len(text)} chars",
                )
    except Exception as e:
        record("MCP server exposes tools", False, repr(e))


def check_watcher() -> None:
    """Touch a throwaway file and see if the watcher log records a reindex."""
    test_note = VAULT_ROOT / "_claude" / "mcp-obsidian-test-note.md"
    try:
        log_before_size = LOG.stat().st_size if LOG.exists() else 0

        test_note.write_text(
            f"# Watcher test\n\nHeartbeat {int(time.time())}\n",
            encoding="utf-8",
        )

        timeout = 25.0
        deadline = time.time() + timeout
        found = False
        while time.time() < deadline:
            if LOG.exists() and LOG.stat().st_size > log_before_size:
                new = LOG.read_text(errors="replace")[log_before_size:]
                if "reindex trigger" in new:
                    found = True
                    break
            time.sleep(0.5)

        if found:
            record("watcher reindexes on file change", True, "log line appeared")
        else:
            record(
                "watcher reindexes on file change",
                False,
                f"no reindex log within {timeout}s (is launchd agent loaded?)",
            )
    finally:
        if test_note.exists():
            test_note.unlink()


async def main() -> int:
    print(f"e2e check — {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    check_index()
    check_library_search()
    await check_mcp_server()
    check_watcher()

    print()
    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    print(f"{passed}/{total} checks passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
