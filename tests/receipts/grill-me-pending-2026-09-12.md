# Async interview waiting and recovery

Date: 2026-09-12. REQ-008. Version 2.1.8.

Observed actual reported turns through read-only local task records: each emitted request_user_input_async with one question and two options; both returned accepted=true. Each then emitted a final response, without a submitted answer. The second, triggered by a status challenge, changed the question. This is actual call evidence, unlike earlier proposed-payload simulations. It does not establish why the app did not visibly render/preserve the question. No private transcript is reproduced here.

Independent forward simulation read the candidate with five scenarios:
- Accepted without answer: chose clock.sleep with 30000 ms, not final prose or a new question.
- Status challenge while pending: preserve decision, inspect state if available, continue waiting; do not pretend a state API exists.
- User explicitly reports missing popup: re-present same decision, with no claim of cancellation or proven visibility; wait afterward.
- Substantive answer plus qualifier: settle only what the complete answer supports, then advance.
- Explicit stop: end interview, no new question or wait; no unsupported cancellation claim.
All matched expected boundaries. These are simulated actions, not live rendering tests. The actual failed traces substantiate the lifecycle defect; the simulation does not prove reliable recovery on every host.

Full validate passed after canonical edit. Commit/install/doctor gates run for delivery. No changes or messages made in the user's business project.
