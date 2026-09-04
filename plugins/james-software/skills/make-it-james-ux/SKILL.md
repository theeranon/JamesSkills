---
name: make-it-james-ux
kind: shared-standard
description: Enforce visual and interaction law on anything rendered, following the project's existing design system first and this house style only as fallback. Applies automatically to visual work; it does not choose the format or write the content.
---

# Make It James UX

Follow the system that is already there, and where there is none, be compact and quiet.

## Scope

- Kind: shared-standard
- Owns: typography, density, spacing, interaction friction, and interface copy in every rendered output, plus the gate that blocks delivery when they fail.
- Boundary: constrains how existing content is presented. Never chooses the artifact format, never authorises a PDF, never invents content to fill a layout.

## Do not use this when

- The rules needed are about wording rather than presentation -> `make-it-james`
- The question is which format the deliverable should take -> `final-it`
- The interface is defective rather than inconsistent -> `dev-are-you-sure`
- The design question is really a strategy question -> `zoom-out`

## Behavior

**Follow the existing system first.** Inspect the project for a design system, component library, framework convention, brand guide, or spec sheet before making any visual decision. Where one exists, follow it, including its typeface, spacing scale, radii, and component patterns. One consistent system across the whole product outranks this house style. Read [references/standard.md](references/standard.md) completely before deciding.

**House fallback, only where no system exists.** `IBM Plex Sans Thai` as the typeface for Thai, Latin, and numerals. Minimal, white, quiet. Compact and information-dense composition with restrained padding. Body line-height between 1.35 and 1.45. A 6px radius on every rectangular surface; genuinely circular objects stay circular. Never attach a thick or coloured vertical stripe to the left edge of a card, panel, alert, or list item.

**Interface copy carries no production residue.** No meta copy, no progress narration, no labels announcing that a machine produced this, no placeholder text shipped as content. Nothing that belongs to the making of the artifact appears inside the artifact.

**Reduce friction before adding explanation.** Ask for nothing before the user has received value. Remove controls irrelevant to the immediate intent. Replace blocking confirmations with optimistic execution plus undo. Break intimidating forms into disclosed steps. Give every control explicit copy rather than an unlabelled icon.

**Format boundary.** An HTML request defaults to HTML-only delivery. Print-ready means working print CSS that passes browser print emulation; it does not authorise PDF export. Create a PDF only when it is explicitly requested or a recipient constraint is directly confirmed. Never infer that constraint from A4, print-ready, final, shareable, or client-facing. Never generate a PDF merely to prove that HTML renders.

**Verify by rendering.** Run `python3 scripts/lint_outcome.py --strict <output-path>` from this skill directory for supported outputs. For an offline portable single file, run `python3 scripts/embed_ibm_plex_thai.py <input.html> --output <portable.html>` and confirm no remote font links remain. A CSS font declaration is never proof that the font loaded.

## Applies to

Every rendered artifact a person will see: interfaces, sites, applications, dashboards, decks, and print-ready documents. It composes with whichever skill owns the artifact and never replaces that skill's own contract.

On Windows invoke the same helper with `python` when `python3` is not on PATH.

## Principles

**Do not make the reader think** — Every element must be self-evident on first sight; anything needing explanation is a defect in the design, not in the reader. Source: Steve Krug, Don't Make Me Think, 2000
**Consistency outranks preference** — Where a system already exists, follow it even when a different choice would be better in isolation, because a mixed system costs more than any single suboptimal rule. Source: Jakob Nielsen, consistency and standards heuristic, 1994
**Maximise the data-ink ratio** — Remove every mark that carries no information; ornament competes with the content it decorates. Source: Edward R. Tufte, The Visual Display of Quantitative Information, 1983
**Proximity defines relationship** — Space is the primary grouping signal, so fix spacing before adding borders, rules, or coloured containers. Source: Gestalt principle of proximity, Max Wertheimer, 1923

## Counter-case

- The user says the dashboard looks wrong, and inspection shows a component throws on narrow viewports. That is a defect rather than a visual inconsistency, so `dev-are-you-sure` owns it.
- A project uses Material Design with 4px radii and its own typeface. The house radius and typeface do not apply; following the existing system is the standard, not an exception to it.
- A page legitimately displays the phrase "AI generated" as the subject of a data label. The banned pattern is the content here, so it stays.

## Hand back

The rendered artifact, which system was followed and why, the strict lint result, the rendered inspection covering typography, density, radius, and interface copy, and any visual gate that remains open.

## Sources

Krug 2000, Don't Make Me Think. Nielsen 1994, Ten Usability Heuristics. Tufte 1983, The Visual Display of Quantitative Information. Wertheimer 1923, Laws of Organization in Perceptual Forms.
