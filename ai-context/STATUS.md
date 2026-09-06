# Status

Last verified: 2026-09-07
Authority: `ai-context/PROJECT.md`
Spec lock: Open
Current version: 2.0.3 candidate
Current branch: main
Repository: public `theeranon/JamesSkills`

## Current outcome

The whole 22-skill upgrade pass is complete and release candidate 2.0.3 is ready.
Compared with 98433f6, 13 instruction bodies were updated; 9 were retained,
including 4 candidates rejected after comparison. Every skill has three new
responsibility/transfer/countercase probes and a recorded disposition. Retained
does not mean every response is flawless; improvements are bounded by evidence.

All 44 local Claude/Codex native bodies match the selected canonical bodies.
Native package metadata is 2.0.2 pending publication/update of 2.0.3. Three Mac
CLIs returned all nine package smoke requests; one Claude code-only response
still appends a short verification note. No universal formatting parity is claimed.

## Done

- 66 new probes across all 22 skills; 117 primary calls, 116 responses and 1 timeout retained. The declared paired recovery returned 2/2.
- Independent cross-group blinded review of all primary responses; per-skill acceptance/rejection decisions retained. No overall efficacy percentage.
- Six real filesystem forward cases plus two targeted retries: done-for-me created/repaired all requested files and preserved unrelated work; never-again executed lesson/pointer repairs and kept draft-only requests non-mutating. A generated draft example still has a semantic limit.
- Four rejected candidates restored after concurrent d6f12c2 publication installed them. Native target changes were detected before writes; owned bodies restored with backups.
- Benchmark CLI supports replaying the new suite with --case-file. Original fixtures and failures remain intact.

## In progress

- Canonical 2.0.3, validated package and export are prepared locally. Exact GitHub publication authorization for the corrective release is the remaining owner gate.
- Existing shared discovery links use the canonical bodies. A remote marketplace update can overwrite local native patches until 2.0.3 is published and installed normally.

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

- Publish the reviewed 2.0.3 corrective release to the existing GitHub repository when authorized, refresh native packages, and verify exact remote/local revision and body hashes.

## Blockers

- No local implementation blocker. Publication and normal marketplace refresh await the target-specific owner decision below.

## Need decision

- Publish corrective 2.0.3 to the existing theeranon/JamesSkills GitHub main branch, then refresh native packages.

## Verification limits

- Response probes do not prove full multi-turn behavior, rendered artifacts, automatic routing, Windows or cloud-account parity.
- Residual generated factual and formatting errors are recorded per skill; discarded candidates are not shipped merely to increase a score or changed-file count.
- Current evidence: `tests/receipts/portfolio-upgrade-2026-09-07/REVIEW.md` and `dispositions.json`.
