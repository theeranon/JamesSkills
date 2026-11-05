---
id: ch17
title: Looking Good Wherever You're Found
part: Part 5: Off-site trust and authority (brand signals)
tags: [profile audit, entity pages, Google Business Profile, LinkedIn, directories, NAP, duplicates, sameAs, traffic light scoring, brand consistency, maintenance]
use_when: Auditing third-party profiles and entity pages (GBP, LinkedIn, directories, review sites) and fixing inconsistent, incomplete or duplicate listings.
---

# ch17 — Looking Good Wherever You're Found

## Core idea
- A brand lives wherever people and machines can find it, not just on the website: LinkedIn, GBP, review profiles, directories, social bios, old forgotten pages.
- If these pages tell the same clear story, trust rises; if they conflict, look abandoned, or say little, both buyers and AI systems get confused.
- Method: audit in a spreadsheet, prioritize into tiers, fix top-tier first, link everything back to the site, then maintain on a schedule with a named owner.

## Entity pages vs profile pages
- Profile pages: accounts/listings you can claim and edit (GBP, LinkedIn company page, social bios, G2, Capterra, Yelp, Clutch, marketplace pages).
- Entity pages: any page that helps define or confirm who you are (About, Contact, founder/author bio, Crunchbase-type database entries, industry directories, chamber/association listings).
- Inclusion rule: if a customer or AI assistant might use the page to understand the business, it belongs in the audit. Each profile fix reinforces the entity.
- Profiles typically communicate: official name, category, products/services, location/service area, URL, phone/address, logo/images, reviews/ratings, specialty, and whether the business looks active.

## Practical profile audit (spreadsheet)
- Columns: Platform | URL | Claimed/unclaimed | Brand name accuracy | Description accuracy | Category accuracy | Contact info accuracy | Logo and imagery | Reviews present | Last updated | Priority | Notes.
- Discovery searches to run: brand; brand + city; brand + founder name; brand + product name; brand + reviews; brand + category.
- Start with the most visible results, then go through the major platforms for the business type.
- Log each meaningful result: URL, platform, whether you control it, green/yellow/red score, fix in Notes (old logo, wrong category, duplicate, missing website link). Mark high priority if it ranks in branded search or is cited by AI.
- Guiding question: which profiles shape how my brand appears when someone goes looking?

## Fields to check on every profile
- Brand name (official?), website URL (correct?), category (accurate?), description (clear?), NAP for local, images/branding (current logo?), reviews (present, recent, relevant?), freshness (looks current or abandoned?).
- If time-limited, check brand name, website URL, and description first.

## Common audit findings
- Duplicate profiles, outdated phone/address, broken links, weak descriptions, wrong categories, inconsistent brand names, empty profiles, old logos, unclaimed listings, unclear founder bios, review pages with no owner replies.

## Traffic-light scoring
- Green = accurate, complete, current. Yellow = mostly okay, needs cleanup. Red = inaccurate, thin, outdated, or unclaimed.

## Prioritization
- High-impact pages show up in search, shape buyer perception, get referenced by AI, support authority, reinforce category/positioning.
- Typical top list: homepage, About, Contact, founder/bio page, GBP (if local), LinkedIn company page, main review-platform profiles, strongest third-party category pages.
- Five-question prioritizer: ranks for branded searches? buyer could see it before choosing? AI could use it as evidence? supports positioning? fixable this week?
- Tiers: Tier 1 = high visibility/trust, fix now; Tier 2 = useful support pages; Tier 3 = low-visibility listings, clean later.

### Focus by business type
| Business type | Prioritize |
|---|---|
| Local | GBP, Apple Maps and Bing Places (if relevant), Yelp, local directories, chamber listings, local review platforms; NAP consistency is key |
| SaaS | Homepage + product pages, About, LinkedIn company page, founder profiles, G2, Capterra, TrustRadius, Crunchbase, Product Hunt; main risk is weak positioning/category alignment |
| Agencies / professional services | Service pages, About, founder bio, LinkedIn, GBP, Clutch, industry directories, review profiles; combine company profile with visible personal authority |
| E-commerce | Brand site, product pages, marketplace storefronts, social commerce profiles, review platforms, retail partner profiles; clarity and product consistency |

## Executing the fixes
### Rewrite weak descriptions
- Replace vague fluff ("innovative, customer-centric solutions...") with plain language stating audience, job, outcome.
- Formula: We help [audience] do [job] through [category or solution].
- Example pattern: "We help SEO agencies create content that performs better in traditional and AI-driven search."

