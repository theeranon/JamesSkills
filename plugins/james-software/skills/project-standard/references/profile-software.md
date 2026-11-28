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
- One Git Manager project per target deploys branch `production`. FTP transport uses the site's own-domain account (home = domain directory) with the hosting record's host, port, explicit TLS and passive mode, Remote Root `/`, Local Path `.`, and a whitelist that matches the artifact; a reviewed same-host publisher may replace FTP. `DEPLOYMENT.md` records the project URL, the transport and whether auto-deploy is on, with the date and evidence of the last check.
- `.release-layout.json` owns explicit source-to-artifact mappings and preserved server paths. Empty mappings are a blocker, not a reason to publish all source files or create a dummy website.
- `tools/release.sh` previews by default, validates the artifact and PHP syntax, and never deploys by itself. `--push` publishes production only after committed source is already pushed; no automatic source push. Where Git Manager auto-deploys `production`, that push starts the live deployment, so it needs production authority and ends with the manager SHA and live checks. No AI context, .git/.github/.claude, .env, runtime secrets or user data in the artifact.
- Keep server config, credentials and persistent files; database changes need migration/fresh/upgrade checks. Back up and verify restore before any runtime relocation. Do not describe desired private-code separation as already implemented.
- Auto-deploy/rebuild stays off until real checkout, destination path, preservation, migration and rollback acceptance. Never run two writers.
- DA Modify may require owner password entry; when rotated, update the paired GWM account with the same value. Agent prepares both pages and never asks for passwords in chat or handles new-password submission.
- `check --ready` verifies configured mapping and any actual production tree. Repo inspection cannot certify live FTP permissions, password correctness, auto-deploy state or application acceptance.
- Preserve existing extra branches until reviewed; deleting unmerged work needs owner confirmation. Hook setup remains `git config core.hooksPath tools/git-hooks`.

## Production command contract

For a software project, `ai-context/DEPLOYMENT.md` must translate “ขึ้น production”, “ขึ้น production เลย”, “deploy production” and “เอาขึ้นเว็บจริง” into the actual project release route. `AGENTS.md` and provider adapters must point to it before release work.

Record the real source branch (including approved legacy exceptions), the exact preview/publication commands, mapping/preserve authority, target manager/environment and health/version evidence. The route is: scoped changes and native checks → commit/push source → preview the generated domain-directory artifact → publish only `production` through the release entrypoint → wait for the accepted writer (or trigger its normal manual deploy) → verify intended SHA and live behavior. Do not hand-edit, force-push or merge the whole source branch into the artifact branch. Publishing a branch alone is not deployment completion.

A named production request authorizes the existing target release within its established gates; do not reconfirm that same request. A docs/preview/source-push request does not authorize deployment, new credentials, destructive data changes or unrelated feature work. Auto-deploy can already be enabled for an accepted target; do not turn it off simply to apply this documentation standard. Preserve its existing acceptance and database gates.

For a child app deployed through a domain aggregate, document BOTH publications: child artifact, then update only that child's exact source/artifact/tree pins in the aggregate, publish the aggregate and verify the aggregate manager SHA plus the child pin. No separate FTP account or second deployment writer for each subdirectory. Preserve unlisted siblings. An independent repository with its own accepted target remains a direct release; do not invent aggregation.
