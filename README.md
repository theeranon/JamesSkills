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
It also activates repository-owned `pre-commit` and `pre-push` gates. Every commit and push runs `scripts/validate` locally, without GitHub Actions or paid runners.

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
- `.githooks`: free local validation before every commit and push

Private by default. Review every file before publishing any subset.

## Core vocabulary

- `give-me-solutions`: research real options and preserve the user's decision
- `done-for-me`: carry authorized work to a verified outcome without micromanagement
- `zoom-out`: solve the system problem before selecting tools
- `prove-it`: require recipient-visible evidence before Done
- `never-again`: convert one bad output into a system correction and regression test
- `final-it`: produce the finished artifact in the appropriate format
- `i-have-adhd`: persistent concise, direct, complete communication mode for the conversation

Skill names are phrases people naturally say when they need the capability. Workflow skills complete a bounded job; mode skills remain active for the conversation after one invocation.
