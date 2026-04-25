# SDR Training Audit — 2026-04-23

Audit of the three linked training docs + the index doc. Ranked by revenue impact, not tidiness.

## ✅ Ground truth confirmed by Noah 2026-04-23

- **Actual offer:** $1,000 setup + $150 per booked appointment + $44/day ad spend (client pays ad spend direct to platform)
- **Setter script is bait-and-switch** — confirmed, must be rewritten to match actual offer
- **Remodelling Sales Framework (`1UNT_P...`) — DELETE.** We don't run upfront-package deposits. Archive or unlink from Sales Rep Master.
- **Tool is Fathom**, not Phantom. Find-and-replace everywhere.


## Docs audited

1. **Index / TRAINING** — `1p0b7oyYQzrzYBM4YubsNWoXI1yv6RSTv7Hff70P2vaM` (thin — a link list, not a doc)
2. **Sales Rep Master** — `18TZFekRUij2a-1cxuur6fr0U2i8AaXu2DgC0ItQyobA` (the closer master)
3. **Setter + Closing Script** — `1ZCuFmB7aIqJNg-P-92YDtcfhdgTZDCvhTotpvO6r0-I` (despite the name, setter-only)
4. **"Sales Script" / Remodelling Sales Framework** — `1UNT_PrlXxbrp7hX4OTcwWj0LYcxyfD5h0R1ac3GDJ0k` (linked from Sales Rep Master as "Sales Script")

---

## The big problem: three incompatible offer models across three docs

A new rep reading top-to-bottom gets three completely different answers to "what are we selling?"

| Doc | Offer model | What rep is told |
|---|---|---|
| **Sales Rep Master** | Pay-per-appointment + setup | Setup $250-1,500 + $150/booked OR $250/shown, $44/day ad spend min |
| **Setter + Closing Script** | Pay-per-job, NOTHING upfront | "No monthly subscription, no upfront — we send estimates, you pay on results" |
| **Remodelling Script** | Upfront deposit packages | $1,500 / $3,000 / $12,000 paid UPFRONT for 15 / 45 / 300 appointments, $50/day ad spend min |

This is not a minor inconsistency — it is three different businesses.

