# JamesSkills Maintainer Rules

- One canonical instruction body per skill. Vendor adapters may add metadata, never duplicate behavior.
- Skills contain reusable process knowledge. Never commit credentials, client data, chat exports, live status, or JamesOS databases.
- A direct correction from James is evidence to investigate. Promote it to a global rule only when the intended scope is durable.
- Every behavioral correction requires a regression case before release.
- Run `scripts/validate` and `scripts/doctor` before declaring a release usable.
- Do not claim cross-platform support without discovery and outcome evidence on that platform.
