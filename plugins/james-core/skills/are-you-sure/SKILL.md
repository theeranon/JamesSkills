---
name: are-you-sure
kind: workflow
license: CC-BY-NC-4.0
description: Re-inspect a business or productivity deliverable with checks matched to its risks and repair evidenced defects inside the requested surface. Use when work looks finished but the diligence behind it is in doubt; not for code, and not for making good work better.
---

# Are You Sure

Go back over what was just delivered and find defects that affect correctness or usefulness.

## Scope

- Kind: workflow
- Owns: one delivered business or productivity artifact — a plan, proposal, model, analysis, document, deck, budget, process, or decision — checked proportionally and repaired in place.
- Boundary: identify the inspection surface before starting; name it when a review report is requested. Repair only inside that surface. Anything outside it is reported, never edited.

## Do not use this when

- The artifact is code, schema, data, or a deployment -> `dev-are-you-sure`
- The doubt is about an outside claim rather than work produced here -> `research-it`
- The work is correct and clean but unambitious, and needs a higher ceiling -> `is-that-the-best-you-can-do`
- One rejected output must become a permanent guard against a whole failure class -> `never-again`
- The work is simply unfinished and must be carried to a usable outcome -> `done-for-me`
- The artifact is clean but answers the wrong question at the wrong level -> `zoom-out`

## Procedure

Define the surface first: the exact artifact or set of artifacts under inspection. Keep this planning internal when the user requests only the repaired artifact. Select the checks relevant to its purpose and risks. A full audit considers all five lenses below; a small check needs only the relevant ones. Repair each evidenced finding immediately, or escalate it when the requested outcome needs a decision you do not hold. A possible risk is not an observed defect. Preserve explicit unknowns rather than inventing facts, owners or deadlines to make the artifact look complete.

1. **Integrity.** Trace the logic end to end. Reconcile every number to a named source. Check material assumptions and downstream consequences where relevant; a simple calculation may need only arithmetic and source fidelity.
2. **Structure.** Check whether the requested structure serves its use, without turning a one-off artifact into a system; find what sits at the wrong altitude, what commitment has no owner, and what decision is being made by a document instead of a person.
3. **Residue.** Resolve obsolete placeholders, stale dates, superseded draft figures, and contradictions between two sections that were written at different times.
4. **Recipient.** Read it as the person who receives it. Identify missing information that actually prevents the intended recipient from acting; do not invent additional decisions or expand a complete notice into a process design. Apply the installed wording standard rather than restating it here.
5. **Longevity.** For artifacts with an ongoing lifecycle, check expiry, ownership and review triggers when relevant. Do not add these to a simple notice or calculation.

Use not applicable when a requested audit lens does not fit, and unverified when evidence is unavailable. Report repaired, escalated or clean only for checks actually performed. A clean artifact stays unchanged. Keep the inspection account proportional and outside an artifact-only response.

## Stop when

The relevant checks (all five lenses for a full audit) are complete against the requested surface, every evidenced defect is repaired or escalated to a known decision holder, and material verification limits are explicit. Do not manufacture findings to justify the review.

## Principles

**Premortem** — Assume the deliverable has already failed badly, then work backwards to the cause; this surfaces defects that forward review consistently misses. Source: Gary Klein, Performing a Project Premortem, Harvard Business Review, 2007
**Swiss cheese model** — Use complementary checks where a defect could evade one lens; the depth follows the artifact's risk rather than a fixed reporting ritual. Source: James Reason, Human Error, 1990
**Chesterton's fence** — Do not remove anything whose purpose you cannot explain; ask why it is there before deleting it as residue. Source: G. K. Chesterton, The Thing, 1929
**Goodhart's law** — Distrust any number in the artifact that is also a target someone is measured on, and trace it to the behaviour it now rewards. Source: Charles Goodhart, 1975, as generalised by Marilyn Strathern, 1997

## Counter-case

- The user asks to sweep a React dashboard for leftover debug output and hardcoded values. The mental move is identical but the layers are software layers, so `dev-are-you-sure` owns it.
- The user asks whether a competitor's pricing claim is true. Nothing produced here is in doubt, so `research-it` owns it.

## Hand back

The repaired artifact, or the requested clean-result confirmation. A request to return the corrected artifact gets that artifact alone; keep surface, layer labels and repair bookkeeping internal unless the user asks for the inspection report. When an inspection report is requested, include the surface and actual findings, with clean, repaired, escalated, not-applicable or unverified status as warranted. Name only the decisions genuinely needed to finish.

## Sources

Klein 2007, Performing a Project Premortem. Reason 1990, Human Error. Chesterton 1929, The Thing. Goodhart 1975, Monetary Relationships; Strathern 1997, Improving Ratings.
