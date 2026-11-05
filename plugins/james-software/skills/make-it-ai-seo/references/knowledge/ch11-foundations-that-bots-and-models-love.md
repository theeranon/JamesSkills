---
id: ch11
title: Establishing Foundations That Bots (and Models) Love
part: Part 3: Building Pages and Foundations
tags: [build ticket, server-side rendering, SSR vs CSR, semantic HTML, internal links, hub and spoke, anchor text, schema, FAQPage, fact hub, Organization schema, retrieval-friendly passages]
use_when: Implementing technical and structural fixes: build tickets, crawlable HTML, SSR, headings, internal linking and hubs, schema choice, FAQ blocks, fact hubs, with validation checklists.
---

# ch11 — Establishing Foundations That Bots (and Models) Love

## Core idea
- Implementation chapter: turn the top fixes from ch10 into build tickets with a defined "done", then verify in practice (not "looks fine in the browser").
- Goal: pages that are accessible, clearly structured, interlinked and backed by stable facts so they are crawled, retrieved, and cited.
- Four systems: clean HTML, architecture/internal links, speed/redirects/404 reclamation, and structured content (schema, FAQ blocks, fact hubs).
- Note: the source text available for this chapter details the first three-quarters of these systems; speed/redirect/404 implementation is only referenced, so use ch10 redirect/200-status gates as the acceptance tests there.

## Build tickets (ship the top three, then the next three)
- Pick the top 3 issues from the ch10 list: those blocking/weakening access to important pages, repeating across a template, tied to commercial prompts/pricing/products/services/locations, and small enough to finish and verify. Rule: highest impact, widest reach, lowest reasonable effort; cosmetic cleanup later.
- Ticket fields: Goal (one primary outcome plus secondary wins: crawl reliability, clear retrieval, citation odds, steady indexing, UX, conversion); Surface area (exact templates, components, systems: blog/service template, navigation, routing, CMS fields, schema generator, caching); Acceptance criteria (plain-language "done" plus the matching validation checklist below); Risk level.
- Risk tags: Low = copy, headings, internal links, small HTML changes. Medium = URL changes, routing, navigation, canonical and redirect updates. High = rendering strategy, caching, big template refactors, JS-heavy behavior changes.
- Tools: spreadsheet for solo work; Asana, Trello, Jira, ClickUp or Monday for multi-person review. Same short format every time; one quick read.
- Example acceptance criteria: main content visible in view source; no redirect chains; FAQ answers visible and match schema; hub links to every spoke.

## Clean, AI-friendly HTML
- Applies strictly to revenue/visibility pages (pricing, service, product, location, pillar); optional elsewhere.
- Core guidelines:
  - Main content in server-rendered HTML whenever possible.
  - Semantic structure that survives without CSS: H1/H2/H3 hierarchy, lists for sets/steps, tables for comparisons, definition-style blocks for terms/entities.
  - Retrieval-friendly passages: short self-contained paragraphs, name the entity, state the claim, avoid pronoun-heavy text.
  - Keep key answers visible, not only inside accordions, tabs, closed dropdowns or post-load content (bots may extract inconsistently or weight it lower).
- SSR vs CSR: SSR delivers real content in the first HTML (best for crawl/retrieval and fast display). CSR delivers a near-empty shell filled by JavaScript; risky because many crawlers/retrieval systems do not reliably wait, render, or execute, and render budgets/timeouts vary.
- Frameworks (React, Vue, Next, Nuxt, SvelteKit): use SSR for money pages, core informational pages meant to be cited, and hub pages controlling linking/discovery.
- If CSR is unavoidable, the initial HTML must still contain the H1, a direct first-answer paragraph, primary body copy (key sections, not just headings), and real internal links.
- Hydration pitfall: server output differs from client output after load, so bots can see inconsistent versions (partial indexing, wrong extraction, missing passages). Keep server and client output identical.
- View-source test: right-click > View Page Source, then search for the H1, first-answer paragraph and a few body lines. Found = a basic crawler likely sees it.
- Good structure: one H1 matching the main topic; H2s mapped to user intents/questions; short standalone paragraphs; lists/tables for comparisons; definition blocks for entities and terms.
- Bad structure: multiple H1s; headings chosen for styling; giant multi-claim paragraphs with unnamed pronouns; key answers locked in collapsible sections.
- Passage pattern (top of key sections): Sentence 1 names the entity and claim ("[Entity] is [category] that [does what]"); Sentence 2 says who/when it fits ("best for [audience] when [condition]"); Sentence 3 gives proof, constraint or next step ("key differentiator is [proof/metric/example]").
- HTML validation checklist: view source has primary headings and core body copy (not placeholders); exactly one H1; H2/H3 hierarchy makes sense skimmed; core answers visible without clicks; key tables/lists are real HTML (not images); internal links are real `<a href>`; critical content not blocked by cookie gates or geo pop-ups; canonical exists and points to the intended URL.

