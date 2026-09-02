# Decisions

Record accepted or superseded project decisions. Raw discussion remains in its source system.

## DEC-001 — One canonical instruction body

- Date: 2026-08-28
- Status: Accepted
- Decision: Each skill has one canonical `SKILL.md`. Compatibility aliases and vendor adapters may add discovery metadata but may not duplicate behavior.
- Why: duplicated instructions drift and make different agents follow incompatible rules.
- Source: repository v0.3.0 architecture and accepted maintainer rules.
- Affects: `catalog.json`, `skills/`, `aliases/`, `adapters/`, `AGENTS.md`.
- Supersedes: divergent provider-owned skill bodies.

## DEC-002 — Candidate Card before promotion

- Date: 2026-08-29
- Status: Accepted
- Decision: A new skill name, alias, framework hierarchy, or promotion state requires an approved Candidate Card, cross-case evidence, failure cases, and a legitimate counter-case.
- Why: general permission to improve the library previously caused premature names, invented framework boundaries, and overfit packages.
- Source: owner corrections and repository v0.7.1 lifecycle repair.
- Affects: `catalog.json`, `AGENTS.md`, `tests/test_portfolio_lifecycle.py`, `tests/behavioral-cases.md`.
- Supersedes: treating repository-wide improvement authority as naming approval.

## DEC-003 — Private portable repository with local release gates

- Date: 2026-08-28
- Status: Accepted
- Decision: Keep JamesSkills private by default, distribute promoted packages through managed local links, and validate with repository-owned pre-commit and pre-push gates instead of GitHub Actions.
- Why: the same reviewed source must travel across machines and agents without paid runner dependency or silent platform-specific copies.
- Source: owner direction and repository install/update history.
- Affects: `README.md`, `scripts/install`, `scripts/update`, `scripts/doctor`, `.githooks/`.
- Supersedes: GitHub Actions as the required validation path.

## DEC-004 — Source and live-state boundary

- Date: 2026-08-28
- Status: Accepted
- Decision: Store reusable process knowledge, reviewed source metadata, original paraphrase, applications, and limitations; exclude credentials, client data, chat exports, live JamesOS state, and copyrighted originals by default.
- Why: the portable library must remain safe to clone and must not turn private operational state into reusable prompt content.
- Source: accepted repository boundary and knowledge-library release rules.
- Affects: `PROJECT.md`, `README.md`, `AGENTS.md`, `packs/`, `scripts/validate`.
- Supersedes: None.

## DEC-005 — Apply project-standard to its own repository

- Date: 2026-08-29
- Status: Accepted
- Decision: JamesSkills must maintain the four minimum project-standard owner files and the ready check must run inside the normal validator.
- Why: a promoted shared standard is not credible when its source repository does not pass that standard itself.
- Source: direct owner correction in the current project review.
- Affects: `PROJECT.md`, `STATUS.md`, `AGENTS.md`, `docs/DECISIONS.md`, `scripts/validate`.
- Supersedes: documenting project-standard as available while leaving this repository outside its gate.

## DEC-006 — One human skill handbook

- Date: 2026-08-29
- Status: Accepted
- Decision: Maintain `docs/SKILLS.md` as the single human navigation guide, grouped by the moment of use and linked to each canonical package. Keep behavior authoritative in each `SKILL.md` and lifecycle authoritative in `catalog.json`.
- Why: a raw catalog and scattered instruction files do not let James browse and choose skills as clearly as the AI Hero model.
- Source: direct owner request for an AIHero-style guide in the current project review.
- Affects: `README.md`, `docs/SKILLS.md`, `catalog.json`, `tests/test_skill_handbook.py`.
- Supersedes: the short README vocabulary list as the only human guide.

## DEC-007 — Three promoted transformation-design skills

- Date: 2026-08-29
- Status: Accepted
- Decision: Promote `build-framework`, `transformation-journey`, and `learning-experience-design` as the three canonical responsibilities. Reverse `design-the-journey` and `design-the-course` into compatibility aliases. Route by accountable outcome, not duration.
- Why: reusable company IP, macro organization transformation, and bounded learning intervention are different objects that require different evidence and ownership.
- Source: accepted owner decisions from the completed transformation-design grilling session and the approved Candidate Cards.
- Affects: `CONTEXT.md`, `catalog.json`, `skills/core`, `aliases`, `packs/frameworks`, `docs/SKILLS.md`, and learning-design regressions.
- Supersedes: the two uninstalled `design-*` pilots and the unresolved LED/TPS hierarchy. TPS is one framework inside LED.

