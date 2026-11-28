---
name: project-standard
license: CC-BY-NC-4.0
metadata:
  kind: workflow
  version: 2.5.3
description: Create or repair one project contract, software or any other kind, so another agent can continue without the chat, and record every insight, decision and deliverable in Git unasked. Use for set up project docs, AGENTS.md, context files, วางมาตรฐานโปรเจกต์, เอกสารโปรเจกต์มั่ว.
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
- The contract exists and engineering work must be planned and built against it -> `done-for-me`
- A rejected output needs to become a durable rule -> `never-again`
- The direction itself is unsettled -> `zoom-out`

## Profiles

Every project takes the same core. The profile decides what is added on top, and the skill picks it itself:

| Profile | Chosen when | Read |
|---|---|---|
| `software` | the repository has a build or package manifest, or three or more program source files | [references/profile-software.md](references/profile-software.md) |
| `general` | anything else: marketing, management, business, research, an idea | [references/profile-general.md](references/profile-general.md) |

Detection is `bootstrap` and `migrate` with no `--profile`; HTML, documents and one-off scripts do not make a project software. Read the chosen profile file before writing. `AGENTS.md` states it on a `Contract profile:` line, which then wins over detection. An owner's word wins over both.

## Record as you go

This applies in both profiles and without being asked. Whenever an insight, key learning, decision, important context, `SKILL.md` change or a new version of a deliverable (HTML included) appears in the conversation:

1. Write it to its owner file: decision to `DECISIONS.md`, insight or learning to `INSIGHTS.md`, deliverable version to `DELIVERABLES.md` with the file itself in the repository, current state and next move to `STATUS.md`, what the next agent must know to continue to `HANDOFF.md`.
2. Commit and push to the project's own remote in the same session. With no remote, commit and say that nothing has left this machine.

Write it so an agent that never saw the chat understands it. Never commit secrets, credentials or personal data the project does not already hold.

## Procedure

Run every command from this skill directory as `python3 scripts/project_standard.py <command> <project-root>`.

