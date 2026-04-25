---
name: Daily to-do list workflow
description: Noah talks through his day in conversation; Claude captures tasks into one markdown file per day in `todos/`.
type: project
originSessionId: 2026-04-23-session
---
Noah wants a daily to-do list built from conversation. The workflow:

- Noah talks — could be "I need to do X," "remind me to Y," "today I have to Z," or general stream-of-thought about his plans.
- Claude extracts actionable items and appends them to **today's** to-do file at `todos/YYYY-MM-DD.md`.
- One file per day. Finished days stay as history.

**Why:** Noah is building a single conversational interface for everything. Todos are part of that — he'd rather talk than manually maintain lists. Stated 2026-04-23.

**How to apply:**
- **"My to-do list" = today's list.** When Noah says "my to-do list" at any point, it refers to `todos/<today>.md`. Tomorrow, "my to-do list" means tomorrow's file. Always resolve against the current date, never a fixed one.
- File format: `# Todo — YYYY-MM-DD`, a `## Today` section with `- [ ] item` checkboxes, and a `## Notes` section for context. Keep it minimal — this is working state, not a polished artifact.
- **Every daily list must include a recurring "sync to Notion" task.** Noah wants the list mirrored to Notion so he can view/check it from there. Add `- [ ] Sync today's to-do list to Notion` on every new day's file by default.
- When Noah mentions a task, **add it to today's file immediately** (don't wait for a "save this" request — the whole point is that he talks, I capture).
- If today's file doesn't exist yet, create it. If the date has rolled over since the last session (check the current date vs. the most recent file), start a fresh file for today.
- When Noah says "done with X" or "finished X," check the box in the file.
- When Noah says "move X to tomorrow" or "not today," move it to tomorrow's file (create if needed).
- Things that aren't tasks (random thoughts, observations) go under `## Notes` in today's file OR into the appropriate vault folder if more substantial. Don't bloat the todo list with non-tasks.
- End of day / first session of a new day: offer a one-line look-back ("yesterday you finished X, Y; Z rolled over"). Don't force it, just offer.
