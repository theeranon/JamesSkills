# JamesSkills Handbook

Choose a skill by the moment you need it. Type the slash command when you want to force a specific workflow. An agent may select the smallest matching workflow automatically when its platform loads the installed skill and supports that routing; this is not verified on every platform.

This handbook is the human navigation layer. `catalog.json` owns category, kind, lifecycle, and aliases. Each linked `SKILL.md` owns the actual behavior, and `docs/SKILL-SCHEMA.md` owns the shape every one of them must satisfy. If a summary here ever conflicts with a canonical skill, the canonical skill wins and this handbook must be repaired.

## Start in 60 seconds

1. Start or repair a project contract with `/project-standard`; return after a gap with `/catchup`.
2. Sharpen a half-formed idea with `/grill-me`; climb to strategy with `/zoom-out`.
3. Settle one doubt with `/research-it`; choose between candidates with `/give-me-solutions`.
4. Use `/proactive-dev` throughout engineering; `/done-for-me` finishes one task within that mode.
5. Check business work with `/are-you-sure` and software with `/dev-are-you-sure`; raise a mediocre result with `/is-that-the-best-you-can-do`.

Mode and standard behavior differs from a normal workflow:

- `/i-have-adhd`, `/proactive-dev` and `/proactive-habits` stay active for the current conversation until explicitly disabled.
- `make-it-james` and `make-it-james-ux` apply automatically to recipient-facing outcomes; invoking one directly is useful for a wording or visual audit.
- `hand-it-off` is installed agent support, not a recommended human command.


## Start or return to work

### `/project-standard`

- Canonical package: `project-standard`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Create or repair one vendor-neutral project contract so any agent or person can work without prior chat, stamped with the standard version it follows. Use when project truth is missing or drifting; not for routine edits that change nothing durable.
- Result: The owner-document changes, requirement identifiers with acceptance/proof, visible intended-versus-actual drift, and checks actually performed. Include regenerated SRS/version only when applicable; for a requested draft, clearly identify proposed text and unverified facts instead of reporting edits or readiness.
- Do not use when: The contract exists and current state after a gap is what is unknown -> `catchup`
  - The contract exists and the work is to build against it -> `done-for-me`
  - Engineering work needs role decomposition rather than a contract -> `proactive-dev`
