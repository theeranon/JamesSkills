---
name: project-standard
kind: workflow
license: CC-BY-NC-4.0
description: Create or repair one vendor-neutral project contract so any agent or person can work without prior chat, stamped with the standard version it follows. Use when project truth is missing or drifting; not for routine edits that change nothing durable.
---

# Project Standard

Give the project one place where each durable fact lives, and say which version of the standard it follows.

## Scope

- Kind: workflow
- Owns: the project contract — requirements, current state, agent rules, decisions, and the generated specification view — created or repaired against a stated contract version.
- Boundary: writes only the owner documents whose truth changed. Never overwrites an existing file with a template, never converts a mentioned tool into a requirement, never reports intended architecture as implemented.

## Do not use this when

- The contract exists and current state after a gap is what is unknown -> `catchup`
- The contract exists and the work is to build against it -> `done-for-me`
- Engineering work needs role decomposition rather than a contract -> `proactive-dev`
- A rejected output needs to become a durable rule -> `never-again`
- The direction itself is unsettled -> `zoom-out`

## Procedure

Run every command from this skill directory as `python3 scripts/project_standard.py <command> <project-root>`.

1. Inspect the repository itself: existing instructions, git state, executable configuration, entrypoints, tests, and runtime evidence. Classify each source as intended truth, current state, history, adapter, or evidence.
2. Choose the smallest mode that fits. `bootstrap` for a project with no contract, `migrate` for one with scattered instructions, targeted repair for one with drift. Preserve every accepted project fact and all project-specific knowledge.
3. Give each durable fact exactly one owner document, and replace every duplicate with a pointer. Mark unsupported claims as not confirmed; record unresolved conflicts under the decision heading rather than choosing.
4. Write requirements as stable identifiers. Each names the observable outcome, its boundary, how it is accepted, and where the proof lives. An agent reporting that it implemented something is not acceptance.
5. Keep intended requirements and current implementation separate, and let the drift between them stay visible. Never rewrite current code as the desired architecture, and never describe the desired architecture as already built.
6. Create `ARCHITECTURE.md` and `DATA_MODEL.md` only when real complexity earns them. Never add empty ceremony.
7. Keep provider adapters thin. `CLAUDE.md`, `GEMINI.md`, and any other adapter add provider mechanics only; shared truth stays in `AGENTS.md` and the contract files.
8. Never introduce a parallel store, table, or identity path without a named requirement and a recorded decision. A persistent-data change updates the canonical model, the migration and rollback path, and the current-state evidence together.
9. Whenever the requirements or data model changed, regenerate the specification view with `render-srs`. Every project gets the same generated SRS from the same renderer, so the standard reads identically across projects. The generated file carries the contract version and a source hash and is never hand-edited.
10. Verify with `check <project-root> --ready`, which reports the contract version it validated against.

## Stop when

Each durable fact has exactly one owner, requirements carry identifiers with acceptance and proof, the generated SRS matches its sources, and `check --ready` passes with its version stated. Routine work that changed no durable fact leaves the contract untouched, which is a pass rather than a skip.

On Windows invoke the same helper with `python` when `python3` is not on PATH.

## Principles

**Single source of truth** — Each fact lives in exactly one document and everywhere else points at it, because duplicated truth diverges silently. Source: standard information-architecture principle; specific attribution uncertain
**Intended and actual are different documents** — Keep the specification separate from current state so the gap between them stays visible instead of being resolved by wishful writing. Source: standing rule in this library
**Architecture decision records** — Record the decision, its context, and its consequence at the moment it is made, because the reasoning is unrecoverable later. Source: Michael Nygard, Documenting Architecture Decisions, 2011
**Requirement keywords must be unambiguous** — State obligation precisely enough that compliance can be checked rather than argued. Source: Scott Bradner, RFC 2119, 1997

## Counter-case

- A routine skill edit changes no outcome, scope, permission, decision, or status. The contract is left alone; rewriting documents here would be ceremony.
- The user returns after two weeks and asks where the project stands. The contract already exists and only current state is unknown, so `catchup` owns it.

## Hand back

The owner documents actually changed, the requirement identifiers with their acceptance and proof, the regenerated SRS with its contract version, the visible drift between intended and actual, and the `check --ready` result.

## Sources

Nygard 2011, Documenting Architecture Decisions. Bradner 1997, RFC 2119, Key words for use in RFCs to Indicate Requirement Levels.
