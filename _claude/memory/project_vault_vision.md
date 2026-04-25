---
name: Vault vision — centralized, long-term second brain
description: The vault is Noah's lifelong centralized knowledge system. Claude + vault replaces scattered use of NotebookLM, Gemini, etc. Everything goes here, grows slowly over time.
type: project
originSessionId: 2026-04-22-session
---
The Obsidian vault at `~/Obsidian/ContractorGrowth` is being built as Noah's **centralized, long-term second brain** — a durable knowledge system that will grow over years. Claude is the primary interface; the vault is the storage.

**Why:** Noah currently uses NotebookLM (for grounded truth), Gemini, Claude, and others — but none of them share context, so knowledge is scattered. The setup now: one vault → searchable via `mcp__obsidian-vault__*` (semantic RAG) → Claude reads and writes it → everything is durable and accumulates instead of evaporating into separate chat histories. Noah trusts Claude's intelligence but was missing the centralized long-memory layer; the vault + MCP solves that. Stated 2026-04-22.

**How to apply:**
- **Default to writing back to the vault.** When Noah shares a document, pastes info, or talks through something non-trivial, save it to the right folder instead of letting it live only in the conversation. Even rough notes are better than nothing — they become searchable context for future sessions.
- **Default to searching the vault first.** Before answering any substantive question, run `mcp__obsidian-vault__search_notes` to check what's already in there. Don't rely on memory of past conversations; rely on what's in the files.
- **The vault is multi-area, not just business.** Noah's eventual target is broad top-level buckets like `personal/`, `business/`, `journal/` with nested subfolders (e.g. `insights/`). Current vault is still business-heavy; life-area structure will be added only when Noah explicitly asks for it, not preemptively from context he shares about himself.
- **Treat this as compounding.** Small regular additions beat big one-off dumps. When Noah mentions something in passing that's worth remembering, offer to save it.
- **Don't silo.** Cross-reference across areas when useful — a journal entry might reference a call; a Stanford note might tie to a business idea. Markdown links and semantic search make this work.
