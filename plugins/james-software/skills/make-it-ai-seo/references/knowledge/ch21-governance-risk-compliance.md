---
id: ch21
title: Playing It Safe: Governance, Risk, and Compliance
part: Part 4: Off-site authority and trust
tags: [compliance, privacy, consent, defamation, YMYL, accessibility, bias, robots.txt, crawler policy, content rights, licensing, permissions log, provenance]
use_when: Reviewing content for legal/ethical risk, setting crawler and AI-use policies, or checking rights to published assets before and during AI SEO work.
---

# ch21 — Playing It Safe: Governance, Risk, and Compliance

## Core idea
- AI systems amplify what you publish: a risky claim, private detail, or unlicensed asset can be indexed, summarized, quoted and reused outside your control.
- Light guardrails beat heavy bureaucracy: review triggers, a permissions log, a one-page crawler policy, and an internal AI-use policy.
- Signals must match intentions: what you say is open/closed must equal what is actually open/closed.
- This is practical guidance, not legal advice; escalate high-stakes items to a qualified reviewer.

## Privacy and consent
- Keep off public pages unless necessary: personal phone/email, customer account details, medical or financial info, internal documents, screenshots exposing sensitive data, anything that could identify or embarrass someone.
- Case studies: readers need only client type, problem, what changed, result, lesson. Skip full names, account screenshots, sensitive numbers unless authorized.
- Permission is needed before publishing: testimonials, logos, headshots, photos/videos, screenshots, quotes from calls/emails/messages, client-identifying case-study details.
- Get written approval (an email is enough). Record: what was approved, where it can be used, whether edits are allowed, whether ads/social/sales pages are covered, any end date.

## Defamation and fact/opinion/allegation
- Risk zones: competitor comparison pages, alternatives pages, review pages, articles alleging misconduct, posts about scams or fraud.
- Describe experiences, not motives. Acceptable: "some users may find the reporting flow takes many steps." Risky: claims of deception or intent to trap users.
- Label content as one of three types and never blur them:
  - Fact: verifiable (e.g., the company changed its pricing page in January).
  - Opinion: your judgment (the new page is harder to understand).
  - Allegation: a claim made by others, unverified (some users say billing was confusing).
- Clear labeling also reduces the chance of misinformation in AI-generated answers.

## Review trigger workflow
- Flag a page for extra review if it contains: health/legal/financial advice, competitor claims, identifiable customer details, sensitive screenshots, regulated topics, bold guarantees, accusation language.
- Triggered-page check: (1) verify names, dates, screenshots, facts; (2) confirm written permission; (3) strip loaded wording and unsupported accusations; (4) save sources and approvals; (5) second reviewer if stakes are high.
- Build the trigger list into the content brief, checklist or PM task template.
- First audit targets: comparison pages, review pages, case studies, testimonial-heavy pages, YMYL pages, downloadable PDFs (extractable text, ideally with an HTML landing/summary page).

## YMYL (Your Money or Your Life) standards
- YMYL = medical, legal, financial, safety, mental health, major life planning. Higher bar than casual posts.
- Evidence bar: trustworthy sources, current, limitations stated, qualified reviewer when needed, updated when facts change; link credible sources, date time-sensitive data, cut claims that cannot be supported.
- Remove false certainty: be cautious with always, never, guaranteed, risk-free, proven, cure, prevent. Use calibrated wording: may help, can reduce, often improves, in many cases, depending on the situation.

## Accessibility (also helps machine understanding)
- Alt text on meaningful images; captions on video; transcripts for audio/video; logical heading order; descriptive link text; no text walls; explain charts/diagrams in surrounding copy.

## Bias review
- Bias = unbalanced framing favoring some viewpoints/groups: lazy reader assumptions, one-sided examples, stereotypes, broad generalizations, polished-but-unfair AI phrasing.
- Pre-publish questions: who is missing from the examples? what assumptions am I making? is the language fair? does the advice hold for people in different situations?

## Reviewing AI-assisted drafts
- Look for: unsupported claims, overconfidence, stereotypes, odd generalizations, missing caveats, advice that sounds universal but is not.
- Edit for judgment, not only grammar. High-stakes topics: review sourcing, remove exaggeration, check accessibility, read for bias, add a second reviewer.

