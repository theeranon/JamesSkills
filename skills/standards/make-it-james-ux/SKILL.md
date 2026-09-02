---
name: make-it-james-ux
description: Apply the visual and UX standard to recipient-facing work. Use automatically when creating, editing, reviewing, or auditing a UI, website, PWA, dashboard, app, slide, PDF, or visual prototype.
---

# Make It James UX

This is a visual standard and delivery gate. 

## Format boundary

- An HTML request defaults to HTML-only delivery. `Print-ready` means the HTML has working print CSS and passes browser print emulation; it does not authorize PDF export.
- Create a PDF only when explicitly requested. Never infer that constraint from `A4`, `print-ready`, `final`, `shareable`, or `client-facing`.

1. Read [references/standard.md](references/standard.md) completely before making visual decisions.
2. Inspect the existing brand and component system. Brand rules may add identity, but they cannot weaken the shared typography, density, or banned-pattern rules.
3. For supported code outputs, run linting from this skill directory:
   `python3 scripts/lint_outcome.py --strict <output-path>`
4. When an HTML deliverable must be one offline portable file, embed the authorized local font files before delivery:
   `python3 scripts/embed_ibm_plex_thai.py <input.html> --output <portable.html>`

## Visual Direction
- Use `IBM Plex Sans Thai` as the default typeface.
- Prefer compact, calm, information-dense composition.
- Default body line-height: `1.35` to `1.45`.
- Every rectangular surface uses a `6px` radius. Genuinely circular objects remain circular.
- Never attach a thick or colored vertical stripe to the left edge of a card, panel, alert, or list item.
- Never generate a PDF merely to prove that HTML renders.

## Completion gate
- Visual work: native checks and strict lint pass, then rendered QA confirms font, density, radius, color discipline, semantic page flow, artifact-appropriate composition, non-duplicative visuals, and absence of ornamental rails, clipping, and avoidable scrolling.

## Behavioral UX & Cognitive Friction Audit Protocol
When tasked with auditing a page, interaction flow, or product UI, evaluate against five core friction tests:

1. **Premature asking:** Identify fields or steps asking for data before the user gets value. Recommend deferring to profile/settings or using smart defaults.
2. **Contextual relevance:** Identify buttons, admin controls, or links irrelevant to the immediate user intent. Recommend tucking into menus.
3. **Interruption discipline:** Identify unnecessary confirmation modals and blocking popups. Recommend optimistic execution with inline status and "Undo".
4. **Information density:** Identify intimidating walls of forms. Recommend progressive disclosure via accordions or wizard steps.
5. **Effort economy:** Identify ambiguous button copy, icon-only buttons without accessible labels, and dead ends. Recommend explicit copy and visible affordances.

### Audit Output Matrix Format
When delivering an audit, structure findings into this clean actionable table:
| Step / Component | Friction Detected | Psychological / UX Root Cause | Action (Cut / Tuck / Defer / Simplify) |
| :--- | :--- | :--- | :--- |

