# JamesSkills Handbook

Choose a skill by the moment you need it. Type the slash command when you want to force a specific workflow. An agent may select the smallest matching workflow automatically when its platform loads the installed skill and supports that routing; this is not verified on every platform.

This handbook is the human navigation layer. `catalog.json` owns category, lifecycle, and aliases. Each linked `SKILL.md` owns the actual behavior. If a summary here ever conflicts with a canonical skill, the canonical skill wins and this handbook must be repaired.

## Start in 60 seconds

1. Start or repair a project contract with `/project-standard`.
2. Return after a gap with `/catchup`.
3. Research choices with `/give-me-solutions`; decide as the human owner.
4. Finish authorized work with `/done-for-me`, then verify the real outcome with `/prove-it`.
5. Ask for `/sum-meet`, `/one-page-pls`, or `/final-it` when the outcome is a recipient-facing artifact; `make-it-james` applies automatically.

Mode and standard behavior differs from a normal workflow:

- `/i-have-adhd` remains active for the current conversation until explicitly disabled.
- `make-it-james` applies automatically to recipient-facing outcomes; invoking it directly is useful for a visual or Final Word audit.
- `james-skill-router` is installed agent support, not a recommended human command.

## Start or return to work

### `/project-standard`

- Canonical package: `project-standard`
- Category: `standards`
- Lifecycle: `promoted`
- Use when: starting or restructuring a project, converting an agreed outcome into requirements, repairing conflicting project truth, or preparing an AI handoff.
- Result: one vendor-neutral contract with clear owners for intent, current state, agent rules, and decisions.
- Do not use when: routine work is already governed by a current contract.
- Common composition: `/project-standard` -> `/done-for-me` -> `/prove-it`.
- Aliases: `project-docs-standard` is a legacy compatibility call.
- Canonical instructions: [`skills/standards/project-standard/SKILL.md`](../skills/standards/project-standard/SKILL.md)

### `/catchup`

- Canonical package: `catchup`
- Category: `core`
- Lifecycle: `promoted`
- Use when: returning after a continuity gap, switching agents, or suspecting that the written status is stale.
- Result: verified current truth, material delta, open work, conflicts, evidence freshness, and the safe continuation point.
- Do not use when: asking for ordinary progress inside an active task or checking one isolated completion claim.
- Common composition: `/catchup` -> the smallest workflow that owns the remaining work.
- Aliases: none.
- Canonical instructions: [`skills/core/catchup/SKILL.md`](../skills/core/catchup/SKILL.md)

## Frame and decide

### `/zoom-out`

- Canonical package: `zoom-out`
- Category: `core`
- Lifecycle: `promoted`
- Use when: work is fragmented, the visible problem may be a symptom, or the architecture and responsibility boundary are unclear.
- Result: a reframed system problem, named outcome, boundary, and direct decision path.
- Do not use when: the target and requested action are already clear enough to execute safely.
- Common composition: `/zoom-out` -> `/give-me-solutions` when external choices still need research.
- Aliases: none.
- Canonical instructions: [`skills/core/zoom-out/SKILL.md`](../skills/core/zoom-out/SKILL.md)

### `/give-me-solutions`

- Canonical package: `give-me-solutions`
- Category: `core`
- Lifecycle: `promoted`
- Use when: comparing products, stacks, services, or other real external alternatives using independent experience as well as official sources.
- Result: comparable viable options, evidence quality, tradeoffs, and a strongest recommendation without stealing the final decision.
- Do not use when: the evidence already exists and only an internal choice remains, or when authority already determines one reversible implementation path.
- Common composition: `/give-me-solutions` -> human decision -> `/done-for-me` -> `/prove-it`.
- Aliases: none.
- Canonical instructions: [`skills/core/give-me-solutions/SKILL.md`](../skills/core/give-me-solutions/SKILL.md)

### `/baseon`

