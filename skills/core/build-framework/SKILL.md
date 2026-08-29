---
name: build-framework
description: Turn a recurring cross-project method need into reusable SolutionsIMPACT intellectual property by searching the house library first, then reusing, piloting, upgrading, or building a cited framework. Use for a reusable model or decision logic, not for repairing one rejected output or designing one course or journey.
---

# Build Framework

Create durable intellectual property, not a fresh diagram for each project. The primary framework must belong to SolutionsIMPACT. Books, research, external frameworks, consulting reports, and case studies are evidence used to derive or challenge the house framework; they are never silently renamed as company property.

## First instinct

Always inspect the house library before proposing anything new:

```text
use an existing framework
-> upgrade an existing framework
-> build a new framework only when the first two cannot solve the recurring problem
```

Run `python3 scripts/framework_library.py search "<problem or outcome>"` from this skill directory when the repository library is available. Search results are candidates, not a keyword-based decision. Read the relevant entry and sources before choosing.

`Use existing` is the reuse branch, not an approval claim. Lifecycle controls what reuse permits: an approved framework may be used actively; a pilot may be used only inside its evidenced pilot boundary with observation; a candidate or source-gap item may inform analysis but may not be presented as active company law.

Use [references/framework-contract.md](references/framework-contract.md) to distinguish a framework from a pattern, tool, template, checklist, or one-off design. Use [references/research-provenance.md](references/research-provenance.md) for every research pass.

## Workflow

1. Define the recurring problem, intended users, decisions improved, scope, and evidence of need.
2. Search the house library and record what was inspected. Choose `use`, `upgrade`, or `build`; disclose the selected item's kind, lifecycle, version, and permitted scope. Explain why the earlier option is insufficient before moving forward.
3. Research the smallest credible source set. Separate source claims, independent evidence, internal case evidence, owner rules, and synthesis.
4. Build the house model: constructs, relationships, decision logic, operating mechanism, outputs, evidence, limits, and counter-cases.
5. Preserve the registered name when reusing an existing item. Present three branded name candidates and one recommendation only when the decision creates a new framework, materially renames an upgrade, or the owner explicitly requests naming. A recommended new name remains working language until approved.
6. Draw one useful visual model. The visual must explain relationships or sequence rather than decorate the report.
7. Test the candidate against distinct scenarios and a legitimate counter-case. A pilot may begin with one real case; approval requires at least three materially different scenarios and one counter-case.
8. Produce one executive HTML report using [references/html-output.md](references/html-output.md) and [assets/framework-decision-report.html](assets/framework-decision-report.html).
9. James is the V1 approver. Save an approved change as a new version; never overwrite the previously active framework silently.

Do not ask the user to select an internal mode. Infer whether the job uses, upgrades, or builds from the request and evidence. Surface only a decision that changes the framework, name, claim, or approval state.

## Framework gate

Call the result a framework only when it has:

- a recurring problem and bounded promise
- named constructs with meaningful relationships
- decision or operating logic that changes action
- inputs, outputs, evidence, and a repeatable way to use it
- limits and counter-cases
- traceable research and internal evidence
- the registered name and version for reuse, or a branded working name for a new or renamed candidate, plus an explanatory visual
- version, owner, lifecycle state, and approval record

If these conditions fail, label the result accurately as a pattern, method, tool, template, checklist, principle, or one-off design.

## Completion

Deliver the cited executive HTML report, not a chat summary. Apply `make-it-james`, run strict outcome lint, embed IBM Plex Sans Thai when one offline file is required, and inspect the rendered report. Every material claim and every borrowed construct must resolve to a source entry.
