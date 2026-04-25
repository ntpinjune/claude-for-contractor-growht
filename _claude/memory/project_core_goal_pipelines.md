---
name: Core goal — streamlined pipelines
description: Noah's top priority is using Claude to synthesize raw source docs into clean operational pipelines/SOPs
type: project
originSessionId: 2026-04-22-session
---
The biggest thing Noah wants out of this setup: **streamlined pipelines for everything.** Concretely — Noah drops in a set of source documents (call transcripts, existing rough SOPs, hiring notes, client notes, etc.) and asks Claude to produce a single clean operational doc that works end-to-end.

**Why:** The agency has a lot of tribal/scattered knowledge — mentor calls, Skool course content, hiring docs, data sheets. Noah wants it synthesized into actionable pipelines (sales pipeline, hiring pipeline, delivery pipeline, etc.) rather than left as raw inputs. Stated 2026-04-22.

**How to apply:**
- When Noah says "make a pipeline" or "synthesize these docs," the output should be a single authoritative markdown file in `business/sops/` (or a dedicated pipeline folder under `business/`) — not a summary, not a list of bullets from each source.
- Pull from ALL relevant sources the user has pointed at, not just the most recent one.
- Preserve Jack's terminology and framing where applicable (PPA, PPL, PIF, PPSA, etc.) — these are house language for the agency.
- Cite source docs inline (e.g., `[see 2026-03-22 call]`) so the synthesis is traceable back to the raw input.
- If source material conflicts, flag the conflict and ask Noah to resolve rather than silently picking.
