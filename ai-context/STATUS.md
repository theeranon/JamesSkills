# Status

Last verified: 2026-09-06
Authority: `ai-context/PROJECT.md`
Spec lock: Open
Current version: 2.0.0
Current branch: main
Repository: public `theeranon/JamesSkills`

## Current outcome

22 promoted canonical skills and 9 aliases. Local install passes with 164 managed
links and 22 enabled Codex skills without duplicates. Coverage now rejects missing
inventories; owned changes roll back on tested failure paths. Claude Desktop shows
all 22 JamesSkills. Antigravity Customizations shows JamesSkills entries; full
invocation remains unverified.

## Done

- Added read-only installer plan, expected-skill coverage, transactional owned-link and Codex-override recovery, and per-skill pilot exclusion.
- Changed Claude marketplace refresh to update without uninstall-first; corrected its local-content claim.
- Added 22 benchmark cards and an A/B/C runner with 15 public probes for the five approved skills; 8 mechanics tests and 22 installer regressions pass.
- Added goal-alignment and proportionality criteria, including legitimate-complexity counter-cases. No canonical skill behavior changed.

## In progress

- Model benchmarking: Claude CLI authentication unavailable; two attempted calls returned no response. Public probes do not establish generalization.
- Cross-host invocation and cold-start proof beyond the existing Codex receipt remain open.

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

- Authenticate the Claude CLI benchmark route, run paired baseline, review outputs and diagnose one mechanism before a candidate rewrite.
- Verify explicit invocation in Antigravity and Claude Desktop; inspect Codex Desktop picker when accessible.

## Blockers

- Claude CLI is not authenticated; Desktop login does not supply its credentials.
- Computer Use cannot access Codex Desktop. Other OS/runtime parity remains unverified.

## Need decision

- Vendor-run store listing remains a separate decision.
- Whether the schema contract needs a numbered requirement beyond its existing non-functional requirement.

## Verification

- Current receipt: `tests/receipts/install-discovery-2026-09-06.md`; earlier explicit Codex invocation: `tests/receipts/install-discovery-2026-09-05.md`.
- Full validation runs benchmark mechanics and installer regressions automatically. Structural tests do not prove model quality.
- DEC-026 records approved benchmark direction; DEC-027 records local installation repair. No publication is claimed.
