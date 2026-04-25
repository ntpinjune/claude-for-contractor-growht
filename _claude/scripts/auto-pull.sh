#!/bin/bash
# Auto-pull the Obsidian vault from GitHub — runs on Claude Code SessionStart hook.
# Best-effort and silent: never blocks session start.

set -u
REPO="$HOME/Obsidian/ContractorGrowth"

[ -d "$REPO/.git" ] || exit 0
cd "$REPO" || exit 0

# If a rebase/merge is mid-flight, don't touch it.
if [ -d "$REPO/.git/rebase-merge" ] || [ -d "$REPO/.git/rebase-apply" ] || [ -f "$REPO/.git/MERGE_HEAD" ]; then
    exit 0
fi

# Only pull if working tree is clean — don't step on user's uncommitted work.
if [ -n "$(git status --porcelain)" ]; then
    exit 0
fi

git pull --rebase --autostash origin main >/dev/null 2>&1 || true
exit 0
