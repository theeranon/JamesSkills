---
name: skill-router
description: Internal-only fallback routing reference; never select it as the primary user workflow. Use only after direct matching finds no clear canonical owner.
---

# Skill Router

Route by the requested outcome and responsibility, not by keywords or product names.

This router produces no user deliverable and never owns the work. If one canonical workflow clearly matches, stop using the router and load that owner directly. A request spanning several responsibilities still receives one real primary owner plus distinct supporting skills; it does not make `skill-router` the primary skill.

Direct-owner rules take precedence over generic classification:

- rejected result that must become a scoped system correction -> `never-again`

1. Try every clear direct-owner rule before using fallback classification. Classify the remaining request as a bounded workflow, persistent mode, shared standard, output workflow, knowledge lens, project context, connector, automation, or direct work.
2. Identify the actual outcome, evidence required, risk, current authority, and remaining human decision.
3. Choose the smallest applicable path. Mentioned products are candidates, not requirements.
4. Compose skills only when their responsibilities are distinct and required. Apply mandatory standards and guardrails automatically.
5. If no skill fits, handle the work directly. Treat repeated uncovered work as discovery evidence, not permission to package it immediately.

Before creating or promoting a skill, present one Candidate Card containing:

- two or three natural invocation-name options
- the bounded job, trigger, exclusions, and output contract
- overlap with every nearby current skill and why an upgrade or composition is insufficient
- source map, recurrence, damage or value, cross-project reuse, and confidence
- representative requests, failure cases, and legitimate counter-cases
- recommendation to upgrade, merge, create as pilot, or reject

Keep the candidate `pilot` and outside global installs until James approves the exact name and scope. Authorization to improve the repository is not naming or ontology approval.

## Portfolio map

- `zoom-out`: reframe the system and responsibility boundary before solving.
- `give-me-solutions`: research real external options and prepare comparable decision material.
- `baseon`: apply or compare a named framework, book, or knowledge lens.
- `done-for-me`: own authorized implementation through the usable outcome.
- `prove-it`: verify a claim at the recipient, provider, persistence, or production boundary that matters.
- `never-again`: convert a rejected result into a scoped system correction and counter-tested guard.
- `catchup`: reconstruct verified current state after a continuity gap, agent handoff, or suspected stale project status; not ordinary active-task progress or one isolated completion claim.
- `project-standard`: create or repair the vendor-neutral project contract when project truth is missing or drifting.
- `sum-meet`: produce one detailed meeting record containing every agenda.
- `one-page-pls`: produce one self-contained one-page artifact per topic or agenda.
- `final-it`: select and finish the recipient-ready artifact when no more specific output workflow owns it.
- `i-have-adhd`: persistent communication mode that composes with the primary workflow.
- `make-it-james`: automatic recipient-facing standard that composes with the selected output for wording and tone.
- `make-it-james-ux`: automatic visual/UI standard for recipient-facing outputs.

## Composition order

1. Preserve any active mode.
2. Use `zoom-out` first only when the problem layer or outcome is wrong or unclear.
3. Give one primary workflow ownership of the job. Add another workflow only for a distinct responsibility.
4. Use the most specific output skill; use `final-it` only when no narrower output owns the artifact.
5. Apply `make-it-james` and `make-it-james-ux` to every recipient-facing result and `prove-it` at the actual completion boundary.

Common valid compositions:

```text
zoom-out -> give-me-solutions
done-for-me -> prove-it
sum-meet or one-page-pls -> make-it-james + make-it-james-ux -> prove-it
project-standard -> done-for-me -> prove-it
never-again -> affected workflow -> regression and counter-case proof
```

Do not load a whole chain merely because the names are related. Each added skill must own a distinct decision or deliverable.

Use `baseon` when the outcome is applying or comparing a named framework, book, or knowledge model. Register a new book as a source first; do not create a new skill or lens merely because its title appears in the request. Treat `wealth-dynamics` and `talent-dynamics` as shortcuts to the same Dynamics lens. Treat `wealth-spectrum` as a separate lens even though it shares the same creator lineage.

`catchup` is promoted for bounded continuity recovery; do not trigger it for ordinary progress inside an active task or one isolated completion claim.

Route a rejected or absurd output and its failure class to `never-again`. A system correction may later expose a reusable candidate, but the two jobs are not interchangeable.

Duration does not determine ownership. The final accountable outcome does. Internal create, audit, repair, and improve states are inferred and never become user-required commands.

Prefer project instructions when they express a more specific accepted decision.

## Live-context adapter boundary

Do not load JamesOS or another personal live-context adapter merely because James owns the task or the work is strategic. Activate one only when the outcome genuinely depends on current cross-channel context, commitments, people or owner routing, a secretary queue, personal operating state, or an explicit request for that system. If the current task or project already provides authoritative requirements and evidence, use those sources and keep the context adapter out. A context adapter supplies missing live state; it never becomes the primary workflow by default.
