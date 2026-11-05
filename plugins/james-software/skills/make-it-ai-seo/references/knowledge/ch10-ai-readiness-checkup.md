---
id: ch10
title: Conducting an AI-Readiness Checkup
part: Part 3: Building Pages and Foundations
tags: [crawl audit, Screaming Frog, robots.txt, noindex, canonical, redirect chain, soft 404, JavaScript rendering, triage score, AI-ready checklist, WAF, orphan pages]
use_when: Auditing whether a site can be fetched, rendered, indexed and trusted by search and AI bots; triaging crawl findings into a prioritized fix list; running the pass/fail eligibility gates.
---

# ch10 — Conducting an AI-Readiness Checkup

## Core idea
- Most AI search systems still depend on classic crawl, index and retrieval. If pages cannot be fetched consistently or main content is not readable on first pass, great content never enters the evidence set.
- Workflow: crawl (two lenses) -> label findings -> cluster issues -> score with a 4-factor model -> Top 10 Fixes -> capped 20-item list -> first sprint -> run the 9-gate pass/fail checklist.
- Deliverables: Crawl Findings Summary (what), Prioritized Fix List (what first), AI-Ready Checklist (eligible or not). This chapter is triage only; implementation is ch11.

## Crawl scope and lenses
- Two passes: Wide lens = whole-site crawl for systemic template/navigation problems. Money lens = 10 most important pages (home, core service/product, pricing, Best and Alternatives pages, top landing pages, main categories). Choose them from analytics or a tool like Rankability.
- User-agent lens: crawl as Googlebot (baseline) and as a generic/unknown bot (reality check). Differences reveal firewall/bot-management rules blocking lesser-known crawlers, which may include AI retrieval and citation bots. With Cloudflare or another WAF, assume false positives; a "blocked" result may be a security rule, not a content issue.
- Render lens: view key pages as HTML-only (raw source, no JS) and as rendered (after JS). Many retrieval systems behave like fast fetchers, not full browsers.
- Scope limits: set depth/URL caps, avoid traps (infinite calendars, parameter combinations, faceted filters, sort/color/size variants). Be consistent rather than perfect.
- Tools: Screaming Frog (status codes, indexability, canonicals, redirect chains, duplicates, internal links, crawl depth); Siteliner (duplicate and thin content); Rankability (anchor the audit on top 10 pages). Tools find; humans decide.

## Reading the crawl (Crawl Findings Summary sheet)
- Sheet columns: Issue, Finding Type, Example URL, URLs Affected, Money Page Impact, AI Retrieval Risk, Red Flag, Notes.
- Keep a finding if it repeats across a template, hits a money page, blocks crawl/render, hides content, or creates source-URL confusion. Park isolated low-value items.
- Finding types: Indexing and access (robots directives, noindex, blocked resources, auth walls); Rendering and missing content (thin/empty HTML, JS-only content, delayed content, hidden text); Canonicalization and duplicates (wrong canonicals, duplicate clusters, parameter variants, near-identical pages); Redirects and status waste (chains, loops, soft 404s, broken internal links, excessive redirects); Architecture and discoverability (deep important pages, orphans, weak internal linking, inconsistent hubs).
- For every kept issue answer: what is it, how to spot it (report/column/pattern), why it matters for retrieval (blocks fetching, reduces trust, or makes extraction inconsistent), where it usually lives (template, plugin, server rule, migration, CMS setting, security layer).
- Red Flag column = Yes when the finding causes: Fetch failure (blocked, gated, noindex, persistent 4xx/soft 404); Render failure (main content missing from HTML-only view); Truth ambiguity (canonicals/duplicates hide the source of truth); Discovery weakness (money pages buried/orphaned/unreinforced); Extraction weakness (content not in clean, extractable sections).
- Finish with a short summary: top 5-10 systemic issues, where they occur (templates/sections), whether money pages are hit, which block access or use by AI.

