"""MCP server exposing the vault index to Claude Code.

Tools:
  - search_notes(query, limit)   semantic search
  - read_note(path)              return full markdown of a vault file
  - list_notes(folder)           list vault .md files, optionally under a subfolder
"""
from __future__ import annotations

import asyncio
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from common import VAULT_ROOT, open_db, get_client, embed_batch, vec_to_bytes, iter_markdown_files

server = Server("obsidian-vault")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_notes",
            description=(
                "Semantic search across the Obsidian vault. Returns relevant "
                "chunks with file path and header trail. Use for queries like "
                "'what did Jack say about price anchoring' or 'find notes on setter hiring'."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Natural-language search query"},
                    "limit": {"type": "integer", "description": "Max results (default 8)", "default": 8},
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="read_note",
            description="Read the full markdown content of a vault file by path (relative to vault root).",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Vault-relative path, e.g. calls/2026-03-08-consulting-call.md"},
                },
                "required": ["path"],
            },
        ),
        Tool(
            name="list_notes",
            description="List markdown files in the vault, optionally filtered to a subfolder.",
            inputSchema={
                "type": "object",
                "properties": {
                    "folder": {"type": "string", "description": "Optional subfolder, e.g. 'calls' or 'clients'"},
                },
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, args: dict) -> list[TextContent]:
    if name == "search_notes":
        return await do_search(args["query"], int(args.get("limit", 8)))
    if name == "read_note":
        return do_read(args["path"])
    if name == "list_notes":
        return do_list(args.get("folder"))
    return [TextContent(type="text", text=f"unknown tool: {name}")]


async def do_search(query: str, limit: int) -> list[TextContent]:
    client = get_client()
    qvec = embed_batch(client, [query])[0]
    conn = open_db()
    rows = conn.execute(
        """
        SELECT c.path, c.header_trail, c.content, v.distance
        FROM vec_chunks v
        JOIN chunks c ON c.id = v.chunk_id
        WHERE v.embedding MATCH ? AND k = ?
        ORDER BY v.distance
        """,
        (vec_to_bytes(qvec), limit),
    ).fetchall()

    if not rows:
        return [TextContent(type="text", text="No results. The index may be empty — run indexer.py.")]

    parts = [f"# {len(rows)} results for: {query}\n"]
    for i, (path, trail, content, dist) in enumerate(rows, 1):
        score = max(0.0, 1.0 - dist)
        snippet = content.strip()
        if len(snippet) > 800:
            snippet = snippet[:800] + "…"
        parts.append(f"## {i}. {path}  (score {score:.2f})\n**{trail}**\n\n{snippet}\n")
    return [TextContent(type="text", text="\n".join(parts))]


def do_read(path: str) -> list[TextContent]:
    abs_path = (VAULT_ROOT / path).resolve()
    if not str(abs_path).startswith(str(VAULT_ROOT)):
        return [TextContent(type="text", text="error: path escapes vault")]
    if not abs_path.exists():
        return [TextContent(type="text", text=f"error: not found: {path}")]
    text = abs_path.read_text(encoding="utf-8", errors="replace")
    return [TextContent(type="text", text=text)]


def do_list(folder: str | None) -> list[TextContent]:
    prefix = (folder.strip("/") + "/") if folder else ""
    paths = []
    for p in iter_markdown_files(VAULT_ROOT):
        rel = p.relative_to(VAULT_ROOT).as_posix()
        if not prefix or rel.startswith(prefix):
            paths.append(rel)
    paths.sort()
    header = f"# {len(paths)} notes" + (f" under {folder}" if folder else "")
    return [TextContent(type="text", text=header + "\n\n" + "\n".join(f"- {p}" for p in paths))]


async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
