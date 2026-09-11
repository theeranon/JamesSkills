# Native route fallback evaluation

Date: 2026-09-11. REQ-008. Narrow correction under DEC-041.

Independent agent read the current canonical skill and four synthetic cases. It did not call real question tools.

- Rejected case: Plan-only request_user_input failed in Default mode, async route available. Selected request_user_input_async with one goal question and three distinct choices. Did not request a mode switch.
- Same-mechanism transfer: AskUserQuestion fails, second permitted native route exists. Selected schema inspection followed by the alternate native route; correctly declined to invent the unspecified API name/payload.
- Legitimate counter-case: no native route. Reported that limitation and asked one concise chat question. Higher-priority session instructions prohibited textual multiple choice, so the simulation properly honored that rather than asserting skill supremacy.
- Pending async answer: waits without a second popup or default adoption.

Actual current-turn request_user_input_async accepted one question about the owner's preferred interview depth, with three choices and host-provided free text. No user answer had arrived when this receipt was written; preferences were not inferred or saved. This is a live call acceptance, not a complete installed-skill behavioral test.

Validation: full repository validator passed after the canonical edit. Release commit and install gates re-run validation. No comparative reliability measurement or UI rendering guarantee is claimed. The improvement is specifically that one failed call no longer authorizes premature text fallback while another permitted route exists.
