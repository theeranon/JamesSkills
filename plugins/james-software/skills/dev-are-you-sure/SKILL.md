---
name: dev-are-you-sure
kind: workflow
license: CC-BY-NC-4.0
description: Re-inspect delivered software with checks matched to its risks and repair findings inside a declared surface. Use when code looks done but the diligence is in doubt; not for business artifacts and not for external claims.
---

# Dev Are You Sure

Recheck the delivered behavior and its evidence, then repair the defects you can substantiate.

## Scope

- Kind: workflow
- Owns: one delivered software surface — code, schema, data, configuration, interface, or deployment — inspected across relevant layers and boundaries, repaired in place.
- Boundary: declare the inspection surface before starting, normally the files changed in this task, and name it in the output. Repair only inside it. Anything outside is reported, never edited, renamed, or deleted.

## Do not use this when

- The artifact is a plan, document, model, or business decision -> `are-you-sure`
- The doubt is whether an outside approach or library claim is sound -> `research-it`
- The code is correct and clean but the solution is mediocre -> `is-that-the-best-you-can-do`
- One rejected output must become a permanent rule across the project -> `never-again`
- The feature is simply unfinished -> `done-for-me`
- Planning and role decomposition are needed before any code is written -> `proactive-dev`

## Procedure

Establish the requested surface and choose checks that could reveal a material defect. For a full audit, cover all five layers and all boundary links, marking genuinely irrelevant checks not applicable. A small local change needs relevant checks, not nine mandatory report sections. Repair inside the surface; escalate what needs a decision.

1. **Integrity.** For stateful flows, exercise sequential use: navigate away and back, act twice, act while loading, act after failure. Trace how each transition preserves its invariant through explicit state, derived values, framework lifecycle or stateless design. An absent reset statement is not evidence of a defect; establish an incorrect reachable behavior before prescribing a reset.
2. **Architecture.** Find hardcoded values, secrets, magic numbers, credentials in source, and logic sitting in the wrong layer. Convert missing configuration into an explicit input contract rather than a plausible default.
3. **Hygiene.** Remove debug output, commented-out blocks, dead branches, unused imports, orphaned variables, and scratch filenames that would be read as intentional by whoever inherits this.
4. **Interface.** Apply the installed visual and interaction standard rather than restating it here. Report anything that standard forbids and cannot be fixed inside the surface.
5. **Longevity.** Inspect plausible compatibility and maintenance risks exposed by this change. Distinguish demonstrated defects from uncertain future risks; use names understandable without this conversation.

For claims that cross systems or concern deployment, walk the relevant boundary chain and mark each applicable link passed, failed or not tested: local source and stored state; provider or API boundary with an authenticated receipt; the real user journey including permissions and persistence; and the deployed identity, version, and recipient-visible result. Evidence from one target never transfers to another.

## Stop when

The requested surface has received the relevant checks, every repairable finding is repaired and rechecked, and material remaining gaps identify the needed evidence or owner. A full audit also accounts for every layer and boundary, including not-applicable ones. Untested is reported as untested and never collapsed into done.

## Principles

**Testing shows presence, not absence** — A passing suite is evidence that known cases work and is never evidence that the omission you are hunting is absent. Source: Edsger W. Dijkstra, Notes on Structured Programming, 1970
**Swiss cheese model** — Use complementary checks for the risks in scope, because a clean result at one layer cannot establish correctness at another. Source: James Reason, Human Error, 1990
**Poka-yoke** — When a defect can recur, prefer changing the design so it becomes impossible over adding another check that must be remembered. Source: Shigeo Shingo, Zero Quality Control, 1986
**Proof does not transfer across targets** — Bind every result to its repository, revision, environment, account, and route, and treat a result from any other target as absent. Source: uncertain attribution; standing rule in this library

## Counter-case

- The user asks whether a five-year business plan holds together. Same five-layer instinct, but the layers are business layers, so `are-you-sure` owns it.
- The user asks the agent to plan and build a new service with proper role decomposition. Nothing exists to inspect yet, so `proactive-dev` owns it.

- A pure formatter has no state-reset statement and produces the correct result on repeated calls. Leave it stateless; do not manufacture a reset defect.
- An asynchronous order action can run twice while pending. Exercise the duplicate request path and repair the violated order invariant rather than merely adding a visual reset.

## Hand back

The repaired outcome, checks actually performed, and material unresolved findings with the evidence still needed. Include the complete layer/boundary inventory when a full audit was requested; keep inspection notes internal for a code-only response.

## Sources

Dijkstra 1970, Notes on Structured Programming. Reason 1990, Human Error. Shingo 1986, Zero Quality Control: Source Inspection and the Poka-yoke System.
