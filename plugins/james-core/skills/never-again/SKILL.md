---
name: never-again
kind: workflow
license: CC-BY-NC-4.0
description: Repair a recurring failure mechanism with a narrow, discoverable lesson or an update to an existing rule. Use when a mistake should never recur; not for fixing the one bad output and not for routine quality sweeps.
---

# Never Again

Repair the mechanism and make the lesson discoverable at the right scope.

## Scope

- Kind: workflow
- Owns: preventing an evidenced recurring failure at the narrowest durable scope, with cases that check the correction.
- Boundary: updates the relevant lesson or rule at the chosen scope and its required-reading pointer when needed. Repairs outputs already affected by the rule. Never rewrites unrelated project requirements.

## Do not use this when

- The single bad output needs repairing and nothing durable is at stake -> `are-you-sure`
- The defect is in delivered code and the sweep is what is wanted -> `dev-are-you-sure`
- The project has no contract yet and truth is scattered rather than wrong -> `project-standard`
- The output is merely mediocre rather than wrong -> `is-that-the-best-you-can-do`
- The correction suggests a whole new capability -> `hand-it-off` for a Candidate Card

## Procedure

1. Trace the actual failure path far enough to identify its mechanism: locate the boundary that allowed the failure class, not merely the final bad phrase or record. Inspect existing rules before changing them; revise, merge or remove a conflicting rule before adding another, targeting the highest-authority reusable rule or mechanism the evidence reaches. Do not analyze nonexistent system layers.
2. Choose the narrowest durable scope the evidence supports: this output, this project, this workflow, or the shared library. Generalise no further: do not add affected statuses, domains or prohibitions merely because they sound related. Do not accumulate one-case keyword bans when the failure actually came from judgment, ownership, evidence, or architecture; fix the mechanism instead. Preserve any transfer scenario explicitly requested by the user; demonstrate the mechanism within it rather than substitute an easier example.
3. Follow the requested action boundary: if asked for a draft or if writing tools are unavailable, return the proposed lesson and regressions and state that nothing was persisted. Never claim a pointer, test or repair was created without executing and verifying it. Otherwise update a relevant existing lesson or, if none covers the mechanism, write the lesson to `ai-context/LESSONS.md` in the project at that scope, as one entry: what happened, the mechanism that allowed it, the rule now in force, and the date.
4. Make it discoverable through the existing automatically loaded contract. Reuse a valid required-reading pointer when present; add the missing pointer only to the actual host contract, without creating unrelated vendor files. A pointer requests reading; it does not prove every runtime read or obeyed it.
5. Add three regressions to the behavioral cases: the rejected case, a different case with the same mechanism, and a legitimate counter-case the rule must still allow.
6. Audit outputs already affected by the new rule and repair them inside scope.

## Stop when

For an execution request, the corrected lesson or rule exists, at least one automatically loaded contract file points at it, all three regressions are written, and affected outputs are repaired. For a draft-only request, the proposed entry and three cases are complete and explicitly not persisted. A rule with no counter-case is not finished, because it cannot be shown to be narrow enough.

## Principles

**Blameless post-mortem** — Ask what made the mistake reasonable for the agent that made it, because a rule aimed at carelessness prevents nothing. Source: John Allspaw, Blameless PostMortems, Etsy, 2012
**Latent condition over active error** — Correct the boundary that allowed the failure class, not the last actor in the chain. Source: James Reason, Managing the Risks of Organizational Accidents, 1997
**Poka-yoke** — Prefer a change that makes the mistake impossible over a rule that must be remembered. Source: Shigeo Shingo, Zero Quality Control, 1986
**Counter-case discipline** — Every new rule ships with a legitimate case it must still permit, or it is overfitting to one example. Source: standing rule in this library

## Counter-case

- The user rejects one paragraph's tone in a single document. No failure class is implied and no rule should outlive the fix, so `are-you-sure` repairs it.
- The rejection reveals a capability the library does not have at all. Writing a rule would not supply it, so `hand-it-off` opens a Candidate Card instead. Approval to repair the failure is not approval of a new name, ontology, or global package.

## Hand back

For executed work: the verified lesson entry and contract pointer, three regressions, repaired outputs and scope. For draft-only work: the proposed entry and cases, with an explicit statement that no file was changed. Never describe proposed persistence as completed.

## Sources

Allspaw 2012, Blameless PostMortems and a Just Culture. Reason 1997, Managing the Risks of Organizational Accidents. Shingo 1986, Zero Quality Control.
