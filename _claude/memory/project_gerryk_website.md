---
name: Gerryk website — parked pending domain transfer
description: Landscaping site deployed to Vercel for Gerryk; content swap + live-domain cutover blocked on $14 Square domain-transfer completing
type: project
originSessionId: 35e4295e-c3fc-4cf7-a7a7-a6f0e38f463e
---
Gerryk (landscaping client) website is live at **https://gerryk-website.vercel.app** — deployed 2026-04-23 from `business/gerryk-website/` (moved from `~/Obsidian/ContractorGrowth/gerryk-website/` during 2026-04-24 vault reorg).

**Status:** fully functional, 91 PageSpeed mobile / 98 desktop, SEO 100/100. Template is Bayshore-style landscaping site rebranded to Gerryk. All 5 pages work: home, about, services, areas, gallery, contact.

**Current blocker (2026-04-24):** Noah is logged into Gerryk's Square account and paid $14 to initiate a domain transfer *to* Square. Now just waiting for the transfer to complete — no action on our side until it lands. Once it does, we pull real content from Square + point the transferred domain at Vercel.

**Still need (once unblocked):**
- Pull real project photos (current site uses stock landscape images)
- Copy over real business info (phone, email, address, license #, founder bio all placeholder)
- Export real testimonials (current ones are pravatar-faced fakes)
- Do the DNS swap from Square → Vercel

**Why:** pointing his real domain at the current Vercel build would show fake content to visitors — worse than the Square site. Need real content first, then domain transfer.

**How to apply:** when the domain transfer lands in Square, resume by: (1) pulling Square content (photos, copy, testimonials), (2) swapping placeholders in the HTML, (3) adding real photos to `business/gerryk-website/photos/`, (4) redeploying, (5) then DNS swap (A record `@` → Vercel IP, CNAME `www` → cname.vercel-dns.com).

**Placeholders still to replace** (grep before swapping):
- Phone `(650) 716-7231`
- Email `gerryklandscapingco@gmail.com`
- License `C-27 #1098432`
- Address `Redwood City 94063`
- Founder bio in index.html story section
- Testimonials in index.html
- Service area cities (currently SF Peninsula — may be wrong)
