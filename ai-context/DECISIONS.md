# Decisions

Record accepted or superseded project decisions. Raw discussion remains in its source system.

## DEC-001 — One canonical instruction body

- Date: 2026-08-28
- Status: Accepted
- Decision: Each skill has one canonical `SKILL.md`. Compatibility aliases and vendor adapters may add discovery metadata but may not duplicate behavior.
- Why: duplicated instructions drift and make different agents follow incompatible rules.
- Source: repository v0.3.0 architecture and accepted maintainer rules.
- Affects: `catalog.json`, `skills/`, `aliases/`, `adapters/`, `AGENTS.md`.
- Supersedes: divergent provider-owned skill bodies.

## DEC-002 — Candidate Card before promotion

- Date: 2026-08-29
- Status: Accepted
- Decision: A new skill name, alias, framework hierarchy, or promotion state requires an approved Candidate Card, cross-case evidence, failure cases, and a legitimate counter-case.
- Why: general permission to improve the library previously caused premature names, invented framework boundaries, and overfit packages.
- Source: owner corrections and repository v0.7.1 lifecycle repair.
- Affects: `catalog.json`, `AGENTS.md`, `tests/test_portfolio_lifecycle.py`, `tests/behavioral-cases.md`.
- Supersedes: treating repository-wide improvement authority as naming approval.

## DEC-003 — Private portable repository with local release gates

- Date: 2026-08-28
- Status: Accepted
- Decision: Keep JamesSkills private by default, distribute promoted packages through managed local links, and validate with repository-owned pre-commit and pre-push gates instead of GitHub Actions.
- Why: the same reviewed source must travel across machines and agents without paid runner dependency or silent platform-specific copies.
- Source: owner direction and repository install/update history.
- Affects: `README.md`, `scripts/install`, `scripts/update`, `scripts/doctor`, `.githooks/`.
- Supersedes: GitHub Actions as the required validation path.

## DEC-004 — Source and live-state boundary

- Date: 2026-08-28
- Status: Accepted
- Decision: Store reusable process knowledge, reviewed source metadata, original paraphrase, applications, and limitations; exclude credentials, client data, chat exports, live JamesOS state, and copyrighted originals by default.
- Why: the portable library must remain safe to clone and must not turn private operational state into reusable prompt content.
- Source: accepted repository boundary and knowledge-library release rules.
- Affects: `PROJECT.md`, `README.md`, `AGENTS.md`, `packs/`, `scripts/validate`.
- Supersedes: None.

## DEC-005 — Apply project-standard to its own repository

- Date: 2026-08-29
- Status: Accepted
- Decision: JamesSkills must maintain the four minimum project-standard owner files and the ready check must run inside the normal validator.
- Why: a promoted shared standard is not credible when its source repository does not pass that standard itself.
- Source: direct owner correction in the current project review.
- Affects: `PROJECT.md`, `STATUS.md`, `AGENTS.md`, `docs/DECISIONS.md`, `scripts/validate`.
- Supersedes: documenting project-standard as available while leaving this repository outside its gate.

## DEC-006 — One human skill handbook

- Date: 2026-08-29
- Status: Accepted
- Decision: Maintain `docs/SKILLS.md` as the single human navigation guide, grouped by the moment of use and linked to each canonical package. Keep behavior authoritative in each `SKILL.md` and lifecycle authoritative in `catalog.json`.
- Why: a raw catalog and scattered instruction files do not let James browse and choose skills as clearly as the AI Hero model.
- Source: direct owner request for an AIHero-style guide in the current project review.
- Affects: `README.md`, `docs/SKILLS.md`, `catalog.json`, `tests/test_skill_handbook.py`.
- Supersedes: the short README vocabulary list as the only human guide.

## DEC-007 — Three promoted transformation-design skills

- Date: 2026-08-29
- Status: Accepted
- Decision: Promote `build-framework`, `transformation-journey`, and `learning-experience-design` as the three canonical responsibilities. Reverse `design-the-journey` and `design-the-course` into compatibility aliases. Route by accountable outcome, not duration.
- Why: reusable company IP, macro organization transformation, and bounded learning intervention are different objects that require different evidence and ownership.
- Source: accepted owner decisions from the completed transformation-design grilling session and the approved Candidate Cards.
- Affects: `CONTEXT.md`, `catalog.json`, `skills/core`, `aliases`, `packs/frameworks`, `docs/SKILLS.md`, and learning-design regressions.
- Supersedes: the two uninstalled `design-*` pilots and the unresolved LED/TPS hierarchy. TPS is one framework inside LED.

## DEC-008 — Skill-first V1 with cited HTML proof

