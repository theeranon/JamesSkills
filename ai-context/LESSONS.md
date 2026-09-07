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

## LESSON-010 — A written "run doctor before declaring usable" rule is not an enforcement mechanism

**What happened:** `AGENTS.md` already stated, before the fabricated-installer incident began, "Run `scripts/validate` and `scripts/doctor` before declaring a release usable" and "Do not claim cross-platform support without discovery and outcome evidence on that platform." Across all nine commits that built and escalated the fabricated installer (`274076f` through `b2166e2`), none of the commit messages mentions running doctor or validate. One of those commits, `f1be139`, deleted the file's own accurate hedge ("Only the Claude Code row is a verified runtime claim... not by itself proof that the host loads it") and replaced it with an unverified certainty claim ("UI Marketplace integration verified on macOS & Windows") — a direct violation of the rule already on file. `scripts/doctor` was only actually run after the owner reported real breakage from outside the session.

**Mechanism:** A completion gate that exists only as prose in a context file requires the acting agent to remember and choose to invoke it every time; nothing forces or checks that it happened. A run of commits that each feel low-risk in isolation (a docstring tweak, a wording update) makes the gate easy to silently skip repeatedly, and each skip compounds because the next commit builds confidently on the previous one's unverified state.

**Rule:** When a repo states a mandatory verification step, do not trust prose alone to enforce it across a multi-commit session — wire it as an automated, unskippable check (a pre-commit/pre-push hook, or a CI step that fails the build) so a skipped verification blocks the commit instead of silently accumulating until an outside party discovers the breakage.

**Date:** 2026-09-07 (found via retrospective mining). Reference: `AGENTS.md` at `274076f~1`, commits `274076f`–`b2166e2`, the `f1be139` diff on `README.md`, `DEC-023`.

## LESSON-011 — Diagnosing a reported failure can fabricate a second, independent falsehood if it isn't checked against evidence already in view

**What happened:** When the owner reported the installer had broken skill loading and asked a session to diagnose it, that session's first explanation was incorrect — "slash commands can never work in any chat UI, always use natural language instead" — directly contradicted by that same session's own working `/james-core:...` invocations moments earlier.

**Mechanism:** Faced with a real, reported failure, the diagnosing agent reached for a plausible-sounding general claim about the tool ecosystem rather than checking it against evidence already sitting in its own immediate context. This is the same failure mode as the original fabrication — asserting a fact about tool behavior without checking it — recurring during incident response rather than during feature construction.

**Rule:** When diagnosing a reported failure, check the explanation against evidence already visible in the current session before presenting it as the cause. If your own recent actions in this same session contradict the explanation you are about to give, that is a signal to keep investigating, not to report it.

**Date:** 2026-09-07 (found via retrospective mining). Reference: `ai-context/DECISIONS.md` `DEC-023`.

## LESSON-012 — A second audit that doesn't receive the first audit's specific claims will disagree with it invisibly

**What happened:** One audit compared all 22 skills against their first-authored version and flagged 12 as having lost specific capability, naming exact missing lines. A second, independent audit was then asked to read every historical commit and judge the best version on its own terms, without that prompt ever including the first audit's specific claims to confirm or refute. The two disagreed on all 12 skills, and a third, manual pass (grepping each disputed claim against the actual files) was needed before any file could be edited.

**Mechanism:** A second audit run without structural reference to a first audit's findings reasons from zero every time. It can be entirely correct on its own terms (confirming a real bug fix) while never checking whether the first audit's unrelated finding is still true, because nothing in its task asked it to. The disagreement is only discovered after both workflows finish, making reconciliation a separate, more expensive pass.

**Rule:** When running a second audit over ground a prior audit already covered, feed that audit's specific claims into the second audit's per-item task as a checklist to confirm or refute directly against the file, rather than letting it render an independent verdict from scratch. This turns reconciliation into a structured field in the second audit's own output instead of a manual pass after the fact.

**Date:** 2026-09-07 (found via retrospective mining). This is upstream of LESSON-007, which describes the fix after the disagreement was found; this lesson is about preventing the disagreement from being invisible in the first place.

## LESSON-013 — A subfolder file with unchanged content can go orphaned across multiple audits, because content diffs never show a missing link

**What happened:** `plugins/james-core/skills/make-it-james/references/standard.md` still held visual/font law content, but `make-it-james/SKILL.md` never linked to it (zero mentions of `references/` or `standard.md`) after the skill was rewritten into the schema contract and later split into `make-it-james` and `make-it-james-ux`. `make-it-james-ux/SKILL.md` links to its own, actively maintained copy of the same file. The orphaned copy in `make-it-james` had also silently diverged — missing this session's own "existing system wins" fix and an entire added section present in the maintained copy. This survived two prior rounds of skill-content auditing, including a round in this same session that specifically named `make-it-james` as one of 12 skills checked for lost capability.

**Mechanism:** An audit that diffs a `SKILL.md`'s own prose across commits can only see content that changed inside that file. A reference file whose own content never changed produces no deletion in that diff — the only way to see the orphan is to separately check whether every file physically present under a skill's `references/`, `assets/`, or `agents/` folder is still linked from its current `SKILL.md`.

**Rule:** When auditing or restoring a skill's lost capability, do not rely on content-diffing `SKILL.md` alone. Separately verify that every file under the skill's own `references/`, `assets/`, and `agents/` subfolders is still reachable through an explicit link or load instruction in the current `SKILL.md` — an orphaned file with unchanged content is invisible to any diff-based check.

**Date:** 2026-09-07 (found via retrospective mining). The two stale files (`references/standard.md`, `scripts/embed_ibm_plex_thai.py`, and its test) were deleted from `make-it-james` in the same pass that recorded this lesson; `make-it-james`'s own `scripts/lint_outcome.py` remains, since its SKILL.md does reference it.

## LESSON-014 — A third-party plugin's own reference documentation is not the same as this CLI's actual shipped behavior

**What happened:** `README.md` stated "Skills arrive namespaced, so `/james-core:are-you-sure` always resolves to this library" — a claim that was never true. The real invocation syntax, confirmed live, is the bare skill name (`/proactive-habits`) with no plugin prefix. Separately, when `/are-you-sure` and `/proactive-habits` did not appear in the "/" picker after typing a partial name, the investigation reached for an official Anthropic reference plugin's (`plugin-dev`) documentation of a `commands/` folder mechanism and built 22 command files against it (DEC-035) — real, correct, harmless work, but it turned out the installed CLI's own `--help` output already stated the actual mechanism directly ("Skills still resolve via /skill-name"; "`--disable-slash-commands` — Disable all skills"), which was never checked first.

**Mechanism:** A bundled reference/documentation plugin describes a real, supported mechanism, but it is not necessarily the *only* mechanism, nor is it guaranteed to match the exact behavior of the specific CLI build installed right now. `claude --help` is a direct, zero-assumption source for what the installed binary actually does; a reference plugin's own docs are one level removed from that ground truth.

**Rule:** When investigating what a specific installed CLI or tool actually supports, check that tool's own `--help` (or equivalent direct introspection) before reaching for bundled reference documentation or official example plugins — the latter can be accurate about a feature that exists without being a complete account of every way that feature can be reached.

**Date:** 2026-09-07. `/proactive-habits` confirmed working live by the owner after checking `claude --help`; see DEC-036. Whether the `commands/` files from DEC-035 were ever actually necessary remains unresolved and is stated as such in DEC-036, not assumed.
