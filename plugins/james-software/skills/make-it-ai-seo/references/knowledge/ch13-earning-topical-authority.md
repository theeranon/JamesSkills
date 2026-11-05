---
id: ch13
title: Earning Topical Authority
part: Part 3: Building Content That Gets Chosen
tags: [topical authority, gap analysis, topic universe, depth layers, entity alignment, entity home, sameAs, freshness, content refresh, consolidation, 301 redirect, update log, cannibalization]
use_when: Planning coverage and content gaps, aligning brand/product entities and sameAs, setting update cadence, or merging overlapping pages.
---

# ch13 — Earning Topical Authority

## Core idea
- In the AI era, authority means systems trust you enough to cite and recommend you repeatedly, not merely that you have many pages. Two outcomes at once: stable rankings for chosen topic clusters and repeat brand mentions/citations for pre-purchase prompts.
- Four stacked elements: Coverage; Gaps and depth; Entity alignment; Freshness and consolidation.
- Real authority shows up as ranking for shoulder queries you never targeted, becoming a frequent citation source, and thin competitor lists no longer leapfrogging you.
- More pages is not the goal; more confidence per page is.

## Map the topic universe
- Set a boundary. In scope: core problem, common use cases, audiences, constraints (budget, tools, time, compliance, skill, risk). Out of scope: adjacent topics that do not help the buyer's decision or business goal; park or make a separate cluster.
- Sort content into four buckets and balance them:
  - Core explanations (definitions, how it works)
  - Decision content (comparisons, alternatives, best-of)
  - Implementation content (steps, checklists, templates, workflows)
  - Proof content (case studies, benchmarks, original data)
- Vocabulary: keyword = exact phrase in a tool; query = what people actually type/say; topic = the broader subject they map to.

## Gap analysis procedure
1. Seed list: 10-20 commercial prompts buyers use when evaluating or comparing; add shorthand modifiers (best tool, alternative, template, checklist, pricing, for agencies, for beginners); add Google Search Console queries that earn impressions even if tools show zero volume. Treat GSC impressions on "zero-volume" phrases as real demand.
2. Matrix: rows = subareas (features, pricing, use cases, objections, integrations, risks); columns = your pages, top competitors, recurring third-party sources. Mark each cell Owned (fully answers intent), Thin (mentioned, not answered) or Missing. Prioritize gaps that recur across competitors and third-party sources.
3. Plan three depth layers per page: primary answer (2-3 sentences); follow-up answers (5-10 next questions drawn from real conversations); decision support (who it is for/not for, tradeoffs, proof).
- Start from "what decisions are buyers making", not "what keywords are missing". Use keyword-gap tools to see competitor terms.

## Entity alignment
- An entity is anything systems can identify: brand, product, person, location, category, credential, competitor. Inconsistency makes mentions fail to consolidate, citations split across name variants, products get confused with categories, and the system recommends someone else.
- Entity Home: one canonical page (usually About, or a dedicated Brand/Company page) containing: exact brand name plus category descriptor; one-sentence what-you-do; who it is for; proof markers (awards, certifications, customers, data points); links to official profiles (LinkedIn, Google Business Profile, Crunchbase, G2, etc.). Everything important links back to it directly or indirectly.
- Consistency checklist:
  - Naming: lock exact brand, product, feature and plan names (do not alternate "Content Optimizer" and "Optimizer").
  - Language lock: fixed wording for positioning, differentiators, service areas.
  - Internal linking: major pages link to the entity home with clean, consistent anchor (usually brand name).
- sameAs: Schema.org property listing URLs that denote the same entity (social, credible directories, Wikipedia/Wikidata, knowledge bases). Only include profiles you control or that clearly represent you. It reinforces consistency, it does not create identity; mismatched off-site profiles amplify confusion.
- Entity alignment sheet (one row per entity): name, type, canonical URL, key attributes, sameAs URLs, where referenced. Add a language lock for core descriptors reused in pages, bios, schema, profiles. (Wider profile audit lives in ch17.)

