# JamesSkills Handbook

Choose a skill by the moment you need it. Type the slash command when you want to force a specific workflow. An agent may select the smallest matching workflow automatically when its platform loads the installed skill and supports that routing; this is not verified on every platform.

This handbook is the human navigation layer. `catalog.json` owns category, kind, lifecycle, and aliases. Each linked `SKILL.md` owns the actual behavior, and `docs/SKILL-SCHEMA.md` owns the shape every one of them must satisfy. If a summary here ever conflicts with a canonical skill, the canonical skill wins and this handbook must be repaired.

## Start in 60 seconds

1. Start or repair a project contract with `/project-standard`; return after a gap with `/catchup`.
2. Sharpen a half-formed idea with `/grill-me`; climb to strategy with `/zoom-out`.
3. Settle one doubt with `/research-it`; choose between candidates with `/give-me-solutions`.
4. Plan engineering properly with `/proactive-dev`; finish an agreed task with `/done-for-me`.
5. Check business work with `/are-you-sure` and software with `/dev-are-you-sure`; raise a mediocre result with `/is-that-the-best-you-can-do`.

Mode and standard behavior differs from a normal workflow:

- `/i-have-adhd` and `/proactive-habits` stay active for the current conversation until explicitly disabled.
- `make-it-james` and `make-it-james-ux` apply automatically to recipient-facing outcomes; invoking one directly is useful for a wording or visual audit.
- `skill-router` is installed agent support, not a recommended human command.


## Start or return to work

### `/project-standard`

- Canonical package: `project-standard`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Create or repair one vendor-neutral project contract so any agent or person can work without prior chat, stamped with the standard version it follows. Use when project truth is missing or drifting; not for routine edits that change nothing durable.
- Result: The owner documents actually changed, the requirement identifiers with their acceptance and proof, the regenerated SRS with its contract version, the visible drift between intended and actual, and the `check --ready` result.
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
- Use when: Reconstruct one project's verified current state after a gap and deliver it as the standard catchup page. Use for where-are-we-now after a handoff or stale status; not for progress inside active work and not for repairing anything.
- Result: One rendered catchup page naming the target, the current situation, what was recently done, the live checklist, what is open with owners, visible conflicts and unknowns, the state of the last task, and the single next action.
- Do not use when: Ordinary progress inside an active task is being reported; let the primary workflow report it -> `done-for-me`
  - The dispute is one isolated completion claim needing verification at its boundary -> `dev-are-you-sure`
  - The project has no contract and truth was never written down -> `project-standard`
- Canonical instructions: [`plugins/james-software/skills/catchup/SKILL.md`](../plugins/james-software/skills/catchup/SKILL.md)

### `/zoom-out`

- Canonical package: `zoom-out`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Step back at least three levels from the detail to the strategy, then agree the direction before any action resumes. Use when work has gone too deep too early; strategy only, never for interface or visual questions.
- Result: The outcome in human terms, the responsibility that is actually failing, what already works and must stay untouched, the strategy with its exclusions, and the agreed direction with the next action it unlocks.
- Do not use when: The question is about layout, interaction, or visual design -> `make-it-james-ux`
  - The direction is settled and options must now be compared -> `give-me-solutions`
  - The direction is settled and the job is to build it -> `done-for-me`
- Canonical instructions: [`plugins/james-productivity/skills/zoom-out/SKILL.md`](../plugins/james-productivity/skills/zoom-out/SKILL.md)

### `/grill-me`

- Canonical package: `grill-me`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Interrogate the user through a branching interview until their own goal and requirement are sharp, then recap and confirm. Use to sharpen a plan before building; not to coach the person and not to research the answer.
- Result: The resolved decision map with every decision, chosen answer, reason, downstream consequence, and unresolved risk, plus the user's explicit confirmation that it is complete, correct, on target, and satisfying.
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
- Result: The claim as stated, the evidence ledger with dates and stakes, the four layers kept separate, the verdict with its condition, and the named remaining unknown. The reader decides what to do about it.
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
- Use when: Apply or compare registered frameworks, books, and models against a real case while keeping source claims separate from evidence and inference. Use to interpret a situation through named knowledge; not to research new sources and not to decide.
- Result: The question, the lenses selected and why, the four layers kept separate, any disagreement between lenses shown rather than resolved, and one reversible experiment with its success and revision rules.
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
- Use when: Carry an already-agreed task all the way to a finished, verified outcome without stopping to ask. Use when the plan is settled and only execution remains; not when the plan still needs work and not for inspecting finished work.
- Result: The working outcome, the evidence that it was exercised, the decisions taken under the agent's own authority, and the genuinely remaining gates with their owners.
- Do not use when: The plan itself is not good enough yet and needs decomposition before building -> `proactive-dev`
  - The work is finished and its diligence is what is in doubt -> `are-you-sure`
  - Delivered code needs a layered sweep and boundary check -> `dev-are-you-sure`
