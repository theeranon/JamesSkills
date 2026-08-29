# JamesSkills

Last verified: 2026-08-29

## Outcome

- Primary user: James Theeranon and the AI agents working for him across Codex, Claude Code, Gemini, and Google Antigravity.
- Problem: reusable working practices drift, duplicate, and become hard to discover when they are scattered across agents, projects, and chat history.
- Successful outcome: one private, portable repository lets a human choose the right workflow, lets an agent load one canonical instruction body, installs only approved packages, validates every change before release, and exposes current project truth without relying on prior chat.

## Authority

- Owner: James Theeranon.
- Requirement authority: this file after owner acceptance, informed by accepted decisions in `docs/DECISIONS.md`.
- Current state: `STATUS.md`.
- Decision history: `docs/DECISIONS.md`.
- Human installation and usage: `README.md` and `docs/SKILLS.md`.
- Package lifecycle and aliases: `catalog.json`.

## Scope

### In

- Portable workflow, mode, standard, output, and internal routing skills.
- Compatibility aliases that point to one canonical instruction body.
- Reviewed knowledge and brand packs that contain no live client or account state.
- Local install, update, doctor, validation, and Git release gates.
- Human-readable skill discovery and usage guidance.

### Out

- JamesOS live state, credentials, client records, chat exports, and production databases.
- Vendor-specific copies of canonical skill behavior.
- Global installation of pilot or unapproved packages.
- Claims of universal model-routing parity without fresh evidence from that platform.
- A public marketing website is not required for this repair; any future public release remains an owner decision.

## Requirements

| ID | Requirement | Boundary | Acceptance | Proof |
|---|---|---|---|---|
| REQ-001 | Every cataloged package has exactly one canonical instruction body. | Aliases and vendor adapters may add routing metadata but may not duplicate behavior. | Catalog entries, canonical directories, and aliases resolve one-to-one with no unlisted package. | `catalog.json`; `scripts/validate`; `tests/test_core_composition_contracts.py` |
| REQ-002 | Every promoted package and promoted alias has a managed link in each configured local discovery root. | Pilot packages remain in the repository for review and are not installed. Existing non-link files or directories are never overwritten. A link does not prove runtime loading or automatic model selection. | Install completes; doctor reports the expected counts with zero missing, collision, broken, wrong-target, or unexpected managed links. | `scripts/install`; `scripts/doctor` |
| REQ-003 | A human can find every canonical skill, its lifecycle, invocation, use case, result, boundary, aliases, and common composition from one handbook. | The handbook summarizes and links; each `SKILL.md` remains the behavioral authority. | `README.md` links the handbook and the handbook coverage test matches `catalog.json`. | `docs/SKILLS.md`; `tests/test_skill_handbook.py` |
| REQ-004 | New names, aliases, framework hierarchies, and promotion states pass the Candidate Card lifecycle. | General authority to improve the repository is not approval of a candidate's exact name or ontology. | A candidate remains pilot and uninstalled until exact owner approval, cross-case evidence, and a legitimate counter-case pass. | `tests/test_portfolio_lifecycle.py`; `tests/behavioral-cases.md` |
| REQ-005 | Install and update fail before changing the active system when validation, Git state, or ancestry is unsafe. | No GitHub Actions or paid runner is required. Local implementation authority does not imply unrelated external publication. | Dirty updates fail; fetched candidates validate before fast-forward; pre-commit and pre-push run the full validator. | `scripts/update`; `.githooks`; `tests/test_update_preflight.py` |
| REQ-006 | JamesSkills applies its own project-standard contract and cannot release while that contract is structurally unready. | Routine skill edits update only the owner documents whose truth changed. | The four minimum contract files exist, agree on requirement IDs, and `scripts/validate` runs the ready gate. | `PROJECT.md`; `STATUS.md`; `AGENTS.md`; `docs/DECISIONS.md`; `scripts/validate` |
| REQ-007 | Every release screens repository content for machine-specific paths, credential assignments, private keys, and reviewed-source boundary violations. | Client data, live state, and unreviewed copyrighted originals remain prohibited. Automated patterns cannot prove semantic absence of every sensitive fact, so human diff review remains required. | Every tracked or non-ignored candidate text file passes the repository boundary scan; knowledge-library provenance and misuse tests pass; release review finds no prohibited content. | `scripts/check_repository_boundary.py`; `tests/test_repo_content_boundary.py`; `skills/core/baseon/tests/test_baseon.py`; reviewed release diff |
| REQ-008 | Promoted skill behavior and every durable correction have representative success, same-mechanism failure, and legitimate counter-case evidence. | Deterministic contracts do not prove that every model vendor will select and follow a skill in a fresh session. Cross-platform parity is claimed only with exact platform receipts. | Package and portfolio behavior tests pass; stronger platform claims name the target and its fresh evidence. | `tests/behavioral-cases.md`; `tests/test_core_composition_contracts.py`; `scripts/validate` |
| REQ-009 | The transformation-design portfolio exposes three stable responsibilities: reusable house frameworks, macro transformation journeys, and bounded learning experiences. | V1 excludes an organization application, employee rollout, client portal, public API, and multi-role approval workflow. External research supports house frameworks and every material claim remains cited. | All three canonical skills are promoted, installed, source-bounded, connected through stable contracts, and produce purpose-specific HTML templates that pass behavior and visual gates. | `skills/core/build-framework`; `skills/core/transformation-journey`; `skills/core/learning-experience-design`; `packs/frameworks/registry.json`; `tests/test_learning_design_contracts.py`; `tests/test_learning_design_output_contracts.py` |

## System boundaries

- Data: Git-tracked Markdown, JSON, scripts, tests, templates, reviewed packs, and local discovery symlinks. There is no application database.
- Permissions: repository-local edits and tests are ordinary work; install changes managed discovery links and this checkout's local Git hook configuration; external publication follows the accepted repository release authority.
- Integrations: private GitHub origin plus local skill discovery directories for Codex, Claude Code, Gemini, and Google Antigravity.
- External actions: the installer may create or refresh managed symlinks and local Git hooks; it must not overwrite unrelated real files or directories.
- Failure behavior: dirty work, non-fast-forward ancestry, or failed candidate validation stops update before the checkout moves. Validation failures stop install before managed links change. Doctor reports post-install link failures but does not roll back the checkout or links automatically.

## Need decision

- Future public hosting or publication of any repository subset remains an owner decision.
