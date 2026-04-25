---
name: Super-agent vision — one Claude, all context
description: Noah's goal is to build one persistent, fully-contexted AI agent (Claude) that replaces outsourced tools rather than juggling many
type: project
originSessionId: 16927e6f-8cad-4c94-9e4a-7746e403f3c6
---
Noah's working goal: make Claude into an "all-time super agent" — one AI with enough persistent context, memory, and tooling that he stops outsourcing to other AI tools/subscriptions and just uses Claude for everything.

**Why:** Stated directly on 2026-04-23. The core pain is fragmentation — context scattered across ChatGPT sessions, Gemini, Perplexity, Notion AI, etc. Every new tool is a new silo to re-explain himself to. The Obsidian vault + Claude Code + GitHub setup is the foundation of the alternative: one portable context store, any AI that reads markdown.

**How to apply:**
- Default to solving new needs *inside* the existing Claude/vault stack before suggesting a separate tool or subscription. If a new capability (research, memory, design, voice) can be bolted on via MCP, skill, or vault structure, prefer that.
- Two memory layers are live and complementary — don't confuse them:
  1. **Vault RAG** (obsidian-vault MCP, `_claude/mcp-obsidian/`) — semantic search over the Obsidian vault (his curated business knowledge: SOPs, strategy, notes). Auto-reindexes on .md changes via launchd watcher. Uses OpenAI embeddings. Index at `_claude/mcp-obsidian/index.db`.
  2. **MemPalace** (mempalace MCP, `_claude/mempalace/`) — semantic search over past Claude Code *conversations* (working memory — decisions, reasoning, back-and-forth that never became a note). Uses local ONNX embeddings (no API key). Palace data at `~/.mempalace/`. Installed 2026-04-23.
- When Noah asks "can you remember X?", decide which layer it belongs in: documents/SOPs/business knowledge → vault; prior-chat decisions/conversations → MemPalace; user/feedback/project facts → `_claude/memory/` markdown files.
- If recommending a new AI tool, justify why it can't be replaced by a vault note + existing MCP + a Claude skill first.
