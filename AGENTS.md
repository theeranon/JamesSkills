# JamesSkills Maintainer Rules

- One canonical instruction body per skill. Vendor adapters may add metadata, never duplicate behavior.
- Keep every promoted package in `catalog.json`. Category determines responsibility; aliases provide migration only.
- Name skills from the natural phrase a person uses at the moment they need the capability. Name the mental move, not an internal department.
- A workflow skill completes one bounded job. A mode skill changes behavior for the remainder of the conversation after one activation.
- A shared standard applies automatically. An output skill owns artifact semantics and consumes the shared standard instead of copying it.
- Skills contain reusable process knowledge. Never commit credentials, client data, chat exports, live status, or JamesOS databases.
- Treat a book, paper, course, or proprietary report as a source before considering a new lens. Do not create one skill per source.
- Keep copyrighted originals outside Git by default. Commit source identity, rights posture, hash, locators, original paraphrase, applications, and limitations.
- Separate source claims, independent evidence, James rules, and inference. Never promote an inferred profile to an official result.
- A direct correction from James is evidence to investigate. Promote it to a global rule only when the intended scope is durable.
- Every behavioral correction requires a regression case before release.
- Release on the shortest critical path: usable package, minimum required proof, install or delivery, then commit and push. Optional audits, documentation cleanup, and extra hardening must not delay the first usable outcome.
- Run `scripts/validate` and `scripts/doctor` before declaring a release usable.
- Do not claim cross-platform support without discovery and outcome evidence on that platform.
