# Project Agent Contract

## Required context

1. Read `PROJECT.md` for outcome, scope, requirements, boundaries, and acceptance.
2. Read `STATUS.md` for current verified state and the next action.
3. Read `docs/DECISIONS.md` when a prior choice or superseded rule matters.
4. Read `ARCHITECTURE.md` or `DATA_MODEL.md` only when the task touches those concerns.

## Working rules

- Preserve unrelated work and existing project conventions.
- Verify current source and runtime before changing a status claim.
- Update the owner document only when the fact it owns changes.
- Keep unsupported facts as `Not confirmed` and unresolved choices as `Need decision`.
- Use provider-specific files only for provider mechanics; shared project truth stays here and in the canonical contract.

## Commands

- Install: Not confirmed
- Test: Not confirmed
- Build: Not confirmed
- Run: Not confirmed
- Contract: `python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" check .`

## Completion

- Satisfy the named requirement and its acceptance proof.
- Run project-native checks.
- Update `STATUS.md` when current truth changes.
- Do not claim Production, delivery, persistence, or external action without the matching evidence.
