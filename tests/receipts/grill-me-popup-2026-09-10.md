# Grill Me native-question correction

Date: 2026-09-10. REQ-008. Supersedes the sufficiency claim of the earlier text-only probe, not its recorded outputs.

## Source and failure

The author read the AIHero article in the first revision but did not then inspect its delegated implementation. Current upstream files were fetched and read in this correction: skills/productivity/grill-me/SKILL.md delegates to skills/productivity/grilling/SKILL.md in mattpocock/skills. The latter specifies text rounds and recommendations. Single native popups with choices are the owner's explicit James requirement. No upstream popup guarantee is claimed.

Rejected mechanism: a well-phrased chat question passed a response-only probe while the required native question call was missing. The 2.1.2 metadata also no longer requested choices.

## Independent tool-selection simulations

An independent agent read the candidate and a synthetic host contract without earlier receipts. It returned proposed calls, without executing them.

A: replacement-system opening. Selected request_user_input_async, one questions entry, three distinct selectable directions, rather than Plan-only request_user_input in Default mode. Question: which aspect should improve first? Choices: next-work visibility, handoff/progress, repeated data entry. Pass selection/payload only.

B: workshop transfer concern selected by the user. Next native call asks where independent learners get stuck: starting, midway, or checking their result. Pass answer-dependent followup with choices, without asserting a diagnosed cause.

C: no native tool. Explicit limitation plus lettered choices and free text. Pass fallback, no fabricated call.

D: settled goal and instruction to draft. Produces a 60-minute outline without further questions. Pass proceed boundary; synthetic prompt lacks the concrete workshop topic.

E: async call accepted but no user reply. Wait, no default adoption or additional popup. Pass pending-input boundary.

F: explicit text-only preference. Uses chat choices. Pass legitimate override.

These are tool-selection simulations, not executed installed-skill tool traces.

## Actual current-host check

The root agent called functions.request_user_input_async with one Thai verification question and two choices. Tool result: accepted=true. This proves the current host accepted a native-question request. It does not prove the user saw the intended rendering or that a fresh installed-skill invocation selected the tool automatically. A user response, if received, is separate evidence.

## Release checks

Full repository validate, install and doctor are required before release completion. Their outputs establish structural and discovery state only. No other host's native UI behavior is inferred.

## Are-you-sure review

Reviewed 2026-09-10 after release. Canonical procedure, native invocation metadata and command adapter agree on the interview requirement. Repaired one stale regression criterion: proposing choices is required; asserting a diagnosis from those choices is the rejected behavior. No skill-body change was needed.

Release evidence from the preceding run: scripts/validate, scripts/install and scripts/doctor exited successfully; Codex skills/list showed the canonical path enabled with the new popup-oriented default prompt. origin/main and HEAD both resolved to 0676c4687e2f23646ca6834f59e3d91251a3b111 before this documentation-only review.

The previously delivered standalone ZIP was version 2.1.2 and is superseded by a 2.1.3 ZIP whose six members were byte-compared with the canonical skill directory. Old versioned download remains for provenance, not as the current deliverable.

Attempted native app visual inspection through the supported computer-use tool. It refused access to com.openai.codex for safety reasons. No bypass attempted. The earlier native-question call's accepted=true remains request-acceptance proof only. A fresh skill invocation, visible question rendering, a real selected answer and the dependent next question remain unverified. Do not report this release as end-to-end verified.
