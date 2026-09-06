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

## LESSON-002 — Inspect the combined runtime inventory, not one discovery directory

**What happened:** The first Codex duplicate fix removed links from its own skill
root and doctor reported zero issues, but the shared `.agents` root still supplied
the same 22 skills beside native plugins. A user screenshot showed the duplicates
persisting. Fresh app-server inventory and a clean GitHub installation reproduced
44 enabled entries for 22 names.

**Mechanism:** The check encoded the installer's incomplete model of discovery.
It never asked the runtime which paths were actually loaded.

**Rule:** A duplicate-loading fix requires a combined runtime inventory and one
explicit invocation. Keep UI evidence separate when the app cannot be inspected.
Preserve shared files used by other hosts; scope overrides to the affected host
and exact local path. Test a second package plus the legitimate no-plugin case.

**Date:** 2026-09-05. DEC-025 and
`tests/receipts/install-discovery-2026-09-05.md`. LESSON-001's historical claim that
Codex lacks a marketplace command was itself corrected by DEC-024; its requirement
for direct evidence remains in force.

## LESSON-003 — Optimize the user's outcome, not a proxy

**What happened:** The owner clarified that overfit includes focusing on irrelevant work and AI overengineering, as well as memorizing practice tasks.

**Mechanism:** A local metric such as completeness, style, test count or speed can improve while the main deliverable becomes less useful or remains unfinished.

**Rule:** Every behavioral benchmark names the user outcome and separately reviews goal alignment and proportionality. A primary-task failure cannot be rescued by formatting scores. More detail is justified when it resolves a real dependency or risk. Each correction needs a rejected case, a transfer case and a counter-case where complexity is necessary. Do not turn this into a rule to always produce less.

**Date:** 2026-09-06. Public development cases in `tests/benchmarks/development.json`; measured improvement remains unproven.