## DEC-008 — Skill-first V1 with cited HTML proof

- Date: 2026-08-29
- Status: Accepted
- Decision: Complete and prove the three portable skills before building an organization application. Each skill must produce a purpose-specific, cited, executive HTML artifact and pass source, routing, behavior, visual, and install gates.
- Why: the immediate outcome is reliable skill behavior. UI, API, employee rollout, and advanced approval design do not improve V1 call accuracy and would delay proof.
- Source: direct owner correction after the architecture discussion expanded beyond the approved scope.
- Affects: `PROJECT.md`, `AGENTS.md`, HTML assets, tests, and release sequencing.
- Supersedes: treating organization UI, public API, client portal, or multi-role approval as part of this release.

## DEC-009 — HTML-only unless PDF is explicitly authorized

- Date: 2026-08-29
- Status: Accepted
- Decision: An HTML request, including A4 or print-ready HTML, delivers HTML only. Browser print emulation is the normal visual proof. Create PDF only when James explicitly requests it or an authoritative recipient constraint requiring one fixed print file is directly confirmed; never infer that need from presentation language.
- Why: automatic PDF export consumed extra execution and review work without serving the requested outcome, and a legacy duplicate meeting-summary skill kept reviving that behavior.
- Source: direct owner correction during the 0.9.0 release audit.
- Affects: `make-it-james`, `final-it`, `sum-meet`, `one-page-pls`, render tests, and local discovery installation.
- Supersedes: automatic HTML-plus-PDF delivery and PDF-based HTML QA.

## DEC-010 — project-standard v2: ai-context layout, generated SRS, spec lock

