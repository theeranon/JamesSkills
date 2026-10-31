# Handoff 2026-10-31: JamesSkills skill redefinition and portability

Written for any agent (any vendor, account or machine) continuing this work. Read `AGENTS.md`, `ai-context/LESSONS.md`, `ai-context/DECISIONS.md` DEC-048 to DEC-051 and `ai-context/STATUS.md` first. Everything below is already recorded there; this page is the sequence.

## What happened in the 2026-10-31 session

1. Pulled 2.1.14 (`4fa1c27`, adds `insight-driven-mode`). Local uncommitted work (DEC-049/050 installer change) was renumbered to avoid the upstream DEC-048 collision and is still uncommitted: `scripts/install.py`, `tests/test_installer_contracts.py`, `plugins/james-software/skills/project-standard/scripts/project_standard.py`.
2. Audit of all 23 skills, installer and 25 platforms: `docs/audits/skill-portfolio-portability-2026-10-31.md`. Highest findings: frontmatter `kind:` blocks claude.ai and Cowork upload (only six spec fields allowed); DEC-050 removed Codex coverage on this machine (Codex app-server lists 0 JamesSkills); `insight-driven-mode` collides with `make-it-james`; `solutionsimpact-*` aliases collide with account skills; manual plugin-cache symlink fights Claude's versioned cache (local-path marketplace loads in place instead).
3. `grill-me` interview, two rounds. The owner defined the real purpose of every skill: DEC-051. Questionnaire and answers: `docs/audits/grill-skill-goals-2026-10-31.md`.
4. Standing rule from the owner: record insights, decisions, skill changes and versions to GitHub continuously without being asked (LESSON-017).

## Pending work, in order

1. Rewrite bodies to DEC-051: `insight-driven-mode`, `proactive-habits`, `done-for-me`, `is-that-the-best-you-can-do`, `hand-it-off` (now a handoff skill), `coach-me` (now a mode), `one-page-pls` and `sum-meet` (footer `Researched by SolutionsIMPACT, Developed by James Theeranon`), `catchup`, `research-it`, `give-me-solutions`, `baseon`, `never-again`, `make-it-james`, `make-it-james-ux` (UX and UI sections). Each rewrite needs the schema (`docs/SKILL-SCHEMA.md`), `tests/behavioral-cases.md` cases, and `./scripts/validate` after every file (LESSON-009).
2. Remove aliases `solutionsimpact-onepagesummary` and `solutionsimpact-meeting-summary-full` from `catalog.json` and `aliases/`.
3. Technical P0 from the audit: `kind:` to `metadata.kind` (schema, test, 23 files); Codex coverage (native plugin or bundled binary detection at `ChatGPT.app/Contents/Resources/codex-cli/bin/codex`; doctor must fail, not skip); local-path marketplace for in-place loading; `skillListingBudgetFraction`.
4. Retire `final-it` and `proactive-dev` with the release that ships the rewrites; move surviving engineering rules into `project-standard` and `dev-are-you-sure`.
5. Bump VERSION and all manifests together (LESSON-005), validate, commit, push, reinstall, and tell the owner to restart the app.

## Owner preferences that shape every step

- Casual Thai in, Thai with English technical terms out. Rank findings; end with the decisions only he can make.
- He names skills by the moment he reaches for them. Several are wake-up commands aimed at the agent (`done-for-me`, `never-again`, `grill-me`, `zoom-out`, `is-that-the-best-you-can-do`): their bodies must describe what the agent does when scolded, not an abstract workflow.
- Never widen authorization: push only where the standing rule or request allows, which now includes this repository.
