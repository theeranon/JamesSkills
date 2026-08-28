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
- Authorization to build the library is not approval of a new skill name, domain boundary, framework hierarchy, alias, or promotion state. Keep a new candidate as `pilot` and uninstalled until James approves its Candidate Card.
- A Candidate Card must show the working name options, bounded job, trigger and exclusions, overlap with current skills, source map and confidence, representative requests, failure cases, and recommended lifecycle state.
- Promote only after cross-case evidence shows a reusable gap, nearby counter-cases show the rule is not overfit, and James approves the exact name and scope.
- Every behavioral correction requires a regression case before release.
- Release on the shortest critical path: usable package, minimum required proof, authorized install or delivery, then a local repository checkpoint. Push, deploy, publish, or send only when the request or accepted project contract authorizes that exact external target. Optional audits, documentation cleanup, and extra hardening must not delay the first usable outcome.
- Run `scripts/validate` and `scripts/doctor` before declaring a release usable.
- Do not claim cross-platform support without discovery and outcome evidence on that platform.
