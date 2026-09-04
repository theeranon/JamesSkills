# Project Agent Contract

## Required context

1. Read `ai-context/PROJECT.md` for outcome, scope, requirements, boundaries, and acceptance.
2. Read `ai-context/STATUS.md` for current verified state and the next action.
3. Read `ai-context/DECISIONS.md` when a prior choice or superseded rule matters.
4. Read `ai-context/ARCHITECTURE.md` or `ai-context/DATA_MODEL.md` only when the task touches those concerns.

## Working rules

- Preserve unrelated work and existing project conventions.
- Verify current source and runtime before changing a status claim.
- Update the owner document only when the fact it owns changes.
- Keep unsupported facts as `Not confirmed` and unresolved choices as `Need decision`.
- Use provider-specific files only for provider mechanics; shared project truth stays here and in the canonical contract.
- After changing `ai-context/PROJECT.md` or `ai-context/DATA_MODEL.md`, regenerate `ai-context/SRS.html` with the render-srs command below. Never hand-edit `SRS.html` — it is a generated view.
- Check `ai-context/STATUS.md`'s `Spec lock` line before editing `ai-context/PROJECT.md` or `ai-context/DATA_MODEL.md`. If it reads `Locked`, do not edit either file without first recording a `Need decision` for the unlock — `check` will fail the commit otherwise.

## Commands

- Install: Not confirmed
- Test: Not confirmed
- Build: Not confirmed
- Run: Not confirmed
- Contract: `python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" check .`
- Render SRS: `python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" render-srs .`
- Lock spec: `python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" lock-spec .`
- Migrate to this layout: `python3 "$HOME/.agents/skills/project-standard/scripts/project_standard.py" migrate .`

## Completion

- Satisfy the named requirement and its acceptance proof.
- Run project-native checks.
- Update `ai-context/STATUS.md` when current truth changes.
- Do not claim Production, delivery, persistence, or external action without the matching evidence.
