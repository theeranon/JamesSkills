---
name: never-again
kind: workflow
license: CC-BY-NC-4.0
description: Turn one rejected output into a written lesson that every future agent is forced to read before working in this repository. Use when a mistake should never recur; not for fixing the one bad output and not for routine quality sweeps.
---

# Never Again

Write the lesson where the next agent cannot avoid reading it.

## Scope

- Kind: workflow
- Owns: converting one rejected result into a durable, force-loaded rule plus the regressions that prove it holds.
- Boundary: writes to the lesson ledger and to the highest-authority rule file at the chosen scope. Repairs outputs already affected by the rule. Never rewrites unrelated project requirements.

## Do not use this when

- The single bad output needs repairing and nothing durable is at stake -> `are-you-sure`
- The defect is in delivered code and the sweep is what is wanted -> `dev-are-you-sure`
- The project has no contract yet and truth is scattered rather than wrong -> `project-standard`
- The output is merely mediocre rather than wrong -> `is-that-the-best-you-can-do`
- The correction suggests a whole new capability -> `hand-it-off` for a Candidate Card

## Procedure

1. Reconstruct the path from source and ingestion through interpretation, state, policy, delivery, and the recipient's experience. Find the boundary that allowed the class, not the final bad phrase.
2. Choose the narrowest durable scope the evidence supports: this output, this project, this workflow, or the shared library. Generalise no further.
3. Write the lesson to `ai-context/LESSONS.md` in the project at that scope, as one entry: what happened, the mechanism that allowed it, the rule now in force, and the date.
4. Make it unavoidable. `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` each carry a required-reading line pointing at the ledger, so any agent entering the repository loads it before working. If those files do not exist, create the pointer in whichever contract file the platform loads automatically, and say which.
5. Add three regressions to the behavioral cases: the rejected case, a different case with the same mechanism, and a legitimate counter-case the rule must still allow.
6. Audit outputs already affected by the new rule and repair them inside scope.

## Stop when

The lesson entry exists, at least one automatically loaded contract file points at it, all three regressions are written, and affected outputs are repaired. A rule with no counter-case is not finished, because it cannot be shown to be narrow enough.

## Principles

**Blameless post-mortem** — Ask what made the mistake reasonable for the agent that made it, because a rule aimed at carelessness prevents nothing. Source: John Allspaw, Blameless PostMortems, Etsy, 2012
**Latent condition over active error** — Correct the boundary that allowed the failure class, not the last actor in the chain. Source: James Reason, Managing the Risks of Organizational Accidents, 1997
**Poka-yoke** — Prefer a change that makes the mistake impossible over a rule that must be remembered. Source: Shigeo Shingo, Zero Quality Control, 1986
**Counter-case discipline** — Every new rule ships with a legitimate case it must still permit, or it is overfitting to one example. Source: standing rule in this library

## Counter-case

- The user rejects one paragraph's tone in a single document. No failure class is implied and no rule should outlive the fix, so `are-you-sure` repairs it.
- The rejection reveals a capability the library does not have at all. Writing a rule would not supply it, so `hand-it-off` opens a Candidate Card instead. Approval to repair the failure is not approval of a new name, ontology, or global package.

## Hand back

The lesson entry, the contract file that now forces it to be read, the three regressions, the list of outputs repaired, and the exact scope the rule covers.

## Sources

Allspaw 2012, Blameless PostMortems and a Just Culture. Reason 1997, Managing the Risks of Organizational Accidents. Shingo 1986, Zero Quality Control.
