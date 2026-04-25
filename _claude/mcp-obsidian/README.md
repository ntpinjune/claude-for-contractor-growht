# mcp-obsidian

Local MCP server that indexes this Obsidian vault with OpenAI embeddings
(`text-embedding-3-small`) stored in sqlite-vec, and exposes semantic search
as tools to Claude Code.

## Tools

- `search_notes(query, limit)` — semantic search, returns ranked chunks with path + header trail
- `read_note(path)` — full markdown of a vault-relative file
- `list_notes(folder)` — list of vault markdown files, optionally under a subfolder

## Files

- `server.py` — MCP stdio server
- `indexer.py` — CLI to build/update the index
- `common.py` — shared db, embedding, chunking
- `pyproject.toml` — dependencies
- `.env` — `OPENAI_API_KEY` (gitignored)
- `index.db` — sqlite-vec store (gitignored, rebuildable)

## Setup on a new machine

```
cd _claude/mcp-obsidian
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mcp openai sqlite-vec python-dotenv watchdog
echo "OPENAI_API_KEY=sk-..." > .env
.venv/bin/python indexer.py
claude mcp add obsidian-vault --scope user -- \
  "$PWD/.venv/bin/python" "$PWD/server.py"
```

## Reindexing

- Incremental (only changed files): `.venv/bin/python indexer.py`
- Full rebuild: `.venv/bin/python indexer.py --full`

Deleted files are detected and their chunks removed.

## Auto-reindex on file changes

A launchd agent runs `watcher.py` in the background. It watches the vault
recursively, debounces 3 seconds, then triggers an incremental reindex.

```
cp launchd.plist ~/Library/LaunchAgents/ai.contractorgrowth.obsidian-indexer.plist
launchctl load ~/Library/LaunchAgents/ai.contractorgrowth.obsidian-indexer.plist
```

Stop / start / reload:
```
launchctl unload ~/Library/LaunchAgents/ai.contractorgrowth.obsidian-indexer.plist
launchctl load   ~/Library/LaunchAgents/ai.contractorgrowth.obsidian-indexer.plist
```

Live log:
```
tail -f _claude/mcp-obsidian/watcher.log
```

## End-to-end check

```
.venv/bin/python test_e2e.py
```

Verifies index, library search, MCP tool protocol, and the watcher pipeline.

## Swapping embeddings / vector store

Everything goes through `common.py`. Change `EMBED_MODEL` + `EMBED_DIM` to
switch OpenAI models. To swap providers entirely (Voyage, local Ollama,
etc.), rewrite `embed_batch()`. To swap sqlite-vec, rewrite `open_db()`
and the two queries in `server.py` / `indexer.py`. The markdown files
never change — only the glue.