## Architecture and internal links
- Mental model: important pages reachable within 3 clicks of home; each cluster has a hub and spokes; descriptive anchors; navigation and breadcrumbs mirror true hierarchy and URL structure.
- Links work like street signs: answer "what should the reader do next, and why?". Anchors describe the destination ("Sump pump repair in Chicago"), never "click here"/"learn more".
- Placement: in main body content (not footer only), near the passage where the concept appears.
- Orphans: every important page needs at least one link from a relevant hub and 2-5 outbound links to closely related pages (stay inside the cluster).
- Good links: contextual with a promise ("see our repair service page for pricing, failure signs, scheduling"; "battery backup versus water-powered backup"). Bad links: generic "click here", footer-only links to key services, random cross-links between unrelated posts.
- Hub-and-spoke: hub (pillar/category, e.g. "Sump pump services") introduces the category and links to repair, installation, backup, cost, FAQ, emergency. Each spoke covers one subtopic, links back to the hub and sideways to 2-3 related spokes (repair -> cost, battery backup). Improves discovery and clarifies relationships.
- Architecture validation checklist: every money page linked from at least one hub; hubs link to all priority spokes; breadcrumbs on deeper pages matching URL structure; important pages not hidden behind search, filters, infinite scroll; links are crawlable HTML anchors (not JS click handlers); anchor text descriptive and varied (not one anchor repeated sitewide).