- Canonical instructions: [`plugins/james-core/skills/done-for-me/SKILL.md`](../plugins/james-core/skills/done-for-me/SKILL.md)

### `/proactive-dev`

- Canonical package: `proactive-dev`
- Category: `james-software`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Work as one person holding the analyst, product, architect, build, and quality roles, planning rigorously before writing code and splitting the work across sub-agents. Use when the plan is not good enough yet; not for executing an accepted plan.
- Result: The restated requirement, the scope with its explicit exclusions, the architecture decision and its rollback, the increments built, the quality result against the done-criteria, and the current state of anything still running or blocked.
- Do not use when: A plan is already accepted and the job is to execute it to a usable outcome -> `done-for-me`
  - Delivered code needs a five-layer sweep and repair -> `dev-are-you-sure`
  - The decision posture, not the engineering method, is what needs to change -> `proactive-habits`
- Canonical instructions: [`plugins/james-software/skills/proactive-dev/SKILL.md`](../plugins/james-software/skills/proactive-dev/SKILL.md)


## Check the work

### `/are-you-sure`

- Canonical package: `are-you-sure`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Re-inspect a business or productivity deliverable across five layers and repair what it finds inside a declared surface. Use when work looks finished but the diligence behind it is in doubt; not for code, and not for making good work better.
- Result: The declared inspection surface, each of the five layers marked repaired, escalated, or clean, the repaired artifact itself, and any escalation with the decision it needs and who holds it.
- Do not use when: The artifact is code, schema, data, or a deployment -> `dev-are-you-sure`
  - The doubt is about an outside claim rather than work produced here -> `research-it`
  - The work is correct and clean but unambitious, and needs a higher ceiling -> `is-that-the-best-you-can-do`
- Canonical instructions: [`plugins/james-core/skills/are-you-sure/SKILL.md`](../plugins/james-core/skills/are-you-sure/SKILL.md)

### `/dev-are-you-sure`

- Canonical package: `dev-are-you-sure`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Re-inspect delivered software across five layers plus the deployment boundary and repair what it finds inside a declared surface. Use when code looks done but the diligence is in doubt; not for business artifacts and not for external claims.
- Result: The declared surface, five layers and four boundary links each marked, the repaired code, and every remaining gap with its owner and the exact evidence still missing.
- Do not use when: The artifact is a plan, document, model, or business decision -> `are-you-sure`
  - The doubt is whether an outside approach or library claim is sound -> `research-it`
  - The code is correct and clean but the solution is mediocre -> `is-that-the-best-you-can-do`
- Canonical instructions: [`plugins/james-software/skills/dev-are-you-sure/SKILL.md`](../plugins/james-software/skills/dev-are-you-sure/SKILL.md)

### `/is-that-the-best-you-can-do`

- Canonical package: `is-that-the-best-you-can-do`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Measure how far a correct but unambitious result sits below its ceiling, then spend parallel effort closing that gap. Use when the work is not wrong but not good enough; not for defects and not for unfinished work.
- Result: The named ceiling, the measured gap, the raised work itself, what was kept from the original and why, and anything still below ceiling with its cost.
- Do not use when: The work contains actual defects, shortcuts, or residue -> `are-you-sure`
  - The defects are in delivered code -> `dev-are-you-sure`
  - The work is unfinished rather than unambitious -> `done-for-me`
- Canonical instructions: [`plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md`](../plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md)

### `/never-again`

