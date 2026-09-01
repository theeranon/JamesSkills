---
name: project-standard
description: Create or repair one vendor-neutral project contract. Use when starting or restructuring a project, turning an agreed goal or architecture into executable requirements, onboarding or handing work to another AI, reconciling conflicting project documents, or repeated agents lose scope, status, decisions, or acceptance criteria; skip routine work when the existing contract remains current.
---

# Project Standard

Keep every agent on the same project truth without turning documentation into ceremony.

## Contract ownership

`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `README.md` stay at the repository root — agent tooling and GitHub look for them there. Every other contract file lives under `ai-context/` so project truth is not scattered across the repository root.

- `ai-context/PROJECT.md` owns intended outcome, scope, authority, requirement IDs, boundaries, and acceptance proof.
- `ai-context/STATUS.md` owns current verified state, active work, next action, blockers, and decisions needed.
- `AGENTS.md` owns the vendor-neutral working contract and points to the project sources it requires.
- `ai-context/DECISIONS.md` owns accepted and superseded decisions with rationale and source.
- `README.md` owns human onboarding and usage when the project needs it.
- `ai-context/ARCHITECTURE.md` and `ai-context/DATA_MODEL.md` exist only when system or persistent-data complexity earns them. When present, `DATA_MODEL.md` owns canonical stores, identity, relations, lifecycle, migration, and rollback.
- `ai-context/SRS.html` is a generated read-only view of `PROJECT.md` and `DATA_MODEL.md` for a human to skim — regenerate it after either source changes; never hand-edit it.
- `STATUS.md`'s `Spec lock` line owns whether the spec may still move. `Open` (the default) means `PROJECT.md`/`DATA_MODEL.md` are expected to keep changing as the project learns; `Locked (date, hash)` means an owner has frozen them as the requirements bible and any further change to either file is a defect until a `Need decision` records the unlock.
- Git, tests, runtime, and provider receipts remain execution evidence. Documentation never turns a claim into proof.

Read [references/contract.md](references/contract.md) when choosing files, resolving conflicts, or adapting an existing repository.

## Workflow

1. Inspect the repository, existing instructions, current git state, executable configuration, entrypoints, tests, and relevant runtime evidence. Classify each source as intended truth, current state, history, adapter, or evidence.
2. Select the smallest mode that fits:
   - **Establish**: create the baseline contract for a new or undocumented project.
   - **Specify**: turn an agreed outcome or architecture into named requirements and acceptance proof.
   - **Repair**: resolve duplicated, stale, or contradictory project documents without deleting useful history.
   - **Handoff**: refresh current state and source pointers so a new agent can continue without chat history.

   For a project with more than a handful of functional requirements, do not keep every requirement in one flat table. Create `ai-context/modules/<module-name>.md` per module, each owning that module's functional requirements using the same `REQ-ID` / Boundary / Acceptance / Proof structure as `PROJECT.md`, and have `PROJECT.md` point to the module files rather than duplicate them. Implement and verify one functional requirement at a time; after each one, re-run the full existing test suite (not only the new test) before moving to the next requirement, so a later change cannot silently break an earlier one without being caught. This is opt-in — small projects stay on the flat table.
3. Preserve accepted project facts. Put each fact in one owner document and replace duplicates with pointers. Mark unsupported claims `Not confirmed`; record unresolved conflicts under `Need decision`.
4. Write requirements as stable IDs. Every requirement must name the observable outcome, boundary, acceptance method, and proof source. A requirement is not complete because an agent says it implemented it.
4a. When a project already has running or shipped code, do not trust that the written requirements describe what actually ships. Have an AI read the implemented code (not the documentation) and generate a functional-requirement description of what it actually does, module by module. Compare that description against `PROJECT.md`'s requirement table and the permission matrix (see `DATA_MODEL.md`'s Permissions section). Flag every mismatch — anything the code does that no requirement names, and anything a requirement names that the code does not do — as a `Reality conflict` in `STATUS.md`, and treat unexpected permission grants (e.g. an external party able to approve its own request) as a boundary defect, not a cosmetic one, even if no requirement was ever written for it.

    Run this reverse-audit using a different AI model or vendor than the one that wrote the code, at least for the final pass. An AI auditing its own prior output under-reports anomalies; a second vendor does not share the first vendor's blind spots. Record which model produced the code and which model performed the audit in `ai-context/DECISIONS.md`.
5. Keep provider files thin. `CLAUDE.md`, `GEMINI.md`, or another provider adapter may add provider mechanics, but shared project truth stays in `AGENTS.md` and the contract files.
6. For multi-agent work, give every worker the same requirement IDs and base revision, assign non-overlapping owned paths, state allowed actions and forbidden external effects, and name the acceptance proof. Use one implementer where shared state makes write scopes inseparable.
7. Do not create a parallel store, table, or identity path without a named requirement or recorded decision. A persistent-data change updates the canonical model, migration and rollback path, and current-state evidence together.
8. Update only the owner documents whose truth changed. Routine code edits do not require rewriting every project document or creating a documentation ceremony.
9. Whenever `PROJECT.md` or `DATA_MODEL.md` changed, regenerate the human-readable spec view:

   ```bash
   python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" render-srs <project-root>
   ```

10. Run the project-native checks, then run:

    ```bash
    python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" check <project-root> --ready
    ```

    `check` fails the commit-worthy state when `Spec lock: Open` and `ai-context/SRS.html` no longer matches `PROJECT.md`/`DATA_MODEL.md`, and when `Spec lock: Locked` but either file changed since the recorded hash. Regenerate `SRS.html` (step 9) or re-run `lock-spec` after an owner-approved unlock to clear either failure. Install [assets/git-hooks/pre-commit](assets/git-hooks/pre-commit) as the project's `.git/hooks/pre-commit` once, so this check runs automatically before every commit instead of relying on an agent remembering to run it.

Walking into an unfamiliar project, run `migrate` first rather than deciding by hand whether to bootstrap or repair:

```bash
python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" migrate <project-root> --name "Project name"
```

`migrate` inspects the project and does the right thing for whatever it finds:

- **No project-standard files at all** — bootstraps a fresh `ai-context/` contract (needs `--name`; add `--profile software` only when architecture and persistent data are real concerns).
- **Legacy root-level files (`PROJECT.md`, `STATUS.md`, `docs/DECISIONS.md`, `ARCHITECTURE.md`, `DATA_MODEL.md`) whose headings already match the canonical template** (including a trailing annotation on the heading line) — moves each one into `ai-context/` and repoints every known cross-reference in the moved files and in root `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`, mechanically, no rewrite needed. Adds `Spec lock: Open` if `STATUS.md` predates that field.
- **A pre-existing document under a different name or heading convention** (a `SPEC.md`, a README-as-spec, a doc that never adopted this template) — is never moved. `migrate` reports exactly which canonical headings are missing per file and leaves it in place; rewriting a foreign document's content into the canonical headings is a judgment call for the Repair workflow above, not something this command guesses at. Re-run `migrate` after the rewrite — anything already moved is skipped automatically, so a mixed project (one file conforming, a sibling foreign) migrates what it safely can and holds the rest.
- **Already on the `ai-context/` layout** — no-op.

Exit code 0 means done (bootstrapped, already migrated, or every found file moved); 1 means nothing was found and no `--name` was given; 2 means at least one file is still held back needing a content rewrite — read its printed `HOLD` lines for exactly what's missing.

For a project you already know is either brand new or already-conformant, `bootstrap` alone still works and never overwrites existing files:

```bash
python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" bootstrap <project-root> --name "Project name"
```

Add `--profile software` only when architecture and persistent data are real project concerns. A fresh bootstrap is structurally valid but deliberately not ready; resolve the owner, outcome, requirements, and current state before running the ready gate.

To freeze the spec once it has matured past routine change (see the Contract ownership note on `Spec lock`), run:

```bash
python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" lock-spec <project-root>
```

and paste the printed line over `STATUS.md`'s `Spec lock:` line. Any later edit to `PROJECT.md` or `DATA_MODEL.md` then fails `check` until an owner decision records the unlock and `lock-spec` is re-run.

## Conflict rule

Separate intended truth from implemented truth:

- Owner-approved requirements decide what should exist.
- Source, schema, configuration, runtime, and receipts decide what currently exists.
- `STATUS.md` names the gap without rewriting either side to make them agree.
- A material conflict stays visible until evidence or an owner decision resolves it.

Never pick the most convenient document, silently merge incompatible decisions, or present a stale plan as current implementation.

## Completion gate

The work is complete only when:

- a fresh agent can identify the goal, scope, authority, current state, next action, and acceptance proof without relying on prior chat;
- each durable fact has one canonical owner and provider adapters do not duplicate it;
- requirements and decisions point to evidence or are explicitly `Not confirmed`;
- persistent data has one canonical model, and every material schema or store change has migration and rollback evidence;
- current state is separated from durable requirements and history;
- project-native verification and `project_standard.py check --ready` pass;
- every remaining conflict is visible under `Need decision` rather than hidden by invented certainty.
