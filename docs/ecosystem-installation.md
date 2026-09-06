# Stable ecosystem installation

Research and local verification: 2026-09-06. Owner approved repairing the installation flow; no universal runtime claim or external publication follows.

## What one installation means

One canonical instruction body, one catalog, one installer entry point. Each host gets its supported discovery adapter. Fixing one host must preserve shared files that other hosts use. A host passes only when expected skills are present once, rather than merely having zero duplicates. Account-managed cloud libraries remain distinct from local files.

The [AI Hero setup page](https://www.aihero.dev/skills-setup-matt-pocock-skills), updated 2026-08-24, separates `npx skills@latest add mattpocock/skills` from its repository setup skill. That setup records issue tracking and domain documentation. The page itself documents a CLAUDE.md/AGENTS.md compatibility gap. It is useful inspiration for shared instructions, not proof of universal native installation.

The distributor's [issue 1874](https://github.com/vercel-labs/skills/issues/1874) reports that a change intended to prevent one host's duplicates skipped global directories for other hosts. This is a public firsthand report, not a reproduction here. Replacing our installer with that command alone does not establish stability.

## Current adapters and proof

| Surface | Mechanism | Current evidence |
|---|---|---|
| Codex CLI/app-server | Native plugins plus exact-path local overrides; shared files retained | 22 enabled canonical skills, missing/duplicate check; Desktop UI blocked by Computer Use |
| Claude Code | Native cache per skill; local fallback only when native skill absent/disabled | 22 current canonical bodies in installed caches; CLI model authentication unavailable |
| Claude Desktop | Account-visible plugin library, separate from CLI credentials | All 22 JamesSkills visible in Customize → Yours; other publishers can share names |
| Antigravity 2.12.2 | Flat global skill links, existing legacy links preserved | Settings → Customizations shows JamesSkills names/descriptions; full invocation unverified |
| Cursor, Gemini CLI, Windows and cloud-only surfaces | Separate discovery/account requirements | Do not infer runtime support from another app or symlinks |

Google's [current skill documentation](https://antigravity.google/docs/skills) identifies `~/.gemini/config/skills` for global skills. Keep that version-specific distinction from older Antigravity paths and Gemini CLI. Do not invent a common plugins.json or relocate working installations because another tool documents a different path.

## Changes implemented

`./scripts/install --plan` validates and previews expected/change/remove counts without changing links, hooks or runtime overrides. Installation preflights collisions, changes only owned links, and rolls back changes when link application or Codex reconciliation fails. Codex checks missing skills and duplicates, preserves user-disabled entries with explicit reporting, and restores owned overrides on failed reconciliation. An unreachable API may prevent complete recovery; report that failure instead of claiming success.

The Claude refresh helper now uses the supported `claude plugin update` command. It no longer uninstalls a working plugin first or claims marketplace updates contain arbitrary local edits. Local cached bodies and account libraries require separate content/version checks.

## Remaining acceptance work

Keep filesystem, discovery UI, explicit invocation and completed task proof as separate columns. Test cold-start loading and a representative task in each claimed host. A repeated install must change nothing and preserve other hosts. New host adapters need verified discovery documentation plus local or CI runtime evidence before claiming support. No new universal plugin framework is needed for this repair.
