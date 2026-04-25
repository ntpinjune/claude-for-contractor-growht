# claude-config

Personal Claude Code config, memory, and skills, synced across Mac and Windows via this private repo.

## What's in here

- `CLAUDE.md` — global instructions loaded into every Claude Code session
- `memory/` — auto-memory files (user profile, feedback, project context, references)
- `skills/` — custom skills (empty for now)

## Wiring a new machine

**1. Clone this repo** somewhere sensible:

```
git clone git@github.com:ntpinjune/claude-memory.git ~/claude-config
```

**2. Point Claude Code at it.** Edit the Claude settings file:
- Mac/Linux: `~/.claude/settings.json`
- Windows: `%USERPROFILE%\.claude\settings.json`

Add:
```json
{
  "autoMemoryDirectory": "~/claude-config/memory"
}
```

**3. Symlink `CLAUDE.md`** so Claude Code finds it in its usual location.

Mac/Linux:
```
ln -s ~/claude-config/CLAUDE.md ~/.claude/CLAUDE.md
```

Windows (PowerShell as Admin, or with Developer Mode enabled):
```
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\CLAUDE.md" -Target "$env:USERPROFILE\claude-config\CLAUDE.md"
```

## Day-to-day workflow

- Before a session on a machine you haven't used in a while: `cd ~/claude-config && git pull`
- After a session where memory changed: `git add -A && git commit -m "update memory" && git push`

If you forget to pull and edits diverge, you'll get a merge conflict in a memory file — resolve by keeping the newer content.
