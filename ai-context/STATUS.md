# Status

Last verified: 2026-09-05
Authority: `ai-context/PROJECT.md`
Spec lock: Open
Current version: 2.0.0
Current branch: main
Repository: private `theeranon/JamesSkills`

## Current outcome

JamesSkills v2 carries 22 promoted canonical packages and 8 compatibility aliases, every one rewritten against a single structural contract in `docs/SKILL-SCHEMA.md` and enforced by `tests/test_skill_schema.py`. Each skill declares its kind, its bounded job, the siblings that own its excluded cases, its stop condition, its named principles with attribution, and at least one counter-case. The boundary graph passes with in-degree at least one for every skill, meaning no skill's job is left unclaimed by the exclusions of its peers. Discovery links are healthy in all five configured roots.

## Done

- `docs/SKILL-SCHEMA.md` defines the mandatory shape for every `SKILL.md`; `tests/test_skill_schema.py` enforces it inside `scripts/validate`.
- All 22 canonical skills were rewritten to the owner's own definitions, captured in a decision interview on 2026-09-05.
- `are-you-sure` split into a business track and `dev-are-you-sure` for software; `prove-it` was renamed `research-it` with `prove-it` kept as an alias.
- `tests/behavioral-cases.md` now covers all 22 packages; the seven skills that previously had no case have one.
- `scripts/validate` was scanning the empty `skills/` directory after the plugin migration, so 7 per-skill test files and 3 HTML asset lints had not run. Paths corrected; a real failure in `test_baseon.py` surfaced and was fixed.
- `scripts/doctor` was checking pre-migration link paths and did not understand the plugin layout used for Gemini and Antigravity. Corrected; all five roots now report zero issues.
- `project_standard.py` stamps `project-standard/1.0` into every generated SRS and into `check` output, so a project states which standard version it follows.
- `catchup` gained a fixed A4 landscape report template so every project's catchup page looks identical.

## In progress

- None in the 0.9.0 implementation scope.

## Requirement state

| ID | Current state | Evidence | Last verified |
|---|---|---|---|
| REQ-001 | Verified | Catalog, canonical path, alias, composition, and portable-structure gates passed in the full 0.9.0 validation. | 2026-08-29 |
| REQ-002 | Verified | Doctor reported every promoted canonical and alias link with zero missing, collision, broken, wrong-target, or unexpected links in all five configured discovery roots; runtime loading is separately tested and not assumed from links. | 2026-08-29 |
| REQ-003 | Verified | Handbook coverage test passed for 17 canonical packages and 10 aliases. | 2026-08-29 |
| REQ-004 | Verified | Candidate lifecycle and anti-overfit regression suite passed in the full 0.9.0 validation. | 2026-08-29 |
| REQ-005 | Verified | Detached-candidate update test passed; doctor confirmed local pre-commit and pre-push gates are installed. | 2026-08-29 |
| REQ-006 | Verified | Minimum owner files and the self-standard regression passed; `scripts/validate` runs `check --ready`. | 2026-08-29 |
| REQ-007 | Verified | Repository-wide candidate text scan, knowledge provenance, source misuse gates, and release diff review passed. Pattern detection remains a guard, not an impossibility proof. | 2026-08-29 |
| REQ-008 | Verified | Package and portfolio behavior contracts, rejected cases, same-mechanism cases, and legitimate counter-cases passed; universal platform parity remains unclaimed. | 2026-08-29 |

## Next

- Decide whether the schema contract earns its own numbered requirement in `PROJECT.md`; it is currently recorded as a non-functional requirement.

## Blockers

- None.

## Need decision

- A public name for `skill-router` remains unapproved; it stays internal support.
- `Satir Model` is recorded as `coach-me`'s coaching lens with `Satya` kept as an alternate spelling in the locator; its provenance card is not yet registered in `packs/knowledge`.
- Fresh-session behavioral parity on every supported AI platform remains unproved.
- Public hosting or release of any repository subset remains unapproved.

## Verification

- Baseline commit before this repair: `7edcb0c0dd718bd84fb72628e164e2a7a2ebc115`.
- Current contract owner files: `ai-context/PROJECT.md`, `ai-context/STATUS.md`, `AGENTS.md`, and `ai-context/DECISIONS.md`.
- `project-standard` (v2): every contract file except `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`README.md` now lives under `ai-context/`; this repository's own layout was migrated in the same change so `scripts/validate` keeps passing against the skill it ships.
- Full 0.9.0 validation passed for 27 packages, including repository boundaries, project readiness, framework registry, routing, behavior, source provenance, update safety, and strict output lint.
- Forward rendering passed for three reports across two real project cases: four embedded IBM Plex Sans Thai weights, zero unresolved tokens, zero remote requests, zero horizontal overflow, desktop and 390px mobile fit, and browser print-media fit. No PDF was generated.
- Doctor passed with Git gates installed and 17 canonical plus 10 alias links in each configured discovery root; missing, collision, broken, wrong-target, and unexpected links are zero.
- Runtime receipt: `tests/receipts/runtime-routing-v0.9.0.md`; Codex implicit 3/3 and explicit behavior passed, Claude implicit 3/3 and isolated explicit reruns 2/2 passed. One earlier Claude parallel label mismatch remains recorded as a low-severity stochastic warning.
- Commit and push evidence are recorded by Git after this status snapshot rather than predicted here.
