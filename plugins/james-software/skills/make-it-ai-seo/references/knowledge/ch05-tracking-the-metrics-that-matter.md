---
id: ch05
title: Tracking the Metrics That Matter
part: Part 2: Measuring AI SEO
tags: [prompt database, coverage, position, share of voice, SoV, citations, branded prompts, Search Console regex, synthetic prompts, self-reported attribution, journey compression, category legitimacy]
use_when: Setting up or auditing how AI visibility is measured: which prompts to track, how to score coverage/position/SoV/citations, and which soft signals to log.
---

# ch05 — Tracking the Metrics That Matter

## Core idea
- AI SEO tracking swaps keywords for prompts and rank for the answer itself: the primary object measured is "what does the AI recommend?", with citations as supporting evidence.
- Build one prompt database as the source of truth, then compute four things from it: coverage, position, share of voice (SoV), citation metrics.
- Clicks undercount AI influence (people read, remember, search later), so add soft signals: self-reported attribution, branded search lift, recency bumps, category legitimacy.

## Prompt intent vs. prompt groups
- Intent (Informational vs Commercial) describes the user's goal; wording does not decide it ("What are the best CRMs..." is commercial).
- Groups describe what you monitor. Two groups produce measurable visibility: Branded prompts and Nonbranded commercial prompts.
- Branded prompts: "[brand] review", "[competitor] vs [brand]", "[brand] alternatives". Use as baseline for sentiment/positioning/description.
- Nonbranded commercial prompts: problem/category/solution without a brand name ("best plumber in Chesterfield, Missouri", "top five affordable air fryers"). This is where AI picks winners; middle/bottom of funnel.
- Informational prompts are for content planning, weak indicators of brand visibility.
- Prompt cluster = related prompts on one topic/need from different angles.
- Starting set: 25-50 strong prompts, mostly nonbranded commercial, branded added separately as baseline checks.

## Prompt database columns
- Brand, Product, Prompt (exact text), Prompt Source (GSC, customer interviews, Synthetic), Category (Local/SaaS/Ecommerce), Stage (Solution Aware / Product Aware / Most Aware), Intent, Status (Active/Paused/Retired), Start Date, Owner, Priority (H/M/L), Cadence (daily/weekly/biweekly/monthly), Country, Language, Location (city/state for local), Notes.
- Stage examples: Solution Aware = "best content-optimization tools for agencies"; Product Aware = "Tool A vs Tool B for agencies"; Most Aware = "Does Tool A have a free trial?".
- Start from one product/service/category, write a short seed ("SEO content optimization tool"), then expand into natural-language prompts.

## Mining prompts from Google Search Console
- Path: Performance > Search results > Add filter > Query > Custom (regex). Test on a short date range first to confirm it surfaces commercial queries.
- Step 1, question-style commercial queries: start-of-query question/superlative word (what|which|best|top|how|should) followed anywhere by a commercial term. Swap the term list by site type:
  - Local: service, company, near me, pricing, cost, affordable, review, comparison
  - SaaS: software, tool, platform, pricing, cost, review, comparison, alternative, vs
  - Ecommerce: buy, price, deal, cheap, affordable, review, alternative
- Step 2, long-tail conversational queries: require 6+ words (regex repetition of word groups, `{5,}` after the first word) plus a commercial term; raise the number to get longer queries.
- Add keepers to the database; skip research-only queries that involve no provider/product choice. GSC says "queries"; AI platforms say "prompts".

## Synthetic prompts
- Ask ChatGPT/Gemini/Claude: "Create ten synthetic prompts that use natural language and are likely to be used in AI platforms for this seed: [SEED]".
- Review, drop unrealistic/generic ones, store with Prompt Source = Synthetic. Repeat per core product/service.

## Coverage
- Binary per prompt-per-platform check: brand present (1) or not (0).
- Coverage rate % = answers mentioning brand / total answers checked x 100.
- Needs sample size: multiple commercial prompts, multiple platforms, repeated regularly (weekly).
- Candidate platforms: Google AI Mode, Google AI Overviews, Gemini, ChatGPT, Perplexity, Claude, Grok, Microsoft Copilot, DeepSeek. Pick at least three that match your audience.

## Position
- Position = order of the brand among brands in the answer. Numbered list: use list number. Prose: order of first distinct brand mention.
- Multiple mentions in one answer: record the first mention.
- Also record total brands in answer (e.g., position 3 of 6).
- Treat as a trend; AI answers vary run to run.

