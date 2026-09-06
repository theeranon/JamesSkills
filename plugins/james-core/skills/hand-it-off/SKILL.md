---
name: hand-it-off
kind: internal-routing
license: CC-BY-NC-4.0
description: Internal fallback that assigns one primary owner when no skill obviously matches. Never select it as the primary workflow, never let it produce a deliverable, and never use it when a direct owner is already clear.
---

# Hand It Off

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

Route by accountable outcome, never by keyword or product name. Choose the workflow that serves the current outcome; compose relevant modes and standards without routing them away. Prefer an explicit project instruction over this router whenever it expresses a more specific accepted decision.

Use the available skill descriptions and load the matching canonical body. Do not maintain a second behavior catalog here. Modes stay active across workflows; standards constrain outputs without competing to own the task.

### Choosing

1. Match the accountable outcome, then the evidence it requires, then the authority it needs. A skill that only reports is never chosen for work that must change something.
2. Prefer the most specific owner. `final-it` is chosen only when no narrower output skill owns the artifact.
3. Preserve any active mode rather than treating it as the primary job.
4. Apply `make-it-james` and `make-it-james-ux` automatically to recipient-facing results.
5. Use `zoom-out` first only when the problem layer or the outcome is genuinely unclear.
6. Routing is internal coordination, not a reason to return only a skill name when the user requested an outcome. Continue the requested work with the selected owner; when an unavailable sibling cannot be loaded, complete the bounded task directly where possible and disclose any actual capability limit. When nothing fits, do the work directly. Repeated uncovered work is discovery evidence, not permission to package.

Common valid chains: `zoom-out` then `give-me-solutions`; `research-it` then `give-me-solutions`; `done-for-me` with persistent `proactive-dev`, using `dev-are-you-sure` for an appropriate review; `sum-meet` or `one-page-pls` then the standards; `never-again` then the affected workflow.

### Candidate Card

Before any new skill, name, alias, or promotion, present one card: two or three natural name options; the bounded job, trigger, exclusions, and output contract; overlap with every nearby skill and why an upgrade or composition is insufficient; source map, recurrence, and confidence; representative requests, failure cases, and a legitimate counter-case; and a recommendation to upgrade, merge, create as pilot, or reject. Keep the candidate at pilot and outside global installs until the owner approves the exact name and scope. Authority to improve the repository is never naming approval.

Do not load a live personal-context adapter merely because the owner is personal or the work is strategic. Activate one only when the outcome genuinely depends on current cross-channel state, and never let it become the primary workflow.

## Stop when

Internal selection is complete. Resume the user's task immediately with the selected workflow and active modes; completing routing is not completing the task.

## Counter-case

- The user asks to finish a task whose plan is already agreed. A direct owner is obvious, so `done-for-me` loads immediately and this router is never selected.
- A request touches research, building, and delivery. It still gets one primary owner per stage rather than making this router the primary skill.

## Hand back

No separate user-facing routing report. The selected workflow delivers the requested outcome; name skills only if the user asked about routing.
