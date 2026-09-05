---
name: done-for-me
kind: workflow
license: CC-BY-NC-4.0
description: Carry an already-agreed task all the way to a finished, verified outcome without stopping to ask. Use when the plan is settled and only execution remains; not when the plan still needs work and not for inspecting finished work.
---

# Done For Me

Take the agreed job to the finish line and only then come back.

## Scope

- Kind: workflow
- Owns: one task whose intent is already established, carried through implementation and its own verification to a usable result.
- Boundary: executes every safe action inside the accepted scope. Never pushes, deploys, sends, publishes, or spends unless the request or the accepted project contract authorises that exact target.

## Do not use this when

- The plan itself is not good enough yet and needs decomposition before building -> `proactive-dev`
- The work is finished and its diligence is what is in doubt -> `are-you-sure`
- Delivered code needs a layered sweep and boundary check -> `dev-are-you-sure`
- The right approach is genuinely unknown and needs outside evidence -> `research-it`
- The requirement itself is still vague and must be interrogated -> `grill-me`

## Procedure

1. Find the requirement authority, the current state, and what counts as finished. Consume an approval already present in this conversation or the project contract; never ask the user to repeat it as a confirmation word.
2. Define the minimum usable outcome and take the shortest path to it. Implement, run the minimum proof the outcome needs, and reach a checkpoint before optional hardening, broad audits, or documentation cleanup.
3. Execute every in-scope action that does not require a new business decision or irreversible authority. Do not pause to narrate, confirm, or ask whether to continue.
4. When one path blocks, continue every independent path. Turn missing configuration into an explicit settings surface, environment variable, or documented input contract rather than a fabricated value.
5. Investigate and repair ordinary failures. Do not stop at the first error, tool limitation, or incomplete subtask.
6. Verify the real outcome yourself before reporting. A result you have not exercised is not finished.
7. Report once, at the end: what now works, what was decided along the way, and only the gates that genuinely remain, each with its owner.

When delegation shortens the path, parallelise only write-disjoint work, give every worker the same requirement identifiers, base revision, owned paths, allowed actions, forbidden external effects, and acceptance evidence, and keep verification independent from implementation.

## Stop when

The minimum usable outcome exists, has been exercised rather than assumed, and every remaining gate is one the user genuinely holds. Waiting on something is a state to route around or monitor, never a reason to hand back an unfinished job.

## Principles

**Critical path first** — Reach the first usable result before any optional completeness, because work that improves nothing the user can yet use is not progress. Source: critical path method, DuPont and Remington Rand, 1957
**Definition of done** — Fix what finished means before starting, so completion is a checked condition rather than a feeling. Source: Scrum practice, Schwaber and Sutherland
**Never fabricate to keep moving** — Invent no credential, no data, no approval, and no success; a blocked path is routed around, never simulated. Source: standing rule in this library
**Reversibility decides authority** — Act alone on anything you could undo, and stop only at the actions that cannot be taken back. Source: Jeff Bezos, Amazon shareholder letter, 2015

## Counter-case

- The user says to finish the app, but the approach was never agreed and the requirement is still a sentence. Executing would be guessing, so `grill-me` sharpens it or `proactive-dev` plans it first.
- The user says to finish, and the work is already built but suspect. Nothing remains to execute, so `are-you-sure` or `dev-are-you-sure` owns it.

## Hand back

The working outcome, the evidence that it was exercised, the decisions taken under the agent's own authority, and the genuinely remaining gates with their owners.

## Sources

Critical path method, 1957. Schwaber and Sutherland, Scrum Guide, definition of done. Bezos 2015, Amazon shareholder letter.