- Canonical package: `baseon`
- Category: `core`
- Lifecycle: `promoted`
- Use when: applying or comparing a named framework, book, research source, or reviewed knowledge lens to a real decision.
- Result: source-bounded analysis that separates author claims, case evidence, inference, limits, and a reversible application.
- Do not use when: no named source or reusable lens is relevant, or when a stored profile is being treated as an official result without confirmation.
- Common composition: `/baseon` may feed `/give-me-solutions`, `/project-standard`, or direct owner judgment.
- Aliases: `wealth-dynamics`, `talent-dynamics`, and `wealth-spectrum` are recommended lens shortcuts; `think-with-this` is a legacy compatibility call.
- Canonical instructions: [`skills/core/baseon/SKILL.md`](../skills/core/baseon/SKILL.md)

### `/grill-me`

- Canonical package: `grill-me`
- Category: `core`
- Lifecycle: `promoted`
- Use when: you have a plan, decision, or idea and want the AI to stress-test it through a branching interview to expose risks and dependencies.
- Result: a clarified decision tree, resolved conflicts, and a concrete action plan, gathered via an interactive UI or Text-Chat fallback.
- Do not use when: you just want a quick opinion without a structured interview.
- Common composition: `/grill-me` -> owner decision -> `/done-for-me`.
- Aliases: none.
- Canonical instructions: [`skills/core/grill-me/SKILL.md`](../skills/core/grill-me/SKILL.md)

## Execute, verify, and learn

### `/done-for-me`

- Canonical package: `done-for-me`
- Category: `core`
- Lifecycle: `promoted`
- Use when: authorized work should be carried through implementation and verification without user micromanagement.
- Result: the minimum usable outcome, safe parallel progress around optional blockers, and only genuine remaining gates.
- Do not use when: a new business decision or ungranted irreversible external action is required.
- Common composition: the chosen workflow -> `/done-for-me` -> `/prove-it`.
- Aliases: none.
- Canonical instructions: [`skills/core/done-for-me/SKILL.md`](../skills/core/done-for-me/SKILL.md)

### `/prove-it`

- Canonical package: `prove-it`
- Category: `core`
- Lifecycle: `promoted`
- Use when: a result, deployment, integration, notification, document, or agent claim must be verified at the boundary that matters to its recipient.
- Result: an evidence-backed pass, fail, or still-unproved verdict tied to the exact target.
- Do not use when: a broad project catchup is needed rather than verification of a bounded promise.
- Common composition: any implementation or recipient-facing output -> `/prove-it`.
- Aliases: none.
- Canonical instructions: [`skills/core/prove-it/SKILL.md`](../skills/core/prove-it/SKILL.md)

### `/never-again`

- Canonical package: `never-again`
- Category: `core`
- Lifecycle: `promoted`
- Use when: one rejected or absurd result exposes a reusable failure mechanism rather than a one-off content error.
- Result: the highest-authority scoped correction plus rejected-case, same-mechanism, and legitimate counter-case regressions.
- Do not use when: only one isolated artifact needs a local factual edit.
- Common composition: `/never-again` -> repair the owning workflow -> `/prove-it` when recipient behavior matters.
- Aliases: none.
- Canonical instructions: [`skills/core/never-again/SKILL.md`](../skills/core/never-again/SKILL.md)

## Produce the outcome

### `/final-it`

- Canonical package: `final-it`
- Category: `outputs`
- Lifecycle: `promoted`
- Use when: a requested result must become the finished recipient-ready artifact in the format that best fits the job.
- Result: one clean final artifact with source truth preserved and production residue removed.
- Do not use when: a more specific output skill such as meeting summary or one-page owns the semantics.
- Common composition: `/final-it` -> automatic `make-it-james` -> `/prove-it`.
- Aliases: none.
- Canonical instructions: [`skills/outputs/final-it/SKILL.md`](../skills/outputs/final-it/SKILL.md)

### `/sum-meet`

- Canonical package: `sum-meet`
- Category: `outputs`
- Lifecycle: `promoted`
- Use when: transcripts, notes, files, or the current conversation must become one complete meeting record containing every agenda.
- Result: one detailed, source-faithful, print-ready A4 portrait HTML with separate agenda zones.
- Do not use when: the user wants one independent page per topic rather than one full record.
- Common composition: `/sum-meet` -> automatic `make-it-james` -> `/prove-it`.
- Aliases: `solutionsimpact-meeting-summary-full` is a legacy compatibility call.
- Canonical instructions: [`skills/outputs/sum-meet/SKILL.md`](../skills/outputs/sum-meet/SKILL.md)

