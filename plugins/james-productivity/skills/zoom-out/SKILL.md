---
name: zoom-out
kind: workflow
description: Step back at least three levels from the detail to the strategy, then agree the direction before any action resumes. Use when work has gone too deep too early; strategy only, never for interface or visual questions.
---

# Zoom Out

Climb back up until the strategy is visible, then agree it before anyone moves again.

## Scope

- Kind: workflow
- Owns: reframing work that has gone too deep, from the current detail up to the project's top view, and holding action until the direction is agreed.
- Boundary: reads plans, decisions, and current evidence. Produces a direction and an agreement gate. Never implements, never selects products, never redesigns a working layer because one surface failed.

## Do not use this when

- The question is about layout, interaction, or visual design -> `make-it-james-ux`
- The direction is settled and options must now be compared -> `give-me-solutions`
- The direction is settled and the job is to build it -> `done-for-me`
- Engineering work needs role decomposition and a build plan -> `proactive-dev`
- The requirement itself is vague and must be extracted from the user -> `grill-me`
- Current project state is unknown after a gap -> `catchup`

## Procedure

Climb at least three levels above wherever the conversation currently sits, then come back down deliberately.

1. **Top view.** What is this project for, and who is it for? State the outcome in business or human terms, not in features.
2. **Whole picture.** What are the parts, which ones already work, and which single responsibility is actually failing right now?
3. **Strategy.** What is the approach that would make the outcome true, and what is deliberately not being done?
4. **Action.** Only now, what is the next move, and what does it depend on?
5. **Research.** What is already known, and what must be found out before committing?
6. **Base package.** What is already owned and working that covers part of this, before anything new is introduced?

Reconcile the latest accepted decision, the current evidence, and any stale plan before treating a document or a mentioned product as authority. A tool that appears in a note is a candidate, never a requirement.

Then stop and agree. State the direction in one paragraph and get explicit agreement before implementation resumes. Do not proceed on inferred consent.

## Stop when

The outcome, the failing responsibility, the strategy, and the deliberate exclusions are all stated, and the user has explicitly agreed to the direction. Agreement is the exit condition; without it the skill has not finished.

## Principles

**Leverage points** — Intervene where the structure of the system changes, not where the symptom is loudest; parameter tweaks are the weakest place to push. Source: Donella Meadows, Leverage Points, 1999
**Dissolve rather than solve** — Prefer redesigning the situation so the problem cannot arise over solving the problem as posed. Source: Russell L. Ackoff, on idealised design, 1978
**Type III error** — Solving the wrong problem precisely is the costliest failure; verify which problem is real before any effort goes into answering it. Source: attributed to Howard Raiffa, 1968, developed by Ian Mitroff
**Theory of constraints** — Improving anything other than the binding constraint produces no improvement in the outcome. Source: Eliyahu M. Goldratt, The Goal, 1984

## Counter-case

- The user says a page feels wrong and asks to step back and rethink it. The layer in question is the interface, so `make-it-james-ux` owns it; climbing to strategy would only delay a design fix.
- The user asks which of three platforms to adopt, and the system boundary is already clear from an accepted decision. Nothing needs reframing, so `give-me-solutions` owns it directly.

## Hand back

The outcome in human terms, the responsibility that is actually failing, what already works and must stay untouched, the strategy with its exclusions, and the agreed direction with the next action it unlocks.

## Sources

Meadows 1999, Leverage Points: Places to Intervene in a System. Ackoff 1978, The Art of Problem Solving. Raiffa 1968, Decision Analysis. Goldratt 1984, The Goal.
