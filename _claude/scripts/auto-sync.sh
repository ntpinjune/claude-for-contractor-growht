#!/bin/bash
# Auto-sync the Obsidian vault to GitHub — runs on Claude Code Stop hook.
# Best-effort and silent: never propagates errors, so session exit is never blocked.
#
# Configure VAULT_DIR to point at where you cloned this vault locally.

set -u
REPO="${VAULT_DIR:-$HOME/Obsidian/vault}"

# Silent no-op if the vault is missing or not a git repo.
[ -d "$REPO/.git" ] || exit 0
cd "$REPO" || exit 0

# If a previous rebase/merge is mid-flight, leave it alone so we don't stomp on user state.
if [ -d "$REPO/.git/rebase-merge" ] || [ -d "$REPO/.git/rebase-apply" ] || [ -f "$REPO/.git/MERGE_HEAD" ]; then
    exit 0
fi

# No working-tree changes? Still try to push any local commits ahead of origin, then exit.
if [ -z "$(git status --porcelain)" ]; then
    git push origin main >/dev/null 2>&1 || true
    exit 0
fi

git add -A >/dev/null 2>&1
git commit -m "auto-sync: $(date '+%Y-%m-%d %H:%M:%S')" >/dev/null 2>&1 || true

# Pull + push. If rebase fails (conflict), abort it so the repo stays clean for next run.
if ! git pull --rebase origin main >/dev/null 2>&1; then
    git rebase --abort >/dev/null 2>&1 || true
    exit 0
fi
git push origin main >/dev/null 2>&1 || true

exit 0
