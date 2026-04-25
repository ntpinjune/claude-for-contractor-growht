---
name: Disabled MCPs — restore on demand
description: Pre-configured MCP servers that were trimmed to save tokens. Stashed configs at `reference_disabled_mcps_configs.json`. When Noah says "use tavily / brave / firecrawl / stripe / [etc]", re-add it to `~/.claude.json` mcpServers and tell him to run `/reload-plugins` or restart.
type: reference
originSessionId: 8112a1f2-b855-417f-9e0b-d90014ac9587
---
## What's disabled locally

Stashed in `~/.claude/disabled_mcps_configs.json` (kept outside git — contains API keys) (not in index — config blob, not human-readable knowledge):
- **brave-search** — web search
- **firecrawl** — advanced scraping / crawl
- **tavily** — research-grade search
- **stripe** — Stripe account/API

## When to restore

Noah says something like "use tavily," "scrape with firecrawl," "check Stripe," etc. Or multi-source research explicitly requires fan-out beyond Exa + Perplexity.

**To restore:**
1. Read `reference_disabled_mcps_configs.json`
2. Merge the requested server back into `~/.claude.json` under `mcpServers`
3. Tell Noah to run `/reload-plugins` (faster) or restart Claude Code
4. Confirm it loaded before using

## What's always on (local)

`mempalace`, `obsidian-vault`, `fathom`, `exa`, `perplexity` — these stay. Core research + memory + meetings.

## claude.ai-side connectors (not controllable from here)

Noah manages these at claude.ai web UI. As of 2026-04-24, these are ON and loading instructions every turn:
Canva, Miro, Stripe, Fathom (duplicate of local), Gmail, Google Calendar, Google Drive, Notion.

Recommend Noah disconnects anything not actively used. **Disconnect Fathom for sure** (duplicate of local). Gmail/Calendar/Drive/Notion keep only if he uses them daily.