## High-impact issues: how to spot, why it matters, where it lives
- Blocked by robots.txt: "Blocked by robots.txt" flags, whole folders missing from crawl. Bot cannot fetch = cannot cite. Lives in robots.txt, security settings, staging rules copied to production. Beware blocking helpful bots while blocking bad ones.
- Noindex on important pages or mixed signals: indexability column shows noindex, or HTTP header conflicts with meta tag. Unstable trust for systems using indexed sets/caches. Lives in CMS plugins, templates, headers, dev settings. Verify whether intentional.
- Redirect chains and loops: more than one hop (301 -> 301 -> 200) or never resolving. Wastes crawl budget, slows discovery. Lives in migrations, http->https and www/non-www rules, old slugs, canonical mistakes.
- Soft 404s and thin not-found pages: 200 status but empty/error-like; low word count, many broken internal links. Poor evidence and broken discovery paths. Lives in deleted pages with poor redirects, expired listings, internal search pages, thin tag archives.
- Thin or empty HTML: HTML-only crawl shows little main content while rendered crawl shows full content. Passages cannot be extracted reliably. Lives in SPAs, heavy JS frameworks, delayed hydration, lazy-loaded or gated sections.
- Canonical confusion: canonical points to an unexpected URL or varies by parameter. Fragments signals, may push the wrong version into evidence. Lives in templates, parameter handling, pagination, i18n, e-commerce filters.
- Duplicate clusters: Siteliner duplicates, near-identical titles/meta, parameter variants. Dilutes authority, raises odds of a weak variant being chosen. Lives in tag archives, facets, location pages, print versions, tracking parameters.
- Money pages deep or orphaned: high crawl depth, orphan URL patterns, low inlink counts. Architecture signals importance. Lives in weak navigation, missing hubs, blog posts that never link to commercial pages.

## Triage: deciding what to fix first
- Buckets: stop-the-bleeding (blocks crawl/index/render), performance drags (crawl waste, weakened trust, fragmented signals), nice-to-have cleanup.
- Group findings into issue clusters: one root cause fixed in one place (template, rule, plugin setting) = one issue even if 5,000 URLs. Examples: legacy redirects chaining across old blog URLs; JS-rendered service pages with thin HTML; inconsistent canonicals on parameter URLs; internal links to non-canonical URLs; tag pages creating duplicates/thin content.
- 4-factor triage score: Priority = Severity + Reach + Commercial impact + Effort, each 1-5 (higher = fix sooner; for Effort 5 = hours, 1 = rebuild).
  - Severity: 5 bots cannot crawl/index/see content; 3 bots confused or waste time (chains, broken links, duplication); 1 cosmetic.
  - Reach: 5 sitewide/multiple templates; 3 one template/section; 1 few pages.
  - Commercial impact: 5 money pages/conversion paths; 3 high-traffic supporting pages; 1 low-value pages.
  - Effort: 5 hours; 3 up to a week; 1 rebuild-level.
  - Worked examples: service pages missing HTML-only content = 5+3+5+3 = 16 (near top); handful of old posts with duplicate titles = 2+1+1+5 = 9 (later). Ties: money pages first, then faster to ship.
- AI eligibility blockers auto-escalate into the Top 10 regardless of score: key pages blocked by robots/WAF; key pages not index-eligible (noindex/conflicts); key content missing in HTML-only mode; canonicals pointing away from the real page; money pages buried or orphaned.
- Top 10 Fixes page (one page, hand-off ready): Issue name (plain English), Bucket, Why it matters (one sentence on crawl/retrieval/revenue), Scope (URL count + 2-3 samples), Priority score, Owner, Notes (dependencies/risks). If not describable in one sentence, it is not ready.
- Prioritized fix list: add next-best items only up to 20 total; the rest wait for the next audit cycle.
- Every fix maps to exactly one bucket (same as ch11): HTML/Rendering; Architecture/Internal Links; Speed/Redirects/404; Schema/FAQ/Fact Hub. Rewrite vague items until they fit.
- First sprint: 3-5 fixes that remove eligibility blockers first, improve money pages first, are high impact/low effort, and ship independently.

