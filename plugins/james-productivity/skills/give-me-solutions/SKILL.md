---
name: give-me-solutions
kind: workflow
license: CC-BY-NC-4.0
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
3. Use the requested candidate set. If the field is open, cover genuinely different classes of answer in one bounded pass; do not expand a closed comparison without a material reason.
4. Gather evidence the way `research-it` does, using supplied sources first and outside research where needed. Keep a ledger when it helps the choice; never invent dates, commercial independence or missing observations to fill it. Delegate that pass to `research-it` when the evidence load is heavy. Mark each piece of evidence as a vendor claim, an independently confirmed fact, an inference, or an unknown. Popularity and polished demos are not outcome proof; weigh them accordingly against independent reviews, long-term user reports, and failure stories.
5. Eliminate anything that fails a hard requirement, and say why rather than leaving it in the table as filler.
6. Compare every survivor against the same relevant requirements, including setup cost, recurring cost, migration effort, lock-in, reliability, security, and operating burden where they affect this choice. Missing cost, setup time or capability is unknown, never zero or satisfied; do not add a guessed value in parentheses or use it later to rank the options. Existing ownership does not prove readiness or team competence. Compute total effort over the stated horizon; keep unknown fees separate from time savings and make recommendations conditional on material gaps.
7. Bind the comparison to this project and this conversation: the stack already in place, the accepted decisions, the constraints stated earlier, and the skills actually available to operate it. A generic ranking is not the deliverable.
8. Present the strongest options first. For each, show why it fits, its advantages, disadvantages, hidden cost, operational risk, and who it suits. Name the best option and say exactly why it wins here. Keep the meaningful alternatives with the condition that would make each of them the right answer instead.

## Stop when

The requested candidates are compared on relevant requirements and the recommendation is supported or conditional on a named material unknown. Search again only to resolve a specific gap that could change the choice; do not run extra passes merely to prove the ranking stays unchanged. Unknowns are stated, not filled.

## Principles

**Widen the frame** — When the choice is open, consider a genuinely different class of answer to avoid a false binary; respect an explicitly bounded candidate set. Source: Chip Heath and Dan Heath, Decisive, 2013
**Dominance filtering** — Remove any option beaten by another on every dimension before spending analysis on it, so effort goes to real trade-offs. Source: standard multi-criteria decision analysis
**Total cost of ownership** — Compare costs over the relevant decision horizon, including migration, operation and exit where material; a one-time choice may need only its stated price. Source: Gartner, total cost of ownership method, 1987
**Reference class forecasting** — Estimate from what actually happened to comparable adopters rather than from the plan for this one. Source: Daniel Kahneman and Amos Tversky, outside view, 1979; developed by Bent Flyvbjerg

## Counter-case

- The user asks whether server components are actually faster in practice. One claim is in question and nothing is being chosen, so `research-it` owns it.
- The user asks which of two internal drafts of the same proposal is stronger. These are versions rather than candidates, so `is-that-the-best-you-can-do` raises the better one.

## Hand back

The bounded role and its hard requirements, what was eliminated and why, the survivors compared on identical criteria against this project's real context, the named best option with its reasoning, and the condition that would flip the decision.

## Sources

Heath and Heath 2013, Decisive. Kahneman and Tversky 1979, Intuitive Prediction; Flyvbjerg on reference class forecasting. Gartner 1987, total cost of ownership.
