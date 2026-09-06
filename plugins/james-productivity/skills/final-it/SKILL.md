---
name: final-it
kind: output
license: CC-BY-NC-4.0
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

1. Identify the real recipient and what they will do with this. Honor an explicitly requested format; choose a format from the recipient’s use only when it is unspecified.
2. Within the requested format, choose the simplest form that serves the use. Plain Markdown is correct whenever visual design adds nothing. A request for HTML stays HTML-only; never infer authorisation for a fixed print file from words like final, A4, print-ready, shareable, or client-facing.
3. Transform instructions, complaints, drafts, and discussion into finished wording. Remove production narration, design rationale, progress notes, and copied requirement language.
4. Preserve source truth exactly while changing presentation. Check every factual clause against the supplied source: do not add an author, contact, reopening date, response promise, workflow or technical implication merely because it sounds conventional. Preserve temporal scope too: a closure on one date does not establish an ongoing closure starting that date. Missing details remain unknown; omit nonessential fields instead of shipping placeholders. Anything unresolved stays visibly unresolved, or comes back as the one remaining content gate.
5. Apply the installed wording and visual standards. Do not force visual treatment onto an artifact that is not visual.
6. Run the native checks the format has, and inspect the delivered pages or slides and the relevant viewports or interaction states for its intended use. When only source or chat text is requested, deliver that surface without claiming rendering or adding an unrequested conversion workflow.

## Stop when

The artifact exists in its chosen format, its native checks pass, the relevant rendered output has been inspected, and the only thing returned alongside it is uncertainty the recipient genuinely needs to know about.

## Principles

**Form follows function** — Let the use guide presentation within the explicitly requested format; choose the format yourself only when it is unspecified. Source: Louis Sullivan, 1896
**Answer first** — Lead with the conclusion the reader needs and support it afterwards, rather than reconstructing the path that produced it. Source: Barbara Minto, The Pyramid Principle, 1987
**Preserve the gap** — Never close an open fact to make the artifact feel finished; an invented resolution is worse than a visible hole. Source: standing rule in this library
**Rendering is not delivery** — A file that exists is not a file that renders correctly; inspect the output in its intended use before calling it done. Source: standing rule in this library

## Counter-case

- The user asks for a polished summary of yesterday's call. That is a meeting record with its own semantic contract, so `sum-meet` owns it.
- The user explicitly asks for a deck containing three numbers. Deliver a concise deck; do not substitute an email. If no format was specified, a short email may serve best.

## Hand back

The finished deliverable. If the user requests the artifact only, return only that artifact; keep format rationale and verification bookkeeping internal. Otherwise include only a material delivery limit or decision still needed, without repeating the finished content.

## Sources

Sullivan 1896, The Tall Office Building Artistically Considered. Minto 1987, The Pyramid Principle.
