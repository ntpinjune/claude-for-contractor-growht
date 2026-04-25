---
name: Daily business brief system
description: Scheduled remote agent that scouts tech/AI launches each morning and drops a business-angle brief into the vault. Where the pieces live and how they fit together.
type: reference
originSessionId: 79cba48b-0dce-4647-83fe-2b75f9066841
---
**Daily briefs land at**: `business/trends/daily-briefs/YYYY-MM-DD.md` in the Obsidian vault (path updated 2026-04-24 vault reorg; local agent prompt updated — the remote scheduled routine in claude.ai may still need its prompt refreshed).

**Schedule**: Remote routine `daily-business-brief` (id: `trig_017hQHG2gLSUY8xtSx4pFQ6o`) runs `0 15 * * *` UTC = 8am PDT / 7am PST daily. Manage at https://claude.ai/code/routines/trig_017hQHG2gLSUY8xtSx4pFQ6o

**What it scans**: Hacker News (top + newest), Reddit (r/SideProject, r/Entrepreneur, r/ClaudeAI, r/LocalLLaMA, r/OpenAI, r/ArtificialIntelligence), Product Hunt, web search queries for recent launches.

**Output shape**: TL;DR → What launched (raw) → Patterns → Business angles for Noah → Worth a deeper look. Business angles flag contractor/local-services fit when it applies.

**Manual local invocation**: subagent file is at `.claude/agents/daily-business-brief.md`. From any Claude Code session in the vault, say "run my daily brief" to trigger it.

**Known dependency**: Remote routine needs GitHub connected for ntpinjune/claude-memory to clone + push. If schedule silently stops working, check https://claude.ai/customize/connectors and re-run /web-setup.
