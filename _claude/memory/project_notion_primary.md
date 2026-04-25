---
name: Obsidian vault is the primary knowledge source
description: All business context, documents, and knowledge live in the Obsidian vault — not Notion. Check the vault first for any business question.
type: project
originSessionId: bf05e759-138b-489a-a930-8626ed895b16
---
The Obsidian vault at `~/Obsidian/ContractorGrowth` is the durable source of truth for this user's business context AND Claude's memory system. Notion is no longer primary — do not search it first. User stated on 2026-04-22 that Obsidian should be the main storage for "basically everything" including memory.

**Why:** User has consolidated on Obsidian. The vault is already where call transcripts, SOPs, clients, ideas, and trends live, and it has a local MCP server (`mcp__obsidian-vault__*`) that provides semantic search. Putting memory in the same place keeps everything co-located and version-controlled in git.

**How to apply:**
- For any business question, search the vault first (`mcp__obsidian-vault__search_notes` for semantic, or Grep/Read for exact). Don't reach for Notion unless the user specifically asks.
- When the user asks to "remember" or "save" something business-related, write it into the vault as a markdown file under `business/` (e.g. `business/sops/`, `business/trends/`, `business/consulting-calls/`) or `notes/` for personal content — not into Notion.
- Memory files still live under `_claude/memory/` inside the vault — that's unchanged, and they're already in the right place.
- If the user does ask about Notion specifically, it still exists as a connector, but treat it as secondary/archival.
