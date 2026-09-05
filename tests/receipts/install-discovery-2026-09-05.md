# Installation and duplicate-discovery receipt

Date: 2026-09-05. Platform: macOS, Apple silicon.
Published baseline: `51c776e97eb6bf8ce4a2e6a9b49d59931c431197`.
Tools: Codex CLI 0.153.4; Claude Code 2.1.220; system Python 3.9.

## Reproduced failure

A new temporary user configuration added `https://github.com/theeranon/JamesSkills.git`
with Codex's own marketplace command and installed all three pillars. The
app-server `skills/list` response showed 22 enabled native skills with no repeated
names. Running the published local installer into that same isolated user
configuration produced 44 enabled entries: every canonical name appeared twice.
The second copy came through the shared `.agents/skills` links. Removing only the
Codex-specific links did not resolve this path.

The actual machine showed the same native-cache/local-source pair for
`james-core:proactive-habits` and `james-software:proactive-dev`. The previous
doctor's zero result covered its filesystem checks, not this combined inventory.

## Repair and verification

- Kept shared links for other agents. Used Codex `skills/config/write` with an
  exact local `SKILL.md` path and `enabled=false`; native counterparts remain enabled.
  Configuration was backed up locally before the changes. No account secrets are
  included in this receipt.
- Fresh app-server after repair: 22 canonical names, 22 enabled entries, no
  repeated enabled names. On the actual machine, all 22 native/shared pairs are
  reconciled. Disabled local entries remain in the raw API response intentionally.
- Applied the candidate installer files to the clean GitHub checkout. First
  install, repeated install, and doctor all exited zero. App-server remained at
  22 enabled canonical names. This tests the local candidate, not an already
  published fix.
- A second empty user configuration tested the candidate local-only route: install
  and doctor passed, with 22 enabled local canonical names and no native plugins.
- The separately downloaded Codex productivity plugin ran
  `skills/baseon/scripts/knowledge_library.py validate` successfully: 7 sources,
  3 lenses. This verifies the packaged helper and its data dependencies.
- A fresh Codex `exec --ephemeral` smoke test explicitly invoked
  `$james-core:proactive-habits`. The command trace read the installed native-cache
  `SKILL.md`; the response activated the mode and correctly stated that publishing
  and spending still require approval. This is one invocation/authority-boundary
  case, not behavioral coverage of all 22 skills.
- Claude Code used another empty configuration directory. Marketplace add from
  GitHub and installation of all three pillars succeeded. This is fresh download
  and registration evidence; it does not extend the earlier runtime receipt to
  Claude Desktop.
- Full repository validation and the installer regression suite passed. Regressions
  exercise the shared/native duplicate, a second pillar, missing/disabled/unrelated
  native plugins, restoration of installer-owned overrides, preservation of user
  disables, partial Claude installation, repeated installation, pilot exclusion,
  pre-existing directory/file/foreign-link collisions, validator failure, and
  symlink-creation failure preserving the previous link.

## Limits and next verification

Codex Desktop UI access was refused by the Computer Use tool. Therefore the
picker screenshot after repair is not verified; reopen its picker or restart the
app and check the two reported names. Do not equate the API result with that UI
receipt. No app process was killed or restarted by this work.

Windows was not available for an on-platform test. The local installer no longer
skips its validator there and no longer deletes folders or copies on link failure.
It requires Bash validation and symlink permissions. Windows, Cursor, Gemini,
Antigravity and Claude Desktop runtime compatibility remain unproved here.
The Gemini/Antigravity plugin-directory layout is retained as filesystem state,
not promoted to a verified integration.

The local candidate must be published before other users receive this installer
repair. Native marketplace-only installation from the baseline already passed.

## Sources checked

- [JamesSkills source](https://github.com/theeranon/JamesSkills).
- Installed Codex CLI `plugin --help`, `plugin marketplace add --help`, and
  `plugin add --help`; generated app-server JSON schemas for `skills/list` and
  `skills/config/write`.
- [OpenAI skill documentation](https://developers.openai.com/codex/skills).
- [Claude configuration isolation](https://code.claude.com/docs/en/env-vars).
- [Codex shared-directory discovery report](https://github.com/openai/codex/issues/22275)
  and [older duplicate-discovery report](https://github.com/openai/codex/issues/8169)
  were considered as leads only. Neither proves this failure's cause; the local
  app-server reproduction does.
