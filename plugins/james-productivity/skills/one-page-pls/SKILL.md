---
name: one-page-pls
kind: output
description: Turn each independent topic into its own self-contained single-page brief. Use when material must stay on one page per topic; not for meeting records that must hold every agenda in one file.
---

# One Page Please

One topic, one page, and nothing material lost to make it fit.

## Scope

- Kind: output
- Owns: producing one decision-ready A4 landscape HTML page per independent topic, each file self-contained.
- Boundary: compresses and renders existing material. Never merges independent topics, never drops material content to force a fit, and never invents a fact to fill the layout.

## Do not use this when

- Every agenda must live in one record together -> `sum-meet`
- The artifact is not page-bound and the format is still open -> `final-it`
- Current project state must be reconstructed rather than summarised -> `catchup`
- The source is unfinished rather than uncompressed -> `done-for-me`

## Procedure

1. Read every supplied source completely before summarising. Detect independent topics from explicit headings, changed outcomes, different owners, separate decisions, or separate timelines.
2. Enforce `one topic = one file`. A source with several topics produces that many separately named, self-contained pages. Never mix independent agendas on one page.
3. Before compressing, account for every material decision, action, owner, date, risk, constraint, number, and evidence item, using [references/content-contract.md](references/content-contract.md).
4. Duplicate [assets/a4-landscape-template.html](assets/a4-landscape-template.html) for each topic and replace every token. Preserve the compact layout and visual invariants; adapt sections only where the topic genuinely requires it.
5. If one topic cannot fit legibly, keep the one-page decision surface and link a clearly named appendix or full record, or return an explicit `one-page unsuitable` verdict. Never hide material or shrink it into unreadability.
6. Render and inspect every output separately using [references/render-qa.md](references/render-qa.md). Deliver editable HTML only by default; produce a PDF only when it is explicitly requested.
7. The shipped template alone is not self-contained proof. For a genuinely portable single file, run the font embedding helper at `../../../james-software/skills/make-it-james-ux/scripts/embed_ibm_plex_thai.py`, confirm no remote font links remain, and verify the rendered typeface. If the font files are unavailable, report that exact portability gate rather than claiming self-containment.

## Stop when

Every independent topic has its own rendered, inspected file, all material content is accounted for, typography has loaded, and nothing is clipped or left as a placeholder. File creation alone is never sufficient.

## Principles

**The constraint is the instrument** — The single page exists to force the decision surface to the top, not to shrink the content; when it will not fit, the answer is a linked appendix, never smaller type. Source: standing rule in this library
**Mutually exclusive topics** — Separate topics so nothing appears in two briefs and nothing falls between them, because overlap is what makes a set of one-pagers unusable. Source: MECE principle, McKinsey practice, popularised by Barbara Minto
**Maximise signal per unit of ink** — Remove anything that does not carry information the reader needs to decide. Source: Edward R. Tufte, The Visual Display of Quantitative Information, 1983
**No silent truncation** — State what was moved to an appendix or left out, because omission the reader cannot see reads as completeness. Source: standing rule in this library

## Counter-case

- The user asks for a one-page summary of a meeting with four agendas. Each agenda becomes its own page here, but if the request is for one auditable record of the whole meeting, `sum-meet` owns it instead.
- A single topic genuinely needs three pages of evidence. This skill keeps the one-page decision surface and links the evidence rather than compressing it into illegibility.

## Hand back

One rendered file per topic with its name, the coverage account showing every material item placed, the inspection result for each page, and any topic returned as unsuitable for one page with the reason.

## Sources

Minto 1987, The Pyramid Principle, on MECE structure. Tufte 1983, The Visual Display of Quantitative Information.