- Date: 2026-08-29
- Status: Accepted
- Decision: Complete and prove the three portable skills before building an organization application. Each skill must produce a purpose-specific, cited, executive HTML artifact and pass source, routing, behavior, visual, and install gates.
- Why: the immediate outcome is reliable skill behavior. UI, API, employee rollout, and advanced approval design do not improve V1 call accuracy and would delay proof.
- Source: direct owner correction after the architecture discussion expanded beyond the approved scope.
- Affects: `PROJECT.md`, `AGENTS.md`, HTML assets, tests, and release sequencing.
- Supersedes: treating organization UI, public API, client portal, or multi-role approval as part of this release.

## DEC-009 — HTML-only unless PDF is explicitly authorized

- Date: 2026-08-29
- Status: Accepted
- Decision: An HTML request, including A4 or print-ready HTML, delivers HTML only. Browser print emulation is the normal visual proof. Create PDF only when James explicitly requests it or an authoritative recipient constraint requiring one fixed print file is directly confirmed; never infer that need from presentation language.
- Why: automatic PDF export consumed extra execution and review work without serving the requested outcome, and a legacy duplicate meeting-summary skill kept reviving that behavior.
- Source: direct owner correction during the 0.9.0 release audit.
- Affects: `make-it-james`, `final-it`, `sum-meet`, `one-page-pls`, render tests, and local discovery installation.
- Supersedes: automatic HTML-plus-PDF delivery and PDF-based HTML QA.

## DEC-010 — project-standard v2: ai-context layout, generated SRS, spec lock

- Date: 2026-09-01
- Status: Accepted
- Decision: `project-standard` moves every contract file except `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`README.md` under `ai-context/`; adds a generated `ai-context/SRS.html` view rendered by `render-srs` from `PROJECT.md` + `DATA_MODEL.md`; adds a `Spec lock` field in `STATUS.md` (`Open` or `Locked (date, hash)`, set via `lock-spec`) enforced by `check`; adds a reverse-SRS/cross-model audit workflow step, a structured permission (role × action) matrix in `DATA_MODEL.md`, a non-functional-requirements table in `PROJECT.md`, and an opt-in per-module requirement breakdown. JamesSkills migrated its own root-level `PROJECT.md`/`STATUS.md`/`docs/DECISIONS.md` into `ai-context/` in the same change so `scripts/validate` keeps passing.
- Why: derived from a production-readiness workflow taught in a private training session — reverse-generating a spec from shipped code, prioritising a permission matrix over generic security language, cross-vendor audit to avoid same-model bias, and a standard project document set — evaluated against the existing skill, which was found to have four genuine gaps. The scattered root-level files were also a standing owner complaint. `SRS.html` and `Spec lock` were owner-directed additions rather than sourced from that material.
- Source: a private training transcript held outside this repository, plus direct owner decisions in the authoring session.
- Affects: `plugins/james-software/skills/project-standard/` (`SKILL.md`, `references/contract.md`, all asset templates, `scripts/project_standard.py`, `tests/`), this repository's own `ai-context/PROJECT.md`, `ai-context/STATUS.md`, `ai-context/DECISIONS.md`, `AGENTS.md`.
- Supersedes: the v1 flat root layout (`PROJECT.md`/`STATUS.md`/`docs/DECISIONS.md`/`ARCHITECTURE.md`/`DATA_MODEL.md` at repository root); migration steps for other v1 projects are recorded in `references/contract.md`'s "Migrating a flat-layout (v1) project into `ai-context/`" section.

## DEC-011 — Fixed a silent content-loss bug in render-srs, found by a workspace-wide state test; added an automated `migrate` command

- Date: 2026-09-01
- Status: Accepted
- Decision: `render_srs`'s heading parser (`extract_section`) now (a) tolerates a trailing annotation on the same heading line — a date stamp or parenthetical note no longer breaks the match, fixing a regex bug where `.*` under `re.DOTALL` swallowed the rest of the document instead of just the heading's own line, and (b) distinguishes "heading not found at all" from "heading found, content genuinely not confirmed": a missing heading now prints a `WARN` per section and renders a visibly flagged banner in `SRS.html`, instead of silently defaulting to `Not confirmed` as if the content had been checked and found empty. Also added `project_standard.py migrate <root>`, a single entry point that bootstraps a project with no existing contract, auto-moves legacy root files into `ai-context/` and repoints every known cross-reference once their headings already match the template, and otherwise reports (exit 2) exactly which headings are missing per file it leaves in place — never guessing at a content rewrite.
- Why: owner asked to state-test `project-standard` v2 against every real project under `AI Workspace/` before trusting the earlier "comprehensive, not overfit, generalizes, old projects can migrate" claim. A read-only audit agent tested `extract_section` against 6 real documents, including the closest real match to the tool's own template (`InvestNow/trading/.../investment-engine/PROJECT.md`, which uses the tool's exact target filename and heading text): 0/6 rendered fully — even the best case failed on `## Requirements (อัปเดตตาม PHP Architecture Pivot 2026-09-01)` because of the trailing annotation. Before the parser fix, a naive v1→v2 migration on any real project in the workspace would have produced an `SRS.html` that looked complete but silently dropped every section with a differently-worded or annotated heading, with no error signal. The migration itself was also manual (move files, hand-edit pointers) with no tooling to actually execute it or to distinguish a clean v1 project from one needing content rewritten first — `migrate` closes that gap for the mechanical part while deliberately refusing to guess at the judgment-call part.
- Source: a read-only audit across the owner's other repositories, which confirmed that none had migrated to the `ai-context/` layout at the time.
- Affects: `plugins/james-software/skills/project-standard/scripts/project_standard.py` (`extract_section`, `section_prose_or_table`, `render_srs`, `render_srs_command`, new `migrate`/`heading_present`/`repoint_text`/`LEGACY_CANONICAL_HEADINGS`/`LEGACY_OPTIONAL_HEADINGS`/`REPOINT`), `plugins/james-software/skills/project-standard/tests/test_project_standard.py`, `plugins/james-software/skills/project-standard/references/contract.md`, `plugins/james-software/skills/project-standard/SKILL.md`, `plugins/james-software/skills/project-standard/assets/AGENTS.template.md`.
- Supersedes: DEC-010's implicit claim that `render-srs` works against any project once files are moved into `ai-context/`, and that migration was "additive... no rename" with no automated command behind it. `render-srs` now works once a project's `PROJECT.md`/`DATA_MODEL.md` use the canonical template headings (trailing annotations tolerated) and loudly flags what it can't parse; migration for a canonical-headed v1 project is now a single automated command, and migration for a foreign-headed pre-existing document is explicitly still a human/agent judgment call, reported precisely rather than silently attempted.

