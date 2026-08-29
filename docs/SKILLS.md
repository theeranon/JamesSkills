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
- Pilot packages stay review-only and are not installed globally.
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

## Lab and internal support

These packages remain in the repository because their contracts need review or because agents use them internally. They are not normal recommended slash commands.

### `design-the-course`

- Canonical package: `design-the-course`
- Category: `core`
- Lifecycle: `pilot`
- Availability: Not installed; working name and LED/TPS boundary require owner approval.
- Use when: reviewing the candidate workflow for one bounded course, workshop, session, or learning day.
- Result: a reviewable course-design contract, not an approved James-wide method.
- Do not use when: presenting the working name or ontology as settled, or designing a macro organizational journey.
- Common composition: none until promotion.
- Aliases: `learning-experience-design` is a pilot alias and is not installed.
- Canonical instructions: [`skills/core/design-the-course/SKILL.md`](../skills/core/design-the-course/SKILL.md)

### `design-the-journey`

- Canonical package: `design-the-journey`
- Category: `core`
- Lifecycle: `pilot`
- Availability: Not installed; working name and universal model require owner approval.
- Use when: reviewing the candidate workflow for an organization-level transformation across several interventions.
- Result: a reviewable journey contract; its five-phase reference applies only to the sourced SolutionsIMPACT AI Transformation Journey offer.
- Do not use when: imposing that offer-specific five-phase spine on a generic transformation or claiming the ontology is approved.
- Common composition: none until promotion.
- Aliases: `transformation-journey` is a pilot alias and is not installed.
- Canonical instructions: [`skills/core/design-the-journey/SKILL.md`](../skills/core/design-the-journey/SKILL.md)

### `james-skill-router`

- Canonical package: `james-skill-router`
- Category: `internal`
- Lifecycle: `promoted`
- Availability: Internal support is installed for agent discovery; it is not a recommended human command and its public name remains unapproved.
- Use when: an agent must select the smallest workflow, mode, standard, output, adapter, or direct-work path for a mixed request.
- Result: one primary owner per stage and only the additional skills with distinct responsibilities.
- Do not use when: a human already invoked the exact skill or direct work is clearly sufficient.
- Common composition: internal routing precedes, but does not compete with, the selected workflow.
- Aliases: none.
- Canonical instructions: [`skills/internal/james-skill-router/SKILL.md`](../skills/internal/james-skill-router/SKILL.md)

## Recommended calls and compatibility names

Recommended canonical calls are the 13 promoted non-internal packages above. Recommended lens shortcuts are `/wealth-dynamics`, `/talent-dynamics`, and `/wealth-spectrum`.

Legacy calls remain functional for migration but should not be taught for new work: `/think-with-this`, `/james-ui-standard`, `/project-docs-standard`, `/solutionsimpact-meeting-summary-full`, and `/solutionsimpact-onepagesummary`.

Pilot names and aliases are not installed: `design-the-course`, `learning-experience-design`, `design-the-journey`, and `transformation-journey`. Candidate Card labels such as `learn-this`, `audit-this`, `systemize-it`, `give-me-choice`, and `make-the-deck` are not existing skills.

## Common flows

1. Unclear system: `/zoom-out` -> `/give-me-solutions` -> owner decision -> `/done-for-me` -> `/prove-it`.
2. New or drifting project: `/project-standard` -> `/done-for-me` -> `/prove-it`.
3. Return after a gap: `/catchup` -> the smallest workflow that owns the verified remaining work.
4. Meeting source: choose `/sum-meet` or `/one-page-pls` -> automatic `make-it-james` -> `/prove-it`.
5. Framework decision: `/baseon` or one lens shortcut -> owner judgment or the workflow that owns the resulting action.