**Ground truth (Jack M, via `business/knowledge-hq/Pricing & Offers.md`):**
- Pay-per-appointment (**auto-charge, not upfront**) is BEST for scaling
- Setup fee $197-$350 — **not $250-1,500, not $12,000 upfront**
- Monthly retainer / big upfront deposits: **"DO NOT USE"** (Jack's words)
- $150-250 per shown appointment
- Never call a lead a "lead" — call it an "estimate request"

The Setter script's language ("we send estimates, pay on results") is closest to Jack's canonical positioning. The Sales Rep Master is *directionally* right but setup fee ranges too high. The Remodelling Script's upfront-package model is the one Jack explicitly warns against.

**Why this matters for revenue:** A setter selling "nothing upfront, pay-per-job" who hands off to a closer pitching "$1,500 upfront + $150/appt" is a bait-and-switch. Prospects who show up to the closer call got sold on a completely different offer. Show-up-to-close conversion collapses. This is likely one of the bigger reasons Jowanna's batch scored 0/5 closes.

---

## Conflicts (ranked by revenue impact)

### 1. Ad spend minimum — three different numbers
- Sales Rep Master: $44/day ($308/week)
- Remodelling Script: $50/day ("example: $50 = 3,000 impressions")
- Index doc's "44 dollars a day x 7 ($319)" payment link → confirms $44 was a real number at some point
- Fix to one number. Update the Stripe link if the number changes.

### 2. The call framework — two competing flows for the closer
- **Sales Rep Master** (6-stage): Intro → KYC (20-30 min) → ROI Build → Temp Check → Price Drop → Show Path/Assumptive Close
- **Remodelling Script** (10-step, Hell/Bridges/Heaven/Fuel): Intro → Agenda → HBHF Discovery → Pre-Pitch → Pitch → Questioning → Temp Check → Logistics/Price Drop → Seal
- A rep is told to "memorize" both. They can't.

### 3. Objection handling — three different frameworks
- Sales Rep Master teaches **Parrot → Clarify → Guard Drop → Isolate → Handle → Question-Based Close** (Jack M / Matt Ryder)
- Setter script has 4 one-line scripted rebuttals
- Remodelling Script has a full NLP-reframe style objection library that does NOT use the parrot-clarify-guard-drop-isolate-handle structure — it's a different school

All three can be useful, but not presented as "the objection framework." A rep reading all three won't know which one to run live.

### 4. "Phantom" vs "Fathom" used interchangeably
- Sales Rep Master says "Phantom is how we record every single call" then links `fathom.ai` two lines later
- Internal SOP also says "Phantom is running and recording BEFORE the call starts"
- The tool is **Fathom**. "Phantom" is a persistent branding error that makes reps look foolish if they use "Phantom" with a client.

### 5. Conflicting openers
- Setter script opener: *"Hey, did you see the message my assistant Alice sent over…"*
- Remodelling script opener: *"You are calling from STATE, right? That's great my uncle actually lives out over in CITY"*
- These are totally different call personas. Pick one.

### 6. "Setter + Closing Script" has no closing content
The doc titled `CG_Setter_&_Closing_Script` contains a setter script + 4 objection handles only. There is no closing section. The Loom-TODO in the index doc confirms this: *"make new loom with updated setter script with closing part."* The name is misleading.

### 7. Jowanna's booking link hardcoded in the setter script doc
The Setter script ends with: *"Booking link: https://api.leadconnectorhq.com/widget/booking/YlZ4kvDiLE6w6px8wni5"* — that's Jowanna's link. If Jay or Alex reads this doc, they'll send the wrong link. Should be a `{{your_booking_link}}` placeholder or a "find yours in the index doc" note.

### 8. Two different "sales scripts"
The index links to `CG_Setter_&_Closing_Script` (`1ZCuFm...`). The Sales Rep Master links to a totally different "Sales Script" (`1UNT_P...` — the Remodelling framework). A rep opening both ends up studying two different call flows. Decide which is canonical.

### 9. "KYC" duration
- Sales Rep Master: "20–30 minutes of questions"
- Remodelling Script Discovery (Hell/Bridges/Heaven/Fuel): no duration
- Setter Script: ~3-5 min of questions before 20-min ask

### 10. Positioning as "owner"
- Setter script: explicitly says "Act as the owner — not a setter. Use your own name." And the closer reveals "I'm [Your Name], the business owner" at the end.
- Sales Rep Master: silent on this. Implies rep is a closer, not the owner.
- If a setter says "I'm the business owner" and then the closer call is with a *different* person, prospects feel conned.

---

## Gaps (missing content claimed or implied but not delivered)

### Critical
- **No Testimonials Sheet link.** Section 7 of Sales Rep Master names it as a resource, provides no link. Reps told to "pull this up immediately" when asked for reviews have nothing to pull.
- **No pitch sheet.** Sales Rep Master describes a pitch sheet with niche-specific openers, KYC question bank, ROI templates, price drop language. No link. The "Contractor Growth System Demo" GHL preview is linked but that's the product demo, not a pitch sheet.
- **No actual closer script / closer Loom.** Acknowledged as TODO in the index doc itself.
- **No contract link.** Remodelling Script says "we will sign the contract" — no link.
- **No onboarding form link.** Remodelling Script says "I will send you the onboarding form" — no link.

### Important
- **No KPI targets.** Sales Rep Master says you'll be evaluated on show rate, close rate, ACV, cash collected, but never states the targets.
- **No follow-up SOP.** "Not following up with a prospect who asked for time" will get a rep fired, but there's no defined cadence, script, or channel for follow-up.
- **No EOD report template.** Required but no format given.
- **No refund/guarantee policy unified.** Remodelling Script promises "full refund + $1,500" if appointments aren't delivered. Other docs say nothing. If a client invokes the guarantee, which rule applies?
- **No pre-call research checklist.** Says "know every prospect's name, niche, and notes before the call" — doesn't say how to research (website, Maps, social).

### Nice-to-have
- **No analysis of the 3 closed-deal Fathom recordings.** They're linked but no timestamped notes ("at 14:22, watch the price drop handle"). Asking a new rep to "take notes" on a 60-min call is low yield without signposts.
- **No daily metrics expectation.** Sales Rep Master mentions EOD reports but not daily dial/conversation targets.

---

## Confusion points (not conflicts, but likely to trip up a new rep)

1. **Doc naming.** `CG_Setter_&_Closing_Script` implies both parts are there. Only the setter part is.
2. **"Sales Script" is ambiguous** — which of the two sales scripts is the real one?
3. **Offer name sprawl.** "Pay-per-job," "pay-per-appointment," "pay-on-results," "PPSA" all used without a glossary. They mean different things.
4. **The index doc includes a TODO as if it's a resource** — *"make new loom with updated setter script with closing part."* That line is in the live training doc reps read.
5. **No "who is this doc for" label.** Sales Rep Master is clearly for closers. Setter script is for setters. But there's no header that says so — a new rep reads both and tries to merge them.

---

## Recommended fix order (highest-leverage first)

**1. Pick one offer model and delete the others.** Not a light rewrite — surgery. Per Jack: pay-per-appointment, auto-charge, $197-350 setup, $150-250/shown. Everything that contradicts gets deleted or archived.

**2. Rewrite the setter script and closer script as ONE coherent handoff.** Same offer, same language, same numbers. Setter tees up exactly what the closer pitches. This alone likely moves close rate 10-20 points.

**3. Fix "Phantom" → "Fathom" everywhere.** Find-and-replace. 5 minutes.

**4. Add the missing resource links.** Testimonials sheet, pitch sheet, contract, onboarding form. If they don't exist, say so explicitly rather than implying they do.

**5. Remove Jowanna's hardcoded booking link from the setter script.** Replace with `{{YOUR_BOOKING_LINK}}` or a note pointing to the index doc.

**6. Consolidate the objection library.** Pick one framework (recommend Jack's parrot-clarify-guard-drop-isolate-handle since it's the mentor's system). Fold the good NLP reframes from the Remodelling doc INTO that framework instead of having them as a parallel system.

**7. Add a one-page "Which doc to read when" map** at the top of the index. Setter reps read X. Closer reps read Y. Everyone reads Z.

**8. Define KPI targets.** Numbers on show rate, close rate, ACV, weekly cash. Without them, "you'll be evaluated on X" is vibes.

---

## TL;DR for Noah

The content isn't the problem — Jack's framework is already in here. The problem is the docs were written at different times without anyone reconciling them, so a new rep reading them all gets three incompatible businesses stacked on top of each other. Biggest single fix: pick ONE offer, ONE script, and delete or archive everything that contradicts. Close rate is probably being dragged down right now by setters and closers pitching different deals.
