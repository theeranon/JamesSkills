---
id: ch07
title: Competitive Intelligence for AI SEO
part: Part 2: Measuring AI SEO
tags: [competitor benchmarking, share of voice, citation gap analysis, source matrix, target list, entity clarity, reputation footprint, market share by platform, AI Mode, AI Overviews]
use_when: Benchmarking competitors in AI answers, finding which sources AI trusts that exclude you, and deciding which platforms and sources to attack first.
---

# ch07 — Competitive Intelligence for AI SEO

## Core idea
- AI winners differ from Google winners. Ask who appears, who appears early, who is backed by citations, and which sources recur across prompts and platforms.
- Reuse the ch05 prompt database and SoV scoring; just add competitor labels and views.
- SoV says who wins; citation gaps say why; entity and reputation checks say what to fix.

## Why AI winners differ from Google winners
- AI platforms may merge several sources into one list.
- They often lean on review sites, directories, and best-of lists, even if those do not rank first for your queries.
- They may favor clear positioning plus strong third-party proof over strong SEO.

## Choose a competitor set
- 5-10 brands max. Too many is unmanageable; too few loses context.
- Types: Direct (same buyer decision set), Adjacent (related tools AI may still suggest), Category Leader (shape the category story).
- Competitor sheet columns: Brand, Type, Website, Category.

## Extend the prompt database
- Keep existing commercial prompts. Add a small set of competitor-branded prompts ("[Competitor] review", "[Competitor] vs [You]", "Alternatives to [Competitor]") and neutral nonbranded commercial prompts ("Best [category] tools for [segment]", "Best [category] providers in [location]").
- Tracking columns: Prompt, AI Platform, Brand, Present (1/0), Position (1,2,3 or None), Notes.
- Same prompts, same platforms, over time; do not overreact to one run since the same prompt can differ within a day.
- If testing ChatGPT for current sources, enable Search; otherwise it may answer mostly from training data.

## Turn presence into SoV and slice it
- Use ch05 position weights (1.0, 0.8, 0.6, 0.4, 0.2). Worked example: answer lists five tools; Competitor A pos 1 = 1.0, B pos 2 = 0.8, you pos 3 = 0.6, others 0.4 and 0.2. Repeat over about 20 prompts and total.
- Views: by AI platform (track AI Mode and AI Overviews separately), by intent stage (Solution/Product/Most Aware), by prompt cluster (Best Tools, Alternatives, Versus, local).
- Output you want: a short list of fixable gaps, e.g., visible in alternatives but not best-tools; visible on one platform only; Competitor A dominates early mentions on solution-stage prompts.
- Insights to expect: you can appear often yet lose (always position 4-5); one cluster can carry a competitor's whole score, revealing their investment and your opening.

