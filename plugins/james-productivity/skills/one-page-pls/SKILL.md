---
name: one-page-pls
description: Turn source material into one self-contained one-page artifact per topic or agenda. Use for one-page summaries, one-pagers, executive briefs, or meeting sources that must stay concise without losing decisions, actions, risks, or evidence.
---

# One Page Please

Produce decision-ready one-page artifacts, not a compressed transcript.

This skill owns recipient readiness for one-page artifacts. Apply `make-it-james` (for wording) and `make-it-james-ux` (for UI) for shared output law. When the artifact is explicitly for SolutionsIMPACT or a related brand, read [the SolutionsIMPACT output pack](../../../packs/solutionsimpact/output-brand.md); the pack may add identity but never weaken the one-topic-per-file contract.

1. Read every supplied source before summarizing. Detect the independent topics or agendas from explicit headings, changed outcomes, owners, decisions, or timelines.
2. Enforce `one topic = one file`. A source with N topics produces N separately named, self-contained one-page artifacts. Never mix independent agendas on one page.
3. Before compression, account for every material decision, action, owner, date, risk, constraint, number, and evidence item. Read [references/content-contract.md](references/content-contract.md).
4. Duplicate [assets/a4-landscape-template.html](assets/a4-landscape-template.html) for each topic and replace every `[[...]]` token. Preserve the compact layout and visual invariants; adapt sections only when the topic requires it.
5. If one topic cannot fit legibly, keep the one-page decision surface and create a clearly linked appendix or full record when allowed. Otherwise return an explicit `one-page unsuitable` verdict. Never hide material or shrink it into unreadability.
6. Render and inspect every HTML output separately using [references/render-qa.md](references/render-qa.md). Deliver editable HTML only by default; when PDF is explicitly requested, add one matching PDF per topic.

For a genuinely portable single-file HTML, run the `make-it-james-ux` [font embedding helper](../../standards/make-it-james-ux/scripts/embed_ibm_plex_thai.py), confirm the remote font links are gone, and verify the rendered font. The shipped template alone is not self-contained proof; if the font files are unavailable, report the exact remaining portability gate.

Do not claim success from file creation alone. Completion requires correct topic separation, semantic coverage, one rendered page per artifact, loaded typography, and no clipping or placeholders.
