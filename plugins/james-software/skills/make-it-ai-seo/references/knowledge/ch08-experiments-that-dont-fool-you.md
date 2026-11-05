---
id: ch08
title: Experiments That Don't Fool You
part: Part 2: Measuring AI SEO
tags: [experiment design, hypothesis, control prompts, platform drift, prompt hygiene, change log, baseline, outcome labels, playbook, A/B testing, noise]
use_when: Designing, running, or judging an AI SEO test; deciding whether a visibility change was caused by your work or by AI variance.
---

# ch08 — Experiments That Don't Fool You

## Core idea
- AI answers vary run to run, and platforms change under you (models, UI, retrieval, personalization), so a single before/after check proves little.
- An experiment answers one question: did our change move results beyond normal variation and platform drift?
- Design: one hypothesis, a small frozen prompt set with direct/related/control roles, a preset schedule, a change log entry, then judge repeated, cross-prompt, control-adjusted movement.

## Sources of false wins
- Model upgrades or switches.
- UI changes that show, hide, or reorder citations.
- Retrieval changes that pull different evidence.
- Personalization differences (logged in vs out, device, plugins, location).
- Prompt wording drift between runs.
- Shipping many changes at once ("we changed ten things and something moved").

## Step 1: Write one hypothesis
- One sentence naming: the change, the prompts expected to move, the platforms, the metrics.
- Examples: comparison page for Brand A should raise coverage and average position on Brand A comparison prompts in ChatGPT and Perplexity; entity cleanup (About page, naming, profiles) should raise SoV on solution-stage prompts in Google AI Mode/Overviews; stronger presence on top-cited review sites should lift citation coverage and SoV on "best tools" prompts.
- Source hypotheses from the ch07 gaps: clusters where competitors dominate SoV, recurring citation sources where they appear and you do not, platforms that matter but where you are absent.

## Step 2: Build the experiment prompt set
- Tag 5-10 prompts from the ch05 database with an Experiment ID (e.g., EXP_03_ComparisonPage).
- Roles: Direct (points straight at the changed asset), Related (same cluster/intent, indirect benefit), Control (similar category, untouched during the test).
- Keep it small; aim for repeatability, not completeness.

## Step 3: Freeze prompts (prompt hygiene)
- Same wording every run; same platforms; prompts that sound like real buyers; new variants wait for the next experiment. Changing wording midtest voids the comparison.

## Step 4: Platforms and cadence (decide before starting)
- 3-5 platforms matching the audience; same surfaces for direct, related, control.
- Baseline window 1-2 weeks; follow-ups 2-4 weeks after launch; optional longer check at 6-8 weeks for slow-to-be-discovered changes.
- Do not change the schedule after seeing results.

## Step 5: Change log entry
- Fields: date (and time if relevant), what changed (page, profile, directory listing, fact hub, review campaign), type of change (comparison page, entity cleanup, profile update, PR mention), one-sentence hypothesis, Experiment ID.
- Fact hub = a page collecting key facts, stats, definitions in one reliable place.

## Step 6: Control for drift
- Record visible version info: model name, mode label, logged-in state, date, surface version.
- Log publicly announced platform events (model upgrades, new search modes, citation display changes) inside the test window.
- Think in time periods, not single runs. If test and control prompts move together, suspect drift.

## Step 7: Run checklist (every capture)
- Run the same frozen prompts filtered by Experiment ID; same platforms; same locale/language (or note differences); same environment (login, device, extensions).
- Capture full answer and citation section.
- Log per prompt: coverage (present/absent), position (first mention/list position), citations (domains), quick notes (missing citations, login change, location mismatch, failed load).

## Step 8: Read results
- Core metrics stack: coverage (direct prompts first, then related), position (average before vs after per role), SoV (relative to competitors so you do not claim wins while rivals gained more), citations (own site, influenced third-party sources; track domains and page types, not raw counts).
- Soft signals as support only: self-reported AI mentions, branded search lift for experiment topics, referral spikes to targeted pages (comparison pages, review profiles, cited third-party sources). They never override core metrics.
- Believability rules: movement across multiple direct prompts, across at least two follow-up runs, on more than one platform. Example thresholds: act when at least 3 direct prompts move the same way; require the movement to hold for 2 consecutive follow-ups.
- Test vs control: direct improving more than controls = more likely your work; related moving as expected; if control moves with test, treat as noise or platform change.

## Step 9: Conclude with simple labels
- Clear win (scale it): expected metrics moved, held across follow-ups, no major downside on key platforms.
- Inconclusive (keep, watch, refine): inconsistent, small, or single-platform; keep live, extend window, or tighten prompts.
- Weak or negative (rethink or roll back): little gain or harm to SoV/position on important prompts; roll back, revise, or try another approach.
- Write label plus one-sentence evidence summary in the experiment sheet.

## Step 10: Playbooks and failure notes
- Wins become a playbook: name, what shipped, prompt roles tracked, platforms, metrics improved and magnitude, conditions that mattered (e.g., worked best on solution-stage prompts, needed strong review presence). Add to standard workflows.
- Failures: record what changed, what was expected, what happened, what to do differently.

## Templates & prompts
- Hypothesis sentence: "If we [change], then [coverage/position/SoV/citations] will improve for [prompt role/cluster] on [platforms]."
- Experiment sheet columns: Experiment ID | Hypothesis | Change shipped | Ship date | Baseline window | Prompts (Direct/Related/Control) | Platforms | Model/mode notes | Platform events | Result per follow-up | Outcome label | Evidence summary | Next step.
- Run log columns: Date | Platform | Prompt | Role | Present | Position | Cited domains | Notes.
- Playbook outline: Name | Shipped | Roles | Platforms | Metrics and deltas | Conditions | When to reuse.

## Audit checks
- [ ] Each experiment states a single hypothesis naming change, prompts, platforms, metrics.
- [ ] Experiments are tagged with an Experiment ID across prompts, log, results.
- [ ] Prompt set has 5-10 prompts including direct, related, and control roles.
- [ ] Prompt wording is frozen for the whole test.
- [ ] Baseline window (1-2 weeks) was captured before the change.
- [ ] Follow-ups were scheduled in advance (2-4 weeks; optionally 6-8).
- [ ] A change log entry exists with date, change, type, hypothesis.
- [ ] Only one meaningful change shipped per test.
- [ ] Model/mode/login/location info and platform events are recorded.
- [ ] Results compare direct vs control movement.
- [ ] Wins required multiple prompts, 2+ follow-ups, and 2+ platforms.
- [ ] Outcome label and evidence sentence are recorded.
- [ ] Wins converted into playbooks; failures documented.

## Actions
- Create an experiment tracking sheet and Experiment ID convention. [Foundation]
- Pick the next hypothesis from the largest ch07 gap. [Quick win]
- Tag direct/related/control prompts and freeze them. [Foundation]
- Capture a 1-2 week baseline before shipping. [Foundation]
- Log platform events during test windows. [Ongoing]
- Review at fixed follow-ups and label outcomes. [Ongoing]
- Write playbooks from clear wins and guardrail notes from failures. [Ongoing]

## Pitfalls
- Calling a single changed answer a win.
- No control prompts, so drift looks like success.
- Editing prompts or timing mid-test.
- Bundling several changes in one test.
- Ignoring competitor movement (use SoV).
- Letting soft signals override core metrics.
- Judging with different login state, location, or device from the baseline.

## Related
- ch03 (baseline), ch05 (metrics, prompt database), ch06 (change log), ch07 (gaps as hypothesis source), ch14 (fixing underperformers), ch22 (myths).
