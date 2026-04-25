---
name: Daily todos must ALWAYS stay synced Obsidian → Notion (no batching, no judgment)
description: Every single edit to a daily todo file in the vault triggers an immediate Notion page update in the same turn — no exceptions, no waiting to batch changes
type: project
originSessionId: afccd839-a643-4618-bdae-67f90fc86daf
---
Daily todos live in `todos/YYYY-MM-DD.md` (vault = source of truth). Noah also wants them accessible on his phone, so mirror each day's list as a Notion page titled `📋 Todo — YYYY-MM-DD` at workspace root (no parent page, he organizes manually if he wants).

**Why:** Noah works on mobile throughout the day. Vault markdown isn't viewable on phone in any ergonomic way; Notion is. He asked for this explicitly on 2026-04-23, and on the same day reinforced that ANY drift between the two sources is a problem — he doesn't want to wonder which version is current.

**How to apply:**
- **EVERY edit to `todos/YYYY-MM-DD.md` — even a single added line — triggers an immediate matching Notion page update in the same turn.** No "substantial change" threshold. No batching multiple edits before syncing. If you wrote to the vault todo file, your next action is to sync Notion before you reply to Noah.
- Use Notion to-do syntax (`- [ ]` / `- [x]`) so items are tappable checkboxes on mobile.
- Group by section headings (Claude/tooling, Business ops, Web/engineering, Research) — easier to scan on a small screen.
- Include a "Done today" section at bottom so progress is visible.
- First sync of 2026-04-23 went to page ID `34b3ebbf-0f35-81fd-a1d2-c00291850136`. Future days = new pages (one per day).
- Don't attempt to two-way sync (Notion → vault). If Noah checks an item off on phone, the vault file stays stale until he tells Claude in conversation. A proper two-way sync would need a background job — flag that as a future project if it becomes a pain point.
