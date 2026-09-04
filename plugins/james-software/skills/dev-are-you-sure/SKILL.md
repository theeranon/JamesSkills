---
name: dev-are-you-sure
kind: workflow
description: Re-inspect delivered software across five layers plus the deployment boundary and repair what it finds inside a declared surface. Use when code looks done but the diligence is in doubt; not for business artifacts and not for external claims.
---

# Dev Are You Sure

Go back through what you touched and find the defect no test will ever catch.

## Scope

- Kind: workflow
- Owns: one delivered software surface — code, schema, data, configuration, interface, or deployment — swept across five layers and the boundary chain, repaired in place.
- Boundary: declare the inspection surface before starting, normally the files changed in this task, and name it in the output. Repair only inside it. Anything outside is reported, never edited, renamed, or deleted.

## Do not use this when

- The artifact is a plan, document, model, or business decision -> `are-you-sure`
- The doubt is whether an outside approach or library claim is sound -> `research-it`
- The code is correct and clean but the solution is mediocre -> `is-that-the-best-you-can-do`
- One rejected output must become a permanent rule across the project -> `never-again`
- The feature is simply unfinished -> `done-for-me`
- Planning and role decomposition are needed before any code is written -> `proactive-dev`

## Procedure

Declare the surface, then sweep all five layers and the boundary chain. Repair inside the surface; escalate what needs a decision.

1. **Integrity.** Simulate sequential use, not just the happy path: navigate away and back, act twice, act while loading, act after failure. For each transition name the exact line that resets the state. If no such line exists, that is the defect.
2. **Architecture.** Find hardcoded values, secrets, magic numbers, credentials in source, and logic sitting in the wrong layer. Convert missing configuration into an explicit input contract rather than a plausible default.
3. **Hygiene.** Remove debug output, commented-out blocks, dead branches, unused imports, orphaned variables, and scratch filenames that would be read as intentional by whoever inherits this.
4. **Interface.** Apply the installed visual and interaction standard rather than restating it here. Report anything that standard forbids and cannot be fixed inside the surface.
5. **Longevity.** Name what breaks on the next dependency or platform update, and rename anything whose meaning depends on knowing this conversation.

Then walk the boundary chain and mark each link passed, failed, not tested, or not applicable: local source and stored state; provider or API boundary with an authenticated receipt; the real user journey including permissions and persistence; and the deployed identity, version, and recipient-visible result. Evidence from one target never transfers to another.

## Stop when

Five layers and four boundary links are each marked with a result against the declared surface, every repairable finding is repaired, and every remaining gap names its exact owner. Untested is reported as untested and never collapsed into done.

## Principles

**Testing shows presence, not absence** — A passing suite is evidence that known cases work and is never evidence that the omission you are hunting is absent. Source: Edsger W. Dijkstra, Notes on Structured Programming, 1970
**Swiss cheese model** — Run every layer even when an earlier one was clean, because defects survive exactly where two blind spots align. Source: James Reason, Human Error, 1990
**Poka-yoke** — When a defect can recur, prefer changing the design so it becomes impossible over adding another check that must be remembered. Source: Shigeo Shingo, Zero Quality Control, 1986
**Proof does not transfer across targets** — Bind every result to its repository, revision, environment, account, and route, and treat a result from any other target as absent. Source: uncertain attribution; standing rule in this library

## Counter-case

- The user asks whether a five-year business plan holds together. Same five-layer instinct, but the layers are business layers, so `are-you-sure` owns it.
- The user asks the agent to plan and build a new service with proper role decomposition. Nothing exists to inspect yet, so `proactive-dev` owns it.

## Hand back

The declared surface, five layers and four boundary links each marked, the repaired code, and every remaining gap with its owner and the exact evidence still missing.

## Sources

Dijkstra 1970, Notes on Structured Programming. Reason 1990, Human Error. Shingo 1986, Zero Quality Control: Source Inspection and the Poka-yoke System.
