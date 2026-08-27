# JamesSkills

Portable, versioned working practices for James Theeranon across Claude Code, Codex, Gemini, and Google Antigravity.

This repository contains reusable process knowledge, not JamesOS data, client records, credentials, or live project state.

## Install

```bash
git clone https://github.com/theeranon/JamesSkills.git "$HOME/.james-skills"
"$HOME/.james-skills/scripts/install"
"$HOME/.james-skills/scripts/doctor"
```

The installer links the canonical skills into the discovery directories available on the machine. It does not overwrite real directories or files.

## Update

```bash
"$HOME/.james-skills/scripts/update"
```

Update uses fast-forward only, validates the repository, then refreshes links. Skill behavior never silently changes in the background.

## Boundaries

- `skills/core`: portable promoted skills
- `adapters`: vendor-specific metadata only; never duplicate core instructions
- `tests`: structural and outcome regression gates
- `scripts`: idempotent install, update, validation, and diagnosis

Private by default. Review every file before publishing any subset.