## Schema, FAQ blocks, fact hubs
- Schema decision guide (label the page's main purpose only): Organization (LocalBusiness if local) on the entity home/About/Contact page; Product (plus Offer when appropriate) on true product/plan pages; FAQPage only when the Q&As are visibly on the page. Never mark up content not shown (invisible Q&A, phantom offers erode trust and cause extraction mismatch).
- FAQ block pattern: brief literal answers; pricing, timing, guarantees, constraints in plain language; no marketing fog. Format: Question (commercial), Answer of at most three sentences = direct answer, one sentence of context, one sentence of proof/constraint/next step.
- Commercial FAQ starter questions: How much does it cost? Which factors affect price? How fast can you schedule? Do you offer emergency service? What brands/areas do you serve? What is included (and not)?
- FAQ example shape: "How much does sump pump repair cost in Chicago?" -> price range with drivers, then diagnostic-fee policy, then next step (schedule an inspection).
- Fact hub: one page gathering key verifiable facts with the claim, entity, date and Last Updated, source link/internal reference, and definition notes. Purpose: one source of truth instead of numbers drifting across ~15 pages.
- Fact hub layout: H1 "[Brand/topic] facts and statistics"; intro (what the page is, update cadence); table with columns Claim | Value | Applies To | Source | Last Verified | Notes; sections for company facts, product facts, pricing facts, performance/stat facts, definitions.
- Linking rule: wherever a key number/claim appears elsewhere, link the claim text to the fact hub row; the hub links out to full-context pages (case study, methodology, docs). Verification path: claim -> source of truth -> supporting evidence.
- Schema/FAQ/fact-hub validation checklist: Organization/LocalBusiness schema on entity home; Product schema only on real product/plan pages (not blog posts); FAQPage only with visible Q&A; FAQ answers short, direct and identical to page copy; fact hub exists for key claims and is linked from pages repeating them; fact hub has Last Updated and source notes for numbers.

## Templates & prompts
- Build ticket: Goal | Surface area | Acceptance criteria (+ checklist) | Risk (Low/Medium/High).
- Retrieval passage: "[Entity] is [category] that [does what]. It's best for [audience] when [condition]. The key differentiator is [proof/metric/example]."
- FAQ item: Q (commercial) / A (direct answer + context + proof or next step; max 3 sentences).
- Fact hub table header: Claim | Value | Applies To | Source | Last Verified | Notes.
- Hub/spoke rule: hub -> all priority spokes; spoke -> hub + 2-3 sibling spokes.

## Audit checks
- [ ] View source of each money page contains the H1, first-answer paragraph and core body copy.
- [ ] Money, core informational and hub pages are server-rendered (or CSR pages have the minimum viable HTML); no hydration mismatch.
- [ ] Exactly one H1 per page; heading levels follow hierarchy and are not used only for styling.
- [ ] Key answers are visible without clicking accordions, tabs or modals.
- [ ] Comparison tables and lists are real HTML, not images.
- [ ] Internal links are `<a href>` anchors, not JavaScript-only handlers.
- [ ] No cookie gate or geo pop-up hides critical content from bots.
- [ ] Each page has a canonical pointing to its intended URL.
- [ ] Money pages are reachable in 3 clicks or fewer from the homepage.
- [ ] Each cluster has a hub linking to every priority spoke; each spoke links back to the hub and to 2-3 related spokes.
- [ ] Breadcrumbs exist on deeper pages and match URL structure.
- [ ] Anchor text is descriptive and varied; no "click here" or footer-only links to key pages.
- [ ] No important page is reachable only through search, filters or infinite scroll.
- [ ] Key sections begin with entity-naming, self-contained passages (claim, audience, proof).
- [ ] Organization (or LocalBusiness) schema exists on the entity home/About/Contact page.
- [ ] Product schema appears only on genuine product/plan pages.
- [ ] FAQPage schema is present only where Q&A is visible and matches the on-page text exactly.
- [ ] FAQ answers are at most three sentences and put prices/timing/constraints in plain language.
- [ ] A fact hub exists with Claim/Value/Source/Last Verified columns and is linked from pages repeating those facts.
- [ ] Redirects are single-hop and internal links point at final URLs (carry over ch10 gates 2, 7, 8).

## Actions
- Convert the top 3 ch10 issues into build tickets with goal, surface area, acceptance criteria and risk; verify before starting the next 3. [Foundation]
- Switch money, pillar and hub pages to SSR (or add H1, answer paragraph, body copy and links to the initial HTML). [Foundation]
- Run the view-source check on money pages and fix any content absent from raw HTML. [Quick win]
- Reduce each page to one H1 and repair heading hierarchy. [Quick win]
- Show core answers openly; move key content out of accordions/tabs/pop-ups. [Quick win]
- Convert image-based tables or lists to HTML. [Quick win]
- Replace JS click handlers with `<a href>` links; swap generic anchors for descriptive ones. [Quick win]
- Build hub pages and interlink spokes; add breadcrumbs; link orphans from relevant hubs. [Foundation]
- Rewrite section openers with the three-sentence passage pattern. [Ongoing]
- Add Organization/LocalBusiness schema on the entity home; Product schema on product pages; FAQPage only for visible Q&A. [Foundation]
- Add commercial FAQ blocks (three-sentence answers) to money pages. [Quick win]
- Create a fact hub and link repeated claims to it; update Last Verified on schedule. [Foundation]
- Collapse redirect chains, fix broken links and reclaim 404s with single-hop redirects to the best equivalent page. [Quick win]
- Re-verify each shipped ticket against its checklist, then queue the next three. [Ongoing]

## Pitfalls
- Trying to clean up everything at once instead of shipping three verified tickets.
- Declaring done because the page looks right in a browser.
- Relying on client-side rendering or hydration that changes content after load.
- Schema or FAQ markup for content that is not visible, or answers that differ from the markup.
- Footer-only or "click here" links; orphaned money pages; one anchor repeated everywhere.
- Facts (prices, stats) duplicated across pages and drifting out of sync.
- Multiple H1s and styling-driven headings.
- Over-long FAQ answers full of marketing language.

## Related
- ch10 (audit and triage that feeds these tickets), ch09 (clusters and pillars), ch12 (BoF pages), ch13 (topical authority), ch15 (images/video/data), ch16 (signals), ch04 (glossary: schema, fact hub), ch21 (crawler governance).
