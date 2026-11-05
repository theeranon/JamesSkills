---
id: ch12
title: Creating Bottom of Funnel Pages That Win Answers
part: Part 3: Building Content That Gets Chosen
tags: [bottom of funnel, BoF, pricing page, policies, FAQ, news roadmap, comparison pages, alternatives, vs pages, listicle, commercial cluster, fan-out queries, source of truth]
use_when: Auditing or building decision-stage pages (pricing, policies/FAQ, news/roadmap, best-of, alternatives, vs, review) and the commercial cluster that links them.
---

# ch12 — Creating Bottom of Funnel Pages That Win Answers

## Core idea
- AI engines return one answer or a short list, so a decision-stage page must finish the buyer's decision, not just earn a click. Clarity, proof and quotability are the goal.
- If you publish no official answer, third parties (review sites, affiliates, forums, stale blogs) fill the gap and AI repeats their version, often wrong (old price, wrong return policy, "SSO costs extra").
- Build an Answer Set of three source-of-truth pages (Pricing, Policies/FAQ, News/Roadmap), then comparison/review content, then wire everything into a commercial cluster built to depth before breadth.

## Answer Set: general rules for all three pages
- Literal titles, a one-sentence "In short" summary at the top, simple structure, short factual text.
- Each page shows Last Updated and Owner; cross-link all three; surface them in nav/footer under an "Official Answers" style block.
- Review and refresh Pricing, Policies and News at least quarterly.
- Failure examples to check against: directory lists old "typical prices"; blogger's return-policy summary outranks your product page; comparison site misstates a plan feature.

## Pricing page
- Show clear prices or an honest range or "starts at"; avoid a bare "Contact us". Even a range beats nothing.
- State what is included and what costs extra.
- Add a chooser ("Choose X if...") or comparison table of tiers.
- Open with a quotable "In short" line (example form: services start around a figure, packages span a range depending on scope).
- Link to Policies/FAQ.

## Policies and FAQ hub (build recipe)
1. Open with an "In short" promise line (returns window, warranty length, uptime target).
2. Uniform entry pattern: question as an H3 written the way a customer would say it; answer in 2-5 sentences or up to 3 bullets; a next-step action (Start a Return, Read Warranty, Contact Support).
3. Group by buyer-intent themes: Pricing, Delivery & Returns, Contracts, Setup, Support, Security, Policies, Implementation.
4. Add a "What happens next" step list (order confirmed, scheduling, delivery/kickoff, review/sign-off).
5. Include specs/standards; use a small table and optionally a mirrored downloadable PDF with version number and Last Updated.
6. Show Last Updated and Owner at the bottom.
7. Add FAQPage schema that matches the visible Q&A word for word in meaning; link to Pricing, Policies, Process, Specs/Security. If no code access, ask dev/CMS/SEO plugin to do it.
- Layout patterns worth copying: top tasks first (Nike), choose product/topic before answers (Google Support), one question per URL with visible Last Updated (Skinnydip).
- Sample quotable statements: local ("workmanship guaranteed one year; install within seven days"), ecommerce ("returns free 30 days; ships in 2-5 business days; final-sale excluded"), SaaS ("kickoff within two days; 99.9% uptime target; encrypted in transit and at rest; credit if uptime missed").

## News and Roadmap page
- One hub listing launches, improvements and upcoming items, filterable by status (Launched, Rolling Out, Planned).
- Entry format: In short (one sentence) / Details (2-4 lines: what, why it matters, who affected) / Status / Date and owner / Links to Pricing, Policies, Docs.
- Include a change log of recent shipments plus a next-quarter roadmap block.
- Start each entry with a benefit-first "In short" line; keep language factual.
- Monthly review; archive old entries but keep them reachable.
- Models: dated newsroom with exec quotes (Apple), status-labelled public roadmap (Microsoft 365), plain-English change log with links to detail (Stripe).
- Local: new service areas/seasonal offers with dates. Ecommerce: drops, shipping updates, restocks. SaaS: features, integrations, release notes.

