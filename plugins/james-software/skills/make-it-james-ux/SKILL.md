---
name: make-it-james-ux
kind: shared-standard
license: CC-BY-NC-4.0
description: Design anything rendered from the user's real flow first, then lay it out left to right and top to bottom on a perfect grid. Colour, font and style follow the project, with house defaults only as fallback. Applies automatically to visual work; also use for fix the look, UI รก, จัดหน้าให้เป๊ะ, ดูไม่โปร.
---

# Make It James UX

Understand the real flow first, then lay it out in reading order on a grid with nothing out of line.

## Scope

- Kind: shared-standard
- Owns: the design approach for every rendered output — strategy and real user flow before layout, reading order, grid and alignment discipline, interaction friction — plus the gate that blocks delivery when they fail.
- Boundary: constrains how existing content is arranged and presented. Colour, typeface and visual style belong to the project; this standard supplies defaults only where the project has none. Never chooses the artifact format, never authorises a PDF, never invents content to fill a layout.

## Do not use this when

- The rules needed are about wording rather than presentation -> `make-it-james`
- The question is which format the deliverable should take -> `final-it`
- The interface is defective rather than inconsistent -> `dev-are-you-sure`
- The design question is really a strategy question about the project itself -> `zoom-out`

## Behavior

Work in this order. Read [references/standard.md](references/standard.md) completely before deciding; it holds the detail behind each rule and the house defaults.

**1. Strategy and real flow before any layout.** Do not draw or code until the use is understood. Establish who uses this, the job they are doing, what brings them here, the actual sequence of steps they take from arrival to done, what they already know and hold at each step, how often and on what device, and the one outcome that means it worked. Take this from the project contract, the existing product, real data and the request; ask only when the flow cannot be established and a wrong guess would change the layout. Then decide the strategy: the single primary action of each view, what is secondary, and what does not belong. Every screen, section and control maps to a step of that flow; anything that serves no step is removed or demoted. Cover the states the real flow reaches, including empty, loading, error and returning. Scale this to the job: a local fix inside an accepted flow needs only the affected step confirmed.

**2. Order follows reading: left to right, top to bottom.** Importance descends from the top and sequence runs from the left. What the user needs first sits top-left; what they do last ends the path. Steps appear in the order they are performed. Overview sits above detail, cause before effect, input before result, label before value, and the same relationship is placed the same way everywhere. The eye never travels backward or jumps across the page to continue. A layout that needs an arrow or a note to explain its order is in the wrong order.

**3. Perfect grid, nothing out of line.** One grid and one spacing scale per artifact, chosen before the first element is placed. Every edge sits on a grid line. Equal things are exactly equal in width, height, padding and gap; siblings share one baseline; a column has one alignment, with numbers aligned so digits compare. Same-level components share radius, border, shadow, icon size and type size. No orphan element, no uneven last row, no value off by a pixel, no spacing chosen by eye. A misalignment a careful reader can find is a defect, however small. Check it on the rendered output at every size it will be seen, not in the source.

**4. Style belongs to the project.** Inspect the project for a design system, component library, framework convention, brand guide, or spec sheet before any visual decision, and follow it for colour, typeface, radius, shadow and tone. One consistent system across the whole product outranks this house style. Only where no system exists, use the house defaults: `IBM Plex Sans Thai` for Thai, Latin, and numerals; minimal, white, quiet; compact density with body line-height between 1.35 and 1.45; a 6px radius on rectangular surfaces, with genuinely circular objects staying circular. Never attach a thick or coloured vertical stripe to the left edge of a card, panel, alert, or list item. Defaults and helper checks remain subordinate to explicit user requirements and the selected project system.

**Preserve the requested content and action.** Supplied labels and facts are the content budget: a card with only a requested button needs no invented body message, success notice or system behavior. Put supplied button copy on that button; do not turn it into body text and invent a generic confirmation control. Add a control only when its action belongs to the requested flow. Interface copy carries no production residue: no meta copy, no progress narration, no machine-authorship label, no placeholder shipped as content.

**Reduce friction before adding explanation.** Defer nonessential questions until they are useful; required authorization and inputs stay at the point they are needed. Remove controls irrelevant to the immediate intent. Use optimistic execution plus undo for safe actions only when reversal really works. Preserve required confirmation for destructive or externally binding actions. Break intimidating forms into disclosed steps. Give every control explicit copy rather than an unlabelled icon.

**Format boundary.** An HTML request defaults to HTML-only delivery. Print-ready means working print CSS that passes browser print emulation; it does not authorise PDF export. Create a PDF only when it is explicitly requested or a recipient constraint is directly confirmed. Never infer that constraint from A4, print-ready, final, shareable, or client-facing. Never generate a PDF merely to prove that HTML renders.

**Verify by rendering.** A code-only or chat-snippet request receives the requested code, with rendering unverified; it does not authorize creating an artifact just to satisfy this gate. For a rendered deliverable, walk the real flow from step 2 through the rendered result in order, then run `python3 scripts/lint_outcome.py --strict <output-path>` from this skill directory for supported outputs. Evaluate lint findings against the chosen system rather than changing valid project styling to satisfy a house default. For an offline portable single file, embed the selected typeface and confirm no remote font links remain. Use `python3 scripts/embed_ibm_plex_thai.py <input.html> --output <portable.html>` only when IBM Plex Sans Thai is the selected font; do not replace a project font merely to use this helper. A CSS font declaration is never proof that the font loaded.

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
