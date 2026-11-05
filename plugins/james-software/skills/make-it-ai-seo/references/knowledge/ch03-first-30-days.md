---
id: ch03
title: Undertaking Your First 30 Days with AI SEO
part: "Part 1: Getting Grounded"
tags: [30-day plan, Day 0 baseline, evidence library, tracking sheet, entity verification, sameAs, quick wins, 90-day roadmap, GSC, GA4, Looker Studio, change log]
use_when: Building the week-by-week starting plan, the baseline/benchmark set, the tracking setup, or the 90-day roadmap for an AI SEO engagement.
---

# ch03 — Undertaking Your First 30 Days with AI SEO

## Core idea
- Four weekly sprints: baseline, tracking, ship quick wins, then a 90-day roadmap tied to metrics.
- Keep the system small and repeatable; every task maps to a metric and every change is logged so gains can be linked to work.
- Schema and entity cleanup help search indexes; do not claim schema alone earns AI visibility.

## Week 1 — Baseline and benchmarks
- Traditional baseline: in Google Search Console go Performance > Search results, set date range, Export; save to a "Day 0 Baseline" folder. Focus on queries/pages that already get impressions or clicks.
- AI baseline: run 10-20 relevant prompts on ChatGPT, Perplexity, Microsoft Copilot, Google AI Mode, Google AI Overviews. Classify each as cited as a source / mentioned by name / absent. Examples: local plumber ("best emergency plumber near [city]"), software ("best AI SEO tools for agencies", "[competitor] alternatives").
- Documentation: screenshot each result; record exact prompt, date, platform, model/version info.
- Verify and strengthen the entity:
  1. Own site: About, Contact, Organization/Person schema show correct name, description, logo, key URLs; if multiple domains or sub-brands, explain the relationship on About/Contact/product pages.
  2. Off-site: name, role, URL consistent on Google Business Profile, LinkedIn, Crunchbase, industry directories; fix typos, stale descriptions, old links.
  3. Structured data: add schema.org `sameAs` in Organization/Person pointing to the verified profiles (helps engines link site and profiles to one entity and may feed a knowledge graph).
- Benchmarks (pick few): AI visibility (appearance rate, first-in-list rate, citation count), traditional visibility (clicks/impressions for key pages and branded queries), operational progress (number of fixes shipped).
- Deliverables: Day 0 folder (screenshots + prompt list); updated entity info/schema; benchmark spreadsheet.

## Week 2 — Tracking setup
- Evidence library: main folder "AI SEO Tracking" with date/week subfolders; per-platform screenshots, prompt lists, notes; consistent filenames such as date_Platform_PromptTopic.png; keep Day 0 files in the same tree.
- Master tracking sheet columns: Date, Platform, Prompt, Brand coverage (Y/N), Position (First/Second/None), Citations/links shown, Notes. Retest the same prompts weekly; color-code improvements.
- Classic analytics: connect Google Search Console (impressions, clicks), GA4 (traffic, engagement on optimized pages), Looker Studio (combined organic dashboard). Classic data shows demand and where clicks still happen.
- Routine: weekly 20-minute "AI SEO Check" calendar event: retest prompts, log results, save screenshots, note changes. Maintain a separate change log (date, URL, short description of every onsite edit or publication).
- Deliverables: organized folder, master sheet, Looker Studio dashboard, recurring reminder.

## Week 3 — Ship quick wins
- Machine-verifiable facts: make company name, offer, location, contact identical across About, Contact, product/service pages; add a short Facts block near the top of main pages (company name, what you do and where, key differentiators); apply Organization, LocalBusiness, Product, FAQ schema where it fits (use exact Schema.org type names).
- Direct-answer passages: on top pages, add a 2-3 sentence stand-alone answer near the top in natural language (no keyword stuffing). Example shape: define the service, then name the company, area, and concrete differentiators (24/7, licensed, upfront fees).
- Off-site proof: update LinkedIn, Crunchbase, key review platforms; submit to credible industry directories or comparison sites; make descriptions/claims/links match the on-site facts.
- Publish one bottom-of-funnel (BoF) asset: "Best for [use case]" or "Alternatives to [competitor]"; add structured data only where natural; include simple comparisons and third-party reviews if permitted; link internally from home, product pages and relevant posts.
- Deliverables: 3-5 updated/new pages; 1 BoF asset; updated profiles/directories; before-and-after screenshots; all changes logged.