- Date: 2026-09-01
- Status: Accepted
- Decision: `project-standard` moves every contract file except `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`README.md` under `ai-context/`; adds a generated `ai-context/SRS.html` view rendered by `render-srs` from `PROJECT.md` + `DATA_MODEL.md`; adds a `Spec lock` field in `STATUS.md` (`Open` or `Locked (date, hash)`, set via `lock-spec`) enforced by `check`; adds a reverse-SRS/cross-model audit workflow step, a structured permission (role × action) matrix in `DATA_MODEL.md`, a non-functional-requirements table in `PROJECT.md`, and an opt-in per-module requirement breakdown. JamesSkills migrated its own root-level `PROJECT.md`/`STATUS.md`/`docs/DECISIONS.md` into `ai-context/` in the same change so `scripts/validate` keeps passing.
- Why: distilled from a SolutionsIMPACT "AI Systemize Business" class transcript (guest expert Max, session EP7) teaching a production-readiness workflow — reverse-generating a spec from shipped code, prioritizing a permission matrix over generic "security," cross-vendor audit to avoid same-model bias, and a standard project `.md` ecosystem — evaluated against the existing skill and found four genuine gaps (full analysis: `scratch/ep5-insights-vs-project-standard.md` in the session that authored this decision). The scattered root-level `.md` files were also a standing owner complaint (harder to navigate than Max's demoed folder structure); `SRS.html` and `Spec lock` were owner-directed additions, not sourced from the transcript.
- Source: `ai-systemize-business-ep5-meeting-record-FULL.html` (source: `🟣[VClass] AI Systemize Business EP5.txt`, full transcript, 1,260 lines) plus direct owner decisions in the authoring session.
- Affects: `skills/standards/project-standard/` (`SKILL.md`, `references/contract.md`, all asset templates, `scripts/project_standard.py`, `tests/`), this repository's own `ai-context/PROJECT.md`, `ai-context/STATUS.md`, `ai-context/DECISIONS.md`, `AGENTS.md`.
- Supersedes: the v1 flat root layout (`PROJECT.md`/`STATUS.md`/`docs/DECISIONS.md`/`ARCHITECTURE.md`/`DATA_MODEL.md` at repository root); migration steps for other v1 projects are recorded in `references/contract.md`'s "Migrating a flat-layout (v1) project into `ai-context/`" section.

## DEC-011 — Fixed a silent content-loss bug in render-srs, found by a workspace-wide state test; added an automated `migrate` command

- Date: 2026-09-01
- Status: Accepted
- Decision: `render_srs`'s heading parser (`extract_section`) now (a) tolerates a trailing annotation on the same heading line — a date stamp or parenthetical note no longer breaks the match, fixing a regex bug where `.*` under `re.DOTALL` swallowed the rest of the document instead of just the heading's own line, and (b) distinguishes "heading not found at all" from "heading found, content genuinely not confirmed": a missing heading now prints a `WARN` per section and renders a visibly flagged banner in `SRS.html`, instead of silently defaulting to `Not confirmed` as if the content had been checked and found empty. Also added `project_standard.py migrate <root>`, a single entry point that bootstraps a project with no existing contract, auto-moves legacy root files into `ai-context/` and repoints every known cross-reference once their headings already match the template, and otherwise reports (exit 2) exactly which headings are missing per file it leaves in place — never guessing at a content rewrite.
- Why: owner asked to state-test `project-standard` v2 against every real project under `AI Workspace/` before trusting the earlier "comprehensive, not overfit, generalizes, old projects can migrate" claim. A read-only audit agent tested `extract_section` against 6 real documents, including the closest real match to the tool's own template (`InvestNow/trading/.../investment-engine/PROJECT.md`, which uses the tool's exact target filename and heading text): 0/6 rendered fully — even the best case failed on `## Requirements (อัปเดตตาม PHP Architecture Pivot 2026-09-01)` because of the trailing annotation. Before the parser fix, a naive v1→v2 migration on any real project in the workspace would have produced an `SRS.html` that looked complete but silently dropped every section with a differently-worded or annotated heading, with no error signal. The migration itself was also manual (move files, hand-edit pointers) with no tooling to actually execute it or to distinguish a clean v1 project from one needing content rewritten first — `migrate` closes that gap for the mechanical part while deliberately refusing to guess at the judgment-call part.
- Source: read-only workspace audit (background agent, this session) covering Infra, InvestNow, James, Library, Shared, SoloCFO, SolutionsIMPACT; confirmed no project outside `Library/JamesSkills` had migrated to the `ai-context/` layout at the time of the audit.
- Affects: `skills/standards/project-standard/scripts/project_standard.py` (`extract_section`, `section_prose_or_table`, `render_srs`, `render_srs_command`, new `migrate`/`heading_present`/`repoint_text`/`LEGACY_CANONICAL_HEADINGS`/`LEGACY_OPTIONAL_HEADINGS`/`REPOINT`), `skills/standards/project-standard/tests/test_project_standard.py`, `skills/standards/project-standard/references/contract.md`, `skills/standards/project-standard/SKILL.md`, `skills/standards/project-standard/assets/AGENTS.template.md`.
- Supersedes: DEC-010's implicit claim that `render-srs` works against any project once files are moved into `ai-context/`, and that migration was "additive... no rename" with no automated command behind it. `render-srs` now works once a project's `PROJECT.md`/`DATA_MODEL.md` use the canonical template headings (trailing annotations tolerated) and loudly flags what it can't parse; migration for a canonical-headed v1 project is now a single automated command, and migration for a foreign-headed pre-existing document is explicitly still a human/agent judgment call, reported precisely rather than silently attempted.

## DEC-012 — README Architecture & Anti-Bloat Standard

- Date: 2026-09-03
- Status: Accepted
- Decision: Adopt `ai-context/README_STANDARD.md` as the enforceable law for `README.md`. The root README is strictly the human onboarding and public entry point ("Front Door"). It must feature an iconic 3-4 skill Before/After showcase and a single, scannable catalog table covering all canonical skills, while routing exhaustive technical deep dives to `docs/SKILLS.md` per DEC-006. Embedding 20+ full HTML tables and decorative AI-generated images on the root landing page is formally prohibited.
- Why: Teamwork subagents bloated `README.md` to 46KB and 800+ lines with 30 auto-generated PNG diagrams and juvenile "AI วิ่งเล่นทุ่งลาเวนเดอร์" tables. This destroyed GitHub scannability, slowed page render times, and violated open-source readability standards benchmarked against top AI repos (Fabric, Anthropic Skills, vLLM).
- Source: direct owner correction on README standards and industry benchmark comparison.
- Affects: `README.md`, `ai-context/README_STANDARD.md`, `tests/test_readme_verification.py`.
- Supersedes: the bloated multi-table README layout authored by the teamwork subagents.
