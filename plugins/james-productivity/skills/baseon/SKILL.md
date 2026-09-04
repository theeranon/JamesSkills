---
name: baseon
kind: knowledge-lens
description: Apply or compare registered frameworks, books, and models against a real case while keeping source claims separate from evidence and inference. Use to interpret a situation through named knowledge; not to research new sources and not to decide.
---

# Base On

Use the model as a lens on the evidence, never as a verdict about the person.

## Scope

- Kind: knowledge-lens
- Owns: applying or comparing registered lenses against a real question, and registering new sources into the library.
- Boundary: reads registered packs and case evidence, and writes source and lens records. Never promotes an inference to an official result, never blends two frameworks into one label, and never becomes a sole hiring, pay, investment, or clinical rule.

## Do not use this when

- The source is not registered yet and the need is outside evidence about a claim -> `research-it`
- Options must be compared and one recommended -> `give-me-solutions`
- The problem layer itself is unclear -> `zoom-out`
- A person is stuck and needs to be moved rather than analysed -> `coach-me`
- A reusable model must be built rather than applied -> `skill-router` for a Candidate Card

## Procedure

1. State the real question, the decision it serves, and the case facts already established. Evidence comes before any framework label.
2. List the library with `python3 scripts/knowledge_library.py list` from this skill directory and select the smallest relevant lens set. A lens is not invoked merely because its name appeared in the request. Never select a `draft` or `retired` pack for a real decision.
3. Resolve each selected pack with `python3 scripts/knowledge_library.py show <lens-id>` and read its entrypoint, concepts, applications, limitations, manifest, and source cards. Read [references/pack-contract.md](references/pack-contract.md) before changing any pack. `wealth-dynamics` and `talent-dynamics` resolve to one shared Dynamics lens, Talent Dynamics being its team adaptation; `wealth-spectrum` is a separate stage model whose shared creator lineage never permits blending the two.
4. Establish the subject input state honestly as `official_user_declared` when the user supplied or confirmed an official result, `working_hypothesis` when it is an inference carrying confidence, alternatives, and disconfirming evidence, or `unknown` when the evidence is insufficient. A stored profile label without a user-confirmed official report remains a prior interpretation: downgrade it to `working_hypothesis` with its date, confidence, alternatives, and review triggers, even when an older profile file states it as fact.
5. Keep four layers visibly separate throughout. **Case fact** is a verified observation, result, constraint, or current metric. **Source claim** is what the framework or author says, with its source identifier and locator. **Inference** is how the lens may explain this case, with confidence and a competing explanation. **Action** is a reversible experiment or decision implication with a success and a revision rule.
6. When lenses disagree, show the disagreement. Never average several frameworks into one synthetic type.
7. End with a reversible experiment carrying a success rule and a revision rule. Drop any lens that did not change the question, the options, or the action.

To register new knowledge, treat the work as a source first. Record creator, edition, date, locator or identifier, lawful-access context, rights posture, and a hash when a local file exists. It becomes a lens only when it has a reusable model and a recurring use case. Copyrighted originals stay outside the repository. Never reproduce proprietary test items, scoring keys, official reports, or diagrams in Git.

## Stop when

Each selected lens has been applied separately with its four layers kept apart, disagreements are visible, and one reversible experiment is defined. A lens that changes nothing is dropped rather than reported.

On Windows invoke the same helper with `python` when `python3` is not on PATH.

## Principles

**A lens explains, it does not decide** — Report what the model illuminates about the evidence and never let a label replace observed results, cash flow, or work samples. Source: standing rule in this library
**Do not blend frameworks** — Keep each model's constructs inside its own boundary, because averaging two models produces a label neither source supports. Source: standing rule in this library
**Barnum effect** — Treat any reading that would feel true to almost anyone as evidence of nothing, and require a claim the case could have failed. Source: Bertram R. Forer, 1949
**Falsifiability of a profile** — State what evidence would disconfirm the interpretation before offering it, or present it as unknown. Source: Karl Popper, The Logic of Scientific Discovery, 1934

## Counter-case

- The user asks which personality or productivity framework the team should adopt. That is a choice between candidates rather than an application of one, so `give-me-solutions` owns it.
- A newly purchased book is mentioned by title. It is registered as a source with its provenance; it does not become a lens or a skill because its name appeared.
- Two frameworks share a creator but solve different problems. They stay separate lenses; shared lineage is not shared science.

## Hand back

The question, the lenses selected and why, the four layers kept separate, any disagreement between lenses shown rather than resolved, and one reversible experiment with its success and revision rules.

## Sources

Forer 1949, The Fallacy of Personal Validation. Popper 1934, The Logic of Scientific Discovery. Registered packs at `packs/knowledge/`.
