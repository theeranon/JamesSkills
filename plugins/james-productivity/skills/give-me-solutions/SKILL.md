---
name: give-me-solutions
kind: workflow
description: Compare real options against this project's actual context and name the best one with its reasoning. Use when a choice must be made between candidates; not for settling a single claim and not for making the decision happen.
---

# Give Me Solutions

Find the real options, judge them against this situation, and say which one wins.

## Scope

- Kind: workflow
- Owns: one open choice between candidates, resolved into ranked options with a named front-runner and the reasoning behind it.
- Boundary: researches, compares, and recommends. Never purchases, signs up, migrates, or commits on the user's behalf.

## Do not use this when

- One claim or approach needs to be settled rather than several compared -> `research-it`
- Which responsibility is actually failing is still unclear -> `zoom-out`
- The choice is already made and the job is to build it -> `done-for-me`
- A registered framework should interpret the situation -> `baseon`
- The candidates are internal drafts of the same artifact -> `is-that-the-best-you-can-do`

## Procedure

1. Establish the real job: the bounded role that must be filled, the hard requirements, the disqualifiers, the budget, and the operating capacity available to run whatever is chosen.
2. Test whether something already owned can fill the role. Reuse is a candidate, not an automatic winner, and it competes on the same requirements as everything else.
3. Cover the candidate field in one bounded pass across genuinely different classes of answer, not several versions of the same one.
4. Keep a source ledger for each candidate, gathering evidence the way `research-it` does: the official position, then independent practitioner accounts with their dates and stated stakes. Delegate that pass to `research-it` when the evidence load is heavy.
5. Eliminate anything that fails a hard requirement, and say why rather than leaving it in the table as filler.
6. Compare every survivor against the same requirement set, including setup cost, recurring cost, migration effort, lock-in, reliability, security, and the ongoing operating burden on this specific team.
7. Bind the comparison to this project and this conversation: the stack already in place, the accepted decisions, the constraints stated earlier, and the skills actually available to operate it. A generic ranking is not the deliverable.
8. Name the best option and say exactly why it wins here. Keep the meaningful alternatives with the condition that would make each of them the right answer instead.

## Stop when

Every relevant class of candidate is covered, each survivor is compared on the same requirements, a front-runner is named with its reasoning, and another search pass no longer changes the ranking or reveals a new failure class. Unknowns are stated, not filled.

## Principles

**Widen the frame** — Refuse a one-option yes-or-no comparison and force at least one genuinely different class of answer into the set. Source: Chip Heath and Dan Heath, Decisive, 2013
**Dominance filtering** — Remove any option beaten by another on every dimension before spending analysis on it, so effort goes to real trade-offs. Source: standard multi-criteria decision analysis
**Total cost of ownership** — Compare lifetime cost including migration, operation, and exit, never the entry price. Source: Gartner, total cost of ownership method, 1987
**Reference class forecasting** — Estimate from what actually happened to comparable adopters rather than from the plan for this one. Source: Daniel Kahneman and Amos Tversky, outside view, 1979; developed by Bent Flyvbjerg

## Counter-case

- The user asks whether server components are actually faster in practice. One claim is in question and nothing is being chosen, so `research-it` owns it.
- The user asks which of two internal drafts of the same proposal is stronger. These are versions rather than candidates, so `is-that-the-best-you-can-do` raises the better one.

## Hand back

The bounded role and its hard requirements, what was eliminated and why, the survivors compared on identical criteria against this project's real context, the named best option with its reasoning, and the condition that would flip the decision.

## Sources

Heath and Heath 2013, Decisive. Kahneman and Tversky 1979, Intuitive Prediction; Flyvbjerg on reference class forecasting. Gartner 1987, total cost of ownership.
