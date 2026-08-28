# Project contract

Use this reference when selecting project documents, repairing an existing repository, or deciding where a fact belongs.

## Minimum profile

Every adopted project has:

| File | Owns | Must not become |
|---|---|---|
| `PROJECT.md` | intended outcome, scope, requirements, boundaries, acceptance | status log or implementation history |
| `STATUS.md` | current verified state and exact next move | changelog or wish list |
| `AGENTS.md` | agent workflow, source map, commands, safety and verification | second copy of product requirements |
| `docs/DECISIONS.md` | accepted and superseded decisions | raw chat archive |

Keep an existing `README.md` for human onboarding. Create one only when users need setup or usage instructions.

## Software profile

Add only when supported by real complexity:

- `ARCHITECTURE.md`: components, boundaries, integrations, trust zones, deployment, and major data flow.
- `DATA_MODEL.md`: fact ownership, entities, relations, lifecycle, constraints, permissions, migrations, derived caches, and snapshots.

Do not create empty architecture or data documents for writing, research, design, or other projects that do not need them.

## Existing repositories

1. Inventory every project-brain file and the tools that load it.
2. Map existing facts to the four minimum owners before editing.
3. Preserve useful details and current tool-specific instructions.
4. Create a thin pointer when an active tool still requires a legacy filename.
5. Remove duplication only after every active caller points to the canonical owner.
6. Keep raw evidence, transcripts, and old decision records as history; do not rewrite them into current truth.

When an active provider requires its own entrypoint, copy the matching thin template from `assets/CLAUDE.template.md` or `assets/GEMINI.template.md` and add only provider mechanics. Shared requirements and operating rules stay in the canonical contract.

Use the installed shared-agent path for reusable Skill commands. Do not write one machine's absolute home path into a project document.

## Requirements

Use stable IDs such as `REQ-001` and keep one row per observable requirement:

| Field | Meaning |
|---|---|
| Requirement | user-visible or operational outcome |
| Boundary | explicit non-goal, permission, data, integration, or failure behavior |
| Acceptance | observable pass condition |
| Proof | source, test, route, receipt, rendered artifact, or provider state that proves acceptance |
| State | `Not started`, `In progress`, `Verified`, `Blocked`, or `Need decision` |

Do not encode implementation tasks as product requirements. Tasks may change while the accepted outcome remains stable.

## Conflict handling

Classify both sides before resolving:

- **Intent conflict**: two accepted requirements disagree. Keep both visible and request the irreducible owner decision.
- **Reality conflict**: documentation disagrees with code or runtime. Preserve the requirement and record the implementation gap in `STATUS.md`.
- **Freshness conflict**: an old status or plan disagrees with newer evidence. Current evidence wins for current state; history remains unchanged.
- **Adapter conflict**: provider files duplicate or weaken shared rules. Keep the provider mechanic and point shared behavior back to `AGENTS.md`.

## Update triggers

- Outcome, scope, requirement, permission, or acceptance changes: update `PROJECT.md` and record the decision.
- Current implementation or blocker changes: update `STATUS.md`.
- Agent workflow, command, or safety boundary changes: update `AGENTS.md`.
- Architecture or data ownership changes: update the relevant conditional document.
- A normal implementation changes none of these: leave the documents alone.
