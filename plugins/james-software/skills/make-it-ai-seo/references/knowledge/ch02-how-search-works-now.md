---
id: ch02
title: Understanding How Search Works Now
part: "Part 1: Getting Grounded"
tags: [crawling, indexing, ranking, reranking, RAG, grounding, query fan-out, training data vs retrieval, SERP domination, levers, robots.txt, server-rendered HTML]
use_when: Diagnosing why a site is or is not being retrieved/cited by AI, explaining the search pipeline to a client, or choosing which onsite/offsite levers to pull first.
---

# ch02 — Understanding How Search Works Now

## Core idea
- Traditional search (crawl, index, rank, rerank) is still the gate; many AI systems retrieve through web search indexes and then filter by relevance, freshness, authority and confidence.
- You usually cannot change what a model learned in training; you can influence (a) the retrieval layer and (b) future training snapshots via broad, high-quality web presence.
- Answer pipeline: retrieve, read, synthesize, cite. Being cited means being used as evidence, not ranking first.

## Traditional pipeline and what to check at each stage
- Crawling: bots follow links, read XML sitemaps, use submissions and API notifications. Control via robots.txt (most major engines respect it; some bots/AI systems do not). Navigation, internal linking and speed affect how deep bots get.
- Indexing: crawled does not mean indexed. Engines extract text, links, metadata, structured data. Unindexed page = not on the shelf = cannot be retrieved or cited. Indexation matters more now because AI grounding pulls from indexes.
- Ranking: order is decided by many signals (query match, content quality/usefulness, freshness, site/page authority), not a single score.
- Reranking: location, device, past behavior, recency adjust results (e.g., "pizza" yields a local pack because intent is local and commercial).
- AI retrieval often relies on classic rankings as a quality gate, so ranking well raises odds of entering the AI source pool.

## Models vs platforms vs retrieval
- Model (GPT, Gemini, etc.): predicts likely next words from training patterns; does not "know" facts.
- Platform (ChatGPT, Google AI Mode, Claude, Perplexity): interface, citation style, follow-ups, display rules. Citations vary: Perplexity shows multiple clickable sources; ChatGPT Search uses compact footnotes/expandable links; Google AI features list a few sources under the answer card.
- RAG: system looks up outside info (web pages, databases) and passes it to the model; improves freshness/grounding but is not perfect.
- Grounding: retrieving external info when training data alone is not confidently sufficient; reduces hallucination (confident but wrong or unsupported output).
- Training snapshots are fixed per model release; day-to-day influence is via retrieval.

## The four answer steps and the implication for content
- Retrieve: system reshapes the user's long query into shorter searches (query fan-out), e.g., a verbose request becomes "best AI SEO tools for agencies" plus related variants and brand-vs-brand comparisons. Implication: cover the short head terms, variants, alternatives and "X vs Y" queries, not just the exact long prompt.
- Read: text is split into tokens; clarity beats cleverness. Buried facts, heavy metaphor and messy formatting hurt. Use clean HTML, clear title tags, useful meta descriptions, logical headings, direct-answer FAQ sections.
- Synthesize: model favors agreement across sources and downplays contradictory or low-confidence info. Consistent descriptions across sources get merged into one confident statement.
- Cite: selected from retrieved evidence; goal is inclusion and trust, not a single position.

## Onsite levers
- Brand and fact hubs: pages that state who you are, what you do, who you serve. Without them AI leans on third parties to describe you.
- Commercial-intent pages by model: Local = service pages + location pages. E-commerce = category + product pages. SaaS = product, feature, comparison pages.
- "Anti-AI" content: generic informational posts are commoditized; prioritize firsthand experience, proprietary data, case studies, unique frameworks, real stories.
- Technical: critical content in clean HTML; JavaScript frameworks OK only if output is crawlable/server-rendered (some retrieval crawlers do not execute complex JS reliably, so HTML-first is safest); fast and mobile-friendly; shallow architecture (important pages within a few clicks of home) with consistent internal links.

