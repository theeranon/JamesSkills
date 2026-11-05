---
id: ch09
title: Building Your Topic Game Plan
part: Part 3: Building Pages and Foundations
tags: [topic plan, awareness stages, keyword template, knowledge base, query fan-out, People Also Ask, keyword gap, scoring, clusters, pillar page, roadmap]
use_when: Deciding which topics/pages to build first, mapping keywords to page types, scoring and prioritizing topics, or designing a pillar plus support-page cluster.
---

# ch09 — Building Your Topic Game Plan

## Core idea
- A topic plan has two jobs: help buyers choose the brand, and help machines understand and trust it. Build pages that match how buyers decide, not "a bunch of blogs".
- Mine real demand signals first (more inputs than you will publish), then filter hard: every topic ends as Build now / Build later / Don't build.
- Ship one cluster at a time: one pillar (commercial) plus support pages (pricing, versus, alternatives, best-for, proof/FAQ), all interlinked.
- AI answers often satisfy the query with no click, so judge low-CTR pages by assisted conversions, internal clicks to bottom-of-funnel (BoF) pages, brand mentions and AI accuracy, not only traffic.

## Customer awareness stages (what to publish per stage)
- Unaware: vague, curiosity queries ("how does SEO work"). Convert poorly, rarely trigger brand mentions. Do NOT build the roadmap around them; only short support pages that define the problem and link to the next stage.
- Problem Aware: symptoms/errors/"why is this happening". Page types: diagnostic guide, common-causes explainer, checklist. Purpose is moving the user to Solution/Product Aware pages via strong internal links. Expect fewer visits; measure engaged sessions, internal clicks to BoF, branded search.
- Solution Aware: knows the category, not the provider. Page types: credible "best/top" lists, use-case pages ("for agencies"), pricing/cost pages, buyer guides comparing approaches. AI produces commercial shortlists here, so this is prime AI-visibility territory.
- Product Aware: comparing named options. Page types: A vs B, alternatives, "best for X" fit pages. Generates AI answers with brand mentions and citations; easiest to track and to show stakeholders.
- Most Aware: brand already in the query (pricing, free trial, "is X worth it"). AI often retrieves straight from the brand's own site. Page types: pricing, FAQ, proof (case studies, testimonials), how-it-works/onboarding. Accuracy is the priority: stale or inconsistent price/features/terms get repeated wrongly by AI.

## Keyword research template (single source of truth)
- Tool: Google Sheets, Airtable, Notion or internal system; keep columns identical across clusters. Rule: if a topic is not in the template, it is not on the roadmap.
- Columns: Priority (P1/P2/P3 = build order), Source (GSC, gap tool, Reddit, Ahrefs, Rankability...), Cluster (one cluster = one roadmap unit), Pillar, Keyword, Volume/Impressions, KD, CPC, Current Position, Current URL, Intent, Opportunity, Primary Keyword, Keyword Variation/Secondary Keyword, Status, Exclude, Notes. Optional entity columns: Primary Entity, Related Entities.
- Volume vs impressions: use tool volume when available; GSC impressions are real counts and often more accurate.
- Opportunity labels by current position: Low-hanging fruit = 2-15 (refresh + internal links + proof); Existing = 16-50 (needs depth, on-page, links, some authority); Clustering opportunity = 51+ (needs pillar + support + linking); Untapped = outside top 100 (net-new full build + cluster).
- Status pipeline: Backlog, Briefed, Drafting, Editing, Published, Updating, Consolidating.
- Exclude flag keeps rejected topics visible but out of the pipeline. Notes hold things like "needs case study", "needs schema", "AI keeps citing competitor", "refresh quarterly".

