---
name: make-it-james
description: Apply James Theeranon's visual and Final Word law to recipient-facing work. Use automatically when creating, editing, reviewing, or auditing a UI, website, PWA, dashboard, app, slide, PDF, report, document, email, caption, or visual prototype; skip raw evidence, transcripts, source archives, and private scratch notes.
---

# Make It James

This is a cross-format standard and delivery gate. It does not choose the artifact format, invent missing content, or replace the workflow producing the artifact.

## Format boundary

- An HTML request defaults to HTML-only delivery. `Print-ready` means the HTML has working print CSS and passes browser print emulation; it does not authorize PDF export.
- Create a PDF only when James explicitly requests PDF or an authoritative recipient constraint requiring one fixed print file is directly confirmed. Never infer that constraint from `A4`, `print-ready`, `final`, `shareable`, `client-facing`, or `recipient-ready`.
- Never generate a PDF merely to prove that HTML renders. Inspect the HTML in screen and print media directly.

1. Read [references/standard.md](references/standard.md) completely before making visual or recipient-facing wording decisions.
2. Preserve raw evidence and archives. Apply the standard to the recipient-facing result, not its source material.
3. Inspect the existing brand and component system. Brand rules may add identity, but they cannot weaken the shared typography, density, copy, or banned-pattern rules.
4. Apply Final Word law to every recipient-facing format. Apply visual law whenever the result renders visually.
5. For supported text or code outputs, run from this skill directory:

   ```bash
   python3 scripts/lint_outcome.py --strict <output-path> [<output-path> ...]
   ```

6. When an HTML deliverable must be one offline portable file, embed the authorized local font files before delivery:

   ```bash
   python3 scripts/embed_ibm_plex_thai.py <input.html> --output <portable.html> [--font-dir <font-directory>]
   ```

   If the font files are unavailable, report that exact portability gate; a Google Fonts link or CSS family declaration is not self-contained proof.
7. Run the artifact's native checks. For visual work, inspect every relevant rendered page, slide, viewport, and state; verify the font actually loaded and Thai marks remain legible.

## Completion gate

- Written-only work: final wording contains no conversation residue, AI theatre, or punctuation-built Thai shorthand.
- Visual work: native checks and strict lint pass, then rendered QA confirms font, density, radius, color discipline, semantic page flow, artifact-appropriate composition, non-duplicative visuals, and absence of ornamental rails, excessive cards, unnecessary pills or chips, clipping, and avoidable scrolling. A claimed offline single-file HTML contains embedded font data and no remote font dependency.
- Legacy work: audit first, record `PASS`, `FIX`, or `EXEMPT`, and repair active surfaces by priority. Never bulk-rewrite evidence or archives.
