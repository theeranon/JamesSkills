---
name: done-for-me
kind: workflow
license: CC-BY-NC-4.0
description: Carry an already-agreed task all the way to a finished, verified outcome without stopping to ask. Use for a one-time instruction to finish an established outcome. Decide routine planning and implementation details yourself; active conversation modes remain in force.
---

# Done For Me

Take the agreed job to the finish line and only then come back.

## Scope

- Kind: workflow
- Owns: one task whose intent is already established, carried through implementation and its own verification to a usable result.
- Boundary: executes every safe action inside the accepted scope. Never pushes, deploys, sends, publishes, or spends unless the request or the accepted project contract authorises that exact target.

## Do not use this when

- The user asks to design a strategy rather than execute an established outcome -> `proactive-dev` can guide engineering planning. Missing implementation details alone do not block execution.
- The work is finished and its diligence is what is in doubt -> `are-you-sure`
- Delivered code needs a layered sweep and boundary check -> `dev-are-you-sure`
- The requested outcome is only an evidence verdict -> `research-it`. If research is needed to complete the agreed job, do it and continue that job.
- The requirement itself is still vague and must be interrogated -> `grill-me`

## Procedure

1. Find the requirement authority, the current state, and what counts as finished. Consume an approval already present in this conversation or the project contract; never ask the user to repeat it as a confirmation word.
2. Define completion for the whole requested outcome and take the shortest path to it. When the request covers a set, track every item through implementation, verification and delivery, or an evidence-backed decision to retain it. A usable first item is a checkpoint, not permission to leave the rest unfinished. Run the proof the requested outcome needs before optional hardening or documentation cleanup.
3. Execute every in-scope action that does not require an unresolved business decision or missing authorization. Keep useful progress updates brief without stopping work or asking whether to continue.
4. When one path blocks, continue every independent path. Use existing configuration mechanisms for missing inputs. Add a settings surface only when the requested product actually needs one; never fabricate a value.
5. Investigate and repair ordinary failures. Do not stop at the first error, tool limitation, or incomplete subtask.
6. Verify the real outcome yourself before reporting. A result you have not exercised is not finished.
7. A failed test starts diagnosis and correction inside scope; it is not a completed delivery. Do not replace execution with another plan or ask whether to continue already-authorized work. Report once, at the end: what now works, what was decided along the way, and only the gates that genuinely remain, each with its owner.

When delegation shortens the path, parallelise only write-disjoint work, give every worker the same requirement identifiers, base revision, owned paths, allowed actions, forbidden external effects, and acceptance evidence, and keep verification independent from implementation.

## Stop when

The complete requested outcome exists, has been exercised rather than assumed, and every remaining gate is one the user genuinely holds. Name an actual external dependency when blocked; never relabel ordinary remaining work as a user gate. Waiting on something is a state to route around or monitor, never a reason to hand back an unfinished job.

## Principles

**Critical path first** — Reach the first usable result before any optional completeness, because work that improves nothing the user can yet use is not progress. Source: critical path method, DuPont and Remington Rand, 1957
**Definition of done** — Fix what finished means before starting, so completion is a checked condition rather than a feeling. Source: Scrum practice, Schwaber and Sutherland
**Never fabricate to keep moving** — Invent no credential, no data, no approval, and no success; a blocked path is routed around, never simulated. Source: standing rule in this library
**Reversibility decides authority** — Choose reversible implementation details inside scope; use existing authorization for consequential actions and ask only when necessary authority is missing. Source: Jeff Bezos, Amazon shareholder letter, 2015

## Counter-case

- The user says to finish an app but two incompatible business outcomes remain unresolved. Ask about that decision while doing independent work. A clear outcome with an unspecified implementation is different: inspect, choose a method and execute.
- The user says to finish, and the work is already built but suspect. Nothing remains to execute, so `are-you-sure` or `dev-are-you-sure` owns it.

## Hand back

The working outcome and concise verification relevant to the request. Include material decisions or genuine remaining dependencies only when useful; keep an artifact-only response artifact-only. Completing this task ends this workflow, not an active conversation mode.

## Sources

Critical path method, 1957. Schwaber and Sutherland, Scrum Guide, definition of done. Bezos 2015, Amazon shareholder letter.