## Crawler and AI signals
- Provenance: be able to show who created content, where published, whether edited, and the original source. Prioritize for original research, media assets, brand statements, public evidence; no need on every page.
- robots.txt: plain text file at domain root. Starter example: `User-agent: *`, `Disallow: /internal-search/`, `Disallow: /staging/`, `Sitemap: https://www.example.com/sitemap.xml`.
- Good uses of robots.txt: internal search, messy parameter URLs, thin utility pages, staging, crawl traps. Never block pages you want discovered, summarized or cited. It is not protection for private content (use authentication).
- Crawler policy (one internal page) answers: which bots are allowed/limited/blocked; which sections stay open; which are restricted or deprioritized; how staging is handled; who approves rule changes; review cadence.
- Signal-vs-intention audit: (1) list major content types; (2) mark each open/limited/blocked; (3) check real settings; (4) find contradictions; (5) assign one owner.
- Typical contradictions: section meant to be found but blocked; "restricted" file publicly reachable; key resources unlinked or missing from the sitemap.
- Highest-drift areas: PDFs, support docs, gated assets, staging, comparison pages, research pages, subdomains, utility folders.

## Content rights
- Inventory asset types: employee articles, freelancer content, stock photos, screenshots, embedded video, customer reviews, third-party study data, user-generated content, contractor graphics/video. Ownership differs per type; paid does not equal owned.
- Freelancer/contractor contracts should state: owner of final work, editing rights, cross-channel reuse, any third-party material used, whether AI tools were used, non-infringement confirmation.
- Third-party material (competitor screenshots, report charts, platform UI shots, article excerpts, public reviews): ask about permission, license/platform terms, minimal use, attribution, second review. Do not build pages around such assets without permission, license, or a clear fair-use rationale.
- Internal AI-use policy answers: may client-private data be pasted into tools? may contracts/internal docs be uploaded? may AI output be published without review? which tools are approved? which facts need human verification?
- Site terms should clarify ownership, permitted use, banned commercial reuse, trademarks, user submissions, disclaimers; most useful if you publish research, templates, data, media.
- Permissions log (spreadsheet) columns: asset name, source, creator, permission status, allowed uses, date approved, expiry, link to agreement.
- Unclear ownership on top-page assets (screenshots, customer proof, contractor visuals, licensed photos, third-party charts, AI drafts from private material) is a fix-now item.

## Templates & prompts
- Permissions log columns above; crawler-policy question list above; review-trigger list above.
- AI-draft review prompt: "List every factual claim, absolute word, and unsupported generalization in this draft; mark each as fact, opinion, or allegation and what source is needed."

## Audit checks
- [ ] No personal contact details, account data, or sensitive screenshots appear on public pages.
- [ ] Every testimonial, logo, headshot, and named case study has documented written permission.
- [ ] Comparison/alternatives/review pages avoid accusation language and separate fact from opinion.
- [ ] A review trigger list exists in the brief or checklist and was used on recent risky pages.
- [ ] YMYL pages cite credible, dated sources and show reviewer/author qualifications.
- [ ] YMYL and marketing pages avoid absolutes (guaranteed, risk-free, proven, cure) without support.
- [ ] Images have alt text; videos have captions; audio/video have transcripts; heading hierarchy is logical.
- [ ] robots.txt exists at root, references the sitemap, and does not block pages meant to rank or be cited.
- [ ] Private or gated content is protected by authentication, not only robots.txt.
- [ ] A documented crawler policy with owner and review cadence exists; staging and subdomains are handled.
- [ ] PDFs have extractable text and an HTML landing page or summary.
- [ ] A permissions log covers screenshots, stock/licensed images, third-party charts.
- [ ] Contractor agreements address ownership, reuse, third-party material, and AI use.
- [ ] Site terms address reuse of original research/templates/media.
- [ ] An internal AI-use policy exists and defines review before publishing.

## Actions
- Audit top pages for risk (comparison, review, case study, testimonial, YMYL, PDF) and fix anything questionable. [Quick win]
- Add review triggers to the content brief template. [Quick win]
- Replace absolute claims with calibrated wording on YMYL pages. [Quick win]
- Obtain and file written permissions; start the permissions log. [Foundation]
- Write a one-page crawler policy and run the signal-vs-intention audit; fix contradictions. [Foundation]
- Update contractor agreements and site terms; publish an internal AI-use policy. [Foundation]
- Add alt text, captions, transcripts, and descriptive link text sitewide. [Foundation]
- Re-run the audit on a schedule and on any subdomain/PDF launch. [Ongoing]

## Pitfalls
- Treating robots.txt as security.
- Publishing a screenshot or quote because "they would not mind."
- Letting different teams edit crawler rules without an owner.
- Using AI to draft YMYL pages with no qualified review.
- Assuming payment equals ownership for freelance work or stock assets.
- Blurring opinion with fact on competitor pages.

## Related
- ch10 (AI-readiness and crawl controls), ch11 (foundations), ch12 (BOFU comparison pages), ch15 (images, video, transcripts), ch19 (reviews), ch20 (outreach and asset rules), ch22 (blocking-crawler and AI-content myths), ch23 (fact hub, trust network)