## Client knowledge base (ground truth for content and AI drafting)
- Purpose: faster research, stored-once facts, safer AI output (you control what is ingested), consistent terminology/entities.
- Minimum contents: basics (services, price ranges, coverage areas, guarantees, differentiators); proof (case studies, testimonials, before/after, screenshots); entities (products, methods, standards, tools, people, locations, brands); policies (what you do/don't do, who you serve/don't); FAQs (sales objections, Most Aware questions); source notes + Last Updated date per fact.
- Store in a per-client workspace (for example a ChatGPT Project holding the keyword template link, KB artifacts, and one folder per cluster). Every draft should reuse approved facts instead of rewriting from memory.

## Finding topics (collect demand signals)
- Mine internal sources with LLM prompts over call notes, support logs, onboarding docs, competitor notes, FAQs:
  - Sales calls: top 25 pre-purchase questions in prospects' wording; objections grouped by theme (one page topic each); questions asked just before pricing/demo/proposal (each is a BoF topic).
  - Churn: top cancellation reasons -> prevention page, FAQ answer, how-it-works clarification; top 10 expectation gaps -> expectation-setting pages; missing features/outcomes -> "who it's for / fit" pages.
  - Onboarding friction: sticking points -> help page with outline; setup confusion -> searchable question + page type; skipped steps -> how-tos; terms customers ask to define -> glossary/FAQ entries; category misconceptions -> myth-busting page linking to the commercial page; pricing/timeline/outcome misunderstandings -> specific, measurable FAQ.
  - Competitor comparisons prospects raise unprompted: decide comparison vs alternatives vs best-for page; capture their comparison phrases as keyword targets; find top 5 comparison themes (price, features, speed, support, outcomes) with 3 supporting topics each.
- Standardized output prompt: ask the LLM to output rows with columns Source, Cluster, Keyword/Topic, Intent, Opportunity Label, Notes, Recommended Page Type; then copy into the full template.
- Search Console signals: high impressions + low clicks; keywords at positions 2-15; pages ranking for mismatched keywords (intent mismatch); branded vs non-branded queries revealing cluster gaps.
- Competitor keyword gap: list 3-10 direct competitors (not giant publishers unless they own the SERP); run Ahrefs Content Gap, Rankability domain compare, or Semrush Keyword Gap; filter commercial modifiers first (best, top, review, versus, compare, alternatives, pricing, cost, for [use case], near me); tag each with likely page type, cluster, opportunity label; map gaps to pages (same intent + same SERP format = one page with sections). One competitor ranking = maybe one-off; three = market expectation and more likely reused by AI.
- UGC (Reddit, Quora, reviews, forums): mine natural-language questions (H2/FAQ/PAA wording), pain points/objections, real vocabulary. Validate each by intent and business value. UGC gives phrasing; keyword tools give scale.
- Keywords from scratch: 5-20 targeted seeds matching the offer; add commercial modifiers (pricing, cost, quote, near me, best, top, reviews, versus, alternatives, for agencies/small business/e-commerce); check "also rank for" on winning competitor pages to find expected subtopics; group by parent topic/intent (one strong page, not five weak); validate against the SERP (page types, winning formats, repeated angles). End each seed with one pillar keyword + 3-10 support keywords.

## Query fan-out and People Also Ask (PAA)
- Fan-out a head term by intent: Problem clarification (why is, common causes, how to fix, signs you need) / Evaluation (best, top, how to choose) / Comparison (A vs B, alternatives) / Action (cost, pricing, near me, quote, trial, is it worth it).
- Assign a page type BEFORE writing: pricing/cost -> pricing page or cost guide; best/top/reviews -> listicle or buyer guide; versus/alternatives -> comparison/alternatives pages; near me/city -> local landing page; how-to -> implementation guide/SOP; worth it/does it work -> proof page, FAQ or decision page.
- PAA harvesting steps: open private window, search the pillar keyword, expand 6-10 questions (each click reveals more), copy into template; repeat for "best/cost/versus/alternatives" variants.
- Section vs page rule: answerable well in 3-6 paragraphs = a section on an existing page (H2 or FAQ); needs steps, examples, proof, full explanation = its own page.