1. Inspect the repository itself: existing instructions, git state, executable configuration, entrypoints, tests, and runtime evidence. Classify each source as intended truth, current state, history, adapter, or evidence. `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `README.md` stay at the repository root; every other contract file lives under `ai-context/` — `ai-context/PROJECT.md`, `ai-context/STATUS.md`, `ai-context/DECISIONS.md`, `ai-context/ARCHITECTURE.md`/`DATA_MODEL.md` when they exist, and the generated `ai-context/SRS.html`.
2. Choose the smallest mode that fits. `bootstrap` for a project with no contract at all, `migrate` for one with scattered legacy instructions, or targeted repair for one with drift. `migrate` returns exit 0 when already on the layout or fully moved, exit 1 when nothing legacy was found and no `--name` was given to bootstrap, and exit 2 when at least one file is held back needing a manual content rewrite — read its printed HOLD line for exactly what is missing. Preserve every accepted project fact and all project-specific knowledge.
3. Give each durable fact exactly one owner document, following the project contract: normally requirements in `PROJECT.md`, current evidence in `STATUS.md`, agent rules in `AGENTS.md`, and decisions in `DECISIONS.md`. Preserve accepted alternative owner names; do not invent a new requirements file or move requirements into agent rules. Replace independently maintained duplicates with pointers; generated views may repeat facts when their source and refresh mechanism are explicit. Mark unsupported claims as not confirmed; record genuinely unresolved decisions without reopening a state contradiction already settled by evidence.
4. Write requirements as stable identifiers. Each names the observable outcome, its boundary, how it is accepted, and where the proof lives. An agent reporting that it implemented something is not acceptance. Preserve approved scope: prototype status does not weaken an offline requirement. Mark missing boundaries or proof as unspecified, and label new acceptance text as proposed; never fabricate test paths as existing evidence.
5. Keep intended requirements and current implementation separate, and let the drift between them stay visible. A false implemented status with code absent normally needs a status correction, not a requirements migration, new standing rule or architecture document. Never rewrite current code as the desired architecture, and never describe the desired architecture as already built. When a project already has running or shipped code, do not trust that the written requirements describe what actually ships: have an AI read the implemented code, not the documentation, and generate a functional description of what it actually does, module by module; compare that against the requirement table and permission matrix, flag every mismatch as a Reality conflict in `STATUS.md`, and treat an unexpected permission grant (for example an external party able to approve its own request) as a boundary defect, not a cosmetic one. Run this reverse-audit with a different AI model or vendor than the one that wrote the code, and record which model produced the code and which model performed the audit in `DECISIONS.md`. When only one model is available, run the audit in a fresh session that has not seen the build conversation and record that single-model limit instead of claiming independence.
6. In the software profile, create `ARCHITECTURE.md` and `DATA_MODEL.md` only when real complexity earns them; the general profile does not use them. Never add empty ceremony. For a project with more than a handful of functional requirements, do not keep every requirement in one flat table: create `ai-context/modules/<module-name>.md` per module, implement and verify one functional requirement at a time, and re-run the full existing test suite after each one before moving to the next.
7. Keep provider adapters thin. `CLAUDE.md`, `GEMINI.md`, and any other adapter add provider mechanics only; shared truth stays in `AGENTS.md` and the contract files.
8. Never introduce a parallel store, table, or identity path without a named requirement and a recorded decision. A persistent-data change updates the canonical model, the migration and rollback path, and the current-state evidence together.
9. For a bootstrap or migration adopting this contract, generate its specification view with `render-srs`. For targeted repair, regenerate only when an input consumed by the existing view changed; a status-only correction does not require creating an SRS or rerendering unrelated sources. The generated file carries the contract version and source hash and is never hand-edited.
10. For bootstrap or migration, verify with `check <project-root> --ready`, which reports the contract version it validated against. For targeted repair, verify the corrected fact and relevant contract checks; run the full ready gate when required by the project contract, without expanding the repair to unrelated documentation. For an explicit chat-only draft, return the minimal changed text, its owner and one verification caveat. Omit repeated scope, contradiction, unchanged-files, not-done and handback sections. Do not run commands, claim inspection beyond the supplied packet, or require generated files for that draft.
11. `STATUS.md`'s `Spec lock:` line owns whether the specification may still move. `Open` (the default) means `PROJECT.md`/`DATA_MODEL.md` are expected to keep changing, so `check` only requires the generated SRS to match their current content. `Locked (date, hash)` means an owner has frozen them; `check` then fails when either file has changed since that recorded hash, and any further change is a defect until a Need decision records the unlock. To lock, run `python3 scripts/project_standard.py lock-spec <project-root>` and paste its printed line over `STATUS.md`'s `Spec lock:` line.

## Stop when

The requested contract work is verified: bootstrap/migration establishes owners, requirement acceptance/proof and a matching generated SRS and passes `check --ready`; targeted repair corrects the relevant owner and verifies affected references or generated views. Routine work that changed no durable fact leaves the contract untouched, which is a pass rather than a skip.

On Windows invoke the same helper with `python` when `python3` is not on PATH.

## Principles

**Single source of truth** — Each durable fact has one authoritative owner; other locations point to it or are explicitly generated from it, preventing independently maintained copies from diverging. Source: standard information-architecture principle; specific attribution uncertain
**Intended and actual are different documents** — Keep the specification separate from current state so the gap between them stays visible instead of being resolved by wishful writing. Source: standing rule in this library
**Architecture decision records** — Record the decision, its context, and its consequence at the moment it is made, because the reasoning is unrecoverable later. Source: Michael Nygard, Documenting Architecture Decisions, 2011
**Requirement keywords must be unambiguous** — State obligation precisely enough that compliance can be checked rather than argued. Source: Scott Bradner, RFC 2119, 1997

## Counter-case

- A routine skill edit changes no outcome, scope, permission, decision, or status. The contract is left alone; rewriting documents here would be ceremony.
- The user returns after two weeks and asks where the project stands. The contract already exists and only current state is unknown, so `catchup` owns it.

## Hand back

The owner-document changes, requirement identifiers with acceptance/proof, visible intended-versus-actual drift, and checks actually performed. Include regenerated SRS/version only when applicable; for a requested draft, clearly identify proposed text and unverified facts instead of reporting edits or readiness.

## Sources

Nygard 2011, Documenting Architecture Decisions. Bradner 1997, RFC 2119, Key words for use in RFCs to Indicate Requirement Levels.

## Software: source and production branches — contract 1.2

A software project keeps two branches. `main` is the working source with its AI context and is never deployed. `production` is generated from the pushed `main` by `tools/release.sh --push` and changes no other way: it mirrors the hosting domain directory with a substantive `public_html/`, assembled only from the explicit mappings in `.release-layout.json`, never a copy or merge of `main`. Private folder names stay app-specific, and runtime config and data are preserved.

Git Manager is the single writer that deploys `production`. Where the target's auto-deploy is on, publishing `production` is the live deployment: run it only under production authority, and call it done only when the manager shows the new production SHA and the live health or version check matches. Where auto-deploy is off, the manager's own Deploy action runs after its gates. A new target keeps auto-deploy off until destination, preservation, migration and rollback are accepted; an accepted one is never switched off just to apply this standard.

An FTP target uses the site's own-domain account, whose home is the domain directory, with Git Manager Remote Root `/` and Local Path `.`; a reviewed same-host publisher may stand in for FTP. The owner types every password, and a DirectAdmin password rotation needs the same value in the paired Git Manager form, so prepare both forms and never ask for the password. `ai-context/DEPLOYMENT.md` records the real route, transport and checked auto-deploy state; [references/profile-software.md](references/profile-software.md) holds the full rules. Legacy projects need an explicit mapping migration, not a silently rewritten contract or a claim that running files moved. Independent deployment-contract audit: gpt-6.1-terra, 2026-11-26; findings applied to templates, builder and checks.
