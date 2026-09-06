# Research-it improvement decision

## Outcome

Do not promote the candidate. The original instruction remains installed and canonical. This is a completed diagnostic comparison, not a delivered behavioral fix.

The ceiling was a correct evidence verdict with logically valid reversal conditions, without unsupported evidence details or unnecessary work. The earlier baseline's Nimbus response had a correct present verdict but an invalid reversal condition: one successful export would soften a universal claim already refuted by a valid failure. Describe that as a mixed answer, not an entirely wrong verdict.

## Comparison

One candidate changed only procedure step 7: preserve claim scope, distinguish invalid counterexamples from later successes, evaluate changed versions separately, and distinguish occurrence from frequency. Inputs and body hashes were frozen before execution. Three existing cases and five independently authored fresh cases received current/candidate pairs, shuffled within each case. All 16 planned calls returned; no retries or failed outcomes were dropped.

An independent assistant reviewed shuffled responses without the condition key. A second assistant independently checked practical factual defects. These are assistant judgments, not calibrated human scores. The five new cases were authored with the mechanism disclosed, before candidate inspection; they are development cases, not sealed holdouts.

| Dimension | Current B | Candidate C |
|---|---|---|
| Logic | 4 pass, 3 fail, 1 uncertain | 7 pass, 1 fail |
| Truth | 2 pass, 4 fail, 2 uncertain | 3 pass, 3 fail, 2 uncertain |
| Proportionality | 7 pass, 1 fail | 7 pass, 1 fail |

The candidate still fails the original Nimbus case: its reversal condition silently substitutes the sales page's possible narrower scope for the original universal claim and leaves the manual's omission unresolved. Both arms also invent some evidence-ledger details, including source independence, timing, or tested input coverage. The candidate's better aggregate logic score does not satisfy the rejected-case regression. No canonical edit, installation, version bump or publication follows.

## Evaluation fairness and next useful work

Judge the entire answer, including reversal conditions, while retaining credit for its correct present verdict. Do not penalize hypothetical caveats as asserted facts, a rejected illustrative percentage as an estimated rate, or headings merely for existing. Separate unsupported claims from insufficiently specified provenance. Do not treat one-shot supplied-evidence tasks as proof of live research or persistent behavior.

Next improvement should address the actual pressure to fill mandatory evidence fields and invent a reversal condition. It needs a revised candidate that passes the original case plus fresh source-provenance and legitimate-revision cases. Another rewrite optimized on these same eight cases would weaken the generalization claim. No numeric uplift for the whole skill or portfolio is established.

## Reproduction boundary

Base revision: 0ce2f74. Current body is that revision's research-it/SKILL.md; rejected-candidate.patch reconstructs the candidate. cases.json, run.json, responses.jsonl, review.json and key.json preserve the inputs, schedule, hashes, provider metadata and judgments. Execution used scripts/benchmark.py invoke with scripts/benchmark_claude.py, a 120-second adapter deadline, two concurrent calls, fresh working directories and no tools. Each payload contained the frozen instruction, empty context and the case prompt. Neither arm was a native-discovery test; no no-skill arm was rerun here.