## Qualifying topics (three questions, then filters)
- Questions: Will it drive the right outcome (revenue, leads, trials, calls)? Can we realistically win (authority, competition, proof, resources)? Is the click worth it (SERP features may steal clicks)?
- Relevance ladder: BoF (pricing, cost, hire, demo, trial, near me, quote, best, reviews, versus, alternatives) > MOFU (how to choose, tools/services for) > TOFU (definitions, broad how-to). Build BoF first, then supporting pages.
- Intent: start with two labels (Informational, Commercial); split later (educational/how-to/definition; comparison/alternatives/pricing/review) only if reporting benefits. Rule: if you cannot name the page type and its job for the user, do not build yet.
- Competition win test: who ranks (giants, government, publishers, niche specialists)? what page types win? what is the minimum bar (depth, proof, reviews, price clarity, authorship, tooling, location signals)? If failing: start with long-tail commercial in the same cluster, build support/proof/internal links first, or park it.
- Keyword value: CPC signals commercial value. High CPC + BoF = build sooner; high CPC + informational = support page unless it funnels well.
- Organic CTR potential: scan SERP for AI answers, ads, local pack, shopping, featured snippet, PAA, video, top stories, knowledge panel. More features above the fold = lower expected CTR. Also account for brand bias in search/AI (established brands favored); newer brands may need third-party mentions, reviews, citations, entity consistency before visibility pays off. Low-CTR topics still worth building if they support BoF via links, earn AI citations, or build trust (pricing, policies, FAQs).

## Scoring and priority rules
- Score each topic 1-5 on: Impact (relevance to offer/BoF proximity), Win probability (competition fit), Monetization (CPC/keyword value), Click opportunity (organic CTR potential), Speed (opportunity label; low-hanging fruit scores higher). Sum, sort, sanity-check against the cluster roadmap.
- Priority order: low-hanging fruit + BoF (pos 2-15, commercial) > BoF + high CPC even if untapped > BoF with clean SERP (high CTR potential) > competitor-owned commercial gaps > support pages that strengthen a cluster (esp. low-CTR SERPs) > informational pages only if they move people forward (links to BoF, objection handling, proof).
- Secondary filters (volume/impressions, KD, etc.) only refine after the primary filters.

## Clusters, pillar, and roadmap
- Cluster = one buyer decision, not similar-looking keywords. One topic = one primary page unless intent clearly differs (prevents cannibalization confusing search and AI retrieval).
- LLM-assisted clustering: give the offer (1-2 sentences), ICP, core products/services, P1/P2 keyword list, must-win clusters. LLM detects modifier families, infers intent/page type, suggests section-vs-page, drafts names. A human validates against the SERP.
- Judge output: cluster names read like decisions ("Choose the best content optimization tool for an agency", not "content optimization keywords"); exactly one commercial pillar (two pillars = two decisions, split); supports mapped to intent (pricing = transactional, alternatives/comparisons = comparison, best-for/use-case = investigative, proof/FAQs = Most Aware).
- Sanity sentence: "If someone is trying to [pillar decision], they'll also ask [pricing], [versus], [alternatives], [best for], [is it worth it]." If it does not flow, the cluster is off.
- Pillar page requirements: targets the primary commercial term; covers decision criteria; hub for internal links; single unambiguous place for AI to learn what you do, who for, why credible. Contents: clear promise above fold (who/problem/outcome); fast conversion path (call, form, quote, demo, trial, or "see pricing/compare" for not-ready users); "choose you" decision content (scope/deliverables, evaluation criteria and red flags, pricing or how pricing works, timelines/first steps/success measures); proof in the flow (reviews, case studies, credentials, certifications, guarantees); links to deeper pages. Written so a buyer can decide without leaving, with links to verify.
- Match pillar format to the dominant SERP format: service page, use-case page, commercial guide ("best X for Y"), or category page.
- Build sequence: (1) ship pillar; (2) ship 2-4 decision helpers (pricing, cost, best-for, use case, alternatives, comparisons); (3) add proof and FAQs; (4) link: every support page links to pillar with intent-matching anchors, pillar links out to supports, comparisons/alternatives cross-link where useful. Finish a cluster before starting the next.