### `/one-page-pls`

- Canonical package: `one-page-pls`
- Category: `outputs`
- Lifecycle: `promoted`
- Use when: source material must become one self-contained executive page per topic or agenda.
- Result: separate concise one-page artifacts without silently blending unrelated agendas or losing decisions, actions, risks, and evidence.
- Do not use when: one detailed multi-agenda meeting record is required.
- Common composition: `/one-page-pls` -> automatic `make-it-james` -> `/prove-it`.
- Aliases: `solutionsimpact-onepagesummary` is a legacy compatibility call.
- Canonical instructions: [`skills/outputs/one-page-pls/SKILL.md`](../skills/outputs/one-page-pls/SKILL.md)

## Persistent and automatic behavior

### `/i-have-adhd`

- Canonical package: `i-have-adhd`
- Category: `modes`
- Lifecycle: `promoted`
- Use when: conversation should stay concise, direct, human, and visibly progressing without discarding decision-critical information.
- Result: a persistent current-conversation communication mode that batches interruptions and preserves necessary options, evidence, and gates.
- Do not use when: brevity would be mistaken for deleting necessary information or limiting the user to one arbitrary option.
- Common composition: wraps any workflow until explicitly disabled.
- Aliases: none.
- Canonical instructions: [`skills/modes/i-have-adhd/SKILL.md`](../skills/modes/i-have-adhd/SKILL.md)

### `/make-it-james`

- Canonical package: `make-it-james`
- Category: `standards`
- Lifecycle: `promoted`
- Use when: creating or auditing recipient-facing UI, websites, PWA, dashboards, slides, PDF, reports, documents, email, captions, or prototypes. It should activate automatically.
- Result: James's Final Word and visual discipline, including IBM Plex Sans Thai, compact density, restrained color, 6px rectangular radius, minimal pills, and rendered QA where visual output exists.
- Do not use when: handling raw evidence, transcripts, source archives, or private scratch notes that are not recipient-facing outcomes.
- Common composition: any output skill -> `make-it-james` -> `/prove-it`.
- Aliases: `james-ui-standard` is a legacy compatibility call.
- Canonical instructions: [`skills/standards/make-it-james/SKILL.md`](../skills/standards/make-it-james/SKILL.md)

## Design transformation

### `/build-framework`

- Canonical package: `build-framework`
- Category: `core`
- Lifecycle: `promoted`
- Use when: a recurring method gap may require reusing, upgrading, or researching a SolutionsIMPACT house framework.
- Result: one cited executive HTML framework decision report, a branded reusable model when justified, scenarios, counter-case, source trace, and an owner decision.
- Do not use when: applying an existing named framework to one decision, designing one client course, or inventing a framework for a one-off activity.
- Common composition: `/build-framework` may supply an approved framework to `/transformation-journey` or `/learning-experience-design`.
- Aliases: none.
- Canonical instructions: [`skills/core/build-framework/SKILL.md`](../skills/core/build-framework/SKILL.md)

### `/transformation-journey`

- Canonical package: `transformation-journey`
- Category: `core`
- Lifecycle: `promoted`
- Use when: designing, auditing, repairing, or improving organization transformation across several interventions, application, evidence, governance, and business impact.
- Result: one cited executive HTML Journey Pack with macro phases, owners, handoffs, intervention briefs, evidence chain, and next-stage decision.
- Do not use when: the accountable outcome is one bounded course or learning intervention, or when an offer-specific phase model lacks authority.
- Common composition: `/transformation-journey` -> `/learning-experience-design` for every bounded learning intervention; use `/build-framework` only for a real recurring method gap.
- Aliases: `design-the-journey` is a legacy compatibility call.
- Canonical instructions: [`skills/core/transformation-journey/SKILL.md`](../skills/core/transformation-journey/SKILL.md)

### `/learning-experience-design`