## DEC-012 — README Architecture & Anti-Bloat Standard

- Date: 2026-09-03
- Status: Accepted
- Decision: Adopt `ai-context/README_STANDARD.md` as the enforceable law for `README.md`. The root README is strictly the human onboarding and public entry point ("Front Door"). It must feature an iconic 3-4 skill Before/After showcase and a single, scannable catalog table covering all canonical skills, while routing exhaustive technical deep dives to `docs/SKILLS.md` per DEC-006. Embedding 20+ full HTML tables and decorative AI-generated images on the root landing page is formally prohibited.
- Why: Teamwork subagents bloated `README.md` to 46KB and 800+ lines with 30 auto-generated PNG diagrams and juvenile "AI วิ่งเล่นทุ่งลาเวนเดอร์" tables. This destroyed GitHub scannability, slowed page render times, and violated open-source readability standards benchmarked against top AI repos (Fabric, Anthropic Skills, vLLM).
- Source: direct owner correction on README standards and industry benchmark comparison.
- Affects: `README.md`, `ai-context/README_STANDARD.md`, `tests/test_readme_verification.py`.
- Supersedes: the bloated multi-table README layout authored by the teamwork subagents.

## DEC-013 — Every skill states its own bounded job, its exclusions, and its named principles, enforced by a schema

- Date: 2026-09-05
- Status: Accepted
- Decision: Adopt `docs/SKILL-SCHEMA.md` as the mandatory shape for every canonical `SKILL.md`, enforced by `tests/test_skill_schema.py` inside `scripts/validate`. Each file declares a `kind` (workflow, mode, shared-standard, output, knowledge-lens, internal-routing), a stance line, `## Scope` with an explicit authority boundary, `## Do not use this when` where every excluded case names the sibling that owns it, a kind-specific middle section and exit condition, `## Principles` written as original paraphrase with attribution, `## Counter-case`, and `## Hand back`. Body length is capped per kind because modes and shared standards stack with the primary workflow at delivery time. All 21 v1 skills were rewritten to the owner's own definitions; `are-you-sure` split into a business track plus `dev-are-you-sure` for software, taking the roster to 22, and `prove-it` was renamed `research-it` with `prove-it` retained as an alias.
- Why: the owner asked whether each skill could be sharper, more clearly bounded, and more generic without overfitting. A 28-agent analysis found 159 concrete defects across the 21 files, led by unfalsifiable instructions (36), rules copied from a sibling skill (32), missing stop conditions (20), and authority a skill's job did not require (16). Separately, the seven skills with no entry in `tests/behavioral-cases.md` were exactly the seven that had drifted furthest from the owner's intent, which identified the behavioral case as the mechanism that actually holds a definition in place. The owner then dictated the real definition of each skill; agent-derived definitions were correct for only one of the first six checked, so the owner's statements govern and the analysis was used only for defect detection and the schema. `prove-it` was the clearest case: its entire file described deployment verification, which by the owner's definition belongs to `dev-are-you-sure`, while its actual job of gathering outside evidence appeared nowhere in the file.
- Anti-overfit mechanism: the validator builds a boundary graph from every `## Do not use this when` entry and fails when any skill has in-degree zero. A skill no sibling ever excludes toward does not have a distinct job. At least one counter-case per skill must name the owning sibling; the remainder may be permission counter-cases, a legitimate request the rule must still allow.
- Source: owner definition interview conducted on 2026-09-05 in this session, plus a 28-agent defect and schema analysis whose per-skill digests informed the rewrites.
- Affects: all 22 canonical `SKILL.md` files, `catalog.json` (`schema_version` 2, `kind` per entry), `aliases/prove-it/`, `docs/SKILL-SCHEMA.md`, `docs/SKILLS.md`, `tests/test_skill_schema.py`, `tests/behavioral-cases.md`, `tests/test_core_composition_contracts.py`, `tests/test_readme_verification.py`, `plugins/james-software/skills/catchup/assets/catchup-report.html`, `README.md`, `AGENTS.md`.
- Supersedes: the v1 freeform `SKILL.md` layout, in which files ranged from 14 to 111 lines with no shared structure, no declared authority boundary, and no requirement to name the sibling owning an excluded case.

