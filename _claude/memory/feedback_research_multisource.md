---
name: Multi-source research default
description: When Noah asks for research, fan out across all installed web-search MCPs (Exa, Tavily, Brave, Perplexity) + Firecrawl for deep reads — never default to a single source
type: feedback
originSessionId: 7a1d0a13-ac6a-451f-97ce-dcaedb84e546
---
When Noah asks for research ("research X", "do research on it", "look into this", "find me…", "what's out there on…"), fan out across **always-on** research MCPs (Exa + Perplexity) in parallel. For deeper/multi-angle research, restore dormant MCPs (Tavily + Brave + Firecrawl) per `reference_disabled_mcps.md` — ask Noah if it's worth the restart first.

**Why:** Noah set up Brave + Tavily + Exa + Perplexity + Firecrawl for comprehensive multi-angle research. But 3 of those 5 are disabled by default as of 2026-04-24 to save session tokens — they dump prose instructions into context every turn even when unused. Exa + Perplexity handle most needs (semantic discovery + synthesized citations). Escalate to restore the others only when the task genuinely warrants it.

**How to apply — match depth to question (Noah flagged over-searching on 2026-04-23):**
- **Basic / single-fact / "tell me about X" / "what is Y"**: Answer directly from training or one quick lookup. No multi-source fan-out. Examples: "what's OpenCode?", "what does this package do?", "when did X launch?". Over-researching these wastes tokens and time.
- **"Do research on…" / "what's the buzz on…" / "who's building X" / open-ended exploration**: This is when you fan out. Parallel queries across Exa + Tavily + Brave + Perplexity, then Firecrawl the best hits.
- **Fetch-the-thing requests** (user gives a URL and asks about it): Just fetch that URL. Don't also run 4 web searches.
- Use Exa when the query is semantic/conceptual ("companies doing X", "writers covering Y"). Use Brave/Tavily for factual/keyword lookups. Let Perplexity give a synthesized baseline with citations. Firecrawl once you have the 2-3 most valuable URLs.
- If a tool isn't yet connected in the current session (newly installed MCPs require a Claude Code restart), note which are unavailable and use what's available rather than silently degrading to one source.
- When synthesizing multi-source research, cite which source each finding came from so Noah can judge confidence and follow up.
