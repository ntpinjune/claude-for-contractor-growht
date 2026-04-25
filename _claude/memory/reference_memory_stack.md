---
name: Memory stack — vault RAG + MemPalace + markdown memory
description: Three-layer memory architecture. Vault RAG for documents, MemPalace for past conversations, markdown memory for curated facts
type: reference
originSessionId: 16927e6f-8cad-4c94-9e4a-7746e403f3c6
---
Noah runs three complementary memory layers. Each solves a different retrieval problem.

**Layer 1 — Curated markdown memory** (`_claude/memory/`)
- What: Typed memory files (user/feedback/project/reference) + `MEMORY.md` index, auto-loaded into every Claude Code session via `autoMemoryDirectory` in `~/.claude/settings.json`.
- When to use: Small, durable facts. User preferences, project state, external references, feedback rules. Things you want available in every session without searching.
- Size: ~16 files as of 2026-04-23.

**Layer 2 — Vault RAG** (obsidian-vault MCP)
- What: Semantic search over the Obsidian vault's markdown. OpenAI embeddings, ChromaDB-style chunks. Auto-reindexed on file changes by launchd watcher `ai.contractorgrowth.obsidian-indexer`.
- Code: `_claude/mcp-obsidian/` (server.py, indexer.py, watcher.py). Index: `_claude/mcp-obsidian/index.db`. Uses OpenAI key in `.env`.
- MCP tools: `search_notes`, `read_note`, `list_notes`.
- When to use: Find SOPs, strategy docs, client notes, trends, ideas — anything Noah has *written down* into the vault.
- Scale: 2,743 chunks / 54 files as of setup.

**Layer 3 — MemPalace** (mempalace MCP)
- What: Semantic search over past Claude Code *conversations* mined from `~/.claude/projects/`. Local ONNX embeddings (all-MiniLM-L6-v2), no API key required. ChromaDB-backed.
- Code: `_claude/mempalace/` (venv only). Palace data at `~/.mempalace/` (binary, not in git).
- CLI: `.venv/bin/mempalace search "query"` / `mempalace status` / `mempalace mine <dir> --mode convos --wing <name>`.
- Wings: `contractor_growth` (vault sessions), `home_dir` (general), `claude_config` (config work). 2,387 drawers as of 2026-04-23.
- When to use: Find reasoning/decisions from past chats that never became a note. "Why did we decide X?" "What were the 3 options Claude gave me?"
- Re-mining: run `mempalace mine ~/.claude/projects/<project-folder>/ --mode convos --wing <name>` periodically to capture new sessions.

**Decision tree — which layer to query:**
- Is it a user preference or permanent fact? → `_claude/memory/` markdown (already auto-loaded, no search needed)
- Is it a document or note Noah wrote? → Vault RAG (search_notes)
- Is it something discussed in a past Claude chat? → MemPalace (mempalace search)
- Not sure? → Try vault RAG first (user-curated = higher signal), then MemPalace.