## Minimum AI-ready checklist (9 gates, pass / fail / needs review)
- Layout: one row per top-10 page, one column per gate, plus note; keep as an "AI-Ready Checklist" tab in the crawl workbook.
- Gate 1 Content in HTML: pass if main content is in raw/server-rendered HTML; fail if HTML is placeholders and content appears only after rendering.
- Gate 2 Clean 200: money pages return 200 consistently; fail on 3xx loops, 4xx, 5xx, soft 404.
- Gate 3 Not blocking crawlers: not blocked by robots.txt or security rules; fail on "blocked"/"access denied"/inconsistent results pointing to bot protection.
- Gate 4 Index-eligible: no unintended noindex, no meta-vs-header conflict.
- Gate 5 Canonicals sane: consistently point to the correct primary URL.
- Gate 6 Discoverable: money pages reachable within a few clicks from navigation/hubs; fail if buried, weakly linked, or orphaned.
- Gate 7 No systemic redirect chains: mostly one hop; chains/loops common on internal links = fail.
- Gate 8 No routine dead ends: broken internal links and soft 404s rare and isolated.
- Gate 9 Structured data valid: schema validates and matches visible content (goal is avoiding trust-eroding errors, not schema everywhere).
- Interpretation: failing several gates means foundations beat more content. Failed gates already in the Top 10 stay there; otherwise add them; tag each into one fix bucket. Failed gates become highest-priority items.

## Templates & prompts
- Crawl Findings Summary columns (above) and the six-question note for each issue.
- Priority formula and 1/3/5 scales (above).
- Top 10 Fixes row: Issue | Bucket | Why it matters | Scope (n URLs + samples) | Score | Owner | Notes.
- AI-Ready Checklist grid: rows = top-10 URLs; columns = Gates 1-9; cell = Pass/Fail/Needs Review + note.

## Audit checks
- [ ] A whole-site crawl and a separate top-10 money-page crawl were run with sane limits and parameter/facet traps excluded.
- [ ] Crawled as Googlebot and as a generic bot; results compared for firewall/WAF differences.
- [ ] Key pages compared in HTML-only vs rendered mode.
- [ ] robots.txt does not block money pages, key folders, CSS/JS needed for rendering, or intended AI/search bots; no staging rules left in production.
- [ ] No important page carries noindex (meta or X-Robots-Tag header) unintentionally; meta and header agree.
- [ ] Main content, H1 and first-answer paragraph appear in raw HTML on money pages.
- [ ] Money pages return a single stable 200 (no 3xx loops, 4xx, 5xx, soft 404).
- [ ] Canonical tags point to the correct primary URL, are not parameter URLs, and do not change by variant.
- [ ] Redirects are single-hop; internal links point to final canonical URLs, not to redirecting ones.
- [ ] Broken internal links and soft 404s are rare and isolated.
- [ ] Duplicate and thin clusters (tag archives, facets, location templates, parameters) are identified and handled.
- [ ] Each money page is within a few clicks of home and linked from a relevant hub; no orphans among them.
- [ ] Bot protection (Cloudflare/WAF) is not challenging or blocking legitimate crawlers.
- [ ] Structured data on key pages validates and matches visible content.
- [ ] Findings are grouped into issue clusters, scored (Severity + Reach + Commercial impact + Effort), and capped at a 20-item list with Top 10 on one page.
- [ ] Every fix item is tagged to exactly one of the four buckets with an owner.
- [ ] All nine gates are scored for each of the 10 money pages.

## Actions
- Run both crawls (Screaming Frog; Siteliner for duplicates) and build the Crawl Findings Summary sheet. [Foundation]
- Test top pages with view-source and an HTML-only crawl to find JS-dependent content. [Quick win]
- Review robots.txt and WAF/bot-management rules for accidental blocks of legitimate bots. [Quick win]
- Remove unintended noindex and resolve meta-versus-header conflicts. [Quick win]
- Cluster issues by root cause, score them, and write the Top 10 Fixes page with owners. [Foundation]
- Escalate every AI eligibility blocker above its raw score. [Quick win]
- Pick a 3-5 item first sprint of independent, high-impact, low-effort fixes. [Quick win]
- Complete the 9-gate checklist for the top 10 pages and add failed gates to the fix list. [Foundation]
- Re-run the checkup each audit cycle; roll deferred items forward. [Ongoing]

## Pitfalls
- Treating every crawler warning as equal; "fixing everything" instead of triaging.
- Fixing the same template issue URL by URL instead of once at the source.
- Assuming noindex or blocking is intentional without checking.
- Trusting only the browser view; the bot may see an empty page.
- Misreading WAF false positives as content problems (or vice versa).
- Letting the fix list grow beyond 20 items or spill past one page.
- Letting a crawl balloon on faceted/parameter URLs.

## Related
- ch11 (implementing the fixes), ch09 (clusters), ch04 (glossary), ch05-ch06 (tracking), ch14 (underperformers), ch16 (signals), ch21 (bot governance).
