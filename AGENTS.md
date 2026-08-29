# JamesSkills Agent Contract

## Required context

1. Read `PROJECT.md` for outcome, scope, requirements, boundaries, and acceptance proof.
2. Read `STATUS.md` for current verified state, blockers, and the next move.
3. Read `docs/DECISIONS.md` when a prior choice, lifecycle decision, or superseded rule matters.
4. Read `docs/SKILLS.md` when selecting or explaining a skill; load the selected `SKILL.md` completely before acting.
5. Read `README.md` for human installation and repository usage.

## Working rules

- One canonical instruction body per skill. Vendor adapters may add metadata, never duplicate behavior.
- Keep every promoted package in `catalog.json`. Category determines responsibility; aliases provide migration only.
- Name skills from the natural phrase a person uses at the moment they need the capability. Name the mental move, not an internal department.
- A workflow skill completes one bounded job. A mode skill changes behavior for the remainder of the conversation after one activation.
- A shared standard applies automatically. An output skill owns artifact semantics and consumes the shared standard instead of copying it.
- Skills contain reusable process knowledge. Never commit credentials, client data, chat exports, live status, or JamesOS databases.
- Treat a book, paper, course, or proprietary report as a source before considering a new lens. Do not create one skill per source.
- Keep copyrighted originals outside Git by default. Commit source identity, rights posture, hash, locators, original paraphrase, applications, and limitations.
- Separate source claims, independent evidence, James rules, and inference. Never promote an inferred profile to an official result.
- A direct correction from James is evidence to investigate. Promote it to a global rule only when the intended scope is durable.
- Authorization to build the library is not approval of a new skill name, domain boundary, framework hierarchy, alias, or promotion state. Keep a new candidate as `pilot` and uninstalled until James approves its Candidate Card.
- A Candidate Card must show the working name options, bounded job, trigger and exclusions, overlap with current skills, source map and confidence, representative requests, failure cases, and recommended lifecycle state.
- Promote only after cross-case evidence shows a reusable gap, nearby counter-cases show the rule is not overfit, and James approves the exact name and scope.
- Every behavioral correction requires a rejected-case regression, another case with the same mechanism, and a legitimate counter-case.
- Release on the shortest critical path: usable package, minimum required proof, authorized install or delivery, then a local repository checkpoint. Push, deploy, publish, or send only when the request or accepted project contract authorizes that exact external target. Optional audits, documentation cleanup, and extra hardening must not delay the first usable outcome.
- Run `scripts/validate` and `scripts/doctor` before declaring a release usable.
- Do not claim cross-platform support without discovery and outcome evidence on that platform.
- Treat managed-link presence as filesystem proof only. Do not call it runtime loading, automatic routing, or behavioral parity without platform evidence.
- Preserve unrelated dirty work. Never treat local implementation authority as permission to deploy, publish, send, or mutate an unrelated external account.
- Update only the owner document whose truth changed. Do not copy requirements into status, status into the handbook, or full skill behavior into an alias.

## Commands

- Install: `./scripts/install`
- Update: `./scripts/update`
- Test: `./scripts/validate`
- Diagnose: `./scripts/doctor`
- Contract: `python3 skills/standards/project-standard/scripts/project_standard.py check . --ready`
- Build: none; this repository distributes source files and managed symlinks directly.

## Completion

- Satisfy the named `PROJECT.md` requirement and its acceptance proof.
- Run `scripts/validate`; it includes the project-standard ready gate.
- Run `scripts/doctor` when install, aliases, lifecycle, or discovery links changed.
- Update `STATUS.md` only when current verified state, blocker, or next move changed.
- Record durable outcome, scope, lifecycle, distribution, or authority changes in `docs/DECISIONS.md`.
- Do not claim cross-platform behavior, installation, delivery, publication, or external action without evidence for the exact target.