## DEC-014 — Repaired the release gates, which had been silently inert since the plugin migration

- Date: 2026-09-05
- Status: Accepted
- Decision: Point `scripts/validate` and `scripts/doctor` at `plugins/` instead of the now-empty `skills/` directory, and teach `doctor` the plugin-link layout the installer uses for Gemini and Antigravity. Stamp `project-standard/1.0` into every generated SRS and into `check` output so a project states which contract version it follows.
- Why: after the 3-pillar plugin migration the installer was updated but the gates were not. `validate` was finding 7 `SKILL.md` files instead of 28, running 0 of 7 per-skill test suites, and linting 0 of 3 HTML assets, while still printing PASS. Re-enabling the suites surfaced a real failure in `test_baseon.py`, whose repository-root path was one directory short. `doctor` was checking the pre-migration canonical path and reported 110 false issues, including 22 phantom missing links per Gemini root where the installer deliberately links whole plugins instead. The owner also asked to be able to tell which version of the project standard a given project follows, which nothing recorded.
- Source: gate audit performed while implementing DEC-013.
- Affects: `scripts/validate`, `scripts/doctor`, `plugins/james-productivity/skills/baseon/tests/test_baseon.py`, `plugins/james-software/skills/project-standard/scripts/project_standard.py`, `ai-context/PROJECT.md`.
- Supersedes: the post-migration assumption in `ai-context/STATUS.md` that REQ-002 and REQ-008 were verified; the evidence behind both claims had stopped running.

## DEC-015 — The transformation-design portfolio left this repository for SecondBrain

- Date: 2026-09-05
- Status: Accepted
- Decision: `build-framework`, `transformation-journey`, and `learning-experience-design` are owned by the SecondBrain repository and are no longer part of JamesSkills. Removed from this repository: REQ-009 in `ai-context/PROJECT.md` and its status row, the three behavioral-case sections, the `framework-library` pack and `packs/frameworks/`, the transformation-design release receipt and its example renderer, the transformation-design paragraphs in `README.md`, and the AGENTS rules governing house frameworks, journey-versus-experience routing, and transformation-design output readiness. `CONTEXT.md` was reduced to the vocabulary this repository still uses: framework, source, lens, and the four evidence layers.
- Why: the owner confirmed the two repositories are separated. The stale references were not cosmetic. REQ-009 named `skills/core/build-framework` and two sibling paths that do not exist here, `skills/` in this repository is empty, and `ai-context/STATUS.md` still reported REQ-009 as Verified, so the contract asserted evidence for packages it does not contain. `packs/frameworks/registry.json` held one entry whose only source locator pointed into `skills/core/learning-experience-design/`, and no skill remaining in this repository read it.
- Boundary: dated historical records were deliberately left intact — `CHANGELOG.md`, the authoring session's research notes, `tests/receipts/runtime-routing-v0.9.0.md`, and earlier entries in this file describe what was true on their dates. Editing them would falsify the record rather than remove drift. Only current-state and executable references were removed.
- Affects: `ai-context/PROJECT.md`, `ai-context/STATUS.md`, `catalog.json`, `CONTEXT.md`, `AGENTS.md`, `README.md`, `tests/behavioral-cases.md`, `packs/frameworks/` (deleted), `tests/receipts/transformation-design-v0.9.0.json` (deleted), `tests/render_transformation_design_examples.cjs` (deleted).
- Supersedes: DEC-009's placement of the transformation-design portfolio in this repository, and REQ-009 in full.

## DEC-016 — Registered the Satir Model as a lens, with its evidence problem recorded as prominently as its method

