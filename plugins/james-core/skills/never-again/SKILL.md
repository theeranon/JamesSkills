---
name: never-again
license: CC-BY-NC-4.0
metadata:
  kind: workflow
  version: 2.4.0
description: Wake-up call when the agent stopped recording and starts forgetting: write the missed lessons, decisions and context into ai-context and push, then keep recording every insight, decision, skill change and version unasked. Use for never again, จำไว้เลย, อย่าให้เกิดอีก, ลืมอีกแล้ว, อย่าเป็นคนขยันแต่โง่.
---

# Never Again

Record what was missed, fix the mechanism that let it slip, and keep recording from now on.

## Scope

- Kind: workflow
- Owns: the recovery from a lapse in recording or a repeated mistake: the missed insights, decisions, context and lessons written to their owner documents, and the narrow rule that stops the repeat.
- Boundary: writes to `ai-context/LESSONS.md`, `ai-context/DECISIONS.md`, `ai-context/STATUS.md` and the project's case file, and commits and pushes them under the project's standing rule. Repairs outputs already affected. Never rewrites unrelated project requirements.

## Do not use this when

- The single bad output needs repairing and nothing durable is at stake -> `are-you-sure`
- The defect is in delivered code and the sweep is what is wanted -> `dev-are-you-sure`
- The project has no contract yet and truth is scattered rather than unrecorded -> `project-standard`
- Another agent must continue this work and needs the full state -> `hand-it-off`

## Procedure

1. Treat the invocation as the finding: recording lapsed, or the same mistake happened twice. Do not defend it; recover.
2. Re-read the conversation from the last recorded point and list every insight, key learning, decision, important context, `SKILL.md` change and deliverable version that was never written down.
3. Write each into the owner document that holds that kind of fact, following `project-standard`'s layout: decisions in `ai-context/DECISIONS.md`, current state in `ai-context/STATUS.md`, lessons in `ai-context/LESSONS.md`. Where the project keeps no such files, create the minimum ones rather than inventing a new system.
4. For a repeated mistake, trace the failure far enough to find its mechanism, revise or merge a conflicting rule before adding one, and write a lesson at the narrowest durable scope: what happened, the mechanism, the rule now in force, the date. Add three regressions where the project keeps its behavioral cases: the rejected case, a different case with the same mechanism, and a legitimate counter-case the rule must still allow. Approval to repair the failure is not approval of a new skill, name or global package; that goes through the Candidate Card in `AGENTS.md`.
5. Audit outputs already affected by the lapse or the rule and repair them inside scope.
6. Commit and push the records now; a lesson that exists only in the chat is the lapse repeating. When asked for a draft only, return the proposed entries and say that nothing was persisted.
7. From this point, record continuously: every new insight, decision, context, skill change and version goes into its owner document and GitHub in the same session, without waiting for an instruction.

## Stop when

Every missed item is written to its owner document and pushed, the lesson for any repeated mistake exists with its three regressions, affected outputs are repaired, and recording has resumed. A rule with no counter-case is not finished, because it cannot be shown to be narrow enough.

## Principles

**Blameless post-mortem** — Ask what made the mistake reasonable for the agent that made it, because a rule aimed at carelessness prevents nothing. Source: John Allspaw, Blameless PostMortems, Etsy, 2012
**Latent condition over active error** — Correct the boundary that allowed the failure class, not the last actor in the chain. Source: James Reason, Managing the Risks of Organizational Accidents, 1997
**Poka-yoke** — Prefer a change that makes the mistake impossible over a rule that must be remembered. Source: Shigeo Shingo, Zero Quality Control, 1986
**Counter-case discipline** — Every new rule ships with a legitimate case it must still permit, or it is overfitting to one example. Source: standing rule in this library

## Counter-case

- The user rejects one paragraph's tone in a single document. No failure class and no lost record; `are-you-sure` repairs it.
- The rejection reveals a capability the library does not have at all. Writing a rule would not supply it; the Candidate Card gate in `AGENTS.md` decides, not this workflow.
- Recording has been continuous and the mistake is new. Write the lesson once; do not rewrite the whole status to prove diligence.

## Hand back

The records written and pushed, with their locations; the lesson and three regressions when a mistake repeated; repaired outputs. For a draft-only request, the proposed entries with an explicit statement that no file was changed.

## Sources

Allspaw 2012, Blameless PostMortems and a Just Culture. Reason 1997, Managing the Risks of Organizational Accidents. Shingo 1986, Zero Quality Control.
