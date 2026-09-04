---
name: skill-router
kind: internal-routing
description: Internal fallback that assigns one primary owner when no skill obviously matches. Never select it as the primary workflow, never let it produce a deliverable, and never use it when a direct owner is already clear.
---

# Skill Router

Find the one owner, hand over, and get out of the way.

## Scope

- Kind: internal-routing
- Owns: choosing the primary owner for a request when direct matching failed, and holding the Candidate Card gate for anything new.
- Boundary: routes only. Produces no user deliverable, never owns the work, never creates or promotes a skill.

## Do not use this when

- One canonical owner already clearly matches -> load that owner, for example `done-for-me`
- The request spans several responsibilities but one outcome is accountable -> give that owner the job, for example `project-standard`
- The user asked to be interrogated rather than routed -> `grill-me`
- The problem layer itself is unclear -> `zoom-out`

## Procedure

Route by accountable outcome, never by keyword or product name. Give exactly one skill the job, add another only for a genuinely distinct responsibility, and apply standards automatically.

### The 22

- `proactive-habits` — mode: decide what is yours, batch the rest to one question.
- `proactive-dev` — mode: plan engineering rigorously across analyst, product, architect, build, and quality roles before code.
- `i-have-adhd` — mode: shape replies so they can be acted on without holding state.
- `make-it-james` — standard: wording law on anything a person reads.
- `make-it-james-ux` — standard: visual law, following the project's existing design system first.
- `done-for-me` — finish an already-agreed task to a verified outcome.
- `are-you-sure` — five-layer sweep and repair of a business or productivity artifact.
- `dev-are-you-sure` — five-layer sweep plus deployment boundary chain for software.
- `is-that-the-best-you-can-do` — measure the gap to the ceiling and spend effort closing it.
- `research-it` — settle one claim with outside evidence, official and real-user.
- `never-again` — write one rejected result into a force-loaded lesson with regressions.
- `zoom-out` — climb to strategy and hold action until the direction is agreed.
- `give-me-solutions` — compare candidates in this context and name the best.
- `grill-me` — interrogate until the requirement is sharp, then recap and confirm.
- `coach-me` — move a person with questions only, always positive.
- `baseon` — apply or compare registered lenses against a real case.
- `catchup` — reconstruct verified current state onto the standard catchup page; not ordinary active-task progress.
- `sum-meet` — one auditable meeting record holding every agenda.
- `one-page-pls` — one self-contained page per independent topic.
- `final-it` — choose the serving format and finish it, when nothing narrower owns it.
- `project-standard` — create or repair the versioned project contract.
- `skill-router` — this fallback.

### Choosing

1. Match the accountable outcome, then the evidence it requires, then the authority it needs. A skill that only reports is never chosen for work that must change something.
2. Prefer the most specific owner. `final-it` is chosen only when no narrower output skill owns the artifact.
3. Preserve any active mode rather than treating it as the primary job.
4. Apply `make-it-james` and `make-it-james-ux` automatically to recipient-facing results.
5. Use `zoom-out` first only when the problem layer or the outcome is genuinely unclear.
6. When nothing fits, do the work directly. Repeated uncovered work is discovery evidence, not permission to package.

Common valid chains: `zoom-out` then `give-me-solutions`; `research-it` then `give-me-solutions`; `proactive-dev` then `done-for-me` then `dev-are-you-sure`; `sum-meet` or `one-page-pls` then the standards; `never-again` then the affected workflow.

### Candidate Card

Before any new skill, name, alias, or promotion, present one card: two or three natural name options; the bounded job, trigger, exclusions, and output contract; overlap with every nearby skill and why an upgrade or composition is insufficient; source map, recurrence, and confidence; representative requests, failure cases, and a legitimate counter-case; and a recommendation to upgrade, merge, create as pilot, or reject. Keep the candidate at pilot and outside global installs until the owner approves the exact name and scope. Authority to improve the repository is never naming approval.

Do not load a live personal-context adapter merely because the owner is personal or the work is strategic. Activate one only when the outcome genuinely depends on current cross-channel state, and never let it become the primary workflow.

## Stop when

One primary owner is named and loaded, any additional skill present owns a genuinely distinct responsibility, and this router has produced nothing else.

## Principles

**Route by outcome, not vocabulary** — Assign the owner from what must become true, because a product name in the request is a candidate rather than a requirement. Source: standing rule in this library
**Most specific owner wins** — Prefer the narrowest skill that fully covers the job, so the general fallback never competes with a specialist. Source: standard dispatch principle; specific attribution uncertain
**One accountable owner** — Exactly one skill is answerable for the outcome; shared ownership produces work nobody finishes. Source: single responsible individual practice; specific attribution uncertain
**Naming is an owner decision** — Never create, rename, or promote a skill without an approved Candidate Card, because a name silently reshapes the whole portfolio. Source: standing rule in this library

## Counter-case

- The user asks to finish a task whose plan is already agreed. A direct owner is obvious, so `done-for-me` loads immediately and this router is never selected.
- A request touches research, building, and delivery. It still gets one primary owner per stage rather than making this router the primary skill.

## Hand back

The named primary owner, any supporting skill with the distinct responsibility it holds, and nothing else. This router never returns a deliverable.

## Sources

No external work is paraphrased above; the principles are standing rules of this library except where marked uncertain.