## Freshness cadence
- Freshness means removing doubt about currency, not chasing dates. Old accurate content can still win; pricing, features and screenshots decay.
- Cadence by type:
  - Money pages: monthly light review (accuracy, internal links, CTAs, gaps); quarterly deep review (additions, restructure, proof, consolidation decisions).
  - Comparisons/alternatives: quarterly, or on any price/feature change.
  - Stats and facts: quarterly and when new data lands; timestamp and source-note every number.
  - Evergreen guides: semiannual.
- Freshness box on key pages: Last updated; what changed (1-3 bullets); link to sources or fact hub.
- Pick a cadence the team will really follow.

## Consolidation
- Triggers: two pages share an intent; one cannibalizes another; pages exist only for keyword variants; a weaker page keeps getting cited/ranking for the wrong intent.
- Playbook:
  1. Choose the winner URL (best history, strongest links, clearest intent match).
  2. Merge only sections that add clarity or decision value.
  3. Add internal anchors/jump links to keep it skimmable.
  4. 301 redirect retired URLs to the winner where appropriate.
  5. Update internal links to the winner.
  6. Update XML sitemap, resubmit in Search Console, verify 301s and that canonicals point to the winner.
- Success test: the merged page makes the decision path easier.
- Update log (one shared sheet): date, URL, what changed, why, expected improvement; covers freshness and consolidation entries so visibility changes can be diagnosed later.

## Templates & prompts
- Gap matrix: Subarea | Your page | Competitor A | Competitor B | Third-party source | Status (Owned/Thin/Missing) | Action.
- Entity sheet columns: Entity | Type | Canonical URL | Key attributes | sameAs | Referenced on.
- Update log columns: Date | URL | Change | Reason | Expected result | Result check date.
- Prompt idea: "List the 20 follow-up questions a buyer asks after [primary question]" to fill depth layers.

## Audit checks
- [ ] Topic boundary (in/out of scope) is written down.
- [ ] Content exists in all four buckets (explain, decide, implement, prove).
- [ ] A seed list of 10-20 commercial prompts and GSC low-volume queries exists.
- [ ] A gap matrix marks Owned/Thin/Missing for subareas.
- [ ] Key pages have a short primary answer, 5-10 follow-up answers, and who-for/not-for plus proof.
- [ ] An Entity Home page states brand + category, one-line description, audience, proof, official profile links.
- [ ] Brand, product, feature and plan names are spelled identically site-wide and off-site.
- [ ] Core positioning wording is stable across pages, bios, schema.
- [ ] Major pages link to the entity home with consistent anchors.
- [ ] Organization (or relevant) schema includes sameAs pointing only to controlled/representative profiles, and those profiles agree with the site.
- [ ] Key pages show a freshness box (last updated, what changed, sources).
- [ ] A review cadence by content type exists and is followed (check dates).
- [ ] No duplicate-intent or keyword-variant pages split relevance.
- [ ] Retired pages 301 to a winner; sitemap and canonicals reflect that.
- [ ] An update log exists and is current.

## Actions
- Draft the topic boundary and bucket inventory. [Foundation]
- Run the seed list + GSC pull + gap matrix, then queue Thin/Missing items. [Foundation]
- Add depth layers (answer, follow-ups, decision support) to top commercial pages. [Foundation]
- Build or fix the Entity Home and fill the entity alignment sheet with a language lock. [Foundation]
- Add or correct sameAs in Organization/Person schema; fix mismatched off-site profiles. [Quick win]
- Add freshness boxes to money and comparison pages. [Quick win]
- Merge overlapping pages with the 6-step playbook. [Foundation]
- Calendar the review cadence and maintain the update log. [Ongoing]

## Pitfalls
- Publishing more pages to feel authoritative while overlap grows.
- Ignoring topics because a tool shows zero volume.
- Using sameAs as a magic fix or linking random mentions.
- Merging everything into one wall of text, or skipping redirects/sitemap updates.
- An update plan too ambitious to follow.
- Reworking identity statements per page so claims cannot attach to the entity.

## Related
- ch09 (topic game plan), ch11 (foundations), ch12 (commercial clusters), ch14 (fixing pages), ch16 (signals), ch17 (profiles and entities audit), ch18 (owning the topic), ch10 (schema/readiness).
