---
name: End-of-day review workflow — build the productivity database
description: Every day, Noah talks through what he actually got done; Claude captures it as an EOD Review section appended to that day's todo file. Over time, this builds a searchable database of productive vs unproductive days and which tasks actually moved the needle.
type: project
originSessionId: a5446d86-dba5-41e6-80a9-8efbf0f14b36
---
# End-of-Day Review Workflow

Noah established this on 2026-04-23. It's a daily ritual that runs at the end of each work session.

## The ritual

1. **Noah talks** — walks through what he actually did today, what moved, what didn't.
2. **Claude captures** — appends an `## EOD Review` section to `todos/YYYY-MM-DD.md` with the structure below.
3. **Noah can check off completed items** from the main Today list at the same time (Claude helps him remember what's still open).
4. **Notion sync fires** immediately after (per the always-sync-Notion rule).

## EOD Review section template

Append to the bottom of the day's todo file:

```markdown
## EOD Review (captured {HH:MM})

### What got done today
- [rating] Item — short context ({minutes spent if known})

Where [rating] is one of:
- 🔥 HIGH leverage (moved the needle — revenue, a hire, a system, a coaching win)
- ⚙️ MEDIUM leverage (maintenance, follow-ups, admin that HAD to happen)
- 📎 LOW leverage (busy work, responded to noise, could have been skipped or delegated)

### Revenue / outcomes today
- Closed deals, payments collected, refunds, disputes, new ads launched, people hired/fired, etc.
- Hard numbers only — dollars, count of X, named people

### What I'd skip in hindsight
- Things Noah regrets spending time on (too long, wrong priority, not his job)

### One-sentence productivity call
- "Was today productive?" — honest yes/no/mixed with one-line reason.

### Energy state (optional)
- Noah's subjective sense: energized / drained / focused / scattered
- Useful over time for spotting patterns (sleep, ad-hoc meetings, context switching)
```

## Why this structure

- **Leverage rating** — the point of the system. Frequent vs rare, easy vs hard don't matter. What moved revenue/systems/people vs what was noise. Over weeks, Noah will see how much time went to HIGH vs LOW.
- **Revenue/outcomes** — hard numbers are the only antidote to the "I felt busy" trap.
- **What I'd skip** — explicit retrospective. Pattern-matching across weeks reveals time sinks.
- **Productivity call** — binary forcing function. No "it was okay." Yes or no.
- **Energy state** — weak signal on its own, strong when cross-referenced with calendar, sleep, meeting load.

## How Claude uses the database over time

After ~2 weeks of EOD entries, Claude can:
- Surface Noah's 3 most productive days and what they had in common (no meetings? SDR coaching? certain time of day?)
- Flag recurring LOW-leverage tasks that keep showing up — candidates for delegation
- Connect revenue events to the actions from N days earlier (e.g., an ad check-in on Monday → $300 paid Wednesday)
- Notice when Noah's energy drops mid-week and whether that correlates with meeting density
- Identify his 80/20: which kinds of HIGH-leverage moves produce 80% of the revenue events

Don't do this analysis proactively every day — it's overkill. Do it when Noah asks for a weekly or monthly review, or when he says "how have I been doing."

## How to apply

- Noah says "EOD" / "end of day review" / "let's wrap up" / "go over today" → this workflow triggers.
- Noah starts talking about what he did. Claude listens, captures into the structured section.
- Claude adds rating and leverage judgment based on the task content. If unclear, ASK ("was that high or medium leverage?") — don't guess on a data point Noah will rely on later.
- Sync Notion after (always-sync rule).
- If Noah hasn't set aside dedicated EOD time, Claude can gently prompt at natural wrap-up moments ("want to do the EOD review?") but doesn't force it.

## What NOT to do

- Don't rate tasks with equal confidence. If Noah hasn't said leverage explicitly and it's ambiguous, ask.
- Don't editorialize. The review is Noah's retrospective — Claude captures, doesn't grade him.
- Don't add "AI suggestions" inside the EOD section. Keep it pure data. Observations go in replies, not in the database.
- Don't skip revenue/outcomes because nothing "big" happened — even small numbers are the honest record.
