---
name: think-with-this
description: Apply a named framework, book, research source, or reusable knowledge lens to a real decision while separating source claims from case evidence and inference. Use when the user asks to think through a person, team, business, plan, or problem with Wealth Spectrum, Talent Dynamics, or another knowledge pack, compare lenses, or add a new source to the library.
---

# Think With This

Use knowledge as a lens, not a verdict.

## Choose the mode

- **Apply:** use one or more existing lenses on a real question.
- **Compare:** run the same evidence through multiple lenses without blending their labels.
- **Intake:** register a framework, book, paper, course, or James-owned model for later use.

## Apply or compare

1. State the real question, desired outcome, decision boundary, and facts already known.
2. From this skill directory, list the library with `python3 scripts/knowledge_library.py list`. Select the smallest relevant lens set. Do not invoke a lens merely because its name was mentioned.
3. Resolve every selected pack with `python3 scripts/knowledge_library.py show <lens-id>`, then read its entrypoint, concepts, applications, limitations, manifest, and referenced source cards.
4. Establish the subject input state:
   - `official_user_declared`: the user supplied or confirmed an official result.
   - `working_hypothesis`: an inference with confidence, alternatives, and disconfirming evidence.
   - `unknown`: evidence is insufficient; discuss observable behavior or operating conditions instead.
   - A stored profile label without a user-confirmed official report remains a prior interpretation. Downgrade it to `working_hypothesis` with `as_of`, confidence, alternatives, and review triggers even when an older profile file states it as fact.
5. Keep four layers visibly separate:
   - **Case fact:** verified observation, result, constraint, or current metric.
   - **Source claim:** what the framework author or source says, with source ID and locator.
   - **Inference:** how the lens may explain this case, with confidence and a competing explanation.
   - **Action:** a reversible experiment or decision implication with a success and revision rule.
6. If lenses disagree, show the disagreement. Never average several frameworks into a synthetic personality label.
7. Drop a lens when it does not materially change the question, options, or action.

## Intake new knowledge

Treat a book as a source first. It becomes a lens only when it has a reusable model and a recurring use case.

1. Register exact provenance: creator, edition, date, URL or ISBN, lawful-access context, rights status, and SHA-256 when a local file exists.
2. Keep full books, paid reports, assessments, diagrams, and training assets outside Git unless redistribution rights are explicit.
3. Create original paraphrased knowledge cards with stable claim IDs and page, chapter, or URL locators.
4. Add counterevidence, limitations, version differences, outdated examples, and prohibited uses.
5. Define questions, reversible experiments, and behavioral fixtures that prove how the knowledge changes work.
6. Validate before promotion with `python3 scripts/knowledge_library.py validate`.

Use `new-source` to register a source without inventing a new lens. Use `new-lens` only when the model deserves an independent application surface. See [pack contract](references/pack-contract.md).

## Hard boundaries

- Never infer an official assessment result from chat, tone, job title, or a short quiz.
- Never select a `draft` or `retired` source or lens for Apply or Compare. Only `reviewed-private` and `promoted` material is runtime-ready.
- Never reproduce proprietary test items, scoring logic, official reports, certification language, or branded visual systems.
- Never use a framework as the sole rule for hiring, firing, pay, credit, investment, medical, or clinical decisions.
- Never turn a current stage into a permanent identity. Time-sensitive hypotheses require an `as_of` date and review trigger.
- Never move private subject data into a portable knowledge pack. Keep it in the subject's profile or project context and join it only at runtime.
- Name the framework when attribution matters, but never imply affiliation, accreditation, or endorsement.

## Output contract

Give the useful conclusion first, then enough traceability to challenge it:

1. What the evidence says now.
2. What the selected lens adds and why it fits.
3. What does not fit, remains unknown, or has a competing explanation.
4. What changes in the decision or next experiment.
5. Lens version, source IDs, locators, and confidence when the result will be reused.

For a short conversational request, compress the structure but preserve all five meanings.