- Aliases: `project-docs-standard` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-software/skills/project-standard/SKILL.md`](../plugins/james-software/skills/project-standard/SKILL.md)

### `/catchup`

- Canonical package: `catchup`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Reconstruct one project's verified current state after a gap and deliver it as the standard catchup page. Use for where-are-we-now after a handoff or stale status; not for ordinary progress inside active work. A request to continue work uses this reconstruction as its starting point.
- Result: The requested chat report or rendered page: target and comparison point, current evidence, material conflict or blocker, and one safe next action. Include history, checklist and last-task state only where established and useful; do not repeat current facts under multiple headings.
- Do not use when: Ordinary progress inside an active task is being reported; let the primary workflow report it -> `done-for-me`
  - The dispute is one isolated completion claim needing verification at its boundary -> `dev-are-you-sure`
  - The project has no contract and truth was never written down -> `project-standard`
- Canonical instructions: [`plugins/james-software/skills/catchup/SKILL.md`](../plugins/james-software/skills/catchup/SKILL.md)

### `/zoom-out`

- Canonical package: `zoom-out`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Step out from implementation detail through the project goal to the strategy that should achieve it. Use when work is optimizing the wrong layer or losing its purpose; not for an isolated implementation or visual fix.
- Result: The strategic reframe: project outcome, approach, how the current work contributes or distracts, and the next aligned move. Name only a genuinely new decision requiring the user. When execution was requested and authorized, carry that work forward rather than stopping at the reframe.
- Do not use when: Only layout, interaction, or visual design needs repair and the project strategy is not in question -> `make-it-james-ux`
  - The direction is settled and options must now be compared -> `give-me-solutions`
  - The direction is settled and the job is to build it -> `done-for-me`
- Canonical instructions: [`plugins/james-productivity/skills/zoom-out/SKILL.md`](../plugins/james-productivity/skills/zoom-out/SKILL.md)

### `/grill-me`

- Canonical package: `grill-me`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Interrogate the user through a branching interview until their own goal and requirement are sharp, then proceed when the necessary decisions are clear. Use to sharpen a plan before building; not to coach the person and not to research the answer.
- Result: The useful decisions and remaining material questions, or the requested work when the user has instructed you to proceed. Keep routine interview bookkeeping internal.
- Do not use when: The block is the person's own hesitation rather than an unclear requirement -> `coach-me`
  - The requirement is clear and options must now be compared -> `give-me-solutions`
  - The requirement is clear and the answer lies in outside evidence -> `research-it`
- Canonical instructions: [`plugins/james-productivity/skills/grill-me/SKILL.md`](../plugins/james-productivity/skills/grill-me/SKILL.md)


## Decide

### `/research-it`

- Canonical package: `research-it`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Settle a doubt about one claim, approach, or requirement with outside evidence from official sources and real users. Use when confidence is missing, not when choosing between options or checking your own work.
- Result: The claim and verdict, the decisive source evidence with locators when available, and the material limits. Keep fact, source assertion and inference clear without requiring separate sections for empty categories. For a research-only request, stop at the verdict. For an authorized larger task, use the finding to continue that task.
- Do not use when: Several candidates must be compared and one recommended -> `give-me-solutions`
  - The doubt is about work produced in this conversation rather than an outside claim -> `are-you-sure`
  - The doubt is about whether shipped code, data, or a deployment behaves correctly -> `dev-are-you-sure`
- Aliases: `prove-it` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-core/skills/research-it/SKILL.md`](../plugins/james-core/skills/research-it/SKILL.md)

### `/give-me-solutions`

- Canonical package: `give-me-solutions`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Compare real options against this project's actual context and name the best one with its reasoning. Use when a choice must be made between candidates; not for settling a single claim and not for making the decision happen.
- Result: The bounded role and its hard requirements, what was eliminated and why, the survivors compared on identical criteria against this project's real context, the named best option with its reasoning, and the condition that would flip the decision.
- Do not use when: One claim or approach needs to be settled rather than several compared -> `research-it`
  - Which responsibility is actually failing is still unclear -> `zoom-out`
  - The choice is already made and the job is to build it -> `done-for-me`
- Canonical instructions: [`plugins/james-productivity/skills/give-me-solutions/SKILL.md`](../plugins/james-productivity/skills/give-me-solutions/SKILL.md)

### `/baseon`

- Canonical package: `baseon`
- Category: `james-productivity`
- Kind: `knowledge-lens`
- Lifecycle: `promoted`
- Use when: Apply or compare registered frameworks, books, and models against a real case while keeping source claims separate from evidence and inference. Use to explain or apply named knowledge, compare interpretations, or register a supplied source; not to replace an evidence-based decision.
- Result: The requested explanation or source record, or a case interpretation with source claims, facts and inference distinguishable. Include disagreements and experiments only where they serve the request.
- Do not use when: The source is not registered yet and the need is outside evidence about a claim -> `research-it`
  - Options must be compared and one recommended -> `give-me-solutions`
  - The problem layer itself is unclear -> `zoom-out`
