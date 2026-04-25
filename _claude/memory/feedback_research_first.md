---
name: Research available tools before improvising a fix
description: When solving a problem, spend time learning what tools, skills, MCP connectors, or proven approaches already exist before jumping to a custom solution.
type: feedback
originSessionId: 79cba48b-0dce-4647-83fe-2b75f9066841
---
Before implementing a fix, research what already exists — skills, MCP connectors, plugins, established patterns. Don't jump to the first workaround that comes to mind.

**Why:** Noah explicitly flagged this on 2026-04-23 while fixing the daily-brief routine: "Before you do something, it's just more well informed with what you do. You don't try a bunch of new things." He'd rather I ground the approach in what's available and proven than iterate through homegrown fixes.

**How to apply:** When hitting a limitation (blocked API, missing capability, etc.), first ask: "What tools/skills/connectors exist for this?" Use the claude-code-guide agent or a targeted web search to find existing options. Only fall back to custom workarounds if nothing fits. Applies especially to tooling/infrastructure decisions — less so to one-off code edits.