## Comparison and review content
- Query shapes buyers and AI use: "best", "alternatives", "vs", "review".
- Start with one pillar listicle: Best [solution] for [year]; then Best [solution] for [use case]; Best [solution] for [location] when local. Pillar defines the category, states evaluation method, links to deeper pages.
- Satellite pages from AI fan-out patterns: [Competitor] alternatives; [Your brand] alternatives; [Your brand] vs [Competitor]; [Comp] vs [Comp] vs [Your brand]; [Competitor] review; [Your brand] review.
- Scale math: ~30 competitors x 3 page types = ~90 pages, plus pillar and use-case pages = ~100 assets from one decision topic.
- Answer-ready blocks on every page: verdict box (best for / not ideal for / takeaway); comparison table (price range, use case, strengths, limits, buying factors); proof near each claim (screenshots, cases, reviews, benchmarks); "choose this if / that if" guidance; BoF FAQs (pricing, onboarding, integrations, support, limits, "is it worth it").
- Tone: help the buyer find fit; do not attack competitors.
- If a client refuses competitor pages on the main domain: place broader "best [solution]" content on industry blogs, associations or partner publications (slower, still participates in the decision space).

## Commercial cluster architecture
- Pick one pillar keyword, build every BoF page that fans out from it, and only then move to an adjacent cluster (often one tied to a different offer).
- Hub and spoke: pillar; use-case pages (audience/industry/location); competitor pages; mini-cluster per competitor linking its review, alternatives and vs pages.
- Link rules: every satellite links to the pillar (contextual link near the top); each competitor group cross-links; lateral links when useful; consistent anchor patterns ("best [solution] tools", "[competitor] alternatives", "[brand] vs [competitor]", "[competitor] review").
- Add a small "related decision pages" module at page bottom (pillar, competitor review, 1-2 related).
- Completion gate before the next cluster: all satellites link to pillar; competitor groups cross-link; every page has a next step; pillar links to key satellites; product, pricing and proof pages linked where relevant.

## Templates & prompts
- Verdict box: Best for: __ | Not ideal for: __ | Bottom line: __.
- Comparison table columns: Option | Price range | Primary use case | Strengths | Limits | Key buying factors | Proof link.
- Entry template (policy/FAQ): H3 question -> short answer -> next-step link -> Last Updated / Owner.
- Release entry: In short / Details / Status / Date + Owner / Links.

## Audit checks
- [ ] A Pricing page exists, is crawlable, and shows prices, a range or a starting-at figure.
- [ ] Pricing page states inclusions and extras and has a plan chooser or table.
- [ ] Pricing, Policies/FAQ and News/Roadmap pages each open with an "In short" line.
- [ ] Each of those pages displays Last Updated and Owner, dated within the last quarter.
- [ ] Policies cover refunds/returns, warranty, delivery, support, security, setup in uniform Q/A format.
- [ ] FAQPage schema exists and matches visible text exactly in meaning.
- [ ] News/Roadmap has status labels and a change log; reviewed monthly.
- [ ] The three official pages link to each other and appear in nav/footer.
- [ ] A category pillar listicle ("best X for year") exists.
- [ ] Alternatives, vs and review pages exist for the main competitors.
- [ ] Each BoF page has a verdict box, comparison table, proof, choose-if guidance, FAQs.
- [ ] Every satellite links to the pillar; competitor groups cross-link.
- [ ] Anchor text patterns are consistent across the cluster.
- [ ] Third-party sources (directories, comparison sites) do not contradict your official price/policy.
- [ ] Each BoF page has a clear next step (demo, buy, call).

## Actions
- Publish or rewrite the Pricing page with an In short line, ranges, inclusions, chooser. [Quick win]
- Build the Policies/FAQ hub using the uniform entry pattern and add matching FAQPage schema. [Foundation]
- Create the News/Roadmap hub with status tags and a monthly review slot. [Foundation]
- Add Official Answers links in nav/footer and cross-link the three pages. [Quick win]
- Write the category pillar listicle, then generate alternatives/vs/review pages per competitor. [Foundation]
- Add verdict box and comparison table to every existing BoF page. [Quick win]
- Fix inaccurate third-party listings by publishing the correct fact on your own page and requesting corrections. [Ongoing]
- Refresh official pages quarterly; log changes. [Ongoing]

## Pitfalls
- Hiding pricing behind "Contact us" so others guess for you.
- Topic hopping: one listicle per category with no depth.
- Hidden or low-value FAQ schema, or schema text that differs from visible text.
- Attack-style competitor pages with no proof.
- Letting official pages go stale, which gives third parties the upper hand.
- Starting a new cluster before the current one passes the completion gate.

## Related
- ch10, ch11 (retrieval-friendly structure), ch09 (topic planning), ch13 (clusters, freshness), ch14 (fixing weak BoF pages), ch15 (FAQ bank, schema), ch19 (reviews), ch20 (citations).