## Templates & prompts
- Template columns: see "Keyword research template" above (copy as a sheet header row).
- Output-format prompt: "Output rows with: Source, Cluster, Keyword/Topic, Intent, Opportunity Label (Low-Hanging Fruit / Existing / Clustering Opportunity / Untapped), Notes, Recommended Page Type."
- Scoring sheet: Topic | Impact | Win prob | Monetization | Click opp | Speed | Total | Decision (Build now/later/Don't).
- Cluster validation sentence (above) and the page-type map from fan-out.

## Audit checks
- [ ] A keyword/topic research sheet exists with consistent columns, including Cluster, Intent, Opportunity, Status and page URL mapping.
- [ ] Every priority keyword maps to exactly one primary URL (no two pages targeting the same intent).
- [ ] Each target keyword has a named page type that matches the dominant SERP format.
- [ ] A pricing/cost page exists and states current prices or ranges, plan details, trial terms.
- [ ] Comparison and alternatives pages exist for competitors that prospects mention.
- [ ] "Best for"/use-case pages exist for main segments.
- [ ] FAQ and proof pages (case studies, testimonials) exist and are linked from the pillar.
- [ ] Each commercial cluster has one identifiable pillar page that is linked from navigation or hubs.
- [ ] Support pages link to the pillar with descriptive anchors, and the pillar links back out to them.
- [ ] Pricing, features and terms are identical across site pages (no conflicting facts).
- [ ] A client/brand knowledge base with proof, policies, entities, FAQs and Last Updated dates exists.
- [ ] Search Console was reviewed for positions 2-15 queries and high-impression/low-click queries.
- [ ] Competitor gap analysis done against 3-10 direct competitors for each target cluster.
- [ ] Unaware/TOFU content is limited and links onward to BoF pages.
- [ ] Each topic has a recorded decision (build now / later / don't) with a score.

## Actions
- Build the research template and populate it from GSC, gap tools, PAA, UGC and internal sales/support data. [Foundation]
- Assemble the knowledge base (facts, proof, policies, entities, FAQs, source + last-updated) and use it as the only input for drafts. [Foundation]
- Run a competitor gap analysis and tag each gap with page type, cluster and opportunity label. [Foundation]
- Refresh pages sitting at positions 2-15: improve content, add proof, add internal links to them. [Quick win]
- Fix inconsistent or outdated pricing, features and terms across all pages. [Quick win]
- Score topics 1-5 on the five criteria and select one critical cluster. [Foundation]
- Ship pillar first, then 2-4 decision helpers, then proof/FAQs, then interlink. [Foundation]
- Merge keywords sharing one intent into one page with sections; consolidate duplicate pages. [Foundation]
- Add FAQ sections built from PAA, sales and UGC questions to the pillar. [Quick win]
- Re-run the gap and Search Console review each cycle and update statuses. [Ongoing]

## Pitfalls
- Choosing topics by volume alone and hitting SERPs you cannot win.
- Turning every fan-out question into a thin blog post; cannibalization.
- Building many clusters at once and finishing none.
- Judging awareness-stage pages only by traffic.
- Using the LLM cluster output without SERP validation; two pillars in one cluster.
- Letting off-template "good ideas" hijack the roadmap.
- Stale pricing/terms on Most Aware pages that AI repeats to buyers.

## Related
- ch07 (competitive intelligence), ch12 (BoF pages), ch13 (topical authority), ch10-ch11 (technical readiness), ch05-ch06 (measuring beyond traffic), ch04 (glossary).
