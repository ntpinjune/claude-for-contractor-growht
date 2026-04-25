# Google Docs MCP Setup — one-time

Goal: give Claude the ability to edit existing Google Docs in place (find/replace, insert sections, delete ranges). Once done, any future conversation in this vault can edit any Google Doc you own.

**Time:** ~8 minutes. ~5 in Google Cloud Console, ~3 in terminal.

---

## Part 1 — Google Cloud Console (your browser, your Google account)

### 1. Create a project

1. Open [console.cloud.google.com](https://console.cloud.google.com).
2. Log in as **noah@contractorgrowth.ai**.
3. Top-left project dropdown → **New Project**.
4. Name it: `contractor-growth-mcp` (or whatever you want). Organization: leave default. Click **Create**.
5. Wait ~10 sec, then switch to the new project in the same dropdown.

### 2. Enable the three APIs you need

Go to **APIs & Services → Library**, search for and **Enable** each of:

1. **Google Docs API**
2. **Google Drive API**
3. **Google Apps Script API**

(Each one takes 5 seconds — search, click, Enable, back, repeat.)

### 3. Configure the OAuth consent screen

1. Left sidebar → **APIs & Services → OAuth consent screen**.
2. User Type: **External**. Click **Create**.
3. App name: `Contractor Growth MCP`
4. User support email: your email
5. Developer contact: your email
6. **Save and Continue** through Scopes (leave empty) and Test Users.
7. Test Users → **Add Users** → add `noah@contractorgrowth.ai`. **Save**.

(You don't need to submit for verification — test user access is enough.)

### 4. Create OAuth Client ID

1. Left sidebar → **APIs & Services → Credentials**.
2. Top → **Create Credentials → OAuth client ID**.
3. Application type: **Desktop app**.
4. Name: `google-docs-mcp`. **Create**.
5. In the popup, click **Download JSON**. Save it to your Downloads folder.
6. Move it to `~/credentials.json`:
   ```bash
   mv ~/Downloads/client_secret_*.json ~/credentials.json
   ```

**Done with Cloud Console.** You now have `~/credentials.json`.

---

## Part 2 — Tell me "ready"

Once `~/credentials.json` exists, tell me "ready" in chat. I'll run:

1. `uv tool install --from git+https://github.com/dbuxton/google-docs-mcp google-docs-mcp` — installs the MCP
2. `google-docs-mcp-auth --credentials ~/credentials.json` — opens a browser, you approve, token saved to `~/.google-docs-mcp/token.json`
3. `claude mcp add google-docs ...` — registers it so Claude can call it

Then we restart the session (`/mcp` to verify), and I start making the actual edits to your training docs.

---

## What this will be used for (immediate)

1. Find/replace "Phantom" → "Fathom" in `CG_Sales_Rep_Training` (Sales Rep Master) and any other doc that has it.
2. Rewrite the "Our Offer — Pricing & Structure" section of `CG_Sales_Rep_Training` to $1,000 setup + $150/booked + $44/day (remove Options A/B).
3. Unlink / delete the Remodelling Sales Framework reference from Sales Rep Master.
4. Replace the `CG_Setter_&_Closing_Script` content with the v2 script already drafted at [sops/sdr-setter-script-v2.md](sdr-setter-script-v2.md).
5. Remove the hardcoded Jowanna booking link from the setter script.

---

## Gotchas

- **Scope creep risk:** the OAuth consent grants read/write to ALL your Google Docs and Drive files — not just the ones we're editing. If you want to limit blast radius, create a secondary Google account and share only the training docs with it, then OAuth as that account. Otherwise, trusting it is same as trusting any app with Drive access (Notion, Zapier, etc.).
- **Token lifetime:** refresh tokens last indefinitely unless you revoke in Google Account → Security → Third-party apps. If you ever want to kill access, revoke there.
- **Test user cap:** external apps in test mode allow up to 100 test users — more than enough.

---

## Why this MCP (dbuxton/google-docs-mcp)

- Search-by-text, not character indices. LLMs are bad at index math — the default Google Docs API design makes edits fragile. This wrapper abstracts that away.
- Standalone, ~2k lines of Python, easy to audit. 2 GitHub stars because it was published April 2026, not because it's bad.
- Alternative (`a-bonus/google-docs-mcp`, 483 stars) works but gives Claude full Gmail + Calendar + Drive + Sheets access — larger blast radius than we need for this job.
