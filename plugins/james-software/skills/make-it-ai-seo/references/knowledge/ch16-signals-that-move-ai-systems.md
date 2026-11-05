---
id: ch16
title: Identifying Signals That Move AI Systems
part: Part 5: Off-site trust and authority (brand signals)
tags: [AI signals, brand consistency, entity, reputation, reviews, sentiment, mentions, citations, links, retrieval-driven prospecting, source of truth, drift]
use_when: Auditing or fixing how consistently and credibly a brand appears across the web (identity, reputation, authority signals) so AI systems mention it accurately.
---

# ch16 — Identifying Signals That Move AI Systems

## Core idea
- AI systems favor consensus over claims: they compare many sources and reward brands whose facts agree everywhere.
- An "AI signal" is any clue about who you are, what you do, whether you are credible, and when to mention you. Most are the same things that make humans trust you.
- Three buckets must line up or doubt is created: Identity (name, category, descriptions, profiles), Reputation (reviews, sentiment, mentions, community talk), Authority (links, expert mentions, digital PR, references from strong sites).
- Mismatch (site says "AI SEO platform", LinkedIn says "content tool", a directory says "blogging software") makes AI mislabel you or pick a clearer competitor.

## Signal buckets and diagnostic questions
| Bucket | What it contains | Question AI effectively asks |
|---|---|---|
| Identity | Brand name, URL, category, descriptions, logo, NAP, profiles | Is this business real, and is its name/offer clear? |
| Reputation | Reviews, sentiment, unlinked mentions, forums, Reddit | Do others describe it the same way? Are customers satisfied? |
| Authority | Links, citations, expert quotes, digital PR | Do trustworthy sites mention or link to it? Is it established in its category? |

## Build a brand "source of truth" and detect drift
1. Write a master reference doc of core facts: exact brand name, URL, category/primary offer, short description, long description, logo/visuals, phone/address/service area (local), public pricing/plans, top products/services/modules.
2. Compare the doc against the public footprint: homepage, About, Contact, Google Business Profile, LinkedIn company page, Crunchbase, G2/Capterra/software directories, local directories/citations, social bios, press mentions, contributor bios.
3. Log drift: inconsistent descriptions, outdated info, conflicting details. If two sources disagree, AI cannot tell which to trust.
- Positioning rule: choose ONE primary category and ONE core message; wording may vary by platform, but the story must match (e.g. all say "AI search visibility / AI SEO software for agencies", not four different categories).

## Fix outdated and conflicting info (priority order)
1. Owned properties first: website, social bios, official profiles; fix one-liners, product descriptions, stats, claims, screenshots, CTAs.
2. Major third-party platforms: Google Business Profile, LinkedIn, review sites, top directories (name, category, description, logo, URL, contact, service area).
3. Pages that already rank for branded searches or get cited by AI: correct pricing, product names, availability, guarantees, feature details first.
4. Standardize details: local = name/address/phone/hours/service areas/categories; non-local = product names, company description, support links, official URLs.
5. Refresh media kits, founder bios, press kits, speaker/podcast bios, partner pages.
- Goal is reducing ambiguity where it matters, not perfecting the whole internet.

## Review signals (trust view; workflow detail in ch19)
- Five qualities of a strong review profile: volume, freshness, specificity, spread across respected platforms, consistent flow (not one burst).
- A review profile = star rating, total count, dates, text, owner responses, photos, recurring themes. It should look active and believable, not thin, stale, or suspicious.
- Specific reviews (mention service, location, problem, outcome) link your brand to use cases and categories, which is what AI cites.
- Local business rule of thumb: about 80-90% of review-request effort to Google Business Profile, 10-20% to the top niche directories.
- Niche platform examples: home services (Angi, Thumbtack, Yelp), legal (Avvo, FindLaw, Justia), healthcare (Healthgrades, Vitals, Zocdoc), software (G2, Capterra, TrustRadius), restaurants/hospitality (OpenTable, TripAdvisor, Yelp).
- Dominate the main platform first, then layer niche directories; do not spread requests thin.
- Never bribe or pressure for positive-only feedback.

## Sentiment management
- Sentiment = emotional tone across reviews, comments, forums, social posts, articles.
- Watch recurring patterns: pricing confusion, onboarding complaints, praise for a feature you rarely promote, negative assumptions from outdated info, expectation mismatch.
- Treat repeated complaints as a messaging/signal problem, not only a support problem: fix the cause, then make the fix visible (clearer pricing table, step-by-step setup docs with timelines, promote the praised feature on sales pages and FAQs). See ch12, ch14.

