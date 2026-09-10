# Status

Last verified: 2026-09-10
Authority: `ai-context/PROJECT.md`
Spec lock: Open
Current version: 2.1.2 (local; distribution not verified)
Current branch: main
Repository: public `theeranon/JamesSkills`

## Current outcome

Grill Me conversational correction prepared locally at 2.1.2. Synthetic response probes cover immediate entry, answer-dependent followup, authorized drafting and trial-needed uncertainty. Invocation metadata and examples now match the canonical behavior. Evidence: `tests/receipts/grill-me-2026-09-10.md`. The separate skill shown in the owner's screenshot has not been inspected or replaced; historical distribution notes below do not establish this version's availability there.

Local wording-linter correction: technical namespace identifiers (snake_case namespace with a long ASCII token) no longer trigger Thai punctuation violations. Only the identifier token is exempt; adjacent prose punctuation remains checked. Synthetic same-mechanism and counter-case CLI probes plus scripts/validate passed. No installation, package publication or cross-platform behavior claimed.

Version 2.0.4 corrected composition and proportionality across all 22 skill bodies
(persistent modes survive one-task workflows; schema no longer forces routing
in-degree or minimum principle counts). 2.0.5 fixed two residual gaps from that
pass: `catchup`'s mislabeled Counter-case bullet and `one-page-pls`'s stale
`sum-meet` exclusion line. 2.0.6 is a full-history capability audit — every
distinct commit per skill was read, not just the first vs. current — which
found current HEAD had fixed a real bug in 12 skills while silently dropping
other, unrelated concrete instructions along the way; those instructions were
restored without reverting the fixes. Three skills (`hand-it-off`, `sum-meet`,
`project-standard`) had a genuinely better intermediate historical version;
its missing pieces were merged into HEAD's current structure. `coach-me` was
deliberately left as-is per an explicit owner decision (non-directive coaching
is the intended design, not a bug). `research-it` and `dev-are-you-sure`
required no content changes; the audit only found a naming/lineage note worth
recording (`research-it`'s real predecessor content lives in `dev-are-you-sure`,
not in `research-it` itself).

## Done

- All 22 audit findings from the 2.0.4 pass addressed in their instruction contracts; schema no longer requires routing in-degree or minimum principle counts.
- 2.0.5: fixed `catchup`'s Counter-case mislabeling and `one-page-pls`'s stale sibling-exclusion line — the two items left open after the 2.0.4 pass.
- 2.0.6: full commit-history capability audit of all 22 skills (not just v1-vs-current) verified directly against file content (grep, not agent trust). Restored verified-missing instructions in 12 skills (`hand-it-off`, `i-have-adhd`, `is-that-the-best-you-can-do` reviewed and left as intentional, `make-it-james`, `never-again`, `baseon`, `give-me-solutions`, `grill-me`, `sum-meet`, `zoom-out`, `catchup`, `proactive-dev`) while preserving every real bug fix already present. Added `scripts/export`: copies promoted skills as plain, committable files into any project's `.agents/skills/`, independent of any global plugin registry — a second, host-agnostic distribution mode alongside the existing symlink installer.
- Real two-turn artifact scenarios executed with baseline, candidate and no-skill arms. Completion and draft boundaries verified; no measured completion uplift claimed.
- 66 response-only forward probes reviewed, plus strategic and output followups. Residual factual/formatting failures retained, not labeled passes.
- Published through 2.0.6 (commit `be49e6d`) to the approved GitHub main branch. `installed_plugins.json` and the Codex app-server inventory both confirmed matching that commit on this machine.
- Evidence: `tests/receipts/composition-upgrade-2026-09-07/REVIEW.md`, `installation.json`, and this conversation's own verification greps (not yet written to a receipt file — see Next).

## In progress

- No publication or installation work remains on this machine. A long-running Claude Code Desktop session must be fully quit and reopened (not just a new tab) to pick up 2.0.6 — the plugin cache is read once per app launch, not hot-reloaded.
- The 2.0.6 restoration work was verified by direct grep against each file, not written up as a dated receipt document the way earlier rounds were. Worth doing if this needs to be re-justified later without replaying this conversation.

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

- Owner must fully quit and reopen Claude Desktop, then retry a skill (e.g. `/are-you-sure` or a plain-language request), to confirm the real fix from DEC-037/LESSON-015: Claude Desktop's own bundled Claude Code binary had never registered the `james-skills` marketplace (`plugin list` showed "failed to load"), separate from the Homebrew CLI this session had been managing all along. Fixed live via `plugin marketplace add`/`plugin install` against that exact binary; `plugin list` now shows `✔ enabled` for all three. DEC-036's earlier "confirmed working" claim was a false positive (the model improvising from request text, not a loaded skill) — retracted, do not cite it as resolved.
- The bare-skill-name syntax fact itself (`/are-you-sure`, no plugin prefix) remains correct per `claude --help`, independent of the DEC-037 fix — README documents both.
- Use 2.1.0 with the documented model-output limitations; collect real failures without adding speculative rules.
- Optional: write a dated receipt for the 2.0.6 capability-restoration audit (git log --follow evidence, before/after quotes) matching the format of earlier receipts, if this decision needs to be replayed without this conversation's history.

## Blockers

- None for publication or installation.

## Need decision

- None for this release; owner authorized publication and installation in this conversation.

## Verification limits

- Response probes do not prove full multi-turn behavior, rendered artifacts, automatic routing, Windows or cloud-account parity.
- Residual generated factual and formatting errors are recorded per skill; discarded candidates are not shipped merely to increase a score or changed-file count.
- The 2.0.6 restoration is a file-content audit (does the instruction exist and read coherently), not a behavioral benchmark; whether the restored instructions change real model behavior in a live conversation is unverified.
- Current evidence: `tests/receipts/portfolio-upgrade-2026-09-07/REVIEW.md` and `dispositions.json`.
