---
name: is-that-the-best-you-can-do
kind: workflow
license: CC-BY-NC-4.0
description: Measure how far a correct but unambitious result sits below its ceiling, then close the material gap with proportionate effort. Use when the work is not wrong but not good enough; not for defects and not for unfinished work.
---

# Is That The Best You Can Do

Name the ceiling, measure the gap, then spend real effort closing it.

## Scope

- Kind: workflow
- Owns: one delivered result that is correct and safe but below what the situation deserves, raised to its practical ceiling.
- Boundary: rewrites the artifact under review. Preserves source facts: do not invent benefits, capabilities, approvers or commitments to make the result stronger. Never invents new requirements, features, or scope the request did not ask for.

## Do not use this when

- The work contains actual defects, shortcuts, or residue -> `are-you-sure`
- The defects are in delivered code -> `dev-are-you-sure`
- The work is unfinished rather than unambitious -> `done-for-me`
- The doubt is whether an outside claim or approach is sound -> `research-it`
- Several options must be compared and one recommended -> `give-me-solutions`
- The result is fine but answers the wrong question -> `zoom-out`

## Procedure

1. Establish the ceiling before touching the work. Identify internally what a strong practical version of this artifact would achieve for its actual recipient, in terms that can be checked. If the goal is genuinely ambiguous, resolve that first rather than guessing at excellence.
2. Measure the gap. Identify concretely where the current result sits against that ceiling and which dimension is furthest behind: depth, evidence, structure, specificity, or usefulness to the decision it serves.
3. Decide the effort the gap justifies. A small gap gets one focused pass. Set a bounded effort budget suited to the stakes. Delegate only when independent angles justify the coordination cost; a large gap does not automatically require agents.
4. Gather what is genuinely missing. When the gap is evidence, go and get the evidence rather than writing more confidently around the hole.
5. Rebuild from the strongest parts of the current draft. Keep what already earns its place.
6. Return the improved work. Include a short explanation only when requested or needed to understand a material tradeoff.

## Stop when

The meaningful gap is closed or the bounded effort budget is reached. Do not run another attempt merely to prove diminishing returns; continue only for an identified material gain justified by its cost. Effort stops at the goal that was actually set; pushing past it into unrequested scope is a failure of this skill, not a success.

## Principles

**Deliberate practice** — Improvement requires a target defined above current performance and honest feedback against it; without a named ceiling, effort produces volume rather than quality. Source: K. Anders Ericsson, The Role of Deliberate Practice, 1993
**Steelman before rebuilding** — State the strongest case for the existing draft before replacing it, so genuine quality is not discarded along with the weakness. Source: principle of charity in argumentation; specific attribution uncertain
**Diminishing returns** — Require a plausible material gain before another pass; cosmetic changes or speculative improvements do not justify extending the work. Source: standard economic principle
**Depth is not decoration** — Longer sentences, denser formatting, and larger vocabulary are not improvement; only added substance, evidence, or clarity counts. Source: standing rule in this library

## Counter-case

- The user says the deck is not good enough, and inspection shows the numbers do not reconcile. That is a defect, not a low ceiling, so `are-you-sure` owns it.
- The user asks for the best available tool for a job. Nothing here needs raising; `give-me-solutions` owns the comparison.

## Hand back

The improved work in the requested format. State material remaining limits when needed; ceiling, gap analysis and change commentary stay internal for artifact-only requests.

## Sources

Ericsson, Krampe and Tesch-Romer 1993, The Role of Deliberate Practice in the Acquisition of Expert Performance.