## Week 4 — Compare, prioritize, roadmap
- Compare to Day 0 across: AI (coverage rate, citation count, new mentions, best-performing prompts/topics), traditional (clicks, impressions, positions for target pages, pages that moved), operational (changes shipped, most substantial ones). Match gains to specific changes when possible.
- Pick 2-3 themes with weekly measurable outcomes:
  - Strengthen entity trust (core brand pages, profiles, Organization/Person schema).
  - Expand AI-ready content (question-matched passages, commercial and comparison pages).
  - Increase coverage across answer engines (new prompts, sources, consistent citations).
- Map every task to a metric: entity/schema updates -> consistent brand info in search/AI features; BoF content -> coverage on commercial/comparison queries; profile consistency -> recognition in search features and AI features built on those indexes.
- 90-day cadence (weekly sprints): roadmap weeks 1-4 = continue onsite optimization and entity cleanup informed by baseline; weeks 5-8 = publish and promote AI-ready, high-intent and BoF content; weeks 9-12 = expand tracking, test new prompts, double down on what worked. Hold a 30-minute Friday review: check dashboards, update sheet and library, record wins/setbacks, adjust next sprint.
- Deliverables: 90-day roadmap (themes, tasks, metrics); prioritized backlog of about 12-18 actions with owners and due dates; blocked review time; refreshed baselines.

## Templates & prompts
- Prompt list shapes to test: "best [category] for [audience]", "[brand] alternatives", "[brand] vs [competitor]", "[category] near me", "[service] pricing", "[brand] reviews", "who should I call for [problem]".
- Tracking sheet columns: Date | Platform | Model/version | Prompt | Brand coverage Y/N | Position | Cited as source / mentioned / absent | Citations shown | Accuracy | Notes | Screenshot path.
- Change log columns: Date | URL | Change description | Expected metric | Owner.
- Roadmap row: Theme | Task | Metric it moves | Owner | Due | Status.

## Audit checks
- [ ] A dated Day 0 baseline (GSC export + 10-20 AI prompt results with screenshots) exists.
- [ ] Prompt list covers best/top/near me/alternatives/vs/pricing/review/audience variants.
- [ ] Brand name, description, URL, role are identical on site and Google Business Profile, LinkedIn, Crunchbase, key directories.
- [ ] Organization (or Person) schema exists with sameAs links to verified profiles and validates without errors.
- [ ] Multi-domain/sub-brand relationships are explained on-site.
- [ ] Search Console, GA4 and a Looker Studio dashboard are connected and working.
- [ ] A master tracking sheet and evidence library exist with consistent filenames.
- [ ] A change log records every onsite edit with date and URL.
- [ ] Top pages have a 2-3 sentence direct answer near the top.
- [ ] A Facts section is present near the top of main pages.
- [ ] At least one BoF page (best-for or alternatives) is published and internally linked.
- [ ] A 90-day roadmap with 2-3 themes and a 12-18 item owned backlog exists.
- [ ] A recurring weekly check and Friday review are scheduled.

## Actions
- Export GSC performance data and run the 10-20 prompt baseline with screenshots. [Quick win]
- Audit and align entity facts across site and profiles; add sameAs. [Quick win]
- Stand up folder, tracking sheet, Looker Studio dashboard, weekly 20-minute routine. [Foundation]
- Add Facts block and direct-answer passages to 3-5 top pages. [Quick win]
- Publish one BoF page and link it from home/product/related posts. [Quick win]
- Compare against baseline and build the themed 90-day roadmap. [Foundation]
- Run weekly retests and Friday reviews. [Ongoing]

## Pitfalls
- Changing things before capturing Day 0 (no before/after proof).
- Tracking too many metrics at once.
- Inconsistent test conditions (changing prompts, platforms or wording week to week).
- No change log, so gains cannot be tied to work.
- Treating schema as an AI visibility lever by itself.
- A roadmap that is a to-do list with no metric per task.

## Related
- ch01, ch02, ch04 (entity, sameAs, schema), ch05 (metrics), ch06 (dashboard), ch08 (experiments), ch12 (BoF pages), ch17 (profiles)