### Consistency, not sameness
- Keep aligned: official name, main category, URL, core offer, positioning, geography, brand visuals. Wording can vary per page.

### Clean up duplicates
1. Claim the correct profile. 2. Save the duplicate URL. 3. Request merge/removal/closure via the platform's own claim/merge/report-duplicate flow. 4. Strengthen the surviving profile. If removal is slow, make the right version fuller and clearer.

### Fix review profiles
- Complete description, category, website link, images, services/products, contact fields.
- Choose closest primary category; remove categories that misrepresent the business.
- Refresh stale reviews with honest requests on the platform that matters most.
- Reply to important reviews with short, specific notes.
- Make description/FAQs reinforce the promise the reviews and site make.

### Connect profiles to the website
- Point each profile to the most relevant page, not automatically the homepage.
- Link from About, Contact, or footer to major profiles where it helps verification.
- Add profile URLs to Organization / LocalBusiness / Person schema `sameAs` where appropriate (ch04).
- Same name, logo, category language on both sides of every link.
- Remove or update links to old domains, old locations, retired social accounts, abandoned profiles.

## Workflow sequence
1. Finalize the source-of-truth doc (ch16). 2. Fix website core identity pages. 3. Update Tier 1 profiles. 4. Clean duplicates and broken links. 5. Strengthen review pages and third-party profiles. 6. Log all changes.

## Maintenance routine
- Tier 1 profiles: review quarterly. Tier 2: twice a year.
- Trigger a profile-update sprint after rebrand, address change, new product launch, pricing shift, new target market.
- Assign one named owner for profile upkeep; log new accounts when created; store credentials/ownership info securely.

## Templates & prompts
- Searches: `"Brand"`, `"Brand" city`, `"Brand" founder`, `"Brand" product`, `"Brand" reviews`, `"Brand" category`.
- Change log columns: date | platform | field changed | before | after | who.
- Owner register: platform | login owner | account email | recovery contact | next review date.

## Audit checks
- [ ] A profile inventory spreadsheet exists with claimed status and scores.
- [ ] Searches for brand, brand+city, brand+founder, brand+product, brand+reviews, brand+category were run and results logged.
- [ ] Every Tier 1 profile (GBP, LinkedIn, main review profile, About, Contact, founder bio) is green.
- [ ] Brand name identical across all inventoried profiles.
- [ ] Website URL on each profile is correct and live (no broken or old-domain links).
- [ ] Category on each profile reflects the real business; no misleading extra categories.
- [ ] Descriptions state audience + job + solution in plain language.
- [ ] Logo/imagery is current everywhere.
- [ ] Local: NAP matches across GBP, Bing Places, Apple Maps, Yelp, directories.
- [ ] No duplicate listings, or merge/closure requests are filed.
- [ ] Review profiles are complete, have recent reviews, and owner responses.
- [ ] Website links to key profiles; Organization/LocalBusiness/Person schema has sameAs for them.
- [ ] No links to retired social accounts or abandoned profiles.
- [ ] A named owner and review cadence (quarterly/twice yearly) exist.
- [ ] Founder/author bio is clear and consistent with company positioning.

## Actions
- Build the audit spreadsheet and run the six discovery searches. [Quick win]
- Score each profile green/yellow/red and tier it. [Quick win]
- Rewrite weak descriptions with the formula on Tier 1 profiles. [Quick win]
- Claim unclaimed listings and request duplicate merges. [Foundation]
- Update logos, categories, URLs, contact data across Tier 1 and Tier 2. [Foundation]
- Add sameAs links in schema and footer/About links to profiles. [Foundation]
- Assign a profile owner and calendar the quarterly/semiannual reviews. [Ongoing]
- Run an update sprint after any major business change. [Ongoing]

## Pitfalls
- Polishing ten obscure listings while the main pages stay wrong (activity is not impact).
- Demanding word-for-word identical copy instead of aligned core facts.
- Pointing every profile at the homepage.
- No owner: neglected profiles quietly become the wrong version of the brand.
- Leaving duplicates uncorrected so trust is split.
- Overengineering the audit; a spreadsheet and traffic lights suffice.

## Related
- ch04 (entity, schema sameAs), ch16 (source of truth, drift), ch19 (review profile quality), ch20 (citations/mentions), ch21 (credential security/governance).