- Date: 2026-09-05
- Status: Accepted
- Decision: Registered `satir-model` as a reviewed-private lens at `packs/knowledge/lenses/satir-model`, backed by three source cards: the 1991 book by Satir, Banmen, Gerber and Gomori; Banmen's 2002 paper in Contemporary Family Therapy; and the International Coaching Federation's 2018 referral guidance. Rewrote `coach-me` to resolve the lens through `baseon`, to open by reading the coping stance and entering where that stance can actually be reached, to stress-test the new belief against the original provocation, and to close with a rehearsed action and a review date. Added an explicit referral rule, which the skill previously did not have at all.
- Why: the owner asked for the model to be researched properly rather than treated as family therapy, and to be brought current. Five findings changed the skill. First, the spelling was corrected to `Satir`; the variant previously carried in house notes is an unrelated Sanskrit word and is now removed from the library. Second, attribution: the Personal Iceberg Metaphor was co-created by John Banmen from observing Satir's work, not published by Satir herself. Third, naming: `STST` is the clinical application's name and would misrepresent a coaching frame, so the umbrella term `Satir Model` is used. Fourth, the coping stances carry a documented entry point each, which is the single most operationally useful part of the model and was absent from the skill. Fifth, and most consequential, no Satir body publishes any guidance on when a non-clinical practitioner must stop and refer; that gap is why the boundary rule is sourced from coaching-profession guidance instead.
- Evidence posture: the lens states plainly that the model is not evidence-based in any setting. There is no meta-analysis, no Cochrane review, and no listing in the APA Division 12 list, the California Evidence-Based Clearinghouse, or NICE. About six confounded trials exist; the most informative found self-esteem improved while family functioning came back null. No published instrument measures any iceberg level. No outcome study exists for organisational or coaching use. The `Satir Change Model` circulating in agile is Gerald Weinberg's rendering with a later web author's added resistance stage and performance axis, and breaks from the original in four documented ways. One untraceable statistic about congruent leadership and turnover is named in the lens as never to be repeated.
- Rights posture: `VIRGINIA SATIR` is a live US service mark held by the Virginia Satir Global Network for training services, registration 4670492. The concept names are not claimed as marks. The lens records concept names, original paraphrase, application notes, and citations only. Book text, official diagrams, assessment instruments, and the institute's paid question booklet stay out, and nothing describes this work as certified or endorsed.
- Source: two research passes conducted on 2026-09-05 against primary institute material, the Banmen 2002 paper, USPTO records, evidence registries, and the software and agile literature.
- Affects: `packs/knowledge/registry.json`, three new source cards, `packs/knowledge/lenses/satir-model/`, `plugins/james-productivity/skills/coach-me/SKILL.md`.

## DEC-017 — Claude Code loads this library as plugins; the installer enforces one route

- Date: 2026-09-05
- Status: Accepted
- Decision: On Claude Code the three pillars are installed as plugins and are the single source of every canonical skill. `scripts/install` detects the pillars in Claude Code's `installed_plugins.json`, then writes only aliases into `~/.claude/skills` and removes any canonical link this repository previously owned there. When the plugins are absent it links every skill as before, so a fresh clone still works. Codex, Cursor, and the shared `.agents` root keep live links unchanged. `scripts/doctor` reports the mode and fails on any canonical link left shadowing an installed plugin. The `Satya` spelling was removed from the library in the same change.
- Why: the owner opened the Claude plugin page, did not find the library, and chose the plugin route. Both routes at once install every skill twice; with both active a skill was observed rendering without its description. The duplication is not avoidable by configuration: an installed plugin is a directory copy, verified for both a GitHub-sourced and a local-path-sourced marketplace, so it cannot be made to track the working tree.
- Cost accepted: the plugin copy is a snapshot. Editing a skill no longer reaches Claude Code until the plugin is reinstalled. `claude plugin update` is not the mechanism: it compares version numbers rather than content, and after an ordinary edit it reports the plugin is already current and copies nothing. `scripts/refresh-claude-plugins` reinstalls each pillar, which is what actually re-copies the files, and no-ops where live links are in use. The owner accepted that in exchange for the library appearing in the plugin interface. Aliases stay as links because they live outside the pillars and have no plugin counterpart, so they cannot collide.
- Affects: `scripts/install`, `scripts/doctor`, `README.md`, `packs/knowledge/lenses/satir-model/index.md`.
- Supersedes: the DEC-015 installer behaviour of always linking every canonical skill into `~/.claude/skills`.

## DEC-018 — The repository is public under CC BY-NC 4.0, and internal material was removed