- Canonical package: `never-again`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Turn one rejected output into a written lesson that every future agent is forced to read before working in this repository. Use when a mistake should never recur; not for fixing the one bad output and not for routine quality sweeps.
- Result: The lesson entry, the contract file that now forces it to be read, the three regressions, the list of outputs repaired, and the exact scope the rule covers.
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
- Use when: Build one auditable meeting record holding every agenda in a single file, with evidence kept separate from interpretation. Use for minutes and detailed meeting records; not when each topic must become its own page.
- Result: One rendered A4 portrait file covering every agenda, the source coverage account, the evidence ledger with locators, everything left explicitly unknown or disputed, and the inspection result for every print page.
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
- Use when: Turn each independent topic into its own self-contained single-page brief. Use when material must stay on one page per topic; not for meeting records that must hold every agenda in one file.
- Result: One rendered file per topic with its name, the coverage account showing every material item placed, the inspection result for each page, and any topic returned as unsuitable for one page with the reason.
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
- Result: The finished artifact in the chosen format, the reason that format was chosen, the verification actually performed, and any content gate that remains genuinely open.
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
- Result: Every reply for the rest of the conversation, shaped so the first line says what to do and the last line says where things stand.
- Do not use when: What needs to change is decision authority rather than presentation -> `proactive-habits`
  - The user is blocked by hesitation rather than by information shape -> `coach-me`
  - The user wants to be questioned until their own requirement is sharp -> `grill-me`
- Canonical instructions: [`plugins/james-core/skills/i-have-adhd/SKILL.md`](../plugins/james-core/skills/i-have-adhd/SKILL.md)

### `/proactive-habits`

- Canonical package: `proactive-habits`
- Category: `james-core`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Work as an effective professional who decides what is theirs to decide and batches the rest into one question at the end. Use to stop subordinate behavior; not for finishing one named task and not for how replies are formatted.
- Result: Work already done under the agent's own authority, stated plainly, plus one batched set of decisions that genuinely need the user, each with a recommendation and its reason.
- Do not use when: One named task must be carried to a finished, verified outcome -> `done-for-me`
  - The need is about reply length, ordering, and interruption shape rather than decision authority -> `i-have-adhd`
  - The work is software and needs role decomposition and a plan before code -> `proactive-dev`
- Canonical instructions: [`plugins/james-core/skills/proactive-habits/SKILL.md`](../plugins/james-core/skills/proactive-habits/SKILL.md)

### `/coach-me`

- Canonical package: `coach-me`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Move a person toward their own goal using questions only, always positively, working beneath the behavior to what is driving it. Use when someone is stuck in themselves; never to give advice and never to do the work for them.
- Result: Their goal in their own words, what was found beneath the behavior, and the next action they named themselves with its timing. No plan they did not author, no template, and no work done on their behalf.
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
- Result: The reworded output plus the specific failures repaired, or the exact wording gate still open when a fact cannot be resolved without inventing it.
- Do not use when: The question is which format the deliverable should take -> `final-it`
  - The output is a screen, layout, or visual artifact and the rules needed are visual -> `make-it-james-ux`
  - The text is wrong rather than badly worded -> `are-you-sure`
- Canonical instructions: [`plugins/james-core/skills/make-it-james/SKILL.md`](../plugins/james-core/skills/make-it-james/SKILL.md)

### `/make-it-james-ux`

- Canonical package: `make-it-james-ux`
- Category: `james-software`
- Kind: `shared-standard`
- Lifecycle: `promoted`
- Use when: Enforce visual and interaction law on anything rendered, following the project's existing design system first and this house style only as fallback. Applies automatically to visual work; it does not choose the format or write the content.
- Result: The rendered artifact, which system was followed and why, the strict lint result, the rendered inspection covering typography, density, radius, and interface copy, and any visual gate that remains open.
- Do not use when: The rules needed are about wording rather than presentation -> `make-it-james`
  - The question is which format the deliverable should take -> `final-it`
  - The interface is defective rather than inconsistent -> `dev-are-you-sure`
- Canonical instructions: [`plugins/james-software/skills/make-it-james-ux/SKILL.md`](../plugins/james-software/skills/make-it-james-ux/SKILL.md)


## Agent support

### `skill-router`

- Internal support: installed for agents, never a human slash command.
- Canonical package: `skill-router`
- Category: `james-core`
- Kind: `internal-routing`
- Lifecycle: `promoted`
- Use when: Internal fallback that assigns one primary owner when no skill obviously matches. Never select it as the primary workflow, never let it produce a deliverable, and never use it when a direct owner is already clear.
- Result: The named primary owner, any supporting skill with the distinct responsibility it holds, and nothing else. This router never returns a deliverable.
- Do not use when: One canonical owner already clearly matches -> load that owner, for example `done-for-me`
  - The request spans several responsibilities but one outcome is accountable -> give that owner the job, for example `project-standard`
  - The user asked to be interrogated rather than routed -> `grill-me`
- Canonical instructions: [`plugins/james-core/skills/skill-router/SKILL.md`](../plugins/james-core/skills/skill-router/SKILL.md)
