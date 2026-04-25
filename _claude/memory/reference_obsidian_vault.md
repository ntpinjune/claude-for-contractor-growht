---
name: Obsidian vault location and structure
description: Path to user's primary Obsidian vault and its top-level folder layout (reorganized 2026-04-24)
type: reference
originSessionId: d42b9b50-d37c-4297-ae34-2ef64243ac58
---
User's Obsidian vault is at `~/Obsidian/ContractorGrowth`.

Top-level layout (post-reorg 2026-04-24 — coarse buckets):
- `business/` — all business content
  - `business/consulting-calls/` — Jack M mentor call transcripts (was `calls/`)
  - `business/knowledge-hq/` — distilled Jack M + Matt Ryder KB (was `skool/sma-knowledge-hq/`); hub file is `_knowledge-hq-index.md`
  - `business/sops/` — standard operating procedures (was `sops/`)
  - `business/trends/` — trend/market notes incl. `daily-briefs/` (was `trends/`)
  - `business/employees/{alex,jowanna}/call-recordings/` — SDR call recordings
  - `business/gerryk-website/` — Gerryk landscaping client site code (HTML/CSS/JS)
- `notes/` — personal content
  - `notes/journal/` — dated journal entries; hub file is `_journal-index.md`
  - `notes/gym.md`, `notes/school.md`
- `todos/` — daily todo files `YYYY-MM-DD.md`; hub is `_todos-index.md`
- `_archive/` — archived notes incl. `_archive/fathom-raw/` (raw call transcripts)
- `_claude/` — Claude memory (`_claude/memory/`), MCP servers, scripts

**How to use:** Read/write these markdown files directly with Read, Write, Grep, Glob — no MCP server required. An Obsidian vault is just a folder of `.md` files. The vault is the **primary store for everything** — business knowledge AND memory — per user direction on 2026-04-22. Claude memory lives under `_claude/memory/` inside the vault. For semantic search across the vault, use `mcp__obsidian-vault__search_notes`; for exact lookups use Grep/Read.

**Caveat:** Native tools don't auto-update `[[wikilinks]]` on rename. If the user renames a note and wants backlinks updated, do a grep-and-replace across the vault or flag the limitation.
