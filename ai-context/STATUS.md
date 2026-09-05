# Status

Last verified: 2026-09-05
Authority: `ai-context/PROJECT.md`
Spec lock: Open
Current version: 2.0.0
Current branch: main
Repository: public `theeranon/JamesSkills`

## Current outcome

22 promoted canonical skills and 9 aliases. The local installer repair resolves
Codex native/shared duplicate loading and preserves existing unrelated files.
Full validation passes. The local Codex app-server now reports 22 enabled canonical
skills with no repeated names. Desktop picker confirmation remains open.

## Done

- Reproduced 44 enabled skills after combining the published installer with native Codex plugins in an isolated user configuration.
- Repaired exact-path local overrides while preserving shared links for other agents; repeated candidate installation returns 22 enabled entries.
- Unified installer and doctor planning; collision preflight, promoted-only selection, per-skill Claude fallback, and mandatory validation replace unsafe behaviors.
- Fresh GitHub native installation succeeded in Codex CLI and Claude Code. Codex explicit installed-skill invocation and packaged knowledge helper passed.
- Updated install guidance to separate tested macOS outcomes from unverified platform claims.

## In progress

- Local candidate awaits publication authorization. Published baseline remains `51c776e97eb6bf8ce4a2e6a9b49d59931c431197` as checked during this repair.
- Codex Desktop picker must be checked after reopening/restart; Computer Use cannot access this app.

## Requirement state

| ID | Current state | Evidence | Last verified |
|---|---|---|---|
| REQ-001 | Verified locally | Catalog and canonical/alias validator: 22 + 9. | 2026-09-05 |
| REQ-002 | Filesystem and Codex API verified; other host runtimes open | Shared/native reconciliation, managed-link plan, doctor; receipt below. | 2026-09-05 |
| REQ-003 | Verified locally | Handbook coverage gate. | 2026-09-05 |
| REQ-004 | Verified locally | Lifecycle gates plus installer pilot exclusion regression. | 2026-09-05 |
| REQ-005 | Verified locally | Update preflight, collision and validation-failure regressions, Git hook configuration. | 2026-09-05 |
| REQ-006 | Verified locally | project-standard ready gate inside full validator. | 2026-09-05 |
| REQ-007 | Automated checks passed | Repository boundary and knowledge provenance gates; no universal semantic guarantee. | 2026-09-05 |
| REQ-008 | Local contracts and one fresh Codex invocation passed | Full validator, installer rejected/same-mechanism/counter-cases, explicit mode boundary smoke test. | 2026-09-05 |

## Next

- Owner: confirm the Codex Desktop picker no longer repeats the two reported names.
- Owner: authorize publishing the reviewed installer repair to the existing GitHub main target.

## Blockers

- Desktop UI proof cannot be collected through the available Computer Use tool.
- Windows, Cursor, Gemini, Antigravity and Claude Desktop runtimes were not verified in this repair. Filesystem checks are not substitutes.

## Need decision

- Publication of this local installer repair; vendor-run store listing remains a separate decision.
- Whether the schema contract needs a numbered requirement beyond its existing non-functional requirement.

## Verification

- Current receipt: `tests/receipts/install-discovery-2026-09-05.md`.
- Full validator passes for 31 packages; doctor checks managed links and actual Codex skill inventory.
- Earlier runtime evidence stays in `tests/receipts/runtime-routing-v0.9.0.md`; it is historical and does not establish current cross-platform parity.
- DEC-025 supersedes the incomplete duplicate fix in DEC-024. No release commit or publication is predicted by this status file.
