---
id: ch04
title: Talk Like an AI SEO Pro
part: "Part 1: Getting Grounded"
tags: [glossary, AEO, GEO, share of voice, entity, knowledge graph, RAG, LLM, context window, passages, fact hub, schema, sameAs, citations, consensus]
use_when: Looking up or explaining an AI SEO term, setting the SoV scoring method, deciding page-vs-passage writing rules, or choosing which schema types to check and how to describe their limits.
---

# ch04 — Talk Like an AI SEO Pro

## Core idea
- Visibility is now about being included and described accurately in answers; learn the vocabulary to diagnose where in the chain (retrieval, model, platform) a brand is losing.
- Entities, knowledge graphs, passages and consensus are the mechanics behind inclusion; schema helps search engines, and only indirectly AI.
- AEO and GEO have no strict standard definitions; use them as lenses, not frameworks.

## Glossary: visibility terms
- AEO (answer engine optimization): earning visibility inside answer experiences (mentions, recommendations, citations).
- GEO (generative engine optimization): helping generative systems understand and repeat your information accurately.
- Practical outcomes either way: (1) recommended in AI answers, (2) facts repeated accurately.
- Share of voice (SoV): how often and how strongly the brand appears in AI answers for commercial queries relative to other brands.
- Citation (in AI answer): any reference to brand, site or published data, with or without a clickable link. Mention: reference to brand/product/person/site, linked or not. Backlink: link from another site (still key for classic ranking and discovery).
- Citation rate: percent of tracked AI answers that mention the brand.
- Fact coverage: number of key facts appearing on other reputable sites. Fact freshness: average age of data in the fact hub and related content.

## Glossary: entities and graphs
- Entity: clearly defined person, organization, place, product or concept with name/type, attributes (location, founding date, pricing tier) and relationships (founded by, headquartered in, competes with).
- Knowledge graph: connected web of facts; lets a system look up an entity, follow relationships, retrieve connected entities. Visible effects: knowledge panels, rich result boxes, direct factual answers.
- Index: store of crawled pages; the graph stores connected facts. Incomplete or inconsistent entity data leads to wrong facts attached or the brand skipped.
- Entity home: the page on your site that is the primary reference for who you are (usually About or a brand page): official name, location/service areas, founders/leadership, core products/services, key descriptors.

## Glossary: LLM stack
- Retrieval system: decides which content to bring in. LLM: generates answer wording (Gemini, ChatGPT, Claude). AI platform: shows the final answer (Google AI features, Copilot, Perplexity).
- RAG: retrieve outside information first, then the LLM generates from it.
- Context window: total text the LLM can process at once. Tokens: text chunks it reads. Long pages are split into passages and only a few get sent.
- LLM predicts likely words/brands from passages in front of it; it is not querying a clean database.
- Card: boxed answer element. Platforms may limit brand count, hide sources behind icons/"show more", truncate long answers.

## Share-of-voice method (market-weighted)
1. Presence: for each tracked query on each platform record yes/no (no = zero SoV for that cell).
2. Position/prominence: first in short list, buried in long list, or single passing mention.
3. Crowding: relative share among all brands named (3 competitors vs 30).
4. Platform weight: assign each platform a rough weight by usage in the target market; multiply presence and position scores by weight; roll up to one view.
- Report together: appearance frequency, position strength, comparison to others in same answer, weighted result. Citations/links are supporting evidence, not the primary SoV measure.
- Supporting indicators: citation rate, fact coverage, fact freshness.

## Three-layer optimization model
- Retrieval level: page ranks in classic search and contains clear self-contained passages naming the brand and what it is useful for.
- Model level: passages make it natural to include the brand for specific jobs (e.g., "AI SEO content optimizer for agencies").
- Platform level: recommendation appears visibly in lists/cards/summaries. A brand can be used as a source yet stay invisible if the platform hides or buries it; short passages that name the brand and answer in one or two sentences are more likely to surface.

## Pages vs passages
- Pages are crawled, indexed, ranked; passages are the units often retrieved and fed to the model. Visibility needs both: page-level authority/relevance wins retrieval; passage-level text shapes what the model says.
- Writing rules for brand-friendly passages: one idea per paragraph answering a specific question; short direct sentences with the claim first plus one or two supports; use brand/product names instead of "it/they"; place numbers, examples, case results next to the claim; use bullets or short lists for tools, steps, features.
- Visible text must stand alone even if schema is ignored.

