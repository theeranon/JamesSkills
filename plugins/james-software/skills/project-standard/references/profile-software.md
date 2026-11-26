# Software profile

Everything in the core (`INSIGHTS.md`, `DELIVERABLES.md`, `HANDOFF.md` included), plus:

| Path | Holds |
|---|---|
| `ai-context/ARCHITECTURE.md` | components, integrations, trust zones, data flow |
| `ai-context/DATA_MODEL.md` | fact ownership, entities, permissions |
| `ai-context/DEPLOYMENT.md` | server, how a release reaches it, what must survive a deploy, how to verify |
| `tools/release.sh` | the only way `production` changes |
| `tools/git-hooks/pre-push` | refuses any branch other than `main` and `production` |

## Two branches, always

- `main` is the working source, with all context. `production` is what the server deploys.
- No feature, agent or trial branch is pushed. Work lands on `main`.
- A release is `tools/release.sh`: it pushes `main`, then adds one commit on `production` holding `main` without the paths in `.release-exclude` (default `ai-context` and `tests`).
- Enable the hook once per clone: `git config core.hooksPath tools/git-hooks`.
- Point the deploy tool at `production`. Until someone has seen it deploy from there, record that as Not confirmed.
- `check --ready` fails while any other local or `origin` branch exists. Deleting one that holds unmerged commits needs the owner's yes.
