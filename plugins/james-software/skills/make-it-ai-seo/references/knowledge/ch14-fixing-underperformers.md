---
id: ch14
title: Fixing Underperformers
part: Part 3: Building Content That Gets Chosen
tags: [underperforming pages, page diagnosis, search intent, on-page SEO, title tag, headings, scannability, competitor outline, content gaps, internal links, change log, measurement window]
use_when: A page gets impressions but few clicks, ranks on page 2, does not convert, or is rarely cited in AI answers, and you need to diagnose, fix and measure it.
---

# ch14 — Fixing Underperformers

## Core idea
- A weak page matters to the business but fails at its job (clicks, conversions, rankings, AI mentions or citations). Diagnose before editing; blind rewrites waste time.
- Fix one main bottleneck at a time, log it, wait the right window, then measure against a pre-defined success metric.

## Pick pages worth fixing
- Prioritize pages that: get high impressions with low clicks; sit on page 2 or low page 1; get traffic without conversions; target valuable topics yet keep losing; are rarely cited/mentioned in AI answers.
- Reason: they already have some signal, so gains are cheaper than starting cold.

## Define the page's job
- Write down: primary keyword, main prompt/question, searcher awareness stage, desired next action. If you cannot state the job, the page is not clear yet.
- Intent check from live results: dominant page type, how fast top pages answer, title angles/promises, repeated subtopics/FAQs/proof, and whether AI answers cite brand pages, review sites, directories or guides.
- Format mismatch rule: if results are mostly comparisons/service/product/local landing/deep guide/FAQ pages and yours is a different type (e.g., a broad article against comparison results), change page type or angle, not just wording.

## On-page basics checklist
- Primary keyword (or a natural close variant) present in: URL, title tag, meta description, H1, first couple of sentences, and one close variant in the first H2. Do not force it.
- Headings: one clear H1; H2s that mirror real questions/subtopics; H3s only when needed; headings that preview content.
- Scannability: short paragraphs, bullets, numbered steps where order matters, tables for comparisons, direct answers at the start of sections.

## Competitor comparison workflow
1. Google: take the top 5-10 organic results for the query; record URL, page type, title angle, recurring sections.
2. AI platforms (AI Mode, ChatGPT, Gemini, Perplexity): run the query or a natural-language version; record cited URLs, mentioned brands, answer format, page types.
3. Merge and de-duplicate into one competitor set.
4. Extract recurring entities, subtopics, questions, features, benefits, objections, decision factors. Recurrence across pages signals essential coverage.
5. Build a stronger outline: direct answer at top; H2s matching recurring subtopics/questions; shared entities and terminology; proof points, examples, decision criteria; FAQs for follow-ups; clear next step.
6. Compare your outline side by side with the recurring list; missing themes are the gaps.
- Tools: ChatGPT or similar for manual extraction; Rankability or Surfer SEO can pull Google and AI-platform competitors, de-dupe and extract topics/entities. Any content-optimization workflow works; build the outline from the whole set, not a single keyword.

## Hidden failure patterns
- Answer buried: long intro, delayed answer, dense paragraphs. Fix: answer early.
- Weak trust: no proof, specifics, credible authorship, consistent brand signals, or evidence for big claims.
- Isolated page: lacks internal links, hubs, FAQ, comparison, proof or cluster support. Sometimes needs backup, not a rewrite.
- Post-click failure: unclear offer, weak next step, no hesitation reduction, insufficient proof.

## Diagnosis-to-fix map
- Intent wrong -> change page type, angle or target query.
- Basics weak -> fix keyword placement, headings, structure.
- Topical gaps -> add subtopics, entities, questions, examples, decision factors.
- Trust weak -> add proof, sources, author details, reviews, screenshots.
- Site support weak -> add internal links from hubs, FAQs, comparisons, cluster pages.
- Conversion gap -> clarify offer, answer objections, stronger CTA.

## Log and measure
- Log per change: URL, date, what changed, why, expected result. Define success before the edit.
- Metric by page job:
  - Awareness/guide: impressions, clicks, rankings, engaged visits, clicks to next-step pages.
  - Comparison/BoF: CTR, rankings, leads, demos, sales, assisted conversions.
  - Local/service: calls, form submissions, map actions (directions requests, clicks), local rankings, booked appointments.
  - AI visibility: mentions, citations, first mention, share of voice across tracked prompts.
- Review windows: small title/meta edits 2-4 weeks; larger rewrites, consolidations, internal-link changes 4-8 weeks; AI visibility tested weekly with a trend judged over at least 4 weeks.
- Ignore noise: brief spikes, short post-publish dips, normal volatility, answer variation between AI runs.
- Sequence: diagnose main bottleneck, make most important fix, measure, escalate only if needed. Example: low clicks -> title first; hesitation -> proof; traffic but no action -> CTA.

## Templates & prompts
- Page job card: URL | Primary keyword | Main prompt | Awareness stage | Desired action | Success metric | Baseline.
- Competitor matrix: Source (Google/ChatGPT/Perplexity/Gemini/AI Mode) | URL | Page type | Title angle | Recurring sections | Entities | Cited? 
- Prompt: "Compare these competitor page texts and list entities, subtopics, questions, objections and decision factors that appear on at least half of them, plus what my page lacks."
- Change log row: Date | URL | Change | Reason | Expected result | Review date | Outcome.

## Audit checks
- [ ] Candidate pages identified from impressions/CTR, page 2 positions, conversion data, AI citation checks.
- [ ] Each target page has a written job (keyword, prompt, stage, action).
- [ ] Page type matches the dominant type in SERP and AI citations.
- [ ] Primary keyword/variant appears in URL, title, meta description, H1, opening lines, first H2.
- [ ] Single H1; H2s phrased as real questions/subtopics.
- [ ] Direct answer appears near the top; no long preamble.
- [ ] Short paragraphs, lists, tables used where helpful.
- [ ] A competitor set (Google plus AI platforms) was compiled and de-duplicated.
- [ ] Page covers recurring entities, subtopics, questions and objections from the set.
- [ ] Proof, examples, author credentials and sources are visible.
- [ ] Internal links point to the page from hubs/FAQ/comparison/cluster pages.
- [ ] Offer, objections handling and CTA are clear.
- [ ] Changes are logged with date, reason and expected result.
- [ ] Success metric and review window were set before editing.
- [ ] Only one main fix was changed per test cycle where feasible.

## Actions
- Pull a priority list from Search Console (high impressions/low CTR, positions 8-20). [Quick win]
- Fill in a page job card and check live SERP/AI intent for each. [Quick win]
- Rewrite title/meta to match winning angle; review after 2-4 weeks. [Quick win]
- Move the direct answer up and tighten headings. [Quick win]
- Build competitor-informed outline and add missing sections, proof, FAQs. [Foundation]
- Add internal links from relevant hubs and cluster pages. [Foundation]
- Strengthen CTA and objection handling for pages with traffic but no conversions. [Foundation]
- Maintain the change log and re-measure at 4-8 weeks. [Ongoing]

## Pitfalls
- Editing before diagnosing.
- Changing title, proof and CTA at once, which hides what worked.
- Judging results in days, or reacting to one AI answer.
- Stuffing keywords instead of making the topic clear.
- Using the same KPI for every page.
- Copying one competitor instead of the recurring set.

## Related
- ch05, ch06 (metrics and dashboard), ch07 (competitors), ch08 (clean experiments), ch10, ch11 (structure), ch12 (BoF pages), ch13 (coverage, consolidation).