- Date: 2026-09-05
- Status: Accepted
- Decision: `theeranon/JamesSkills` is public and licensed under Creative Commons Attribution-NonCommercial 4.0 International. `LICENSE` carries the canonical legal code; `NOTICE` states the copyright holder, the scope, how to attribute, what NonCommercial means in practice, and the third-party material that is not licensed here. The SPDX identifier is stamped into `.claude-plugin/marketplace.json` and all three plugin manifests. Internal material was removed from the working tree.
- Why: GitHub reported the repository PUBLIC, and had since it was created on 2026-08-27, while `LICENSE`, `ai-context/PROJECT.md`, `ai-context/STATUS.md` and the README all described it as private. Nine days of exposure with zero stars and zero forks. The owner chose to keep it public, remove the internal material, and move toward marketplace distribution. The previous all-rights-reserved licence was incompatible with that: a marketplace distributes by definition, so anyone installing would have been in breach.
- Removed: four internal audits under `research/` carrying the owner's own operating failure rates across seven months, a reference to a bank client engagement, and quoted private remarks; thirteen throwaway migration scripts at the repository root; a named guest expert, a class transcript filename, a private scratch path, and an inventory of the owner's other repositories from `ai-context/DECISIONS.md` and `CHANGELOG.md`.
- Kept: `research/2026-08-28-framework-knowledge-source-audit.md`, which is a registered knowledge source cited by its source card rather than internal material. The library validator rejects raw files under `packs/knowledge/sources/`, so it stays where its card points, and `research/README.md` now states what may live in that directory.
- Known limit: removal affects the working tree only. Six commits touching `research/` remain readable in public history. Rewriting that requires a force-push over published history and was not done.
- Affects: `LICENSE`, `NOTICE`, `README.md`, `.claude-plugin/marketplace.json`, all three plugin manifests, `ai-context/PROJECT.md`, `ai-context/STATUS.md`, `CHANGELOG.md`, `research/`.
- Supersedes: the all-rights-reserved licence, and every statement in this repository that it is private.

## DEC-019 — Knowledge packs travel inside the plugin that uses them

- Date: 2026-09-05
- Status: Accepted
- Decision: `packs/` and the one cited research document moved from the repository root into `plugins/james-productivity/`, beside the skills that read them. `scripts/package-plugins` copies both into the archive. The knowledge library's discovered root is now the plugin rather than the repository.
- Why: a publishability audit found `/baseon` and its four lens aliases non-functional in every distributable artifact. `discover_repo_root` walks ancestors for `packs/knowledge/registry.json`; with `packs/` at the repository root it was absent from both the built archive and the installed Claude plugin, so every library read failed. Reproduced before the fix as `FAIL registry missing`, and verified after it by unpacking the archive outside any clone and running `list` and `validate` successfully. Six of twenty-two skills were broken in exactly the route the README recommends.
- Second defect closed by the same move: `coach-me` carries the Satir-derived question sequence in its own body while pointing at `packs/knowledge/lenses/satir-model` for the limitations and the trademark disclaimer. That directory was not in the shipped plugin, so the paraphrase travelled and the rights posture and the mandatory "not evidence-based in any setting" caveat did not. Both now ship together.
- Also corrected: `.claude-plugin/marketplace.json` still described the library as private, which is the first string a browsing installer reads, and `README.md` pointed at a research file that had been deleted as internal material and was reachable only through public history.
- Affects: `plugins/james-productivity/packs/`, `plugins/james-productivity/research/`, `catalog.json`, `scripts/package-plugins`, `.claude-plugin/marketplace.json`, `README.md`, the baseon test's root resolution.

## DEC-020 — Cleared four of the five publication blockers without an owner decision

- Date: 2026-09-05
- Status: Accepted
- Decision: Four items previously escalated to the owner were resolved directly. (1) The private-training provenance behind `project-standard` v2 is not a third-party rights question: the transcript is SolutionsIMPACT's own class, with an invited guest presenting, and the four features taken from it are methods rather than expression. (2) The licence keeps CC BY-NC 4.0 on the substance, as chosen, and additionally offers Apache-2.0 on the utility code in `scripts/`, `tests/`, `mcp-server/`, `adapters/`, and per-skill script directories, because Creative Commons advises against applying its licences to software. (3) The two Dynamics lenses no longer reproduce the source's own arrangement of profiles or the colour-level sequence; they name the model, cite the page, and describe the use, matching the posture the Satir lens already used. (4) Operating references to the owner by name are gone from the shipped skills, the knowledge packs, and the behavioral cases; the brand names `JamesSkills`, `make-it-james`, and `make-it-james-ux` remain, because a house style is legitimately named after its author.
- Why: the audit escalated all five to the owner. On inspection only one genuinely required a decision. The provenance question was manufactured by this repository's own sanitisation, which stripped the company name and left the audit unable to tell whose class it was. The rights question on the Dynamics packs had a fix that removes the exposure without needing counsel. The licence and the personal references were straightforward edits.
- Behavioral guard changed rather than removed: `test_baseon.py` previously asserted the personal phrasing of the limitation. It now asserts the rule — a generic pack is never anyone's personal assessment, and a stored label stays a working hypothesis until its subject confirms an official report — and additionally fails if the limitations file names a person.
- Remaining owner decision: rewriting public git history. A class transcript, a brand specification, and internal operating audits are still retrievable from published commits, and a working-tree deletion does not remove them from a public host.
- Affects: `NOTICE`, `plugins/james-productivity/packs/knowledge/lenses/wealth-dynamics/`, `.../wealth-spectrum/`, `plugins/james-productivity/skills/baseon/references/pack-contract.md`, `plugins/james-productivity/skills/grill-me/references/interactive-html.md`, `tests/behavioral-cases.md`, `plugins/james-productivity/skills/baseon/tests/test_baseon.py`.

