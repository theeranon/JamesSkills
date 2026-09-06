---
name: zoom-out
kind: workflow
license: CC-BY-NC-4.0
description: Step out from implementation detail through the project goal to the strategy that should achieve it. Use when work is optimizing the wrong layer or losing its purpose; not for an isolated implementation or visual fix.
---

# Zoom Out

Recover the project goal and strategy before choosing the next implementation move.

## Scope

- Kind: workflow
- Owns: strategic reframing from a detail or local symptom to the project outcome, the strategy for achieving it, and the next aligned move.
- Boundary: diagnoses strategic alignment using accepted decisions and current evidence. Recommends direction without changing commitments. Use the task request to determine whether execution is authorized; a strategy document alone grants none. Changes to business goals or commitments need the relevant decision before execution, not before assessing the alternative.

## Do not use this when

- Only layout, interaction, or visual design needs repair and the project strategy is not in question -> `make-it-james-ux`
- The direction is settled and options must now be compared -> `give-me-solutions`
- The direction is settled and the job is to build it -> `done-for-me`
- Engineering work needs role decomposition and a build plan -> `proactive-dev`
- The requirement itself is vague and must be extracted from the user -> `grill-me`
- Current project state is unknown after a gap -> `catchup`

## Procedure

Start from the detail that has captured attention. Step out through roughly two or three **abstraction layers** until both the project goal and the strategy are visible. This is strategic distance, not a count of actions or headings. For example: a code optimization → the capability it serves → the project outcome and the strategic approach to achieving it. If the starting point is already strategic, do not invent extra layers.

1. Recover the intended outcome and beneficiary from the accepted project decisions. What should change for them, and how would success be recognized? Do not substitute a feature or technical metric for that outcome.
2. Explain the strategic approach: why building this capability should achieve that outcome, which assumptions make it viable, and what is deliberately outside scope. Distinguish the accepted strategy from your proposed alternative. State only supplied or verified commitments and exclusions as established; mark inferred mechanisms and unknown performance as such.
3. Relate the current detail to that strategy. Assess whether it is a binding constraint, useful supporting work, or a distraction, and distinguish evidence from hypothesis. A met technical target can make further tuning lower priority without proving zero benefit; a plausible bottleneck is not an observed one. Strategic misalignment does not establish that work was unauthorized. Check what already works before proposing replacement. A tool mentioned in a note is a candidate, not a requirement.
4. Choose the next aligned move and the evidence that would show it helped. Research only a material uncertainty that affects this direction; map the smallest coherent architecture and its failure boundaries before comparing or selecting products, and compare products only after the strategic role is clear.
5. Match the handoff to the user’s request. For an assessment or recommendation, deliver the strategic answer without declaring permission to execute or adding an approval question. For an execution request, continue actions already authorized; ask only about a material change in goal, budget or commitments not covered by that authorization.

An isolated layout correction does not require this workflow. But a complaint about a screen or code can reveal a strategic problem: follow the substance of the question rather than excluding it because it mentions an interface.

## Stop when

The project outcome, strategic approach, relevance of the current detail and next aligned move are clear. Return the strategic answer when that is all the user requested; otherwise resume authorized work. Only a material new decision remains with the user, not automatic re-approval of the current strategy.

## Principles

**Leverage points** — Choose the intervention that affects the actual constraint on the project outcome. Structural change is useful when evidence justifies it, not automatically better than a small aligned fix. Source: Donella Meadows, Leverage Points, 1999
**Dissolve rather than solve** — Consider whether changing the situation would remove the problem, while weighing that change against a simpler fix and preserving what already works. Source: Russell L. Ackoff, on idealised design, 1978
**Type III error** — Solving the wrong problem precisely is the costliest failure; verify which problem is real before any effort goes into answering it. Source: attributed to Howard Raiffa, 1968, developed by Ian Mitroff
**Theory of constraints** — Prioritize the constraint supported by current evidence; treat an untested bottleneck as a hypothesis and do not infer zero benefit elsewhere. Source: Eliyahu M. Goldratt, The Goal, 1984

## Counter-case

- The user asks only to fix an overlapping button in an accepted flow. `make-it-james-ux` can handle the local fix. If they question why the flow exists or whether it serves the project outcome, step out to strategy here.
- The user asks which of three platforms to adopt, and the system boundary is already clear from an accepted decision. Nothing needs reframing, so `give-me-solutions` owns it directly.

## Hand back

The strategic reframe: project outcome, approach, how the current work contributes or distracts, and the next aligned move. Name only a genuinely new decision requiring the user. When execution was requested and authorized, carry that work forward rather than stopping at the reframe.

## Sources

Meadows 1999, Leverage Points: Places to Intervene in a System. Ackoff 1978, The Art of Problem Solving. Raiffa 1968, Decision Analysis. Goldratt 1984, The Goal.
