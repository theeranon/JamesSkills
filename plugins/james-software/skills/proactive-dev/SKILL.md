---
name: proactive-dev
kind: mode
license: CC-BY-NC-4.0
description: Work as one person holding the analyst, product, architect, build, and quality roles, planning rigorously before writing code and splitting the work across sub-agents. Use when the plan is not good enough yet; not for executing an accepted plan.
---

# Proactive Dev

Make the plan good enough to be worth building, then build it and watch it.

## Scope

- Kind: mode
- Owns: how engineering work is decomposed, planned, sequenced, delegated, and monitored for the remainder of the session.
- Boundary: reads the project contract and architecture before proposing. Writes code and plans inside the accepted scope. Never introduces a new store, identity path, or external dependency without a recorded decision and a rollback.

## Do not use this when

- A plan is already accepted and the job is to execute it to a usable outcome -> `done-for-me`
- Delivered code needs a five-layer sweep and repair -> `dev-are-you-sure`
- The decision posture, not the engineering method, is what needs to change -> `proactive-habits`
- Which layer of the system is failing is still unclear -> `zoom-out`
- The project has no contract yet and truth is scattered -> `project-standard`

## Behavior

Hold five roles in sequence and hand off between them explicitly. Split a role into its own sub-agent whenever its work is large enough to be checked independently, and give every sub-agent the same requirement identifiers, base revision, owned paths, allowed actions, forbidden external effects, and acceptance evidence.

1. **Analyst.** Restate what is actually being asked, separately from what was said. Name the real user, the failing responsibility, and the fact that must become true.
2. **Product.** Fix scope, order, and done-criteria before design. Cut what does not change the outcome. State what is deliberately not being built.
3. **Architect.** Read `ARCHITECTURE.md` and the project contract before proposing structure. New work conforms to the recorded architecture or arrives with an explicit decision to change it. Verify three things every time: each fact has exactly one source of truth, the schema expresses the real relationships rather than a convenient shape, and no parallel store or duplicated identity path is being introduced.
4. **Builder.** Implement in the smallest coherent increments. Parallelise only write-disjoint work; use one implementer for shared state.
5. **Quality.** Check against the done-criteria written in step two, not against the code just written. Keep this role independent from the builder when the risk justifies it.

Then monitor. State what is finished, what is running, and what is blocked, without being asked.

Plan rigorously, then act. A plan that has not named its failure mode, its rollback, and its blast radius is not finished being planned.

## Stays active until

The user turns it off or the engineering work ends. It does not carry into unrelated conversation or into non-engineering work.

## Principles

**Begin with the end in mind** — Write the done-criteria before the design, and let them decide what is built rather than discovering scope while coding. Source: Stephen R. Covey, The 7 Habits of Highly Effective People, 1989
**Single source of truth** — Every fact lives in exactly one place; any second copy is a defect with a migration attached, not a convenience. Source: standard data-modelling principle; specific attribution uncertain
**Make the change easy, then make the easy change** — When a change is hard, first restructure until it is easy, and keep the two steps in separate commits. Source: Kent Beck, 2012
**Yellow-stage mastery** — Produce work a master would sign without supervision, and treat any point where everything routes through you as the defect to remove next. Source: Wealth Spectrum, registered in this library's knowledge pack
**Blast radius before execution** — Before any mutating action, state what else it touches, what it costs if wrong, and how it is undone. Source: uncertain attribution; standing rule in this library

## Counter-case

- The user approved a plan last week and asks to finish building it. Nothing needs replanning, so `done-for-me` owns it and this mode's planning gate would only add delay.
- A single component renders wrong and the fix is a two-line CSS change. Full role decomposition is waste; `dev-are-you-sure` or direct work owns it.

## Hand back

The restated requirement, the scope with its explicit exclusions, the architecture decision and its rollback, the increments built, the quality result against the done-criteria, and the current state of anything still running or blocked.

## Sources

Covey 1989, The 7 Habits of Highly Effective People. Beck 2012, public statement on preparatory refactoring. Wealth Spectrum stage material, registered at `packs/knowledge/lenses/wealth-spectrum`.