- Aliases: `think-with-this`, `wealth-dynamics`, `talent-dynamics`, `wealth-spectrum` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-productivity/skills/baseon/SKILL.md`](../plugins/james-productivity/skills/baseon/SKILL.md)


## Build and finish

### `/done-for-me`

- Canonical package: `done-for-me`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Carry an already-agreed task all the way to a finished, verified outcome without stopping to ask. Use for a one-time instruction to finish an established outcome. Decide routine planning and implementation details yourself; active conversation modes remain in force.
- Result: The working outcome and concise verification relevant to the request. Include material decisions or genuine remaining dependencies only when useful; keep an artifact-only response artifact-only. Completing this task ends this workflow, not an active conversation mode.
- Do not use when: The user asks to design a strategy rather than execute an established outcome -> `proactive-dev` can guide engineering planning. Missing implementation details alone do not block execution.
  - The work is finished and its diligence is what is in doubt -> `are-you-sure`
  - Delivered code needs a layered sweep and boundary check -> `dev-are-you-sure`
- Canonical instructions: [`plugins/james-core/skills/done-for-me/SKILL.md`](../plugins/james-core/skills/done-for-me/SKILL.md)

### `/proactive-dev`

- Canonical package: `proactive-dev`
- Category: `james-software`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Keep engineering work proactive from understanding the goal through implementation, testing and delivery. A conversation mode that scales planning and delegation to the task and stays active alongside individual workflows.
- Result: The usable plan or implementation, with the decisions, scope, rollback and acceptance evidence needed to assess it. State actual progress and remaining dependencies once; do not repeat the same plan as analyst, architect and handback summaries.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-software/skills/proactive-dev/SKILL.md`](../plugins/james-software/skills/proactive-dev/SKILL.md)


## Check the work

### `/are-you-sure`

- Canonical package: `are-you-sure`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Re-inspect a business or productivity deliverable with checks matched to its risks and repair evidenced defects inside the requested surface. Use when work looks finished but the diligence behind it is in doubt; not for code, and not for making good work better.
- Result: The repaired artifact, or the requested clean-result confirmation. A request to return the corrected artifact gets that artifact alone; keep surface, layer labels and repair bookkeeping internal unless the user asks for the inspection report. When an inspection report is requested, include the surface and actual findings, with clean, repaired, escalated, not-applicable or unverified status as warranted. Name only the decisions genuinely needed to finish.
- Do not use when: The artifact is code, schema, data, or a deployment -> `dev-are-you-sure`
  - The doubt is about an outside claim rather than work produced here -> `research-it`
  - The work is correct and clean but unambitious, and needs a higher ceiling -> `is-that-the-best-you-can-do`
- Canonical instructions: [`plugins/james-core/skills/are-you-sure/SKILL.md`](../plugins/james-core/skills/are-you-sure/SKILL.md)

### `/dev-are-you-sure`

- Canonical package: `dev-are-you-sure`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Re-inspect delivered software with checks matched to its risks and repair findings inside a declared surface. Use when code looks done but the diligence is in doubt; not for business artifacts and not for external claims.
- Result: The repaired outcome, checks actually performed, and material unresolved findings with the evidence still needed. Include the complete layer/boundary inventory when a full audit was requested; keep inspection notes internal for a code-only response.
- Do not use when: The artifact is a plan, document, model, or business decision -> `are-you-sure`
  - The doubt is whether an outside approach or library claim is sound -> `research-it`
  - The code is correct and clean but the solution is mediocre -> `is-that-the-best-you-can-do`
- Canonical instructions: [`plugins/james-software/skills/dev-are-you-sure/SKILL.md`](../plugins/james-software/skills/dev-are-you-sure/SKILL.md)

### `/is-that-the-best-you-can-do`

- Canonical package: `is-that-the-best-you-can-do`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Measure how far a correct but unambitious result sits below its ceiling, then close the material gap with proportionate effort. Use when the work is not wrong but not good enough; not for defects and not for unfinished work.
- Result: The improved work in the requested format. State material remaining limits when needed; ceiling, gap analysis and change commentary stay internal for artifact-only requests.
- Do not use when: The work contains actual defects, shortcuts, or residue -> `are-you-sure`
  - The defects are in delivered code -> `dev-are-you-sure`
  - The work is unfinished rather than unambitious -> `done-for-me`
- Canonical instructions: [`plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md`](../plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md)

### `/never-again`

