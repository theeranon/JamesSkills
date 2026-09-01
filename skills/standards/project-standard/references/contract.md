# Project contract

Use this reference when selecting project documents, repairing an existing repository, or deciding where a fact belongs.

## File layout

`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `README.md` stay at the repository root because agent tooling and GitHub only discover them there. Every other contract file lives under `ai-context/` so project truth does not scatter across the repository root next to source code.

## Minimum profile

Every adopted project has:

| File | Owns | Must not become |
|---|---|---|
| `ai-context/PROJECT.md` | intended outcome, scope, requirements, boundaries, acceptance | status log or implementation history |
| `ai-context/STATUS.md` | current verified state and exact next move | changelog or wish list |
| `AGENTS.md` | agent workflow, source map, commands, safety and verification | second copy of product requirements |
| `ai-context/DECISIONS.md` | accepted and superseded decisions | raw chat archive |

Keep an existing `README.md` for human onboarding. Create one only when users need setup or usage instructions.

## Software profile

Add only when supported by real complexity:

- `ai-context/ARCHITECTURE.md`: components, boundaries, integrations, trust zones, deployment, and major data flow.
- `ai-context/DATA_MODEL.md`: fact ownership, entities, relations, lifecycle, constraints, permissions, migrations, derived caches, and snapshots. Its Permissions section owns the role × action matrix. Treat a role able to act on its own submitted record, or reach a page or field never named as in-scope for its role, as a requirement defect to record under `Need decision` — not a cosmetic bug.

Do not create empty architecture or data documents for writing, research, design, or other projects that do not need them.

## Generated spec view

`ai-context/SRS.html` is a generated, human-readable render of `PROJECT.md`'s outcome, scope, requirements, and non-functional requirements, plus `DATA_MODEL.md`'s permission matrix when present. Regenerate it with `project_standard.py render-srs <project-root>` any time either source file changes; treat a stale or hand-edited `SRS.html` as a defect, not as a second source of truth.

It is a generated snapshot, not a live view: it does not update itself when `PROJECT.md`/`DATA_MODEL.md` change, and opening it directly from disk (`file://`) cannot safely fetch and re-parse sibling Markdown at open time in a general-purpose browser. `check` (see Spec lock below) catches a forgotten regeneration before commit; it is not a substitute for actually running `render-srs`.

`render-srs` only reads the exact canonical headings (`## Outcome`, `## Scope`, `## Requirements`, `## Non-functional requirements`, `## System boundaries`, and `## Permissions` in `DATA_MODEL.md`) — a trailing annotation on the same heading line (a date stamp, a parenthetical note) is tolerated, but a differently-worded heading, a different heading level, or a pre-existing spec document that never adopted the template is not recognized. When a heading is not found, `render-srs` prints a `WARN` line per missing heading and marks that section in `SRS.html` as flagged (visually distinct from a genuine `Not confirmed`) rather than silently rendering it as empty — always read the command's `WARN` output, and treat a project with warnings as not yet actually captured in `SRS.html` even though the command exited 0.

## Spec lock

`STATUS.md` carries a `Spec lock:` line with two states:

- `Open` (the default, including for a project with no line at all — v1 compatibility): `PROJECT.md`/`DATA_MODEL.md` are expected to change as the project learns. `check` requires `ai-context/SRS.html`, if it exists, to match their current content — regenerate it with `render-srs` before committing.
- `Locked (date: <date>, hash: <hash>)`: an owner has frozen the spec as the requirements bible, produced by `project_standard.py lock-spec <project-root>`. `check` then fails if `PROJECT.md` or `DATA_MODEL.md` changes at all — revert the change, or record a `Need decision` for the unlock and re-run `lock-spec` to record the new accepted hash.

Choose Locked only once the spec has matured past routine change — the transcript this rule is drawn from ties it to experience and stakes, not to project age: a first build should stay Open and let the spec keep catching up with reality, while a spec that must not silently drift (e.g. a contractual SRS, a regulated system) should lock.

## Existing repositories

1. Inventory every project-brain file and the tools that load it.
2. Map existing facts to the four minimum owners before editing.
3. Preserve useful details and current tool-specific instructions.
4. Create a thin pointer when an active tool still requires a legacy filename.
5. Remove duplication only after every active caller points to the canonical owner.
6. Keep raw evidence, transcripts, and old decision records as history; do not rewrite them into current truth.

