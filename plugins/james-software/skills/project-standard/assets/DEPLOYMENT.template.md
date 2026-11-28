# Deployment

- Contract: domain-directory/v1; production root mirrors one hosting domain directory and MUST contain public_html/.
- Source branch: main; source and AI context never deployed directly.
- Public web root: public_html; other private directory names follow the actual app, not a fixed app/storage example.
- FTP home: own domain directory (actual host/domain Not confirmed).
- Git Manager Remote Root: /; FTP-only Local Path: .
- Git Manager project: URL Not confirmed; branch production; transport (own-domain FTP or reviewed same-host publisher) Not confirmed.
- Release: tools/release.sh (preview, never deploys); tools/release.sh --push publishes `production`. If Git Manager auto-deploys this target, that push is the live deployment.
- Mapping and server files to preserve: .release-layout.json; configure real mappings before release.
- Auto-deploy/rebuild: remain OFF until destination, checkout, preservation, migration and rollback accepted; actual live state Not confirmed. Record the actual state with the date and evidence of the last check.
- Credentials: owner fills DA and paired GWM forms; a DA password rotation requires matching GWM update. No passwords in source/chat.
- Server paths, backup/restore and packaged application acceptance: Not confirmed.

## Meaning of “ขึ้น production”

For a software project, `ai-context/DEPLOYMENT.md` must translate “ขึ้น production”, “ขึ้น production เลย”, “deploy production” and “เอาขึ้นเว็บจริง” into the actual project release route. `AGENTS.md` and provider adapters must point to it before release work.

Record the real source branch (including approved legacy exceptions), the exact preview/publication commands, mapping/preserve authority, target manager/environment and health/version evidence. The route is: scoped changes and native checks → commit/push source → preview the generated domain-directory artifact → publish only `production` through the release entrypoint → wait for the accepted writer (or trigger its normal manual deploy) → verify intended SHA and live behavior. Do not hand-edit, force-push or merge the whole source branch into the artifact branch. Publishing a branch alone is not deployment completion.

A named production request authorizes the existing target release within its established gates; do not reconfirm that same request. A docs/preview/source-push request does not authorize deployment, new credentials, destructive data changes or unrelated feature work. Auto-deploy can already be enabled for an accepted target; do not turn it off simply to apply this documentation standard. Preserve its existing acceptance and database gates.

For a child app deployed through a domain aggregate, document BOTH publications: child artifact, then update only that child's exact source/artifact/tree pins in the aggregate, publish the aggregate and verify the aggregate manager SHA plus the child pin. No separate FTP account or second deployment writer for each subdirectory. Preserve unlisted siblings. An independent repository with its own accepted target remains a direct release; do not invent aggregation.

Before first publication, replace unconfirmed commands/target coordinates with this project's actual route. Do not execute example coordinates.
