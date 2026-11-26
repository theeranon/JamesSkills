# Software profile

Everything in the core (`INSIGHTS.md`, `DELIVERABLES.md`, `HANDOFF.md` included), plus:

| Path | Holds |
|---|---|
| `ai-context/ARCHITECTURE.md` | components, integrations, trust zones, data flow |
| `ai-context/DATA_MODEL.md` | fact ownership, entities, permissions |
| `ai-context/DEPLOYMENT.md` | server, how a release reaches it, what must survive a deploy, how to verify |
| `tools/release.sh` | the only way `production` changes |
| `tools/git-hooks/pre-push` | refuses any branch other than `main` and `production` |

## Source and production

- `main` is working source, with context. Existing owner-approved source branch names are preserved during migration.
- `production` mirrors the hosting **domain-directory**, with substantive `public_html/` required at its root. Other private folders retain application-specific names. Never invent app/storage folders just to satisfy an example.
- Web Docroot is public_html. FTP login home is the own-domain directory; Git Manager Remote Root `/`, FTP-only Local Path `.`. A child app keeps its intended subdirectory within public_html.
- `.release-layout.json` owns explicit source-to-artifact mappings and preserved server paths. Empty mappings are a blocker, not a reason to publish all source files or create a dummy website.
- `tools/release.sh` previews by default, validates the artifact and PHP syntax, and never deploys. `--push` publishes production only after committed source is already pushed; no automatic source push. No AI context, .git/.github/.claude, .env, runtime secrets or user data in the artifact.
- Keep server config, credentials and persistent files; database changes need migration/fresh/upgrade checks. Back up and verify restore before any runtime relocation. Do not describe desired private-code separation as already implemented.
- Auto-deploy/rebuild stays off until real checkout, destination path, preservation, migration and rollback acceptance. Never run two writers.
- DA Modify may require owner password entry; when rotated, update the paired GWM account with the same value. Agent prepares both pages and never asks for passwords in chat or handles new-password submission.
- `check --ready` verifies configured mapping and any actual production tree. Repo inspection cannot certify live FTP permissions, password correctness, auto-deploy state or application acceptance.
- Preserve existing extra branches until reviewed; deleting unmerged work needs owner confirmation. Hook setup remains `git config core.hooksPath tools/git-hooks`.