## Share of voice (SoV) scoring
- Position score: 1 = 1.0, 2 = 0.8, 3 = 0.6, 4 = 0.4, 5 or lower = 0.2, absent = 0.
- Sum your scores over all prompt x platform combos; sum all brands' scores over the same combos.
- AI SoV % = your total / all-brands total x 100. Rises with better coverage, better position, or both.
- Use as headline metric; drill down per prompt/platform to explain changes.

## Citation tracking
- When retrieval is used (current, commercial, open-ended queries), the model pulls external sources and may show citations; simple well-known facts are answered from training data with no citations.
- Retrieval often leans on search indexes (Google surfaces use Google; Microsoft-backed systems use Bing; others mix search APIs, own crawlers, third parties). Ranking well and being on trusted third-party sites raises odds of being retrieved.
- Citation coverage fields per prompt/platform: Website Cited (Y/N), Brand on Third-Party Source (Y/N), citation position (first, third, fifth), key third-party sites mentioning the brand.
- Summary metrics: own-site citation coverage rate; third-party domain coverage rate; average citation position.
- Realistic goal: become one of the recurring sources across prompts/platforms, not the only source. AI answers form from consensus across domains.
- Track brand presence on industry's common retrieval sources (review sites, directories, comparison posts, niche publications); gaps become outreach/PR/link targets (see ch07, ch20).
- "Evidence stack" = the set of sources an AI uses to support answers.
- Referral traffic from citations is small but high intent; measure engagement and conversion.

## Soft signals and self-reported wins
- Self-reported wins: customer says "ChatGPT recommended you". Soft signals: branded search rising alongside SoV.
- Journey compression: problem to vendor choice inside one chat; analytics credit last touch (direct, branded, email).
- Capture it: form field "How did you first hear about us?" with an AI-platform option; ask on sales calls/support tickets "Did any AI platform help you research?"; tag CRM records (AI Mention, ChatGPT, Perplexity, Copilot) and review quarterly.
- Branded search: track in GSC and Bing Webmaster Tools; watch brand name, core product names, common misspellings. Supporting signal only; suspect a link when it rises with SoV.
- Recency effect: bumps after launches, conferences, PR wins, new roundup mentions. Log events in the change log (ch06) and compare dates with tracking runs.
- Category legitimacy: inclusion in "top X"/"best for Y" lists, association with category leaders, buyers repeating AI phrasing ("alternative to [leader]"). Keep a short ideal-category prompt list and watch surrounding competitors and position.

## Templates & prompts
- Synthetic prompt generator: see above.
- Per-answer record: Date | Platform | Prompt | Brand Present (1/0) | Position | Total Brands | Website Cited | Brand on 3rd-party source | Citation position | Notes.
- Form field: "How did you first hear about us?" with options including "AI assistant (ChatGPT, Perplexity, etc.)".

## Audit checks
- [ ] A prompt database exists with intent, stage, cadence, owner, country/language columns.
- [ ] At least 25 prompts, majority nonbranded commercial.
- [ ] Prompts sourced from GSC queries and/or customer language, not only synthetic.
- [ ] Branded baseline prompts exist (review, vs, alternatives).
- [ ] Coverage rate is computed per platform across at least three platforms.
- [ ] Position is recorded (first mention) with total brands count.
- [ ] A documented SoV scoring scale is in use and consistent.
- [ ] Citation fields (own site, third-party presence, position) are logged.
- [ ] Prompts run on a fixed cadence (weekly typical).
- [ ] Lead forms or CRM capture self-reported AI attribution.
- [ ] Branded search is monitored in GSC and Bing Webmaster Tools.
- [ ] Events (launches, PR, reviews) are logged against tracking dates.
- [ ] A category-level prompt shortlist is tracked for legitimacy.

## Actions
- Create the prompt database sheet with the column set above. [Foundation]
- Run the two GSC regex filters per site type and import qualifying queries. [Quick win]
- Generate and vet synthetic prompts per core offering. [Quick win]
- Choose 3+ platforms by audience and begin weekly runs. [Ongoing]
- Add SoV and coverage trend charts built from the database. [Foundation]
- Add AI-source option to forms and CRM tags. [Quick win]
- Build a list of recurring third-party citation domains and gaps. [Ongoing]

## Pitfalls
- Tracking informational prompts as if they measure brand visibility.
- Treating one run as truth; answers vary.
- Recording only mention, not position, so SoV stays flat while you appear in slot 5.
- Rewording prompts between runs (breaks trend).
- Reading branded-search lift as proof rather than a hint.
- Assuming a ChatGPT answer without Search enabled reflects fresh web retrieval.

## Related
- ch03 (evidence library start), ch06 (dashboard build), ch07 (competitor SoV and citation gaps), ch08 (experiments), ch12 (bottom-funnel pages), ch20 (citations and links).