## Credibility signals and fact hub
- Fact hub: single organized page of key facts, stats, definitions with source, date and update history; tables and headings; schema where sensible. Build by listing recurring facts across content, publishing one page, keeping numbers current, aligning older content to it.
- Consensus: AI favors facts repeated across trusted sources. Build by consistent terminology, publishing facts in referenceable formats (reports, studies, blog posts), encouraging partners/customers/media to cite them, updating stale content. Raises odds, no guarantee.
- AI platforms show few brands/sources per answer; a visible mention resembles a top position.

## Schema and structured data (what to implement and how to describe it)
- Structured data = machine-readable formatting; schema = Schema.org vocabulary. JSON-LD = script blocks holding the markup.
- Stance: no solid public proof that general LLMs weigh schema directly. Schema helps search engines understand, qualify and feature content (rich results, knowledge panels); AI benefits indirectly through the same indexes.
- Organization: official name, logo, contact, HQ, founding date, founders, social profiles and `sameAs` (tells systems that profiles and listings are the same entity).
- Person (authors): full name, role, credentials/title, affiliated organization, photo, verified profile links.
- Content: Article/BlogPosting, TechArticle, FAQPage, HowTo; each with headline, short description, author, publisher, datePublished, dateModified, mainEntityOfPage.
- Product: name, description, image, brand, SKU, GTIN, offers/price/availability, AggregateRating and Review (ratings count/average; verified reviewer info where allowed).
- Service: service type, area served, provider.
- Claim/evidence patterns: ClaimReview for genuine fact-checks; CreativeWork with citation properties (URLs, titles, access dates); `sameAs` and `about` linking entities to external identifiers such as Wikidata, LinkedIn, Crunchbase. Speakable is limited/experimental; optional.
- QA workflow: version-control JSON-LD files, test with Google Rich Results Test and Schema.org validators, include structured-data review in publishing checklist, keep a schema change log per release.

## Templates & prompts
- Entity home checklist: official name | location/service areas | founders/leadership | core offerings | one-line descriptor | links to profiles | Organization schema with sameAs.
- Fact hub table: Fact | Value | Source | Date verified | Last updated | Pages that reuse it.
- SoV grid: Query x Platform with cells [present Y/N, position score, competitors named, platform weight].

## Audit notes for auditors
- When a client says "we have schema, so AI should cite us", correct the claim: schema supports search-engine understanding; verify visible text too.
- Separate findings by layer (retrieval / model / platform) so the owner knows whether to fix pages, passages, or presentation.
- Use "citation" and "mention" precisely in reports; define which one a metric counts.

## Audit checks
- [ ] An entity home page exists and lists official name, location, leadership, offerings, descriptor.
- [ ] Brand name, spelling and core description are identical across site, profiles and directories.
- [ ] Organization schema present, valid, with `sameAs` to verified profiles.
- [ ] Author pages/Person schema exist for content authors with credentials and affiliation.
- [ ] Article pages carry headline, author, publisher, datePublished and dateModified in markup and visibly.
- [ ] Product/Service/Review schema matches visible page content and passes Rich Results Test.
- [ ] A fact hub exists with source, date and update history per number.
- [ ] Key facts appear identically on third-party reputable sites (fact coverage checked).
- [ ] Core pages contain self-contained passages naming the brand and use case near the top.
- [ ] Passages use the brand name rather than pronouns and place proof next to claims.
- [ ] SoV is tracked per query per platform with position and a documented weighting.
- [ ] JSON-LD is in version control with a change log and testing step in publishing.
- [ ] No schema claims exceed the evidence (no "schema guarantees AI visibility").

## Actions
- Create or fix the entity home page and add Organization schema with `sameAs`. [Foundation]
- Build the fact hub with sourced, dated facts. [Foundation]
- Rewrite buried brand statements into short stand-alone passages. [Quick win]
- Implement SoV grid with platform weights from audience data. [Foundation]
- Add schema validation to the publishing checklist. [Ongoing]
- Update fact hub and align older pages when numbers change. [Ongoing]
- Seed consistent facts into referenceable third-party formats (studies, partner pages, press). [Ongoing]

## Pitfalls
- Debating AEO vs GEO labels instead of measuring outcomes.
- Treating links as the only authority signal; AI answers surface mentions and citations.
- Counting any platform mention equally regardless of audience usage.
- Letting a brand appear only inside a dense paragraph where platforms truncate it.
- Using schema types without visible matching content, or promising AI gains from them.
- Inconsistent naming that causes entity confusion; cleaning bad data matters as much as adding data.

## Related
- ch01, ch02, ch03, ch05 (coverage/position/SoV tracking), ch11 (HTML and schema implementation), ch13, ch16 (signals), ch17 (profiles), ch20 (citations, mentions, links)
