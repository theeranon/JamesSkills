---
name: done-for-me
license: CC-BY-NC-4.0
metadata:
  kind: workflow
description: Wake-up call when the agent keeps asking after enough insight and decisions were given. Re-read the whole conversation and every settled decision, then act at once; build what is still ambiguous as a changeable setting or as three to five variants. Use for just do it, stop asking, ทำให้จบ, ทำสักที, พอแล้วถามอยู่นั่น.
---

# Done For Me

Stop asking, re-read everything already decided, and build it now.

## Scope

- Kind: workflow
- Owns: the turn in which the agent recovers every decision the conversation already holds and carries the work to a finished, verified result without another question.
- Boundary: executes every safe action inside the accepted scope. Never pushes, deploys, sends, publishes, or spends unless the request or the accepted project contract authorises that exact target. Never fabricates a value, an approval or a test result to keep moving.

## Do not use this when

- The work is finished and its diligence is what is in doubt -> `are-you-sure`
- Delivered code needs a layered sweep and boundary check -> `dev-are-you-sure`
- The goal itself has never been stated and no file or message holds it -> `grill-me`, once, then return here
- The requested outcome is only an evidence verdict -> `research-it`

## Procedure

1. Treat the invocation as feedback that you asked once too often or lost the thread. Do not apologise and do not explain; recover.
2. Re-read the whole conversation and the project's `ai-context/` from the start: the goal, every decision the user made in their own words, every correction, the insight already given, and the artifact as it stands. Context may have been lost; rebuild it from the record, not from memory. Write nothing new until this is done.
3. List privately what is settled and what is still open. Settled points are never re-asked and never reversed.
4. For each open point, decide anyway, in one of two ways, and say which you used:
   - **Setting.** Build it so the choice can be changed later: a named configuration value, a constant in one place, a parameter with a sensible default. Never a hardcoded guess buried in the work.
   - **Variants.** State plainly that the point is ambiguous and deliver three to five concrete versions that differ on that point, so the user picks instead of answering a question.
5. Before building each piece, turn its goal into a check that can fail: a bug gets a reproduction that fails first and passes after the fix, a feature gets the test or observable result that proves it. Then execute every in-scope action to the finish. Investigate and repair ordinary failures; a failed test starts diagnosis, not a report. When one path blocks, continue every independent path. When delegation shortens the path, parallelise only write-disjoint work and give every worker the same requirement identifiers, base revision, owned paths, allowed actions, forbidden external effects and acceptance evidence; keep verification independent from implementation.
6. Verify the real outcome yourself, as the user would use it, before reporting. A result you have not exercised is not finished.
7. Report once, at the end: what now works, which open points became settings or variants, and only the gates the user genuinely holds (an irreversible external action, missing credentials). Never ask the user to repeat an approval as a confirmation word, and never hand back a list of things still undone.

## Stop when

The complete requested outcome exists, has been exercised rather than assumed, every formerly open point is either a changeable setting or a set of variants, and the only remaining gates are ones the user genuinely holds. Waiting on something is a state to route around, never a reason to return unfinished work.

## Principles

**Definition of done** — Fix what finished means before starting, so completion is a checked condition rather than a feeling. Source: Scrum practice, Schwaber and Sutherland
**Reversibility decides authority** — Decide every reversible point yourself; a decision made as a setting costs nothing to change, while a question costs the user a turn. Source: Jeff Bezos, Amazon shareholder letter, 2015
**Never fabricate to keep moving** — Invent no credential, no data, no approval, and no success; a blocked path is routed around, never simulated. Source: standing rule in this library
**Goal-driven execution** — A goal stated as a check that can fail lets the work loop to completion on its own; "make it work" cannot be verified and invites another question. Source: Andrej Karpathy, post on LLM coding failures, 2026, via the karpathy-guidelines CLAUDE.md
**Recognition over recall** — Show three to five concrete versions to pick from rather than asking the user to compose an answer. Source: Jakob Nielsen, usability heuristics, 1994

## Counter-case

- The user says to finish an app while two incompatible business outcomes remain unresolved and no record favours either. Build both as variants or behind one switch and deliver; do not stop to ask.
- The user says to finish, and the work is already built but suspect. Nothing remains to execute, so `are-you-sure` or `dev-are-you-sure` owns it.
- The next step is sending the result to a client. Finishing never supplies that authorization; deliver the ready artifact and name that one gate.

## Hand back

The working outcome and its verification. The list of open points turned into settings or variants, each in one line. Only genuine user-held gates, each with its owner. An artifact-only request gets the artifact alone.

## Sources

Karpathy 2026, post on LLM coding failures (x.com/karpathy/status/2015883857489522876), as paraphrased in multica-ai/andrej-karpathy-skills. Schwaber and Sutherland, Scrum Guide, definition of done. Bezos 2015, Amazon shareholder letter. Nielsen 1994, Ten Usability Heuristics.
