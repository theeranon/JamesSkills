# General profile

For any project that is not software. The repository is the project's memory.

| Path | Holds |
|---|---|
| `ai-context/INSIGHTS.md` | dated insights and key learnings, each with its source: who said it, which file, which link |
| `ai-context/DELIVERABLES.md` | one row per deliverable version: date, name, version, path, what changed, who received it |
| `ai-context/HANDOFF.md` | what a new agent needs to continue: where things stand, what is promised, what is waiting on whom |
| `deliverables/` | the files themselves, HTML included; a new version is a new file or a new commit, never a silent overwrite of one already sent |

- One branch, `main`. No deploy, no `production` branch, no architecture or data documents.
- Requirements are outcomes of the work (a campaign, a plan, a decision) with an observable acceptance, not features.
- Chat is not storage: distil what was agreed into the owner files. A raw transcript or source goes under `ai-context/sources/` only when the owner supplied it and it may be stored.