## Turning mentions into stronger signals
- Mention sources to scan: listicles, review roundups, industry blogs, podcasts, news, forums, Reddit, YouTube descriptions/transcripts, event speaker pages, sponsorship pages.
- Per mention check: brand name correct? description accurate? tone positive/neutral/negative? aligned with desired positioning? could it become a link or profile?
- An accurate unlinked mention can beat a linked mention with a wrong description.
- To get corrections made, hand the publisher an easy-to-verify source: updated About page, current media kit, product page, or short correction note (official name, category, URL, one-sentence description).

## Links vs citations vs mentions
- Link = clickable URL to you. Citation = source refers to your business/info (often name+address+URL). Mention = brand name appears. AI seems influenced by the full footprint, not one type.
- Shift: from "which sites look powerful" to "which sites already shape answers in my market".
- Follow vs nofollow vs sponsored: do not obsess. Presence on a heavily-cited source, described accurately, with clear category/expertise, often beats a follow link on an irrelevant site nobody retrieves. Relevance and context still matter; spam is still spam.

## Retrieval-driven prospecting (process)
1. Run many realistic customer prompts across AI platforms.
2. Record cited domains and repeated sources.
3. Build a master source list (book suggests eventually 500-1,000 citations in your industry).
4. For each frequent source, identify a realistic path in: directory listing, roundup inclusion, expert quote, podcast, original-data citation, review profile, sponsorship, local/industry press.
5. Prioritize domains that appear most often.
- Tactic per target: directory = claim/submit profile; roundup = pitch a specific update with proof; podcast/expert article = offer a quotable point of view.

## Templates & prompts
- Brand facts sheet columns: field | canonical value | where it must appear | last verified | owner.
- Mention triage columns: URL | type (mention/citation/link) | name correct | description correct | sentiment | action (correct / pitch link / ignore).
- Citation source tracker columns: prompt | AI platform | cited domain | count | opportunity type | status.
- Correction note: "Official name: X. Category: Y. URL: Z. One-line description: ..."

## Audit checks
- [ ] A written master brand-facts document exists and is current.
- [ ] Brand name, URL, category, and description are identical in meaning on site, LinkedIn, GBP, Crunchbase, review sites, directories, social bios.
- [ ] One primary category/positioning statement is used everywhere (no conflicting category labels).
- [ ] No outdated pricing, product names, addresses, or descriptions on pages that rank for branded queries or are cited by AI.
- [ ] Local: NAP, hours, service areas, categories match across platforms.
- [ ] Review profile on main platform has recent (last few months), detailed reviews, not just old star ratings.
- [ ] Reviews exist on 1-3 relevant platforms for the niche, not only one.
- [ ] Owner responses present on reviews.
- [ ] Recurring complaint themes have been addressed in site content (pricing, onboarding FAQs).
- [ ] Brand mentions (listicles, podcasts, forums) have been inventoried and checked for accuracy.
- [ ] A list of domains AI cites in the niche exists, with the brand's presence marked per domain.
- [ ] No spammy links, junk directory submissions, or exact-match anchor patterns in the profile.
- [ ] Founder/media bios use current positioning.

## Actions
- Create the master brand-facts document and circulate it. [Foundation]
- Fix owned properties and top third-party profiles to match it. [Quick win]
- Correct high-visibility outdated pages (branded results, AI-cited pages) first. [Quick win]
- Pick one category + positioning line and rewrite conflicting profile descriptions. [Quick win]
- Run prompts across ChatGPT/Perplexity/Gemini/AI Overviews, log cited domains, build the source list. [Foundation]
- For top-cited domains, pursue listing, roundup inclusion, expert commentary, original data. [Ongoing]
- Send correction notes to publishers with wrong brand descriptions. [Quick win]
- Fix complaint-driving content gaps (pricing table, setup guide) and publish the fix. [Quick win]
- Run the review system monthly and re-check drift quarterly. [Ongoing]

## Pitfalls
- Chasing mysterious "ranking factors" instead of fixing consistency.
- Treating nofollow/follow purity as the main criterion.
- Buying bulk links, spammy guest posts, fake-persona outreach, junk directories, exact-match anchor stuffing.
- Spreading review requests over too many platforms.
- Letting old directories, stale media kits, or old stats keep spreading.
- Assuming the claim "we are the best" counts; third-party agreement is what counts.
- Prospecting by generic authority instead of by what AI actually cites.

## Related
- ch04 (entity/glossary, sameAs), ch12 (BOFU pages), ch14 (underperformers), ch17 (profile audit), ch19 (review workflow), ch20 (links/mentions/citations).