## DEC-021 — Rewrote public git history to remove material that a file deletion could not

- Date: 2026-09-05
- Status: Accepted
- Decision: Purged `scratch/`, the root `research/`, and `packs/solutionsimpact/` from every commit with `git filter-repo`, then force-pushed. Removed from public reach: a full private-class transcript, a brand specification, and internal operating audits naming eight background daemons, an advertising spend deadline, and the owner's own error rates over seven months. Sixty-two commits of development history remain intact. The one cited research document survives at its new path inside `plugins/james-productivity/research/`.
- Why: the owner instructed that internal material be removed. On a public host a working-tree deletion is not a removal, and the content was still retrievable with `git show`. The window was unusually clean: the repository had zero forks and zero stars, so no third party held a copy to keep the old objects alive.
- Verified: a fresh `git clone` from GitHub contains zero matches for the purged paths, `git log --all` finds no commit touching any of them, and `scripts/validate` passes from that clean clone.
- Recovery: a full `git bundle --all` of the pre-rewrite repository was taken first and a `backup-before-history-rewrite` branch was created. Both are local only and are not published.
- Known limit: GitHub can continue to serve an orphaned commit by its exact SHA until it garbage-collects, and cached views may persist. Anyone wanting that content would need a SHA they could only have obtained before the rewrite. Ask GitHub Support to purge the cache if that residual matters.
- Affects: every commit in the repository. All hashes changed.

## DEC-022 — `skill-router` renamed to `hand-it-off`, its public name resolved

- Date: 2026-09-05
- Status: Accepted
- Decision: The internal-routing skill previously named `skill-router` is now canonically `hand-it-off`, taken from its own opening line ("Find the one owner, hand over, and get out of the way"). `skill-router` remains as a compatibility alias resolving to `hand-it-off`, following the same pattern as `prove-it` -> `research-it`. Every canonical reference — catalog.json, docs/SKILLS.md, README.md, the four tests that read the router file, and the two sibling skills (`baseon`, `never-again`) that route a Candidate Card to it — now uses the new name.
- Why: STATUS.md had carried "a public name for skill-router remains unapproved" as an open item since the v2 rewrite. The owner asked directly for a public name. `hand-it-off` was chosen over generic alternatives (dispatcher, router, traffic-control) because it names the mental move in the same imperative-phrase family as the rest of the roster (`done-for-me`, `research-it`, `final-it`) rather than reading as internal jargon, while still being unlikely to be typed as a direct command — its own file and docs/SKILLS.md both still state it is agent support, not a recommended human slash command.
- Affects: `plugins/james-core/skills/hand-it-off/` (renamed from `skill-router`), `aliases/skill-router/` (new), `catalog.json`, `docs/SKILLS.md`, `README.md`, `tests/test_catchup_contracts.py`, `tests/test_portfolio_lifecycle.py`, `tests/test_core_composition_contracts.py`, `tests/test_skill_handbook.py`, `plugins/james-productivity/skills/baseon/SKILL.md`, `plugins/james-core/skills/never-again/SKILL.md`, `ai-context/STATUS.md`.
- Supersedes: the unresolved naming item in `ai-context/STATUS.md`'s Need decision section.

## DEC-023 — Reverted a fabricated installer rewrite that broke Cursor, Codex, and .agents

