# Local installer and benchmark receipt — 2026-09-06

Scope: owner-approved local repair and research. Base revision cbd1a62. macOS only. No external publish or universal runtime claim.

## Installer

- `./scripts/install --plan`: validation passed; six roots, expected 164 owned links total, zero changes/removals. No links, hooks or runtime configuration changed by plan.
- `./scripts/install`: exit 0; full validation passed; Codex app-server enabled=22, user-disabled=0, native/shared pairs=22, unresolved=0; managed links=164.
- Installer contracts: 22 tests pass, including empty/partial/foreign inventories, native/shared coexistence, user disables, pilot exclusion, link rollback, uncertain configuration response rollback, coverage-failure rollback, and failed Claude update without uninstall/install. These use isolated fake clients/filesystems, not six real OS installations.
- Claude update help locally confirms `plugin update <plugin> --scope user`. The refresh helper was not run against the network; its failure ordering was tested with a fake executable.

- Final `./scripts/validate`, `./scripts/doctor` and `git diff --check`: exit 0; doctor again reports 22 enabled skills and 164 managed links.

## Actual host evidence

- Codex CLI 0.153.4: authenticated; live app-server shows 22 enabled JamesSkills without duplicates. Computer Use refuses access to com.openai.codex, so Desktop picker is not verified here.
- Claude Code: three installed native packs contain 22 canonical bodies matching this checkout before behavior changes (none made). CLI auth status: loggedIn=false, authMethod=none.
- Claude Desktop 1.46388.4: directly navigated Customize → Skills → Yours. All 22 canonical JamesSkills visible, with the three James pack labels. Other publishers have similarly named skills; they were preserved. Discovery proof only, not invocation proof.
- Antigravity 2.12.2: directly opened Settings → Customizations. UI reports 49 total skills and shows JamesSkills entries including are-you-sure, baseon, catchup, coach-me, dev-are-you-sure, done-for-me, final-it, give-me-solutions and grill-me. This is partial UI discovery evidence, not an enumeration or task proof for all 22. Global managed files checked separately.
- No runtime proof for Windows, Cursor, Gemini CLI, or universal cloud-account synchronization.

## Benchmark

- 22 responsibility cards; 15 public synthetic probes across five approved skills.
- 8 runner mechanics tests pass. Dry-run schedules 30 A/B attempts with performance_score=null.
- Two actual Claude adapter attempts returned no model response. Diagnosed missing CLI authentication; new adapter preflight returns auth_unavailable without a model call. No claim of measured skill improvement.
- No sealed holdout, calibrated human/LLM judge, or full artifact/persistent-mode evaluation completed. Canonical instruction bodies unchanged.

## Recovery limit

Owned symlink and Codex override changes roll back on tested failures. A concurrently modified path is preserved and reported; an unreachable API can prevent full recovery. No claim of guaranteed rollback under arbitrary process termination or external service failure.

## Follow-up: authenticated Codex alternative

Codex 0.153.4 returned BENCHMARK_READY with exit 0 using existing ChatGPT authentication, ephemeral fresh cwd, read-only sandbox, ignored user config, disabled apps/plugins/shell_tool, and the advertised skip_host_skill_discovery feature. However, the same event stream reported that skills remained visible and descriptions were shortened to fit the context budget; input usage was 17,153 tokens. This route is authenticated but not demonstrated clean for a no-skill baseline. No A/B scores were collected or inferred, and global user skills/configuration were not changed. Claude CLI authentication still reports unavailable.

## Authentication blocker resolved

After owner email verification, Claude CLI authenticated successfully. Subsequent 41 calls all returned model responses. See `benchmark-2026-09-06/REVIEW.md` for findings and limitations. Earlier unauthenticated attempts above remain historical evidence, not current blockers.
