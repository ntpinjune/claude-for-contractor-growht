#!/usr/bin/env python3
"""
Fathom share-link batch downloader.

For each share URL:
  1. Fetch the HTML, parse the embedded JSON from <div id="app" data-page="...">.
  2. Extract call_id, title, host, duration, started_at, copyTranscriptUrl.
  3. Fetch copyTranscriptUrl -> JSON with {"html": "..."}.
  4. Strip HTML, keep speaker/timestamp/text structure, save as plain markdown.
  5. Save metadata JSON alongside.

Output:
  _archive/fathom-raw/<token>.md         # plain-text transcript
  _archive/fathom-meta/<token>.json      # extracted metadata
  _archive/fathom_index.json             # master index
"""

import json
import re
import sys
import html
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

VAULT = Path.home() / "Obsidian" / "ContractorGrowth"
RAW_DIR = VAULT / "_archive" / "fathom-raw"
META_DIR = VAULT / "_archive" / "fathom-meta"
URLS_FILE = VAULT / "_archive" / "fathom_urls.txt"
INDEX_FILE = VAULT / "_archive" / "fathom_index.json"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"

def http_get(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")

def extract_share_token(url: str) -> str:
    return url.rstrip("/").split("/")[-1]

def parse_share_page(html_text: str) -> dict:
    """Extract the data-page JSON from the share page HTML."""
    m = re.search(r'<div id="app" data-page="([^"]+)"', html_text)
    if not m:
        raise ValueError("could not find data-page div")
    raw = html.unescape(m.group(1))
    data = json.loads(raw)
    props = data.get("props", {})
    call = props.get("call", {})
    return {
        "call_id": call.get("id"),
        "title": call.get("title"),
        "topic": call.get("topic"),
        "byline": call.get("byline"),
        "duration_minutes": call.get("duration_minutes"),
        "duration_seconds": props.get("duration"),
        "started_at": call.get("recording", {}).get("started_at") or call.get("started_at"),
        "host_email": call.get("host", {}).get("email"),
        "host_domain": call.get("host", {}).get("company", {}).get("domain"),
        "state": call.get("state"),
        "copy_transcript_url": props.get("copyTranscriptUrl"),
        "action_items_url": props.get("clipboardActionItemsUrl"),
    }

def strip_html_to_transcript(html_blob: str) -> str:
    """Fathom transcript HTML has <p>@TIME - <b>SPEAKER</b></p><p>TEXT</p> structure.
    Convert to plain text: [TIME] SPEAKER: text"""
    s = html.unescape(html_blob)
    # Normalize <br /> to newlines
    s = re.sub(r"<br\s*/?>", "\n", s)
    # Drop anchor wrappers around timestamps, keep the timestamp text
    s = re.sub(r"<a[^>]*>(@\d+:\d+(?::\d+)?)</a>", r"\1", s)
    # Bold speaker names -> keep plain
    s = re.sub(r"<b>([^<]+)</b>", r"\1", s)
    # Convert </p><p>...</p> into line-break structure
    s = re.sub(r"</p>\s*<p[^>]*>", "\n", s)
    s = re.sub(r"<p[^>]*>", "", s)
    s = re.sub(r"</p>", "\n", s)
    # Drop any remaining tags
    s = re.sub(r"<[^>]+>", "", s)
    # Collapse 3+ blank lines
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def process_one(url: str) -> dict:
    token = extract_share_token(url)
    out = {"url": url, "token": token, "ok": False}
    try:
        share_html = http_get(url)
        meta = parse_share_page(share_html)
        transcript_url = meta.get("copy_transcript_url")
        if not transcript_url:
            raise ValueError("no copy_transcript_url in page data")
        raw_json = http_get(transcript_url)
        payload = json.loads(raw_json)
        transcript_html = payload.get("html", "")
        transcript = strip_html_to_transcript(transcript_html)

        # Write files
        raw_path = RAW_DIR / f"{token}.md"
        meta_path = META_DIR / f"{token}.json"
        header = (
            f"# {meta.get('title') or meta.get('topic') or token}\n\n"
            f"- **Share URL:** {url}\n"
            f"- **Call ID:** {meta.get('call_id')}\n"
            f"- **Started:** {meta.get('started_at')}\n"
            f"- **Duration:** {meta.get('duration_minutes')} min\n"
            f"- **Host:** {meta.get('host_email')} ({meta.get('host_domain')})\n"
            f"- **Participants byline:** {meta.get('byline')}\n\n"
            "---\n\n"
        )
        raw_path.write_text(header + transcript, encoding="utf-8")
        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

        out.update({"ok": True, "meta": meta, "bytes": len(transcript)})
    except Exception as e:
        out["error"] = f"{type(e).__name__}: {e}"
    return out

def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    META_DIR.mkdir(parents=True, exist_ok=True)
    urls = [u.strip() for u in URLS_FILE.read_text().splitlines() if u.strip()]
    print(f"Processing {len(urls)} URLs with 6-way parallelism...", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(process_one, u): u for u in urls}
        for i, fut in enumerate(as_completed(futures), 1):
            r = fut.result()
            results.append(r)
            status = "OK" if r["ok"] else f"FAIL: {r.get('error')}"
            title = r.get("meta", {}).get("title", "?") if r["ok"] else "-"
            print(f"[{i}/{len(urls)}] {r['token'][:18]}... {status} | {title}", flush=True)
    INDEX_FILE.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    ok = sum(1 for r in results if r["ok"])
    print(f"\nDone. {ok}/{len(urls)} succeeded. Index: {INDEX_FILE}")

if __name__ == "__main__":
    main()
