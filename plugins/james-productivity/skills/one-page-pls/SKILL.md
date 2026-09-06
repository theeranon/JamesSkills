---
name: one-page-pls
kind: output
license: CC-BY-NC-4.0
description: Turn material into a self-contained single-page brief, with one page per topic by default. Use when material must stay on one page per topic; not for meeting records that must hold every agenda in one file.
---

# One Page Please

One useful page at the requested scope, without hiding material omissions.

## Scope

- Kind: output
- Owns: producing a decision-ready one-page brief at the requested scope and surface; default to a self-contained A4 landscape HTML page per independent topic.
- Boundary: compresses and renders existing material. Honors an explicit combined-page request, never silently drops material content to force a fit, and never invents a fact to fill the layout.

## Do not use this when

- Every agenda must live in one record together -> `sum-meet`
- The artifact is not page-bound and the format is still open -> `final-it`
- Current project state must be reconstructed rather than summarised -> `catchup`
- The source is unfinished rather than uncompressed -> `done-for-me`

## Procedure

Confirm the requested output surface from the existing request. If the user asks for brief content in chat, deliver the requested brief there without claiming files or render checks. If the request belongs to a sibling, use that owner rather than refusing a straightforward answer solely because its instructions are not loaded. The one-page file default never overrides an explicit request for a consolidated meeting record.

1. Read every supplied source completely before summarising. Detect independent topics from explicit headings, changed outcomes, different owners, separate decisions, or separate timelines.
2. Use one topic per page by default. If the user explicitly requests one combined page, keep all requested topics on that page with clear sections; if they request separate pages, deliver separate pages. Do not convert a combined brief into several files.
3. Before compressing, account for every material decision, action, owner, date, risk, constraint, number, and evidence item, using [references/content-contract.md](references/content-contract.md). Preserve each item's meaning: a decision deadline is not an execution deadline, an owner is not automatically the approver, and a risk does not establish current status. Do not add currency, approval, causality or progress absent from the source. A proposed appendix location is not an existing verified link.
4. For HTML delivery, duplicate [assets/a4-landscape-template.html](assets/a4-landscape-template.html) for each requested page and replace every token. Preserve the compact layout and visual invariants; adapt sections only where the topic genuinely requires it.
5. If one topic cannot fit legibly, keep the one-page decision surface and link a clearly named appendix or full record, or return an explicit `one-page unsuitable` verdict. Never hide material or shrink it into unreadability.
6. For rendered file delivery, render and inspect every output separately using [references/render-qa.md](references/render-qa.md). Deliver editable HTML only by default; produce a PDF only when it is explicitly requested.
7. For portable HTML delivery, the shipped template alone is not self-contained proof. For a genuinely portable single file, run the font embedding helper at `../../../james-software/skills/make-it-james-ux/scripts/embed_ibm_plex_thai.py`, confirm no remote font links remain, and verify the rendered typeface. If the font files are unavailable, report that exact portability gate rather than claiming self-containment.

## Stop when

For file delivery, every requested page has been rendered and inspected, all material content is accounted for, typography has loaded, and nothing is clipped or left as a placeholder. File creation alone is never sufficient. For explicitly requested chat content, the requested brief is complete; no rendering claim is made.

## Principles

**The constraint is the instrument** — The single page exists to force the decision surface to the top, not to shrink the content; when it will not fit, the answer is a linked appendix, never smaller type. Source: standing rule in this library
**Mutually exclusive topics** — Separate topics into clear sections or pages according to the requested scope, avoiding duplication and gaps. Source: MECE principle, McKinsey practice, popularised by Barbara Minto
**Maximise signal per unit of ink** — Remove anything that does not carry information the reader needs to decide. Source: Edward R. Tufte, The Visual Display of Quantitative Information, 1983
**No silent truncation** — State what was moved to an appendix or left out, because omission the reader cannot see reads as completeness. Source: standing rule in this library

## Counter-case

- The user asks for one combined page covering four agendas. Deliver one page with four clear sections. A full auditable meeting record instead uses `sum-meet`.
- A single topic genuinely needs three pages of evidence. This skill keeps the one-page decision surface and links the evidence rather than compressing it into illegibility.

## Hand back

The requested page or chat brief. Keep coverage and inspection bookkeeping internal unless requested; disclose any material omission, linked appendix or delivery limitation the reader needs.

## Sources

Minto 1987, The Pyramid Principle, on MECE structure. Tufte 1983, The Visual Display of Quantitative Information.
