# First authenticated development run

Date: 2026-09-06. Base: 59cd9af plus documented local status changes. Canonical instructions unchanged. Source fixtures and instruction hashes in aggregate.json preserve run identity.

## Execution

41/41 calls returned: 2 smoke, 30 baseline (15 cases × A/B), 9 candidate (3 cases × A/B/C). Claude Code 2.1.220, low effort, no tools, safe-mode, no session persistence, forced instruction injection. Every call reports claude-sonnet-5 plus auxiliary claude-haiku-4-5-20251001 usage. Provider-reported aggregate cost USD 0.2738247; this is metered usage, not a claim about subscription billing. Cache conditions vary, so latency/cost comparisons are exploratory.

A = no tested instruction; B = frozen current instruction; C = temporary proactive-habits candidate. This does not measure native skill discovery, multi-turn persistence, rendering or file execution.

## Review method and limits

The root assistant inspected all returned outputs against the public rubrics, with conditions visible. This is an unblinded diagnostic review, NOT independent human review or a calibrated quality score. Original runner states remain awaiting_human_review or necessary_checks_failed. One response per condition/case is insufficient for generalization. No sealed holdout was used. Exact raw responses stay outside Git because a baseline response spontaneously included the signed-in account's contact address. The account identity is not evidence supplied by the task; do not publish it or credit it as a correct contact.

## Findings by responsibility

| Skill | Observed result | Decision |
|---|---|---|
| proactive-habits | Current B adds a separate decision/offer about the irrelevant notification platform and learning strategy in both relevant cases. The real choice case retains two windows and a question. | Diagnose decision-queue overreach; do not treat all out-of-scope suggestions as user decisions. |
| done-for-me | Both arms return CSV and calculate 400; both introduce an unspecified dollar currency in the total case. Reconciliation retains unmatched B/payment, though B calls the invoice unpaid/outstanding instead of simply unresolved. | No demonstrated uplift; tighten truth review before editing. |
| make-it-james | Both arms preserve main facts and exact quotation. Both reorder 30 November to November 30. | Equivalent dates are a checker defect, not a quality failure. No demonstrated uplift. |
| sum-meet | Both preserve final budget, unresolved ownership, and Lin's informal commitment. B is more elaborate; both describe L1 approval as a proposal in the injected-notes case. | Main evidence tasks succeed; detail is not automatically better. No demonstrated uplift. |
| hand-it-off | Both choose the expected owner for all three explicit routing probes. | These probes cannot separate current skill from baseline; no uplift claim. |

## Candidate rejected

The temporary candidate changes only relevance filtering and conditional final questions (patch attached). It still brings up the notification platform and learning strategy in both cases. It preserves the genuine window question, but additionally recommends the later window based on assumed user activity. Reject this candidate for promotion: it does not fix the targeted mechanism, and introduces an unsupported recommendation. Keep canonical body and installed versions unchanged.

Next candidate should reconcile ALL unconditional queue/hand-back wording rather than append another rule. Evaluate against new task families and cases where an external decision is genuinely required; do not repeatedly optimize against these three public examples alone.

## Checker correction

Original baseline: 28 necessary-check passes, 2 failures. Both failures were the same semantic date expressed as November 30. After inspecting the outputs, added declared equivalent-form literal checks and regression tests: rejected date order, same mechanism on a second date, wrong-date rejection, and exact-quote counter-case. Historical run counts/hashes remain unchanged. This post-hoc checker correction is not a new model run, a model improvement, or a 100% quality pass.

## Retained evidence

aggregate.json contains response hashes, instruction hashes, original statuses and exact raw-log hashes. rejected-candidate.patch reproduces the tested change. Raw logs remain in the local temporary run directory; they are not a durable public artifact and may expire. No credentials or account contact details are committed. No public release performed.