## Offsite levers
- SERP domination: own the best page for the query, then review the rest of page 1 for other asset types (YouTube, Reddit, Quora, industry blogs, publications, directories, review sites) and build a presence where sensible. Multiple page-1 assets pointing to the brand raise odds of selection as a retrieval source.
- Reviews and reputation: platforms by niche. Local: Google Business Profile, Bing Places, Avvo/FindLaw (legal), Angi/Yelp/Thumbtack (home services). E-commerce: onsite product reviews, Amazon/niche marketplaces. SaaS: G2, Capterra, Trustpilot. Reviews are treated as trust/relevance signals and are high-leverage but hard to earn.
- Mentions (brand references, linked or not), citations (sources AI references), links (clickable references). Find target sites by collecting the citations AI answers in your space repeatedly use; add recurring domains to an outreach/presence list and earn legitimate coverage there.
- Profile hygiene: write one standard brand description (category, topics, locations, services) and reuse it everywhere (site, Google Business Profile, LinkedIn, directories, socials) with only minor wording variation. Explicit text such as "personal injury law firm in [city, state] focusing on [practice areas]" is easier for entity extraction (NLP) than vague phrasing.
- Evidence discipline: log assets published, update dates, performance; save screenshots of AI answers mentioning the brand with the triggering prompt; log prompt, platform, date, appeared?, sources cited, screenshot link.
- Two clean long-term influence paths: static training data (broad presence on high-quality sites) and retrieval/search (visible and trusted in web search).

## Audit checks
- [ ] robots.txt exists, does not block key pages or intended crawlers, and any AI-crawler rules are deliberate.
- [ ] XML sitemap lists canonical indexable URLs and is submitted/discoverable.
- [ ] Key commercial and brand pages are indexed (confirm with Search Console URL inspection / index coverage or site: checks).
- [ ] Critical content is present in the initial server-rendered HTML (view-source or fetch without JS).
- [ ] Important pages are reachable within a few clicks and linked from navigation/hubs.
- [ ] Pages load fast and render well on mobile.
- [ ] A brand/fact hub page states who, what, whom, where.
- [ ] Commercial pages exist for the business model (service/location, category/product, feature/comparison).
- [ ] Content includes original proof (data, case studies, firsthand experience), not only generic explainers.
- [ ] Page 1 for each priority commercial query was reviewed and non-owned asset types (video, Reddit, directories, roundups) noted.
- [ ] Brand has profiles on the niche's review platforms with recent real reviews.
- [ ] One standard brand description is used consistently across site and profiles.
- [ ] Repeating cited domains from AI answers in the niche were collected into a target list.
- [ ] An evidence tracker with dated prompts and screenshots exists.

## Actions
- Verify indexation of top 20 commercial/brand URLs and fix noindex, canonical, robots or render blockers. [Quick win]
- Replace JS-only critical content with server-rendered HTML or pre-rendering. [Foundation]
- Build a brand/fact hub and commercial pages per model. [Foundation]
- Write the standard brand description and roll it out to all profiles. [Quick win]
- Run page-1 and AI-citation source mapping per priority query; build target-site list. [Foundation]
- Start review generation on the right platforms. [Ongoing]
- Keep the evidence tracker updated weekly. [Ongoing]
- Cover fan-out variants (short head term, alternatives, vs-comparisons) for each priority topic. [Ongoing]

## Pitfalls
- Assuming crawled equals indexed, or indexed equals ranking.
- Expecting to rewrite what a model already learned; focus on retrieval and future presence.
- Relying on a JS framework that ships empty HTML.
- Counting on robots.txt to stop every AI bot.
- Optimizing only the exact long prompt and missing fan-out queries.
- Flooding the web with misleading claims or fake mentions; risks legal and ethical problems.
- Producing more generic blog content that AI can write itself.

## Related
- ch01, ch03, ch04, ch10 (readiness diagnosis), ch11 (implementation), ch16/ch19 (signals, reviews), ch20 (links, mentions, citations)
