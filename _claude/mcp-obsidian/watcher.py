"""Watches the vault for .md changes and triggers incremental reindexing.

Debounces bursts of events (Obsidian writes temp files, renames, etc.) so
a single save produces one indexer run, not many. Runs indefinitely as a
launchd agent.
"""
from __future__ import annotations

import subprocess
import sys
import threading
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from common import VAULT_ROOT, EXCLUDE_DIRS

DEBOUNCE_SECONDS = 3.0
HERE = Path(__file__).resolve().parent
INDEXER = HERE / "indexer.py"
VENV_PY = HERE / ".venv" / "bin" / "python"


def log(msg: str) -> None:
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}", flush=True)


class DebouncedIndexer:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._timer: threading.Timer | None = None
        self._running = False

    def trigger(self, reason: str) -> None:
        with self._lock:
            if self._timer:
                self._timer.cancel()
            self._timer = threading.Timer(DEBOUNCE_SECONDS, self._run, args=(reason,))
            self._timer.daemon = True
            self._timer.start()

    def _run(self, reason: str) -> None:
        with self._lock:
            if self._running:
                return
            self._running = True
        try:
            log(f"reindex trigger: {reason}")
            result = subprocess.run(
                [str(VENV_PY), str(INDEXER)],
                capture_output=True, text=True, cwd=str(HERE),
            )
            out = (result.stdout or "").strip().splitlines()
            if out:
                log("indexer: " + out[-1])
            if result.returncode != 0:
                log(f"indexer FAILED rc={result.returncode}")
                err = (result.stderr or "").strip()
                if err:
                    log("stderr: " + err[-500:])
        finally:
            with self._lock:
                self._running = False


def is_excluded(path: Path) -> bool:
    try:
        rel = path.resolve().relative_to(VAULT_ROOT).as_posix()
    except ValueError:
        return True
    for ex in EXCLUDE_DIRS:
        if rel == ex or rel.startswith(ex + "/"):
            return True
    return False


class MarkdownHandler(FileSystemEventHandler):
    def __init__(self, debouncer: DebouncedIndexer) -> None:
        self.debouncer = debouncer

    def on_any_event(self, event) -> None:
        if event.is_directory:
            return
        paths = [event.src_path]
        if hasattr(event, "dest_path") and event.dest_path:
            paths.append(event.dest_path)
        for raw in paths:
            p = Path(raw)
            if p.suffix != ".md":
                continue
            if is_excluded(p):
                continue
            self.debouncer.trigger(f"{event.event_type} {p.name}")
            return


def main() -> int:
    if not VENV_PY.exists():
        log(f"venv python missing at {VENV_PY}")
        return 1
    if not INDEXER.exists():
        log(f"indexer missing at {INDEXER}")
        return 1

    log(f"watching {VAULT_ROOT}")
    debouncer = DebouncedIndexer()
    observer = Observer()
    observer.schedule(MarkdownHandler(debouncer), str(VAULT_ROOT), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        log("stopping")
        observer.stop()
    observer.join()
    return 0


if __name__ == "__main__":
    sys.exit(main())
