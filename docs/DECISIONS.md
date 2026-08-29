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