- Canonical package: `never-again`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Repair a recurring failure mechanism with a narrow, discoverable lesson or an update to an existing rule. Use when a mistake should never recur; not for fixing the one bad output and not for routine quality sweeps.
- Result: For executed work: the verified lesson entry and contract pointer, three regressions, repaired outputs and scope. For draft-only work: the proposed entry and cases, with an explicit statement that no file was changed. Never describe proposed persistence as completed.
- Do not use when: The single bad output needs repairing and nothing durable is at stake -> `are-you-sure`
  - The defect is in delivered code and the sweep is what is wanted -> `dev-are-you-sure`
  - The project has no contract yet and truth is scattered rather than wrong -> `project-standard`
- Canonical instructions: [`plugins/james-core/skills/never-again/SKILL.md`](../plugins/james-core/skills/never-again/SKILL.md)


## Deliver an artifact

### `/sum-meet`

- Canonical package: `sum-meet`
- Category: `james-productivity`
- Kind: `output`
- Lifecycle: `promoted`
- Use when: Build one auditable meeting record holding every agenda in a single file, with evidence kept separate from interpretation. Use for minutes or meeting summaries at the requested depth; full records retain every agenda, while a requested short summary stays short.
- Result: The requested short summary, or the full rendered meeting record with source coverage and traceability. Keep verification bookkeeping internal unless requested or material; show unknown or disputed facts where relevant.
- Do not use when: Each agenda must become its own separate page -> `one-page-pls`
  - The artifact is not a meeting record and the format is open -> `final-it`
  - Project state must be reconstructed from the repository rather than a transcript -> `catchup`
- Aliases: `solutionsimpact-meeting-summary-full` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-productivity/skills/sum-meet/SKILL.md`](../plugins/james-productivity/skills/sum-meet/SKILL.md)

### `/one-page-pls`

- Canonical package: `one-page-pls`
- Category: `james-productivity`
- Kind: `output`
- Lifecycle: `promoted`
- Use when: Turn material into a self-contained single-page brief, with one page per topic by default. Use when material must stay on one page per topic; not for meeting records that must hold every agenda in one file.
- Result: The requested page or chat brief. Keep coverage and inspection bookkeeping internal unless requested; disclose any material omission, linked appendix or delivery limitation the reader needs.
- Do not use when: Every agenda must live in one record together -> `sum-meet`
  - The artifact is not page-bound and the format is still open -> `final-it`
  - Current project state must be reconstructed rather than summarised -> `catchup`
- Aliases: `solutionsimpact-onepagesummary` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-productivity/skills/one-page-pls/SKILL.md`](../plugins/james-productivity/skills/one-page-pls/SKILL.md)

### `/final-it`

- Canonical package: `final-it`
- Category: `james-productivity`
- Kind: `output`
- Lifecycle: `promoted`
- Use when: Choose the format that actually serves the recipient and finish the work in it. Use when no narrower output skill owns the artifact; not for meeting records, not for one-page briefs, and not for supplying missing content.
- Result: The finished deliverable. If the user requests the artifact only, return only that artifact; keep format rationale and verification bookkeeping internal. Otherwise include only a material delivery limit or decision still needed, without repeating the finished content.
- Do not use when: The source is a meeting and the record must hold every agenda -> `sum-meet`
  - Each topic must become its own single page -> `one-page-pls`
  - A project contract, not a deliverable, is what is needed -> `project-standard`
- Canonical instructions: [`plugins/james-productivity/skills/final-it/SKILL.md`](../plugins/james-productivity/skills/final-it/SKILL.md)


## Modes and standards

### `/i-have-adhd`