## Citation gap analysis (4 steps)
- Citation patterns differ by platform; analyze per surface.
- Step 1, collect: pick 10-20 priority commercial prompts and 3-5 platforms; run each; log source domains in a Citation Sources tab with date, prompt, platform, source domain, page type, whether you/competitors appear on that source. Summarize repeating domains in a "Core Evidence Sources" block at the top.
- Step 2, classify sources and match the play:
  - Review platforms: earn real reviews, respond, complete profile
  - Directories/marketplaces: claim listing, pick right category, align description with positioning
  - Media/niche publications: pitch data, expert commentary, original research
  - Best-of listicles/comparisons: build comparison pages, strengthen proof, outreach when missing or misrepresented
  - Brand sites (yours and rivals'): add clear passages, proof, reusable facts
- Step 3, who's-featured-where matrix: rows = sources, columns = brands, cells Y/N for meaningful presence, plus Priority (H/M/L). High = frequently cited by AI AND favorable to competitors AND realistically influenceable (claimable profile, review site you can earn on, pitchable publication).
- Step 4, target list: Source + URL, Type, Priority, Play (profile, reviews, editorial pitch, contribution).

## Why AI picks certain sources: reverse-engineer
- AI-ready passages: for prompts competitors win, open the cited pages and find the 2-3 sentences that could be lifted. Typical traits: say what it is, who it is for, and the outcome in plain words; scannable format; specifics like numbers, reviews, named use cases. Rework your key pages so your "recommendable paragraph" is obvious.
- Entity clarity quick checks on competitors: clear About/Company page (what, who, where, credibility)? consistent brand/product names across site, LinkedIn, listings? basic structured data (Organization, Product)? consistent links to canonical profiles? Then tighten your own entity home, naming consistency, and core schema.
- Reputation footprint: compare review volume per key platform, review recency (stale = weaker), and proof near the main offer (testimonials, logos, ratings, case studies, short proof points near top of key pages). Respond with a review-and-profile strategy: earn reviews, update profiles AI already cites, surface proof on-site.

## Market share by AI platform
- Treat each platform as a separate market (different sources, competitors, formats).
- Scorecard row per platform: your SoV, top competitors' SoV, your average position, your citation coverage, notes on gaps. Label each: Lead (ahead), Chasing (close), Absent (rarely shows).
- Prioritize with three filters: audience fit (where buyers are), pipeline signals (platforms appearing in attribution/sales calls), reachability (cited sources you can influence).

## Templates & prompts
- Competitor sheet: Brand | Type | Website | Category.
- Citation Sources tab: Date | Prompt | Platform | Source domain | Page type | You present? | Competitor present?
- Matrix: Source | You | Comp A | Comp B | ... | Priority.
- Target list: Source URL | Type | Priority | Play.
- Platform scorecard: Platform | Your SoV | Top competitor SoV | Avg position | Citation coverage | Status (Lead/Chasing/Absent) | Notes.

## Audit checks
- [ ] A competitor list of 5-10 brands exists, typed Direct/Adjacent/Leader.
- [ ] Competitor-branded and neutral commercial prompts are in the tracking set.
- [ ] SoV is computed per competitor with the same scoring model.
- [ ] SoV is broken out by platform, intent stage, and prompt cluster.
- [ ] AI Mode and AI Overviews are tracked separately.
- [ ] A Citation Sources log with 10-20 prompts across 3-5 platforms exists.
- [ ] Core Evidence Sources (repeating domains) are listed.
- [ ] A who's-featured-where matrix with priorities exists.
- [ ] A target list maps each gap to a specific play.
- [ ] Competitors' top-cited pages were reviewed for liftable passages.
- [ ] Brand/entity consistency (About page, names, Organization/Product schema, profile links) was compared with competitors.
- [ ] Review count, recency, and above-the-fold proof were compared.
- [ ] A per-platform scorecard with Lead/Chasing/Absent labels exists.

## Actions
- Define the competitor set and add competitor prompts. [Foundation]
- Run SoV across platforms and publish a per-platform scorecard. [Foundation]
- Build the Citation Sources tab and who's-featured-where matrix. [Foundation]
- Claim and complete directory/review profiles marked High. [Quick win]
- Write a clear recommendable paragraph on key pages (what, who, outcome, proof). [Quick win]
- Start a review-generation program on the platforms AI cites. [Ongoing]
- Pitch editorial/listicle sources from the target list. [Ongoing]
- Align entity signals: About page, naming, schema, canonical profile links. [Foundation]
- Re-run the benchmark on a fixed cadence. [Ongoing]

## Pitfalls
- Assuming Google rank equals AI visibility.
- Tracking too many competitors.
- Treating all citation sources alike instead of matching the play to source type.
- Assuming one platform's cited sources apply to all.
- Reading single-run differences as real.
- Chasing sources you cannot influence.

## Related
- ch05 (scoring), ch06 (sheets/dashboard), ch08 (turn gaps into tests), ch11 (entity/foundations), ch12 (comparison pages), ch19 (reviews), ch20 (citations and mentions).
