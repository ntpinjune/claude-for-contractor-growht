# Obsidian Vault Template

A starter Obsidian vault wired up for Claude Code as a long-term second brain.

## What's in here

```
.
├── .claude/                  Claude Code project config + custom agents
│   └── agents/
│       └── daily-business-brief.md   custom agent that writes a daily tech brief
├── .obsidian/                Obsidian app settings (clean defaults)
├── _claude/
│   ├── CLAUDE.md             global instructions Claude reads every session
│   ├── memory/               auto-memory system (persistent across sessions)
│   │   └── MEMORY.md         index — empty to start, fills in over time
│   ├── mcp-obsidian/         local MCP server: semantic search across the vault
│   ├── mempalace/            (placeholder) prior-conversation RAG
│   └── scripts/
│       ├── auto-pull.sh      pulls vault from GitHub on session start
│       └── auto-sync.sh      commits + pushes vault on session end
├── business/                 your operational docs (sops, employees, etc.)
├── clients/                  per-client notes
├── ideas/                    half-baked thoughts
├── notes/                    journal, freeform notes
├── templates/                Obsidian note templates
├── todos/                    daily to-do files
└── trends/                   daily briefs from the agent
```

The folder tree is opinionated but optional — rearrange to your taste.

## Setup

### 1. Clone the repo

```bash
git clone <this-repo-url> ~/Obsidian/vault
cd ~/Obsidian/vault
```

### 2. Open in Obsidian

Open Obsidian → "Open folder as vault" → pick `~/Obsidian/vault`.

### 3. Set up Claude Code

If you don't have it: install from https://claude.com/claude-code.

Then point Claude Code at the memory directory. Edit `~/.claude/settings.json` and add:

```json
{
  "autoMemoryDirectory": "~/Obsidian/vault/_claude/memory"
}
```

Symlink the global CLAUDE.md so Claude loads it every session:

```bash
ln -s ~/Obsidian/vault/_claude/CLAUDE.md ~/.claude/CLAUDE.md
```

(Windows: `New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\CLAUDE.md" -Target "$env:USERPROFILE\Obsidian\vault\_claude\CLAUDE.md"` from an admin PowerShell or with Developer Mode on.)

### 4. Customize the prompt

Open `_claude/CLAUDE.md` and fill in the `> Customize this section` blocks — your role, your work context, any standing rules. Claude will read this every session.

### 5. (Optional) Install the local Obsidian MCP server

This adds semantic search across your vault as a Claude Code tool. Requires an OpenAI API key for embeddings.

```bash
cd _claude/mcp-obsidian
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mcp openai sqlite-vec python-dotenv watchdog
echo "OPENAI_API_KEY=sk-..." > .env
.venv/bin/python indexer.py
claude mcp add obsidian-vault --scope user -- \
  "$PWD/.venv/bin/python" "$PWD/server.py"
```

To auto-reindex on file changes, see [`_claude/mcp-obsidian/README.md`](_claude/mcp-obsidian/README.md).

### 6. (Optional) Auto-sync to GitHub

The `scripts/auto-pull.sh` and `auto-sync.sh` files are designed to run as Claude Code SessionStart and Stop hooks. They keep your vault synced across machines silently.

To wire them up, edit `~/.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      { "matcher": "*", "hooks": [{ "type": "command", "command": "VAULT_DIR=$HOME/Obsidian/vault $HOME/Obsidian/vault/_claude/scripts/auto-pull.sh" }] }
    ],
    "Stop": [
      { "matcher": "*", "hooks": [{ "type": "command", "command": "VAULT_DIR=$HOME/Obsidian/vault $HOME/Obsidian/vault/_claude/scripts/auto-sync.sh" }] }
    ]
  }
}
```

### 7. (Optional) Daily business brief agent

The `.claude/agents/daily-business-brief.md` file defines a custom agent that scrapes Hacker News, Reddit, and Product Hunt each morning and writes a brief to `business/trends/daily-briefs/`. Edit the "The user" section in that file to match your niche, then either invoke it manually (`/agents` → daily-business-brief) or schedule it via Claude Code's `/schedule` command.

## How the auto-memory system works

When Claude Code starts a session, it reads `_claude/memory/MEMORY.md` (which is the index) into context. As you work, Claude saves new memories — your role, preferences you've stated, project context — to individual files in `_claude/memory/` and adds a one-line entry to the index.

There are four memory types:
- **user** — who you are, how you work
- **feedback** — corrections you've given Claude or approaches you've validated
- **project** — ongoing work, deadlines, why decisions were made
- **reference** — pointers to external systems (Linear, dashboards, etc.)

You can also explicitly ask Claude to "remember X" to force-save something, or "forget X" to remove a memory.

## Notes

- Empty directories use `.gitkeep` files so they persist in git. Delete them once you have real content.
- The `_claude/mcp-obsidian/index.db` and `.venv/` are gitignored — they're rebuilt on each machine.
- Workspace layout (`.obsidian/workspace*`) is gitignored too, so each machine keeps its own panel arrangement.