- Date: 2026-09-05
- Status: Accepted
- Decision: Removed a set of commits (`274076f` through `b2166e2`) that rewrote `scripts/install.py`, `install.bat`, and README to invoke a `codex plugin marketplace`/`codex plugin add` CLI, write a fabricated `plugins.json` config to every platform's home directory, and hard-copy entire plugin trees into `~/.cursor/plugins`, `~/.codex/plugins`, and `~/.agents/plugins` — directories none of those tools read. Rewrote `scripts/install.py` to mirror the proven bash `scripts/install` logic exactly (the same `installed_plugins.json` duplicate-avoidance check, real per-skill symlinks, Windows junctions), rewrote `tests/test_installer_contracts.py` to assert the correct behavior instead of the fabricated one, deleted `docs/UNIVERSAL_PLUGIN_STANDARD.md` and the two stray `plugins/<pillar>/plugin.json` files it required at the wrong path, removed the false "verified on macOS & Windows" and "guarantees" language from README along with an instruction telling readers to have an AI agent autonomously clone and execute the installer, and removed the two now-orphaned images.
- Why: `scripts/doctor` went from 0 issues to 99 after this installer ran on this machine — Cursor, Codex, and `.agents` each dropped from 22 working skills to 0, because the rewrite deleted the correct existing symlinks and replaced them only with 9 alias stubs pointing at skills that no longer had symlinks. The owner reported the breakage after another agent session, asked to diagnose it and told an incorrect story ("slash commands can never work in any chat UI, always use natural language instead") that was directly contradicted by this session's own working `/james-core:...` invocations. The actual cause was a different agent session fabricating a Codex CLI surface and a `plugins.json` config format that do not exist, verified against this repository's own earlier dedicated research into official distribution channels, and shipping it with unverified "guaranteed" language.
- Evidence: `codex plugin marketplace`/`codex plugin add` do not appear in any source this repository's distribution-channel research located. `~/.claude/plugins/installed_plugins.json` is the real, previously-verified Claude Code state file; a bare `plugins.json` with an `entries` array is not read by Claude, Cursor, Codex, or Gemini. Reproduced the break, then reproduced the fix: `./scripts/doctor` returned to canonical=22 with 0 broken/missing/collisions across all six discovery roots after the corrected installer ran.
- Affects: `scripts/install.py`, `install.bat`, `tests/test_installer_contracts.py`, `README.md`, `docs/UNIVERSAL_PLUGIN_STANDARD.md` (deleted), `plugins/*/plugin.json` (deleted, wrong path), `assets/universal_install_guide.jpg` and `assets/claude_desktop_install_guide.jpg` (deleted, now orphaned), `AGENTS.md`, `ai-context/LESSONS.md` (new).
- Supersedes: commits `274076f`, `d77fa02`, `6a9e0b2`, `bc1e100`, `f1be139`, `4017adb`, `5693ca3`, `5a00eda`, `b2166e2`.

## DEC-024 — Codex CLI has a real plugin marketplace; fixed the duplicate it caused

- Date: 2026-09-05
- Status: Accepted
- Decision: Corrected DEC-023's own research gap. Codex CLI 0.147.0+ genuinely reads `.claude-plugin/marketplace.json` and installs plugins natively — confirmed live: `codex plugin list` showed `james-core@james-skills` etc as "installed, enabled", and `codex exec` logged "Codex can still see every skill" before any unrelated model-selection error. This means Codex was loading all 22 skills through two parallel paths at once: its own real plugin mechanism, and the loose per-skill symlinks this installer also writes into `~/.codex/skills`. The owner's own screenshot showed the result: `proactive-habits` and `proactive-dev` each listed twice in Codex Desktop's command picker. Added the same duplicate-avoidance branch already used for Claude: `scripts/install`, `scripts/install.py`, and `scripts/doctor` now check `~/.codex/config.toml` for a `[plugins."<name>@james-skills"]` entry (Codex's real, confirmed state file — TOML, not JSON) and, when present, write only aliases into `~/.codex/skills` and remove any canonical link this repository owns there.
- Why: verified by direct, repeated interaction, not assumption — the prior DEC-023 lesson about not asserting an unverified CLI surface was itself at risk of being applied backwards here (assuming Codex had no marketplace CLI, when it demonstrably does). Re-ran `./scripts/install` after the fix and confirmed `proactive-habits` no longer exists as a loose file under `~/.codex/skills`, reachable only through Codex's own plugin. `./scripts/doctor` reports `~/.codex/skills via plugins=3 aliases=9 duplicates=0`.
- What remains unverified: Codex Desktop must be restarted to clear its cached command list before the fix is visible in its UI — this was communicated to the owner. Claude Desktop (`com.anthropic.claudefordesktop`) could not be tested; it is blocked from computer-use control for self-modification safety, and its own `local-agent-mode-sessions/skills-plugin` staging area was found to hold the account-level claude.ai Skills feature (unrelated skill names), not this repository's plugins — there is no evidence it reads `~/.claude/plugins/installed_plugins.json`. Antigravity's files are correctly placed (`doctor` reports 0 issues) but live invocation could not be confirmed: neither `/` command search nor `@` mention lists skills by name in the tested build, and a functional natural-language test was blocked by the account's own model quota, unrelated to this fix.
- Affects: `scripts/install`, `scripts/install.py`, `scripts/doctor`, `tests/test_installer_contracts.py`.
