---
name: project-standard
description: Create or repair one vendor-neutral project contract. Use when starting or restructuring a project, turning an agreed goal or architecture into executable requirements, onboarding or handing work to another AI, reconciling conflicting project documents, or repeated agents lose scope, status, decisions, or acceptance criteria; skip routine work when the existing contract remains current.
---

# Project Standard

Keep every agent on the same project truth without turning documentation into ceremony.

## Contract ownership

- `PROJECT.md` owns intended outcome, scope, authority, requirement IDs, boundaries, and acceptance proof.
- `STATUS.md` owns current verified state, active work, next action, blockers, and decisions needed.
- `AGENTS.md` owns the vendor-neutral working contract and points to the project sources it requires.
- `docs/DECISIONS.md` owns accepted and superseded decisions with rationale and source.
- `README.md` owns human onboarding and usage when the project needs it.
- `ARCHITECTURE.md` and `DATA_MODEL.md` exist only when system or persistent-data complexity earns them. When present, `DATA_MODEL.md` owns canonical stores, identity, relations, lifecycle, migration, and rollback.
- Git, tests, runtime, and provider receipts remain execution evidence. Documentation never turns a claim into proof.

Read [references/contract.md](references/contract.md) when choosing files, resolving conflicts, or adapting an existing repository.

## Workflow

1. Inspect the repository, existing instructions, current git state, executable configuration, entrypoints, tests, and relevant runtime evidence. Classify each source as intended truth, current state, history, adapter, or evidence.
2. Select the smallest mode that fits:
   - **Establish**: create the baseline contract for a new or undocumented project.
   - **Specify**: turn an agreed outcome or architecture into named requirements and acceptance proof.
   - **Repair**: resolve duplicated, stale, or contradictory project documents without deleting useful history.
   - **Handoff**: refresh current state and source pointers so a new agent can continue without chat history.
3. Preserve accepted project facts. Put each fact in one owner document and replace duplicates with pointers. Mark unsupported claims `Not confirmed`; record unresolved conflicts under `Need decision`.
4. Write requirements as stable IDs. Every requirement must name the observable outcome, boundary, acceptance method, and proof source. A requirement is not complete because an agent says it implemented it.
5. Keep provider files thin. `CLAUDE.md`, `GEMINI.md`, or another provider adapter may add provider mechanics, but shared project truth stays in `AGENTS.md` and the contract files.
6. For multi-agent work, give every worker the same requirement IDs and base revision, assign non-overlapping owned paths, state allowed actions and forbidden external effects, and name the acceptance proof. Use one implementer where shared state makes write scopes inseparable.
7. Do not create a parallel store, table, or identity path without a named requirement or recorded decision. A persistent-data change updates the canonical model, migration and rollback path, and current-state evidence together.
8. Update only the owner documents whose truth changed. Routine code edits do not require rewriting every project document or creating a documentation ceremony.
9. Run the project-native checks, then run:

   ```bash
   python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" check <project-root> --ready
   ```

For a new repository, bootstrap files without overwriting existing work:

```bash
python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" bootstrap <project-root> --name "Project name"
```

Add `--profile software` only when architecture and persistent data are real project concerns. A fresh bootstrap is structurally valid but deliberately not ready; resolve the owner, outcome, requirements, and current state before running the ready gate.

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
