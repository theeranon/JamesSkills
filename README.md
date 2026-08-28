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

Update fetches a fast-forward candidate, validates it in a detached temporary worktree before moving the active checkout, then refreshes links. An invalid candidate cannot replace the working version. Skill behavior never silently changes in the background.

## Boundaries

- `catalog.json`: canonical package category, promotion state, and compatibility aliases
- `skills/core`: bounded reasoning and execution workflows
- `skills/modes`: persistent conversation behavior
- `skills/standards`: automatically applied James-wide output law
- `skills/outputs`: reusable recipient-facing artifact workflows
- `skills/internal`: routing and composition mechanics
- `packs`: optional brand or domain references with no live state or client data
- `adapters`: vendor-specific metadata only; never duplicate core instructions
- `tests`: structural and outcome regression gates
- `scripts`: idempotent install, update, validation, and diagnosis
- `.githooks`: free local validation before every commit and push

Private by default. Review every file before publishing any subset.

## Vocabulary

### Core workflows

- `give-me-solutions`: research real options and preserve the user's decision
- `baseon`: base a decision on cited frameworks, books, or reusable knowledge lenses without turning author claims into facts
- `done-for-me`: carry authorized work to a verified outcome without micromanagement
- `zoom-out`: solve the system problem before selecting tools
- `prove-it`: require recipient-visible evidence before Done
- `never-again`: convert one bad output into a system correction and regression test

### Pilot candidates

- `design-the-course`: working package for one bounded learning experience; invocation name and LED/TPS boundary await James's approval
- `design-the-journey`: working package for macro transformation design; its five-phase reference is scoped to the sourced SolutionsIMPACT AI Transformation Journey offer

Pilot packages remain in the repository for review and testing but are excluded from global installs.

### Mode and standard

- `i-have-adhd`: persistent concise, direct, complete communication mode for the conversation
- `make-it-james`: automatically apply James's visual and Final Word law to recipient-facing work
- `project-standard`: keep outcome, requirements, current status, decisions, and agent instructions in one vendor-neutral project contract

### Outputs

- `final-it`: produce the finished artifact in the appropriate format
- `sum-meet`: turn transcripts, notes, files, or the current conversation into one print-ready portrait HTML meeting record containing every agenda as a separate zone
- `one-page-pls`: detect topics first and create one self-contained one-page artifact per topic or agenda

`james-skill-router` is internal composition logic. Compatibility aliases keep older calls working during migration without creating another instruction body.

## Knowledge library

`baseon` owns the application workflow. Sources and lenses live separately under `packs/knowledge` so a new book does not create another skill or inflate `SKILL.md`.

```bash
python3 skills/core/baseon/scripts/knowledge_library.py list
python3 skills/core/baseon/scripts/knowledge_library.py validate
```

The first reviewed-private lenses are `wealth-dynamics` and `wealth-spectrum`. `talent-dynamics` resolves to the same Dynamics lens because it is the team adaptation of the same model. Wealth Spectrum remains a separate model with the same creator lineage. Their full source PDFs remain outside Git. Source cards keep version, rights posture, SHA-256 when applicable, and locators; lens files contain original paraphrase, applications, and limitations.

Direct calls are available as `/baseon`, `/wealth-dynamics`, `/talent-dynamics`, and `/wealth-spectrum`. The framework shortcuts only preselect a lens; they contain no duplicate knowledge or reasoning rules. `/think-with-this` remains a compatibility alias.

The learning-design package names and aliases are working candidates, not approved calls. The current source record also contains an ontology conflict: James's newest correction places TPS inside LED, while older material described LED as one TPS lever. The library preserves the conflict instead of silently choosing a hierarchy.

Clone the full repository when moving machines. A detached copy of `baseon` alone intentionally has no duplicated knowledge library; set `JAMES_SKILLS_ROOT` to the full clone if a platform cannot use the installer links.

Skill names are phrases people naturally say when they need the capability. Workflow skills complete a bounded job; mode skills remain active for the conversation after one invocation.

## Candidate lifecycle

Discovery comes before packaging. A new skill remains a pilot until its Candidate Card shows repeated cross-project need, non-duplication, source confidence, representative failures, legitimate counter-cases, and James approves the exact name and scope. General permission to improve this repository does not approve a candidate's name or ontology.

The current cross-history portfolio audit recommends `catchup` as the next pilot, followed by `learn-this`, `audit-this`, and `systemize-it`. These are Candidate Cards, not installed skills. See `research/2026-08-29-skill-portfolio-audit.md`.
