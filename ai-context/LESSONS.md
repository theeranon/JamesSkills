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


## LESSON-004 — Composition is not exclusion

**What happened:** Mode/workflow exclusions and mandatory reports displaced completion of the requested task.

**Mechanism:** Structural routing quotas were mistaken for distinct useful responsibilities; new exceptions were added without reconciling descriptions, principles and stop conditions.

**Rule:** Keep persistent modes active while workflows execute. Test the combined instructions through user corrections and real artifact changes. Reconcile the whole instruction contract when changing a rule; a structural pass is not behavioral proof.

**Date:** 2026-09-07. Owner clarification and DEC-032.

## LESSON-005 — A plugin content edit is invisible until the version changes and the app restarts

**What happened:** Across several rounds this session, a skill file was edited, committed, and pushed, but the owner's running Claude Code session kept showing the old text. Twice this was mistaken for a fresh bug ("used to work, now doesn't") when it was actually the same cache staying stale.

**Mechanism:** Claude Code's plugin cache is keyed by the plugin manifest's own `version` field, not by content or commit hash. `claude plugin update` compares that version number and no-ops when it is unchanged. `claude plugin uninstall`/`install` still resolves to the same cached version directory if the number did not change. Beyond that, a plugin's already-running Claude Code Desktop session loads its plugin list once per app launch; it does not hot-reload mid-session even after a correct reinstall.

**Rule:** Any content-only change to a shipped skill requires, in order: bump `VERSION` and every `plugins/*/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` version field together, validate, commit, push; then `claude plugin marketplace update`, uninstall and reinstall each affected plugin, and confirm `installed_plugins.json` shows the new version and the pushed commit SHA. Then tell the owner to fully quit and reopen the app (not just open a new tab or window) before re-testing — this last step cannot be verified from a terminal and must be stated as a remaining step, not assumed done.

**Date:** 2026-09-07. Recurred across the 2.0.1, 2.0.2, and 2.0.6 releases in this conversation.

## LESSON-006 — Verify the remote, not just the local commit log

**What happened:** A version bump and several skill edits were committed locally across multiple turns, but `git push` was never run for some of them. Local `git log` looked complete and current, so the gap was invisible until a direct `git fetch` and `git log origin/main` comparison was run.

**Mechanism:** A local commit is real work but is not distributed work. Reading only `git log` (local HEAD) cannot distinguish "pushed and live everywhere" from "sitting on this machine only" — both look identical from that one command.

**Rule:** Before telling the owner something is published, installed, or available to others, diff local HEAD against `origin/main` (`git fetch && git log origin/main..HEAD`), not just local history. Treat any non-empty diff as unpublished regardless of how many commits exist locally.

**Date:** 2026-09-07. Discovered when three commits (`0ce2f74`, `dbdbea6`, `98433f6`) plus an uncommitted version bump were found sitting unpushed while the marketplace and installed plugins had already been (correctly) resolving to the last commit that *had* been pushed.

## LESSON-007 — A synthesis verdict of "current is best" does not mean nothing was lost

**What happened:** Two independent full-portfolio audits of the same 22 skills disagreed on 12 of them. One audit (v1 vs. current) said specific concrete instructions were missing from the current file. A second, deeper audit (every historical commit, not just the two extremes) concluded current HEAD was the best version for those same 12 skills, because it had fixed a real, verifiable bug that no earlier version had fixed. Both were right about different things: the bug-fix trajectory was real, and the other, unrelated instructions were also genuinely gone. Trusting only the second audit's "current is best" summary would have left 12 real regressions in place.

**Mechanism:** An agent judging "which version is best" reasons holistically about internal consistency and bug history. That reasoning can be entirely correct on its own terms while never checking whether some *other*, unrelated capability quietly disappeared along the way, because nothing in its task asked it to re-verify a different audit's specific line-item claims.

**Rule:** When two audits (or an audit and a synthesis) disagree, do not average or pick a side by confidence — `grep` or directly read the actual current file for each specific disputed claim before accepting or rejecting it. A "best version" verdict is a claim about one axis (bug fixes, internal consistency); it is not proof that every other axis (capability completeness) was also checked.

**Date:** 2026-09-07. Found while reconciling the two 2.0.6 audits for `baseon`, `grill-me`, `coach-me`, `make-it-james`, `never-again`, and `proactive-dev`.

## LESSON-008 — A skill's identity fork goes to the owner, not to the agent's best argument

**What happened:** An audit argued that `coach-me`'s early version (which executed backend work on the owner's behalf) was "not real coaching" by appeal to non-directive coaching literature (Deci & Ryan, Miller & Rollnick), and that the current, strictly non-directive version was therefore the correct fix rather than a loss. The reasoning was internally coherent, but it answered a question only the owner can actually settle: what `coach-me` is *for*, in this specific library, for this specific person.

**Mechanism:** A well-cited, philosophically consistent argument can substitute for the owner's own intent, especially when it resolves an uncomfortable ambiguity in the agent's favor (it removes the disagreement instead of surfacing it). This is the same failure class as the AI-guessed skill definitions corrected earlier in this project's history, wearing academic clothing instead of a confident guess.

**Rule:** When a proposed change would alter what a skill fundamentally *is* (not just how well it does its stated job), present it to the owner as an explicit fork with named options, even when one option has a stronger-sounding citation. Do not silently resolve it and report the result as a bug fix.

**Date:** 2026-09-07. Owner resolved `coach-me` as non-directive (option B) after the fork was surfaced explicitly, rather than the audit's own recommendation being applied automatically.

## LESSON-009 — Run the full check after every file edit in a multi-file restoration, not just at the end

**What happened:** Restoring a dropped instruction into `sum-meet`'s Procedure accidentally deleted the literal phrase "same file" while rewording the surrounding sentence. `tests/test_output_contracts.py` asserts that exact literal substring is present. The break was caught immediately because `./scripts/validate` was run right after that one file's edit, not batched until the end of a 12-file round.

**Mechanism:** A static contract test can key on exact wording inside a skill's prose, not only on structural headings. Rewording a sentence for one purpose (restoring a dropped instruction) can silently break an unrelated literal-match check elsewhere, and the two failures look unrelated unless caught close to the edit that caused them.

**Rule:** In any batch of skill-file edits, run the validator after each file, not only after the whole batch. A failure surfacing 11 edits later is far more expensive to localize than one surfacing immediately.

**Date:** 2026-09-07. Caught before commit during the 2.0.6 restoration round; see DEC-033.