- Canonical package: `learning-experience-design`
- Category: `core`
- Lifecycle: `promoted`
- Use when: designing, auditing, repairing, or improving one bounded course, workshop, session, learning day, or intervention.
- Result: one cited executive HTML Design Pack connecting learner movement, the smallest fitting house design authority and lifecycle, experience, facilitation, work evidence, and impact; delivery-ready only when every gate passes.
- Do not use when: the assignment owns sponsor governance and organization transformation across several interventions.
- Common composition: receives a child brief from `/transformation-journey`; routes a recurring framework gap to `/build-framework`.
- Aliases: `design-the-course` is a legacy compatibility call.
- Canonical instructions: [`skills/core/learning-experience-design/SKILL.md`](../skills/core/learning-experience-design/SKILL.md)

## Internal support

### `james-skill-router`

- Canonical package: `james-skill-router`
- Category: `internal`
- Lifecycle: `promoted`
- Availability: Internal support is installed for agent discovery; it is not a recommended human command and its public name remains unapproved.
- Use when: direct matching finds no clear canonical owner and the agent needs a fallback routing reference.
- Result: one real primary workflow per stage and only the additional skills with distinct responsibilities; the router itself never owns or produces the work.
- Do not use when: a human already invoked the exact skill, one canonical workflow clearly matches, or direct work is clearly sufficient. A mixed request alone is not a reason to make the router primary.
- Common composition: internal routing precedes, but does not compete with, the selected workflow.
- Aliases: none.
- Canonical instructions: [`skills/internal/james-skill-router/SKILL.md`](../skills/internal/james-skill-router/SKILL.md)

## Recommended calls and compatibility names

Recommended canonical calls are the 16 promoted non-internal packages above. Recommended lens shortcuts are `/wealth-dynamics`, `/talent-dynamics`, and `/wealth-spectrum`.

Legacy calls remain functional for migration but should not be taught for new work: `/think-with-this`, `/james-ui-standard`, `/project-docs-standard`, `/solutionsimpact-meeting-summary-full`, `/solutionsimpact-onepagesummary`, `/design-the-course`, and `/design-the-journey`.

There are no pilot packages in this release. Candidate Card labels such as `learn-this`, `audit-this`, `systemize-it`, `give-me-choice`, and `make-the-deck` are not existing skills.

## Common flows

1. Unclear system: `/zoom-out` -> `/give-me-solutions` -> owner decision -> `/done-for-me` -> `/prove-it`.
2. New or drifting project: `/project-standard` -> `/done-for-me` -> `/prove-it`.
3. Return after a gap: `/catchup` -> the smallest workflow that owns the verified remaining work.
4. Meeting source: choose `/sum-meet` or `/one-page-pls` -> automatic `make-it-james` -> `/prove-it`.
5. Framework decision: `/baseon` or one lens shortcut -> owner judgment or the workflow that owns the resulting action.
6. Transformation design: `/build-framework` only when needed -> `/transformation-journey` -> `/learning-experience-design` -> automatic `make-it-james` -> `/prove-it`.

### `/proactive-habits`

- Canonical package: `proactive-habits`
- Category: `modes`
- Lifecycle: `promoted`
- Use when: you want the AI to act decisively, never wait for orders, never recap, and simply finish the job.
- Result: sets the communication and behavioral mode to highly autonomous and proactive.
- Do not use when: you want the AI to act passively and ask for permission at every step.
- Aliases: none.
- Canonical instructions: [`skills/modes/proactive-habits/SKILL.md`](../skills/modes/proactive-habits/SKILL.md)

### `/proactive-dev`

- Canonical package: `proactive-dev`
- Category: `standards`
- Lifecycle: `promoted`
- Use when: you are starting a coding session and want strict guarantees on evidence-based diagnosis, blast radius checking, and architecture adherence.
- Result: enforces strict engineering safety protocols before any code mutation.
- Do not use when: you are brainstorming ideas and do not need strict code mutation protocols.
- Aliases: none.
- Canonical instructions: [`skills/standards/proactive-dev/SKILL.md`](../skills/standards/proactive-dev/SKILL.md)
