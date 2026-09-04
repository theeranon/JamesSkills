---
name: are-you-sure
kind: workflow
description: Re-inspect a business or productivity deliverable across five layers and repair what it finds inside a declared surface. Use when work looks finished but the diligence behind it is in doubt; not for code, and not for making good work better.
---

# Are You Sure

Go back over what was just delivered and find what nobody would ever fail it on.

## Scope

- Kind: workflow
- Owns: one delivered business or productivity artifact — a plan, proposal, model, analysis, document, deck, budget, process, or decision — swept across five layers and repaired in place.
- Boundary: declare the inspection surface before starting and name it in the output. Repair only inside that surface. Anything outside it is reported, never edited.

## Do not use this when

- The artifact is code, schema, data, or a deployment -> `dev-are-you-sure`
- The doubt is about an outside claim rather than work produced here -> `research-it`
- The work is correct and clean but unambitious, and needs a higher ceiling -> `is-that-the-best-you-can-do`
- One rejected output must become a permanent guard against a whole failure class -> `never-again`
- The work is simply unfinished and must be carried to a usable outcome -> `done-for-me`
- The artifact is clean but answers the wrong question at the wrong level -> `zoom-out`

## Procedure

Declare the surface first: the exact artifact or set of artifacts under inspection. Then sweep all five layers in order. Repair each finding immediately, or escalate it when repair needs a decision you do not hold.

1. **Integrity.** Trace the logic end to end. Reconcile every number to a named source. Name the assumption that, if wrong, collapses the rest, and state what happens then. Find the cascading failure, not the typo.
2. **Structure.** Find what is one-off that should be repeatable, what sits at the wrong altitude, what commitment has no owner, and what decision is being made by a document instead of a person.
3. **Residue.** Remove placeholders, stale dates, draft figures, unresolved TBDs, copied requirement language, and contradictions between two sections that were written at different times.
4. **Recipient.** Read it as the person who receives it. Every question they would have to ask before acting is a defect. Apply the installed wording standard rather than restating it here.
5. **Longevity.** State what makes this expire, who owns it after handover, and what event should trigger a review.

Report every layer as repaired, escalated, or clean. Never report a layer you did not run.

## Stop when

All five layers have been run against the declared surface, every finding is repaired or escalated with a named owner, and the report states the surface inspected. A layer with nothing to fix is reported as clean, which is a result, not a skip.

## Principles

**Premortem** — Assume the deliverable has already failed badly, then work backwards to the cause; this surfaces defects that forward review consistently misses. Source: Gary Klein, Performing a Project Premortem, Harvard Business Review, 2007
**Swiss cheese model** — Treat every layer as porous and run all five, because defects survive precisely where one layer's blind spot lines up with another's. Source: James Reason, Human Error, 1990
**Chesterton's fence** — Do not remove anything whose purpose you cannot explain; ask why it is there before deleting it as residue. Source: G. K. Chesterton, The Thing, 1929
**Goodhart's law** — Distrust any number in the artifact that is also a target someone is measured on, and trace it to the behaviour it now rewards. Source: Charles Goodhart, 1975, as generalised by Marilyn Strathern, 1997

## Counter-case

- The user asks to sweep a React dashboard for leftover debug output and hardcoded values. The mental move is identical but the layers are software layers, so `dev-are-you-sure` owns it.
- The user asks whether a competitor's pricing claim is true. Nothing produced here is in doubt, so `research-it` owns it.

## Hand back

The declared inspection surface, each of the five layers marked repaired, escalated, or clean, the repaired artifact itself, and any escalation with the decision it needs and who holds it.

## Sources

Klein 2007, Performing a Project Premortem. Reason 1990, Human Error. Chesterton 1929, The Thing. Goodhart 1975, Monetary Relationships; Strathern 1997, Improving Ratings.
