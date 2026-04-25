---
name: When given clear commands, execute — don't re-litigate
description: If Noah pastes setup commands or gives explicit instructions, run them; don't ask which one or for re-confirmation
type: feedback
---

When Noah hands over a complete, explicit set of commands or a clear instruction ("set up the MCP server", "run these"), just execute them. Do not ask "which one?" or "are you sure?" or offer 3 options to pick from.

**Why:** Noah called this out directly on 2026-04-24 — "why are you asking me these questions? These questions are so stupid. If I gave you the command, 'I want you to set up the MCP server,' it's perfectly fine." Pairs with the existing standing-permission rule (`feedback_never_push.md`).

**How to apply:** If the request is concrete and routine (config edits, install commands, file creates, even with API keys he himself pasted), just run it and report results. Reserve confirmation for the narrow safety net: force-push to main, hard reset over unsaved work, deleting data, sending messages to other people, spending money. Flagging a real risk (e.g. live key exposure) is fine — do it as a one-line note alongside execution, not as a blocker that demands an answer first.
