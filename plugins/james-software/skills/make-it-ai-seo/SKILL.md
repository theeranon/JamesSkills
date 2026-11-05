---
name: make-it-ai-seo
license: CC-BY-NC-4.0
metadata:
  kind: workflow
  version: 2.4.0
description: Make a website rank on Google and get cited by ChatGPT, Perplexity, Gemini and AI Overviews. Ask positioning, brand and target keywords once, audit into a checklist, plan, then fix the site. Use for ทำ SEO, ติด SEO, ออดิตเว็บ, AI SEO, AEO, GEO, ติดคีย์เวิร์ด, ให้ AI รู้จักแบรนด์.
---

# Make It AI SEO

Lock the brand's position, prove what the site lacks, then fix it until search and AI can cite it.

## Scope

- Kind: workflow
- Owns: one website's AI-search visibility job end to end: goal brief, evidence-backed audit checklist, prioritized action plan, and the in-repository fixes that plan assigns to the agent.
- Boundary: reads the site, its repository and any analytics the owner grants; writes `seo-brief.md`, `seo-audit.md`, `seo-changelog.md` and code or content changes in that project. Off-site work (reviews, PR, outreach, third-party profiles) is delivered as drafts. Publishing, sending, deploying and changing external accounts need their own authorization.

## Procedure

Knowledge lives beside this file. Load only what the current step needs.

| Path | Holds |
|---|---|
| `references/knowledge/00-index.md` | Map of 24 distilled chapter files and which question each answers |
| `references/knowledge/chNN-*.md` | Frameworks, steps, Audit checks, Actions, Pitfalls per chapter |
| `references/checklists/01-intake-questions.md` | Intake questions and the `seo-brief.md` template |
| `references/checklists/02-master-audit-checklist.md` | 320 audit items in 13 areas (A-M), each tagged with its chapter |
| `references/checklists/03-action-plan-template.md` | Scoring, report skeleton, action plan, execution rules |
| `scripts/search.py` | Local BM25 retrieval: `python3 scripts/search.py "<english query>" -k 5` from this skill directory |

1. Recon before asking. Identify the target: repository (framework, routing, head/meta handling, sitemap, robots, schema) and/or live URL (homepage, robots.txt, sitemap.xml, money pages). Read `references/knowledge/00-index.md`. Result: a short inventory of what exists.
2. Intake in one batch. Open `references/checklists/01-intake-questions.md`, pre-fill every answer the site already reveals, then ask the owner the rest once, in their language, as concrete choices with a recommendation: positioning statement, branding and tone, primary KPI, target keywords and buyer prompts, competitors, target platforms, access and permissions. Skip anything already answered in the conversation. Write `seo-brief.md` at the project root and mark unconfirmed items `assumed`.
3. Baseline. Record what is measurable now: Search Console or index state when granted, and a prompt sample of 10-30 buyer prompts from the brief on each reachable AI platform, noting brand mention, position, cited sources and competitors named (ch03, ch05). Anything unreachable is logged as a gap with the access needed, or handed to the owner as a ready prompt list.
4. Audit. Score every item in `references/checklists/02-master-audit-checklist.md` as pass, partial, fail or cannot-verify, each with evidence (URL, file and line, response capture). Area D (crawl, index, render) first because it blocks the rest. Pull deeper criteria per finding with `scripts/search.py`; run the citation-gap method in ch07 against the named competitors. Merge duplicate items from different chapters into one finding that keeps every chapter id.
5. Report and plan. Write `seo-audit.md` with `references/checklists/03-action-plan-template.md`: goal recap, baseline, scorecard per area, bullet checklist with evidence, top ten priorities, and a phased plan (weeks 1-2, weeks 3-4, days 31-90, monthly) where every item has an owner and an observable done-when.
6. Execute the agent-owned items in priority order: crawl and index blockers, server-rendered semantic HTML, titles, meta and H1, direct-answer passages, internal links and hubs, truthful schema with `sameAs`, fact hub, about and author pages, bottom-of-funnel pages (pricing, best-for, versus, alternatives, reviews), FAQ blocks, media alt text and transcripts, crawler rules. Verify each change by build, render or re-fetch and schema validation, then log date, URL, change and expected effect in `seo-changelog.md`.
7. Prepare off-site and measurement work. Draft review requests, PR pitches, profile corrections and outreach from ch16-ch20 for the owner to send. Document tracking from ch06: GA4 AI-referral channel, prompt tracker, evidence library, change log, and the monthly re-check date.

## Stop when

`seo-brief.md`, `seo-audit.md` and `seo-changelog.md` exist in the project; every checklist item carries a status with evidence or a named access gap; every agent-owned action is applied and verified or recorded with the observed blocker; and the remaining items are off-site drafts or owner decisions listed in the plan with their owner.

## Principles

**Visibility is earned off the page as much as on it** — Treat profile consistency, reviews, mentions and citations as part of the audit, not an optional extra, because AI systems assemble answers from many sources. Source: Nathan Gotch, AI SEO For Dummies, 2026
**Measure prompts, not a rank** — Judge AI visibility by repeated sampling of the same buyer prompts across platforms, because single answers vary run to run. Source: Nathan Gotch, AI SEO For Dummies, 2026
**Fix blockers before content** — Clear crawl, index and render failures before writing anything new, because unreadable pages cannot be retrieved or cited. Source: Nathan Gotch, AI SEO For Dummies, 2026
**Facts come from the owner** — Never invent statistics, reviews, credentials, prices or schema values; leave `TODO(owner)` instead. Source: standing rule in this library

## Counter-case

- The owner asks only for a list of what is wrong with the site, without changes. The audit and plan are delivered and step 6 is skipped; the repository is not touched.
- The owner asks to email ten bloggers for backlinks from the plan. The pitches are drafted, but sending them waits for the owner's explicit approval of recipients and text, because sending is outside this skill's authority.
- The question is whether one page's new FAQ block actually shipped to production. That is one completion claim at one boundary, so `dev-are-you-sure` owns it.

## Hand back

The three project files (brief, audit with plan, change log), the verified code and content changes, off-site drafts ready to send, and the measurement setup with its next check date. The owner can approve off-site actions, grant missing access, or rerun the prompt sample to compare against the baseline.

## Sources

Nathan Gotch, AI SEO For Dummies, John Wiley & Sons, 2026. Registered as `gotch-ai-seo-for-dummies-2026` in `plugins/james-productivity/packs/knowledge/sources/`. The original stays outside Git; `references/knowledge/` holds original paraphrase organized by chapter.
