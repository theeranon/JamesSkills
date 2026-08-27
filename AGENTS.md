# JamesSkills Maintainer Rules

- One canonical instruction body per skill. Vendor adapters may add metadata, never duplicate behavior.
- Name skills from the natural phrase a person uses at the moment they need the capability. Name the mental move, not an internal department.
- A workflow skill completes one bounded job. A mode skill changes behavior for the remainder of the conversation after one activation.
- Skills contain reusable process knowledge. Never commit credentials, client data, chat exports, live status, or JamesOS databases.
- A direct correction from James is evidence to investigate. Promote it to a global rule only when the intended scope is durable.
- Every behavioral correction requires a regression case before release.
- Run `scripts/validate` and `scripts/doctor` before declaring a release usable.
- Do not claim cross-platform support without discovery and outcome evidence on that platform.
