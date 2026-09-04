---
name: final-it
kind: output
description: Choose the format that actually serves the recipient and finish the work in it. Use when no narrower output skill owns the artifact; not for meeting records, not for one-page briefs, and not for supplying missing content.
---

# Final It

Pick the simplest form that serves the reader, then finish it properly.

## Scope

- Kind: output
- Owns: selecting the artifact format and taking the work to a delivered state, when no more specific output skill owns it.
- Boundary: transforms existing material into its finished form. Never invents a fact, quote, number, owner, deadline, approval, or resolution to make the artifact look complete.

## Do not use this when

- The source is a meeting and the record must hold every agenda -> `sum-meet`
- Each topic must become its own single page -> `one-page-pls`
- A project contract, not a deliverable, is what is needed -> `project-standard`
- The content is unfinished rather than unformatted -> `done-for-me`
- The content is finished but below its ceiling -> `is-that-the-best-you-can-do`

## Procedure

1. Identify the real recipient and what they will do with this. The format follows that, not the impressiveness of the request.
2. Choose the simplest form that serves the use. Plain Markdown is correct whenever visual design adds nothing. A request for HTML stays HTML-only; never infer authorisation for a fixed print file from words like final, A4, print-ready, shareable, or client-facing.
3. Transform instructions, complaints, drafts, and discussion into finished wording. Remove production narration, design rationale, progress notes, and copied requirement language.
4. Preserve source truth exactly while changing presentation. Anything unresolved stays visibly unresolved, or comes back as the one remaining content gate.
5. Apply the installed wording and visual standards. Do not force visual treatment onto an artifact that is not visual.
6. Run the native checks the format has, and inspect every rendered page, slide, viewport, or state when rendering exists.

## Stop when

The artifact exists in its chosen format, its native checks pass, every rendered state has been inspected, and the only thing returned alongside it is uncertainty the recipient genuinely needs to know about.

## Principles

**Form follows function** — Let the use decide the format; a shape chosen before the purpose produces decoration rather than a deliverable. Source: Louis Sullivan, 1896
**Answer first** — Lead with the conclusion the reader needs and support it afterwards, rather than reconstructing the path that produced it. Source: Barbara Minto, The Pyramid Principle, 1987
**Preserve the gap** — Never close an open fact to make the artifact feel finished; an invented resolution is worse than a visible hole. Source: standing rule in this library
**Rendering is not delivery** — A file that exists is not a file that renders correctly; inspect every state before calling it done. Source: standing rule in this library

## Counter-case

- The user asks for a polished summary of yesterday's call. That is a meeting record with its own semantic contract, so `sum-meet` owns it.
- The user asks for a beautiful deck when the decision needs three numbers in an email. The simplest serving form wins, and this skill delivers the email.

## Hand back

The finished artifact in the chosen format, the reason that format was chosen, the verification actually performed, and any content gate that remains genuinely open.

## Sources

Sullivan 1896, The Tall Office Building Artistically Considered. Minto 1987, The Pyramid Principle.
