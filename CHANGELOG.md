# Changelog

## 0.9.1 - 2026-09-01

- Upgraded `project-standard` to v2: moved every contract file except `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`README.md` into an `ai-context/` folder so project truth stops scattering across the repository root.
- Added a generated `ai-context/SRS.html` view (`render-srs` command), rendered from `PROJECT.md` and `DATA_MODEL.md`, as a read-only human-readable spec — never hand-edited, regenerated on demand.
- Added a `Spec lock` field in `STATUS.md` (`Open` or `Locked (date, hash)`, set via the new `lock-spec` command) that `check` enforces: Open requires `SRS.html` to stay in sync before commit, Locked fails the check if `PROJECT.md`/`DATA_MODEL.md` drift from the recorded hash.
- Added an optional `assets/git-hooks/pre-commit` template so the freshness and lock checks can run automatically before every commit instead of depending on an agent remembering.
- Added a reverse-SRS/cross-model audit workflow step, a structured permission (role × action) matrix in `DATA_MODEL.md`, a non-functional-requirements table in `PROJECT.md`, and an opt-in per-module requirement breakdown (`ai-context/modules/<module>.md`) — all distilled from a SolutionsIMPACT "AI Systemize Business" class transcript and evaluated against the prior skill version for genuine gaps only.
- Migrated JamesSkills' own root-level `PROJECT.md`/`STATUS.md`/`docs/DECISIONS.md` into `ai-context/` in the same change so `scripts/validate`'s project-standard ready gate keeps passing against the skill this repository ships.
- Recorded the full decision as `DEC-010` in `ai-context/DECISIONS.md`; migration steps for other v1 (flat-layout) projects are documented in `project-standard`'s `references/contract.md`.
- State-tested the upgrade against every real project under `AI Workspace/` (read-only) and found `render-srs` silently dropped any section whose heading carried a trailing annotation or didn't match the template verbatim — confirmed on 0/6 real documents, including the closest real match to the template. Fixed the regex bug causing it, made a genuinely-missing heading print a `WARN` and render a flagged banner instead of a silent `Not confirmed`, and recorded the finding as `DEC-011`.
- Added `project_standard.py migrate <root>`, a single command that bootstraps a project with no existing contract, auto-moves a v1 project's legacy root files into `ai-context/` and repoints every known cross-reference once the headings already match the template, and otherwise reports (exit 2) exactly which headings are missing per file it leaves in place rather than guessing at a content rewrite — recorded alongside the parser fix in `DEC-011`.

## 0.9.0 - 2026-08-29

- Promoted `build-framework`, `transformation-journey`, and `learning-experience-design` as the three canonical transformation-design responsibilities.
- Reversed `design-the-course` and `design-the-journey` into compatibility aliases so formal responsibility names remain portable across AI platforms.
- Added a source-ranked house framework registry and enforced reuse, upgrade, then new-build order before creating SolutionsIMPACT IP.
- Bound every registry asset to version, permitted scope, source locators, and approval state; unaudited principle and pattern names remain candidates, while the AI five-phase asset remains a pilot pattern rather than being mislabeled a framework.
- Kept the AI five-phase journey pattern offer-specific, and kept Transformative Productivity System as one framework inside Learning Experience Design rather than the discipline itself.
- Added purpose-specific, print-ready executive HTML contracts for framework decisions, transformation journeys, and bounded learning experiences.
- Added provenance, impact-chain, routing, counter-case, alias-target, installation-target, and strict visual regression gates.
- Tightened the internal router so clear work owners are selected directly; fresh Codex and Claude sessions passed the framework, journey, and bounded-learning routes.
- Made HTML-only the default for HTML and print-ready work; PDF now requires an explicit request or a directly confirmed authoritative recipient constraint, and browser print emulation replaces PDF generation for visual QA.
- Added the Codex discovery root to the portable installer and made legacy non-link collisions fail visibly instead of leaving an older duplicate skill active.
- Pinned the local browser-QA dependency and documented one reproducible command that refreshes the hash-bound HTML render receipt without exporting PDF.
- Kept V1 skill-first: no application UI, public API, employee portal, client portal, or multi-role approval workflow.

## 0.8.1 - 2026-08-29

- Applied `project-standard` to JamesSkills itself with canonical outcome, requirement, status, agent, and decision owners.
- Added one human skill handbook organized by when to reach for each workflow, including lifecycle, aliases, boundaries, and common compositions.
- Added catalog-complete handbook and self-standard regression gates.
- Made every validate, install, update, commit, and push fail when the repository's own project contract is not ready.
- Expanded portability and secret-pattern checks from skill folders to every tracked or non-ignored candidate text file.

## 0.8.0 - 2026-08-29

- Promoted and installed the approved-name `catchup` workflow for reconstructing verified current state without turning a bounded question into a history excavation or audit.
- Added a read-only project snapshot helper covering target identity, branch, HEAD, upstream divergence, dirty and untracked work, contract-file presence, and optional checkpoint delta.
- Added clean, dirty, stale-status, missing-upstream, invalid-checkpoint, non-Git, scoped-workstream, Git-error, and already-clear counter-cases before promotion.
- Made authorized workflows consume prior exact approval instead of asking the user to repeat a magic confirmation word.

## 0.7.1 - 2026-08-29

- Demoted both learning-design packages to pilot because their names and framework ontology were never approved.
- Scoped the five-phase model to the sourced SolutionsIMPACT AI Transformation Journey offer instead of presenting it as a universal Learning Experience model.
- Recorded the conflict between the newest direct TPS-inside-LED correction and older source material rather than choosing a hierarchy silently.
- Added Candidate Card, cross-case evidence, and legitimate-counter-case gates to prevent premature promotion and one-case overfitting.
- Updated the installer to prune managed packages and aliases that are no longer promoted.
- Hardened `give-me-solutions`, `zoom-out`, `prove-it`, `final-it`, and `i-have-adhd` with authority, reuse, freshness, bounded-stop, target-identity, semantic-proof, source-fidelity, and mode-boundary rules.
- Added shared multi-agent ownership and independent-verification contracts to `done-for-me`, `project-standard`, and `prove-it`.
- Strengthened `make-it-james` lint and print rules for decorative rails, rectangular radius, pills, line-height, document flow, page grouping, and redundant visuals.
- Added an idempotent offline font embedder so single-file HTML can carry four IBM Plex Sans Thai weights instead of depending on a Google Fonts link.
- Made updates fail before changing the active checkout by validating the fetched candidate in a temporary worktree; expanded doctor to report version, commit, dirty state, and stale managed links.
- Added a cross-history portfolio audit with ranked Candidate Cards and explicit hold, merge, and control-plane boundaries; `catchup` is the recommended next pilot but remains uninstalled.
- Narrowed the portable live-context boundary so JamesOS is not selected for generic project work, and made delegated action authority explicit down to each worker packet.

## 0.7.0 - 2026-08-29

- Added `design-the-course`, the general Learning Experience Design workflow for one bounded course, workshop, session, or learning day.
- Added `design-the-journey`, the organization-level five-phase transformation workflow with stable internal phase identities and explicit evidence handoffs.
- Added `/learning-experience-design` and `/transformation-journey` as direct formal-name aliases.
- Separated the general LED discipline from the narrower knowledge-transfer e-learning product and from Transformative Productivity System terminology that remains unapproved.
- Added regression gates for the course-versus-journey boundary, five-phase spine, one-way composition, and obsolete phase-model rejection.
- Added request and promise traceability so topic compression cannot silently drop requirements or preserve low-value content by habit.

## 0.6.0 - 2026-08-28

- Renamed the canonical framework workflow from `think-with-this` to `baseon`; retained the old name as a compatibility alias.
- Added permanent `/wealth-dynamics`, `/talent-dynamics`, and `/wealth-spectrum` lens shortcuts with no duplicated reasoning body.
- Unified Wealth Dynamics and Talent Dynamics under one canonical Dynamics lens while keeping Wealth Spectrum as a separate model in the same creator family.
- Added registry alias resolution and separate creator-family/model-family metadata with collision and behavioral regression gates.
- Added the official Wealth Dynamics source card and a history-grounded candidate audit for future lenses.

## 0.5.0 - 2026-08-28

- Added the source-first framework knowledge library and its then-current `think-with-this` application workflow.
- Added reviewed-private Wealth Spectrum and Talent Dynamics lens material with citations, provenance, rights boundaries, and reversible-experiment rules.
- Added deterministic source, lens, lifecycle, path-containment, duplicate-claim, and prohibited-raw-content validation.

## 0.4.0 - 2026-08-28

- Added `project-standard`, combining the useful parts of `project-docs-standard`, `write-the-spec`, and `keep-the-project-straight` into one vendor-neutral standard.
- Added minimal and software project templates plus an idempotent bootstrap and structural validator.
- Separated intended requirements, current state, agent workflow, and decision history into distinct owners without forcing documentation churn on routine edits.
- Added the `project-docs-standard` compatibility alias and retired the two divergent Gemini instruction bodies from canonical ownership.

## 0.3.1 - 2026-08-28

- Added a critical-path rule: deliver, verify, install, and push the minimum usable outcome before optional audits, documentation cleanup, taxonomy work, or extra hardening.
- Added a regression case for existing-skill adaptations that are delayed by unrelated completeness work.

## 0.3.0 - 2026-08-28

- Split the library into core, modes, standards, outputs, and internal packages with one canonical `catalog.json`.
- Restored the global output authority as `make-it-james`, including a portable deterministic linter and behavior test.
- Added `sum-meet`: one source-faithful A4 portrait HTML meeting record containing every agenda as a separate zone.
- Added `one-page-pls`: one independently usable A4 landscape artifact per detected topic or agenda, with a no-silent-loss gate.
- Rebuilt both HTML templates around IBM Plex Sans Thai, compact density, 6px radius, restrained cards, and all-page visual QA.
- Added a data-free SolutionsIMPACT output pack so the two generic workflows can apply brand identity without hardcoding it into their semantic logic.
- Added migration aliases for `james-ui-standard`, `solutionsimpact-meeting-summary-full`, and `solutionsimpact-onepagesummary` without duplicating instructions.
- Installer, doctor, and validation now operate from the typed catalog rather than assuming every skill belongs in `skills/core`.

## 0.2.0 - 2026-08-28

- Reframed skill names as natural invocation phrases rather than system modules.
- Added `give-me-solutions`, `done-for-me`, `zoom-out`, `prove-it`, `never-again`, and `final-it`.
- Added persistent conversation mode `i-have-adhd`; concise communication no longer means one arbitrary answer or lost information.
- Retired `same-page`, `read-the-room`, and `follow-the-money` from the proposed set.
- Installer now prunes retired managed links and installs only promoted core skills.

## 0.1.1 - 2026-08-28

- Added repository-owned pre-commit and pre-push validation gates.
- Installer now activates local Git hooks without GitHub Actions or paid runners.

## 0.1.0 - 2026-08-28

- Initial private skill library.
- Added router, project control, source-first research, proof gate, UI standard, and handoff.
- Added cross-platform installer, updater, validator, and doctor.
