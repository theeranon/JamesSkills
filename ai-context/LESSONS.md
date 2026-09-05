# Lessons

Force-read by any agent entering this repository, per the mechanism `never-again`
requires. Each entry: what happened, the mechanism that allowed it, the rule now
in force, and the date.

## LESSON-001 — A confident, self-titled "standard" doc is not evidence

**What happened:** A separate agent session rewrote `scripts/install.py` and
`install.bat`, added `docs/UNIVERSAL_PLUGIN_STANDARD.md` (titled itself "The
Never Again Rule"), and updated README to assert as fact: that Codex CLI has
`codex plugin marketplace add` / `codex plugin add` subcommands, that Gemini
and Antigravity read a config file named `plugins.json` with an `entries`
array, and that "This guarantees that the plugins appear properly in the
Installed or Personal tabs" on every platform. None of this had been run
against a real Codex or Gemini installation. The new test file
(`tests/test_installer_contracts.py`) asserted that the installer's source
code *contained* these fabricated strings — a test that could only ever pass
by confirming the hallucination was present, never by confirming it worked.
The installer also hard-copied entire plugin trees into `~/.cursor/plugins`,
`~/.codex/plugins`, and `~/.agents/plugins` — directories none of those tools
read — and, in the process, deleted the real, working 22-skill symlinks it
was replacing. Running it took `scripts/doctor` from 0 issues to 99: Cursor,
Codex, and `.agents` went from 22 working skills to 0.

**The mechanism that allowed it:** A test was written to assert the presence
of the new code's own claims rather than an independently verified outcome.
Nothing forced the claim "verified on macOS & Windows" to be checked against
this repository's own prior, dated research (`research-it`'s own evidence
standard: official position, then independent practitioner accounts) before
it was committed. A confident tone and a document titled "standard" and
"mandate" substituted for a source.

**The rule now in force:** A README or code comment may never claim a
platform integration is "verified" or "guaranteed" without a dated, named
test that actually exercised it. A CLI subcommand may never be invoked in an
installer, or asserted in documentation, without a locatable source (that
product's own documentation or a direct reproduction) — "it seems like it
should exist" is not evidence. A test that asserts a string is present in
source code is not a behavioral test; it must be named and reviewed as a
"source contains X" check, never mistaken for a "the behavior works" check.

**Date:** 2026-09-05. Reference: `ai-context/DECISIONS.md` DEC-023.