### Migrating a flat-layout (v1) project into `ai-context/`

A project bootstrapped before the `ai-context/` layout existed keeps `PROJECT.md`, `STATUS.md`, `docs/DECISIONS.md`, `ARCHITECTURE.md`, and `DATA_MODEL.md` at the repository root. Run the automated command first:

```bash
python3 project_standard.py migrate <project-root>
```

It moves every legacy file whose headings already match the canonical template into `ai-context/`, repoints every known cross-reference inside the moved files and inside root `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`, and adds `Spec lock: Open` to `STATUS.md` if that field predates the file. Nothing needs a `--name` unless the project has no project-standard files at all (see the Workflow section of `SKILL.md` for the full decision tree and exit codes).

After a clean `migrate` (exit 0, nothing held back):

1. Run `project_standard.py render-srs <project-root>` once to generate `ai-context/SRS.html` for the first time.
2. Optionally install [assets/git-hooks/pre-commit](../assets/git-hooks/pre-commit) as `.git/hooks/pre-commit` so a stale `SRS.html` or a broken spec lock blocks the commit automatically instead of depending on an agent remembering to check.
3. If a project-local script, CI job, or another tool still reads the old root-level paths, add a thin pointer file at the old path rather than breaking that caller, and remove the pointer once the caller is updated.

`migrate` only moves a file once its headings already match the canonical template (a trailing annotation on the heading line, e.g. a date stamp, is tolerated). A project with a pre-existing spec/architecture document under a different name or heading convention (a `SPEC.md`, a README that doubles as spec, a Notion export) is reported, not moved — `migrate` exits 2 and prints exactly which headings are missing per held-back file. Moving or renaming that file yourself does not fix this: `check`'s structural gate already requires the canonical headings verbatim, and `render-srs` lists every non-matching section as a `WARN` instead of rendering it. Migrating that kind of project means rewriting its content into the canonical headings — this is a judgment call for the Repair workflow, not something `migrate` guesses at — then re-running `migrate`, which skips whatever it already moved and picks up only what's left.

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

Every delegated work packet also carries the same base revision, owned paths, allowed actions, forbidden external effects, and proof contract. Local implementation authority never implies permission to push, deploy, publish, send, or mutate an external account.

Keep mutable state in `STATUS.md`, keyed by the same requirement ID:

| Field | Meaning |
|---|---|
| Current state | `Not started`, `In progress`, `Verified`, `Blocked`, or `Need decision` |
| Evidence | current proof or exact proof gap |
| Last verified | date or timestamp of the current-state check |

Do not encode implementation tasks as product requirements. Tasks may change while the accepted outcome remains stable.

Non-functional requirements (scale, uptime, security posture) are owner-supplied facts, not agent-invented targets. Record them in `PROJECT.md`'s Non-functional requirements table before an architecture or deployment decision is finalized in `ARCHITECTURE.md`.

## Conflict handling

Classify both sides before resolving:

- **Intent conflict**: two accepted requirements disagree. Keep both visible and request the irreducible owner decision.
- **Reality conflict**: documentation disagrees with code or runtime. Preserve the requirement and record the implementation gap in `STATUS.md`.
- **Freshness conflict**: an old status or plan disagrees with newer evidence. Current evidence wins for current state; history remains unchanged.
- **Adapter conflict**: provider files duplicate or weaken shared rules. Keep the provider mechanic and point shared behavior back to `AGENTS.md`.

## Update triggers

- Outcome, scope, requirement, permission, or acceptance changes: update `PROJECT.md`, record the decision, and regenerate `SRS.html`.
- Current implementation or blocker changes: update `STATUS.md`.
- Agent workflow, command, or safety boundary changes: update `AGENTS.md`.
- Architecture or data ownership changes: update the relevant conditional document; regenerate `SRS.html` if `DATA_MODEL.md`'s Permissions section changed.
- Spec maturity changes (an owner decides the spec is now stable, or decides to reopen a locked one): update `STATUS.md`'s `Spec lock` line and, when locking, run `lock-spec` to record the accepted hash.
- A normal implementation changes none of these: leave the documents alone.
