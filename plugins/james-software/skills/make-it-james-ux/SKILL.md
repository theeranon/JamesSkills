---
name: make-it-james-ux
license: CC-BY-NC-4.0
metadata:
  kind: shared-standard
description: No slop in UX, UI and web app design, as principles a user or project design system may override. UX: real flow of every user group, fewer steps, no needless modal, left to right, top to bottom, exact grid. UI: locked type and radius, no accent border, nothing jumps, fixed heights. Use for UI รก, จัดหน้าให้เป๊ะ.
---

# Make It James UX

Design the real flow first, then a grid nothing jumps on; follow the project's system, and never ship slop.

## Scope

- Kind: shared-standard
- Owns: the design approach for every rendered output — strategy and real user flow before layout, reading order, grid and alignment discipline, interaction friction — plus the gate that blocks delivery when they fail.
- Boundary: constrains how existing content is arranged and presented. Colour, typeface and visual style belong to the project; this standard supplies defaults only where the project has none. Never chooses the artifact format, never authorises a PDF, never invents content to fill a layout.

## Do not use this when

- The rules needed are about wording rather than presentation -> `make-it-james`
- The interface is defective rather than inconsistent -> `dev-are-you-sure`
- The design question is really a strategy question about the project itself -> `zoom-out`

## Behavior

These are principles, not fixed values: an explicit user design decision wins, then a project design system found in the repository or brief, then the defaults here. Read [references/standard.md](references/standard.md) for the detail behind each rule and the defaults.

**UX: experience of use, checked by eye.**
- Start from the real flow of every user group of this system: who they are, what brings them to this screen, the exact steps from arrival to done, and the one outcome that means it worked. Every screen, section and control maps to a step; what serves no step is removed or demoted. Cover empty, loading, error and returning states.
- Don't make me think: fewer steps, the next action obvious, labels that say what happens. Defer nonessential questions; keep required inputs at the point of use.
- No popup or modal unless the task truly needs interruption; no nesting of anything inside a modal.
- Reading order is left to right, top to bottom: what the user needs first sits top-left, steps appear in the order performed, overview above detail, label before value, the same relationship placed the same way everywhere. A layout that needs an arrow to explain its order is in the wrong order.
- Choose the component that fits what is shown: a table for comparable rows, a card for one thing, a list for a sequence, never a table inside a table.
- Compact and consistent: low padding, one spacing scale, equal things exactly equal.
- Verify by walking the rendered result as each user group, in order, at every size it will be seen.

**UI: front-end discipline that never ships slop.**
- Lock the type scale, font weights and border radius once per artifact and never vary them by eye. Default when nothing is specified and the project has no system: white, clean, minimal; `IBM Plex Sans Thai` for Thai, Latin and numerals, no weight heavier than semi-bold; body line-height between 1.35 and 1.45; a 6px radius on rectangular surfaces.
- Never attach a thick or coloured accent border or vertical stripe to the left edge of a card, panel, alert or list item.
- Exact grid: every edge on a grid line; siblings share baseline, width, height and gap; numbers align so digits compare; no orphan element, no uneven last row, nothing off by a pixel.
- Nothing jumps: changing page keeps the navigation and layout in place; expanding or collapsing anything moves nothing else; cards, rows and table rows keep fixed heights and never stretch with content, so choose what to show or truncate with an explicit control.
- No nested designs: no modal inside a modal, no table inside a table, no card inside a card.
- Design desktop and mobile both; never ship one locked page width and call it responsive, unless the user explicitly asks for a fixed width.
- Interface copy carries no production residue: no meta copy, no progress narration, no machine-authorship label, no placeholder shipped as content. Supplied labels and facts are the content budget; invent nothing to fill a layout.

**Format boundary.** An HTML request defaults to HTML-only delivery. Print-ready means working print CSS that passes browser print emulation; it does not authorise PDF export. Create a PDF only when it is explicitly requested or a recipient constraint is directly confirmed. Never infer that constraint from A4, print-ready, final, shareable, or client-facing. Never generate a PDF merely to prove that HTML renders.

**Verify by rendering.** A code-only or chat-snippet request receives the requested code, with rendering unverified. For a rendered deliverable, walk the real flow through the rendered result, then run `python3 scripts/lint_outcome.py --strict <output-path>` from this skill directory for supported outputs, judging findings against the chosen system rather than changing valid project styling to satisfy a default. For an offline portable single file, embed the selected typeface and confirm no remote font links remain; use `python3 scripts/embed_ibm_plex_thai.py <input.html> --output <portable.html>` only when IBM Plex Sans Thai is the selected font. A CSS font declaration is never proof that the font loaded.

## Applies to

Every rendered artifact a person will see: interfaces, sites, applications, dashboards, decks, and print-ready documents. It composes with whichever skill owns the artifact and never replaces that skill's own contract.

On Windows invoke the same helper with `python` when `python3` is not on PATH.

## Principles

**Design for the goal, not the screen** — Work out what the person is trying to get done and the path they really take before deciding what any view contains. Source: Alan Cooper, About Face, 1995
**Reading gravity** — Place content along the path the eye already takes, from top-left to bottom-right, so order needs no explanation. Source: Gutenberg diagram, commonly credited to Edmund C. Arnold; uncertain attribution
**The grid is the discipline** — Decide the grid first and let every element answer to it, because alignment by eye drifts with each addition. Source: Josef Müller-Brockmann, Grid Systems in Graphic Design, 1981
**Consistency outranks preference** — Where a system already exists, follow it even when a different choice would be better in isolation, because a mixed system costs more than any single suboptimal rule. Source: Jakob Nielsen, consistency and standards heuristic, 1994
**Proximity defines relationship** — Space is the primary grouping signal, so fix spacing before adding borders, rules, or coloured containers. Source: Gestalt principle of proximity, Max Wertheimer, 1923

## Counter-case

- The user says the dashboard looks wrong, and inspection shows a component throws on narrow viewports. That is a defect rather than a visual inconsistency, so `dev-are-you-sure` owns it.
- A project uses Material Design with 4px radii, its own typeface and a brand colour. None of the house defaults apply; following the existing system is the standard, not an exception to it.
- A project is written in Arabic or another right-to-left language. Sequence runs in that language's reading direction; the rule is reading order, not the left edge.
- One button overlaps its neighbour in an accepted flow. Confirm the step it belongs to, fix the alignment and verify it; no strategy pass is required.
- A page legitimately displays the phrase "AI generated" as the subject of a data label. The banned pattern is the content here, so it stays.

## Hand back

The requested code or rendered artifact. For a rendered deliverable, report the flow it was designed for, the system followed, actual lint/render evidence and material open gates. For code-only output, return exclusively code; keep verification notes internal.

## Sources

Cooper 1995, About Face. Müller-Brockmann 1981, Grid Systems in Graphic Design. Nielsen 1994, Ten Usability Heuristics. Wertheimer 1923, Laws of Organization in Perceptual Forms.
