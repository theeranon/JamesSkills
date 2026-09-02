# James Visual and Final Word Law

Authority: James's durable cross-project preference. Apply it across AI vendors, frameworks, and recipient-facing formats. A project may add brand colors, logos, and domain-specific constraints, but may not silently weaken this law.

## Visual direction

- Use `IBM Plex Sans Thai` as the default typeface for Thai, English, and numbers. Do not introduce a separate Latin display font.
- Prefer compact, calm, information-dense composition. Preserve Thai readability; compact must not become cramped or clipped.
- Default body line-height: `1.35` to `1.45`. Dense metadata and table rows may use `1.2` to `1.3`. Values above `1.5` require a content or accessibility reason.
- Default control height: `32px` to `38px`; panel padding: `12px` to `16px`; section gap: `12px` to `20px`.
- Every rectangular surface uses a `6px` radius. Genuinely circular objects remain circular.
- Prefer typography, alignment, grouping, rows, tables, and restrained neutral surfaces before decoration.
- Adapt scale to viewing distance for websites, product UI, slides, PDFs, reports, email, captions, and documents without switching to an airy or decorative visual language.
- Match the artifact to its reading job. A report should read as a document or report, not default to an app dashboard merely because HTML is available.
- For print, group page breaks by meaning and reading sequence. Repair overflow within the affected section; do not remove page structure or shrink the entire document to hide one layout defect.
- Show one dataset in the visual form that best serves the decision. Repeating the same information as cards, chart, table, and callout requires a distinct reading purpose for each form.

## Format and export

- Preserve the native editable format. HTML is the default final artifact when HTML was requested.
- `Print-ready HTML` means correct print CSS and direct browser inspection, not an automatically exported PDF.
- Export PDF only after an explicit PDF request or an authoritative recipient constraint requiring a fixed print file is directly confirmed. Never infer that constraint from `A4`, `print-ready`, `final`, `shareable`, `client-facing`, or `recipient-ready`. Do not spend a render cycle creating PDF solely as HTML QA.

## Banned pattern

Never attach a thick or colored vertical stripe to the left edge of a card, panel, alert, list item, or section. This includes decorative `border-left`, positioned bars, and pseudo-elements used as status or category rails.

Use a compact text label, icon plus label, status column, restrained whole-surface tint, or plain hierarchy instead. A thin neutral structural divider, genuine quotation rule, or real timeline remains valid.

## Cards, pills, chips, and color

- A card must be interactive, carry independent state, be reorderable, or prevent a real reading error. Otherwise use a section, divider, row, or table.
- Pills and chips are exceptional. Use them only for an interactive filter, removable selection, or compact status scanned across many rows.
- Dates, owners, categories, metadata, and explanation remain plain text.
- Use one primary accent per page. Red, amber, and green carry semantic status only.
- Reject decorative gradients, rainbow cards, color-per-section palettes, and ornamental status color.

## Behavioral UX and cognitive friction gate

When designing, reviewing, or auditing any user flow or interface, eliminate cognitive friction and avoidable user hesitation across five core axes:

1. **Premature asking (Why ask now?):** Never demand non-essential user data or upfront commitment before delivering tangible value. Defer phone numbers, birthdays, addresses, and full registration to post-onboarding or point-of-need. Use smart defaults and auto-detection instead of forcing choices.
2. **Contextual relevance (Why is this here?):** Align visible elements with the user's single dominant intention in the current view. Ensure primary actions stand out alone; tuck secondary controls, settings, or administrative actions into dropdowns, overflow menus, or lower hierarchy.
3. **Interruption discipline (Why did this pop up?):** Eliminate modal overload. Ban blocking confirmation dialogs for safe, easily reversible actions; execute optimistically and provide an inline status or temporary "Undo" notification. Reserve modals strictly for catastrophic, irreversible destructive actions.
4. **Information density and form fatigue (Tuck or defer?):** Prevent form intimidation. Group inputs logically; show P0 essentials immediately and tuck specialized or advanced inputs (P1/P2) inside accordions or expandable disclosures. Split multi-step workflows with clear, visible progress steps.
5. **Effort economy and hesitation reduction:** Eliminate ambiguous labels, cryptic icons without text, and uncommunicated consequences. Micro-copy must explicitly state the outcome (e.g., "Confirm Order — $29" rather than "Continue"). Every clickable control must carry clear affordance (`cursor: pointer`, hover feedback). Never leave the user in a dead end.

## Interaction and accessibility gate (Pro Max engineering)

Adopt deterministic UI engineering and accessibility standards across every platform:

- **Contrast ratio (WCAG 2.1 AA):** Ensure text contrast against its immediate background achieves at least `4.5:1` for normal text and `3:1` for large text or graphical control borders.
- **Visible focus indicator:** All interactive controls must provide an unambiguous, high-contrast focus ring during keyboard navigation (`:focus-visible` with a minimum 2px outline and 2px offset). Never suppress focus outlines (`outline: none`) without an accessible visible replacement.
- **Mobile touch ergonomics:** On coarse pointer devices (`@media (pointer: coarse)`), interactive tap targets must measure at least `44×44px` to prevent misclicks, while desktop preserves the compact `32px` to `38px` control height.
- **Motion discipline:** Strictly respect `prefers-reduced-motion: reduce`. When active, disable decorative translations, scale shifts, and disorienting parallax. Keep standard transition durations between `150ms` and `250ms` with ease-out curves.
- **Icon affordance and accessibility:** Never use emoji as functional UI icons; use standard SVG icon sets (Lucide or Heroicons). Every icon-only button must include an explicit `aria-label` or accessible screen-reader text.
- **Defensive layout and reflow:** Test views across four explicit breakpoints: `375px` (Mobile), `768px` (Tablet), `1024px` (Desktop), and `1440px` (Wide). Prevent horizontal viewport overflow (`overflow-x: hidden`). Ensure tags, chips, badges, and Thai vowel/tone marks reflow cleanly without clipping or breaking mid-word.

## Final Word law

Every outcome must read as finished material intentionally written for its real recipient. Transform James's intent into final wording.

Remove conversation residue, instructions to AI, complaints, preparation notes, production state, design rationale, copied requirement language, interface narration, and AI theatre. Labels such as `AI prepared`, `Powered by AI`, `Artifact Progress`, `ระบบกำลังคิด`, `ตอนนี้มีแล้ว`, and `บทนี้จะเติม` fail unless the term itself is the subject.

Natural Thai sentences are the default. Do not compress Thai thought with emoji or `: — – → / + |`. Exact URLs, code, formulas, file paths, versions, times, ratios, and direct quotations are exceptions.

## Proof

- New work starts from this law; it does not invent a new font or spacious card system.
- Self-host `IBM Plex Sans Thai` for production when available. A CSS family name is not proof; inspect the rendered font.
- Run deterministic lint plus the artifact's native checks.
- Inspect desktop, mobile, and print media where applicable. Inspect every requested fixed page or slide rather than a sample.
- Fail delivery when Thai marks clip, important content disappears, generic AI-dashboard styling remains, or unnecessary scrolling is introduced.
- Audit historical work before repair. Preserve raw sources and record debt rather than claiming bulk remediation.