- Canonical package: `i-have-adhd`
- Category: `james-core`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Shape every reply so it can be acted on immediately without holding state in memory. Use to change how answers are presented; not to change what the agent is allowed to decide and not to shorten by removing needed information.
- Result: A reply that is easy to understand and act on, with progress only when relevant. Preserve the requested artifact format; no mandatory action or status footer.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-core/skills/i-have-adhd/SKILL.md`](../plugins/james-core/skills/i-have-adhd/SKILL.md)

### `/proactive-habits`

- Canonical package: `proactive-habits`
- Category: `james-core`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Work as an effective professional who decides what is theirs to decide and asks only for unresolved decisions required by the user outcome. Activate once to work proactively throughout this conversation, including planning, execution, correction and verification; composes with one-task workflows and presentation modes.
- Result: The completed requested deliverable, or an observed blocker after independent work is finished. Repeated invocation during unfinished work resumes execution immediately; an explicit audit-only request still returns findings.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-core/skills/proactive-habits/SKILL.md`](../plugins/james-core/skills/proactive-habits/SKILL.md)

### `/coach-me`

- Canonical package: `coach-me`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Move a person toward their own goal through questions and reflection at the depth they want. Use when someone wants coaching; respect an explicit switch to advice, a factual answer, or task execution.
- Result: A reflection or question that serves the current coaching conversation, and their chosen next step when reached. If they changed the request, deliver the requested answer or work instead. Never attach an inferred psychological label.
- Do not use when: The person wants the task done rather than to be moved -> `done-for-me`
  - What is unclear is the requirement rather than the person -> `grill-me`
  - The person wants options researched and compared -> `give-me-solutions`
- Canonical instructions: [`plugins/james-productivity/skills/coach-me/SKILL.md`](../plugins/james-productivity/skills/coach-me/SKILL.md)

### `/make-it-james`

- Canonical package: `make-it-james`
- Category: `james-core`
- Kind: `shared-standard`
- Lifecycle: `promoted`
- Use when: Enforce the wording law on anything a real person will read, so it reads as native writing rather than as translated or machine-generated text. Applies automatically to recipient-facing work; it does not choose the format or supply missing content.
- Result: The reworded output. Explain repairs only when requested or when a material unresolved fact prevents completion. Do not append editing commentary to an artifact-only request.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-core/skills/make-it-james/SKILL.md`](../plugins/james-core/skills/make-it-james/SKILL.md)

### `/make-it-james-ux`

- Canonical package: `make-it-james-ux`
- Category: `james-software`
- Kind: `shared-standard`
- Lifecycle: `promoted`
- Use when: Enforce visual and interaction law on anything rendered, following the project's existing design system first and this house style only as fallback. Applies automatically to visual work; it does not choose the format or write the content.
- Result: The requested code or rendered artifact. For a rendered deliverable, report the system followed, actual lint/render evidence and material open gates. For code-only output, return exclusively code; keep verification notes internal.
- Do not use when: The rules needed are about wording rather than presentation -> `make-it-james`
  - The question is which format the deliverable should take -> `final-it`
  - The interface is defective rather than inconsistent -> `dev-are-you-sure`
- Canonical instructions: [`plugins/james-software/skills/make-it-james-ux/SKILL.md`](../plugins/james-software/skills/make-it-james-ux/SKILL.md)


## Agent support

### `hand-it-off`

- Internal support: installed for agents, never a human slash command.
- Canonical package: `hand-it-off`
- Category: `james-core`
- Kind: `internal-routing`
- Lifecycle: `promoted`
- Use when: Internal fallback that assigns one primary owner when no skill obviously matches. Never select it as the primary workflow, never let it produce a deliverable, and never use it when a direct owner is already clear.
- Result: No separate user-facing routing report. The selected workflow delivers the requested outcome; name skills only if the user asked about routing.
- Do not use when: One canonical owner already clearly matches -> load that owner, for example `done-for-me`
  - The request spans several responsibilities but one outcome is accountable -> give that owner the job, for example `project-standard`
  - The user asked to be interrogated rather than routed -> `grill-me`
- Aliases: `skill-router` (legacy compatibility call).
  - The user asked to be interrogated rather than routed -> `grill-me`
- Canonical instructions: [`plugins/james-core/skills/hand-it-off/SKILL.md`](../plugins/james-core/skills/hand-it-off/SKILL.md)
