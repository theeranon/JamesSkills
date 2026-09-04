---
name: is-that-the-best-you-can-do
kind: workflow
description: Measure how far a correct but unambitious result sits below its ceiling, then spend parallel effort closing that gap. Use when the work is not wrong but not good enough; not for defects and not for unfinished work.
---

# Is That The Best You Can Do

Name the ceiling, measure the gap, then spend real effort closing it.

## Scope

- Kind: workflow
- Owns: one delivered result that is correct and safe but below what the situation deserves, raised to its practical ceiling.
- Boundary: rewrites the artifact under review. Never invents new requirements, features, or scope the request did not ask for.

## Do not use this when

- The work contains actual defects, shortcuts, or residue -> `are-you-sure`
- The defects are in delivered code -> `dev-are-you-sure`
- The work is unfinished rather than unambitious -> `done-for-me`
- The doubt is whether an outside claim or approach is sound -> `research-it`
- Several options must be compared and one recommended -> `give-me-solutions`
- The result is fine but answers the wrong question -> `zoom-out`

## Procedure

1. Establish the ceiling before touching the work. State what the best possible version of this artifact would achieve for its actual recipient, in terms that can be checked. If the goal is genuinely ambiguous, resolve that first rather than guessing at excellence.
2. Measure the gap. Say concretely where the current result sits against that ceiling and which dimension is furthest behind: depth, evidence, structure, specificity, or usefulness to the decision it serves.
3. Decide the effort the gap justifies. A small gap gets one focused pass. A large gap gets parallel work, with each agent given a distinct angle rather than the same instruction repeated, and each returning something that can be compared.
4. Gather what is genuinely missing. When the gap is evidence, go and get the evidence rather than writing more confidently around the hole.
5. Rebuild from the strongest parts of the current draft. Keep what already earns its place and say what you kept.
6. Return the raised work itself, plus a short account of what was below ceiling and what changed.

## Stop when

Another parallel attempt no longer changes the result, or the remaining gap is named along with what it would cost to close. Effort stops at the goal that was actually set; pushing past it into unrequested scope is a failure of this skill, not a success.

## Principles

**Deliberate practice** — Improvement requires a target defined above current performance and honest feedback against it; without a named ceiling, effort produces volume rather than quality. Source: K. Anders Ericsson, The Role of Deliberate Practice, 1993
**Steelman before rebuilding** — State the strongest case for the existing draft before replacing it, so genuine quality is not discarded along with the weakness. Source: principle of charity in argumentation; specific attribution uncertain
**Diminishing returns** — Keep spending effort only while it still changes the answer, and stop at the point where another pass would not. Source: standard economic principle
**Depth is not decoration** — Longer sentences, denser formatting, and larger vocabulary are not improvement; only added substance, evidence, or clarity counts. Source: standing rule in this library

## Counter-case

- The user says the deck is not good enough, and inspection shows the numbers do not reconcile. That is a defect, not a low ceiling, so `are-you-sure` owns it.
- The user asks for the best available tool for a job. Nothing here needs raising; `give-me-solutions` owns the comparison.

## Hand back

The named ceiling, the measured gap, the raised work itself, what was kept from the original and why, and anything still below ceiling with its cost.

## Sources

Ericsson, Krampe and Tesch-Romer 1993, The Role of Deliberate Practice in the Acquisition of Expert Performance.
