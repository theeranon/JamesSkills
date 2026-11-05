---
id: master-audit
title: Master AI SEO audit checklist
tags: [audit, checklist, master, scorecard, technical, content, brand, reviews, links, schema]
use_when: Step 4 of the workflow — score every item against the real site with evidence.
---

# Master AI SEO audit checklist
Total items: 320. Sources: every chapter's `## Audit checks` section (regenerate with scripts/build_index.py).


Score each item ✅ / ⚠️ / ❌ / ❓ with evidence (see 03-action-plan-template.md). Open the source chapter for criteria and fixes. Items marked off-site may need the user's accounts.

## A. Goal, positioning & topic ownership
- [ ] Home, About, Contact, pricing, product/service pages answer the seven source-of-truth questions. `ch01`
- [ ] Each key page opens with a direct answer (2-3 sentences) near the top. `ch01`
- [ ] Headings mirror real customer questions. `ch01`
- [ ] Comparison tables exist where buyers choose between options. `ch01`
- [ ] Core facts (name, description, category, location, pricing) are identical on site and top profiles. `ch01`
- [ ] Pricing/policy/product details and statistics are current (dated or recently reviewed). `ch01`
- [ ] Brand has a presence on the review/directory platforms relevant to its model. `ch01`
- [ ] A Day 0 prompt baseline (10-20 prompts) exists with dated screenshots. `ch01`
- [ ] Internal links connect key pages to their next-question pages. `ch01`
- [ ] Testimonials, screenshots, reviews used have permission and are verifiable. `ch01`
- [ ] Reporting includes more than traffic (coverage, position, SoV, citations, accuracy, sentiment). `ch01`
- [ ] Searching brand and category in classic search and AI tools shows no conflicting descriptions. `ch01`
- [ ] A dated Day 0 baseline (GSC export + 10-20 AI prompt results with screenshots) exists. `ch03`
- [ ] Prompt list covers best/top/near me/alternatives/vs/pricing/review/audience variants. `ch03`
- [ ] Brand name, description, URL, role are identical on site and Google Business Profile, LinkedIn, Crunchbase, key directories. `ch03`
- [ ] Organization (or Person) schema exists with sameAs links to verified profiles and validates without errors. `ch03`
- [ ] Multi-domain/sub-brand relationships are explained on-site. `ch03`
- [ ] Search Console, GA4 and a Looker Studio dashboard are connected and working. `ch03`
- [ ] A master tracking sheet and evidence library exist with consistent filenames. `ch03`
- [ ] A change log records every onsite edit with date and URL. `ch03`
- [ ] Top pages have a 2-3 sentence direct answer near the top. `ch03`
- [ ] A Facts section is present near the top of main pages. `ch03`
- [ ] At least one BoF page (best-for or alternatives) is published and internally linked. `ch03`
- [ ] A 90-day roadmap with 2-3 themes and a 12-18 item owned backlog exists. `ch03`
- [ ] A recurring weekly check and Friday review are scheduled. `ch03`
- [ ] One priority topic cluster is defined with a stated association. `ch18`
- [ ] Each of the nine query types has a dedicated asset or a deliberate decision to skip. `ch18`
- [ ] Each asset has a distinct job; no two pages target the identical intent. `ch18`
- [ ] A pillar page plus internal-linked supporting content and proof exists on the site. `ch18`
- [ ] Live SERP and AI answers for the topic were reviewed; gaps (video, alternatives, third-party) noted. `ch18`
- [ ] Multiple formats exist (page, post, video, comparison, checklist) for the topic. `ch18`
- [ ] A messaging sheet exists and site, YouTube, bios use consistent claims/terminology. `ch18`
- [ ] Brand appears on 3-5 relevant third-party audiences (podcasts, newsletters, roundups, publications). `ch18`
- [ ] Brand has genuine, non-promotional presence in 2-3 communities. `ch18`
- [ ] Past appearances were repurposed on site/social. `ch18`
- [ ] A monthly scorecard (visibility, coverage, trust) is maintained. `ch18`
- [ ] Not all proof lives only on the brand's own domain. `ch18`

## B. Measurement, baseline & tracking
- [ ] A prompt database exists with intent, stage, cadence, owner, country/language columns. `ch05`
- [ ] At least 25 prompts, majority nonbranded commercial. `ch05`
- [ ] Prompts sourced from GSC queries and/or customer language, not only synthetic. `ch05`
- [ ] Branded baseline prompts exist (review, vs, alternatives). `ch05`
- [ ] Coverage rate is computed per platform across at least three platforms. `ch05`
- [ ] Position is recorded (first mention) with total brands count. `ch05`
- [ ] A documented SoV scoring scale is in use and consistent. `ch05`
- [ ] Citation fields (own site, third-party presence, position) are logged. `ch05`
- [ ] Prompts run on a fixed cadence (weekly typical). `ch05`
- [ ] Lead forms or CRM capture self-reported AI attribution. `ch05`
- [ ] Branded search is monitored in GSC and Bing Webmaster Tools. `ch05`
- [ ] Events (launches, PR, reviews) are logged against tracking dates. `ch05`
- [ ] A category-level prompt shortlist is tracked for legitimacy. `ch05`
- [ ] GA4 has a custom channel group containing an "AI Chatbots" channel. `ch06`
- [ ] The AI channel regex covers at least chatgpt.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com, and escapes dots. `ch06`
- [ ] The AI group sits above default rules in priority. `ch06`
- [ ] AI channel appears in User acquisition report with data. `ch06`
- [ ] Data window used for AI reporting is 28+ days. `ch06`
- [ ] A shared evidence folder and tracking sheet exist with the listed columns. `ch06`
- [ ] Anchor prompts are captured on a regular schedule with screenshots. `ch06`
- [ ] Looker Studio report is connected to GA4, Search Console, and the sheet. `ch06`
- [ ] "AI Platform" and "AI Prompt Bucket" calculated fields exist. `ch06`
- [ ] Citation Rate formula returns a sensible value and ignores blank rows. `ch06`
- [ ] A change log exists and has recent entries. `ch06`
- [ ] A sanity-check routine runs before reports are shared. `ch06`
- [ ] Each experiment states a single hypothesis naming change, prompts, platforms, metrics. `ch08`
- [ ] Experiments are tagged with an Experiment ID across prompts, log, results. `ch08`
- [ ] Prompt set has 5-10 prompts including direct, related, and control roles. `ch08`
- [ ] Prompt wording is frozen for the whole test. `ch08`
- [ ] Baseline window (1-2 weeks) was captured before the change. `ch08`
- [ ] Follow-ups were scheduled in advance (2-4 weeks; optionally 6-8). `ch08`
- [ ] A change log entry exists with date, change, type, hypothesis. `ch08`
- [ ] Only one meaningful change shipped per test. `ch08`
- [ ] Model/mode/login/location info and platform events are recorded. `ch08`
- [ ] Results compare direct vs control movement. `ch08`
- [ ] Wins required multiple prompts, 2+ follow-ups, and 2+ platforms. `ch08`
- [ ] Outcome label and evidence sentence are recorded. `ch08`
- [ ] Wins converted into playbooks; failures documented. `ch08`

## C. Competitors & citation gaps
- [ ] A competitor list of 5-10 brands exists, typed Direct/Adjacent/Leader. `ch07`
- [ ] Competitor-branded and neutral commercial prompts are in the tracking set. `ch07`
- [ ] SoV is computed per competitor with the same scoring model. `ch07`
- [ ] SoV is broken out by platform, intent stage, and prompt cluster. `ch07`
- [ ] AI Mode and AI Overviews are tracked separately. `ch07`
- [ ] A Citation Sources log with 10-20 prompts across 3-5 platforms exists. `ch07`
- [ ] Core Evidence Sources (repeating domains) are listed. `ch07`
- [ ] A who's-featured-where matrix with priorities exists. `ch07`
- [ ] A target list maps each gap to a specific play. `ch07`
- [ ] Competitors' top-cited pages were reviewed for liftable passages. `ch07`
- [ ] Brand/entity consistency (About page, names, Organization/Product schema, profile links) was compared with competitors. `ch07`
- [ ] Review count, recency, and above-the-fold proof were compared. `ch07`
- [ ] A per-platform scorecard with Lead/Chasing/Absent labels exists. `ch07`
- [ ] robots.txt exists, does not block key pages or intended crawlers, and any AI-crawler rules are deliberate. `ch02`
- [ ] XML sitemap lists canonical indexable URLs and is submitted/discoverable. `ch02`
- [ ] Key commercial and brand pages are indexed (confirm with Search Console URL inspection / index coverage or site: checks). `ch02`
- [ ] Critical content is present in the initial server-rendered HTML (view-source or fetch without JS). `ch02`
- [ ] Important pages are reachable within a few clicks and linked from navigation/hubs. `ch02`
- [ ] Pages load fast and render well on mobile. `ch02`
- [ ] A brand/fact hub page states who, what, whom, where. `ch02`
- [ ] Commercial pages exist for the business model (service/location, category/product, feature/comparison). `ch02`
- [ ] Content includes original proof (data, case studies, firsthand experience), not only generic explainers. `ch02`
- [ ] Page 1 for each priority commercial query was reviewed and non-owned asset types (video, Reddit, directories, roundups) noted. `ch02`
- [ ] Brand has profiles on the niche's review platforms with recent real reviews. `ch02`
- [ ] One standard brand description is used consistently across site and profiles. `ch02`
- [ ] Repeating cited domains from AI answers in the niche were collected into a target list. `ch02`
- [ ] An evidence tracker with dated prompts and screenshots exists. `ch02`

## D. Crawl, index, render & AI-ready foundations
- [ ] A whole-site crawl and a separate top-10 money-page crawl were run with sane limits and parameter/facet traps excluded. `ch10`
- [ ] Crawled as Googlebot and as a generic bot; results compared for firewall/WAF differences. `ch10`
- [ ] Key pages compared in HTML-only vs rendered mode. `ch10`
- [ ] robots.txt does not block money pages, key folders, CSS/JS needed for rendering, or intended AI/search bots; no staging rules left in production. `ch10`
- [ ] No important page carries noindex (meta or X-Robots-Tag header) unintentionally; meta and header agree. `ch10`
- [ ] Main content, H1 and first-answer paragraph appear in raw HTML on money pages. `ch10`
- [ ] Money pages return a single stable 200 (no 3xx loops, 4xx, 5xx, soft 404). `ch10`
- [ ] Canonical tags point to the correct primary URL, are not parameter URLs, and do not change by variant. `ch10`
- [ ] Redirects are single-hop; internal links point to final canonical URLs, not to redirecting ones. `ch10`
- [ ] Broken internal links and soft 404s are rare and isolated. `ch10`
- [ ] Duplicate and thin clusters (tag archives, facets, location templates, parameters) are identified and handled. `ch10`
- [ ] Each money page is within a few clicks of home and linked from a relevant hub; no orphans among them. `ch10`
- [ ] Bot protection (Cloudflare/WAF) is not challenging or blocking legitimate crawlers. `ch10`
- [ ] Structured data on key pages validates and matches visible content. `ch10`
- [ ] Findings are grouped into issue clusters, scored (Severity + Reach + Commercial impact + Effort), and capped at a 20-item list with Top 10 on one page. `ch10`
- [ ] Every fix item is tagged to exactly one of the four buckets with an owner. `ch10`
- [ ] All nine gates are scored for each of the 10 money pages. `ch10`
- [ ] View source of each money page contains the H1, first-answer paragraph and core body copy. `ch11`
- [ ] Money, core informational and hub pages are server-rendered (or CSR pages have the minimum viable HTML); no hydration mismatch. `ch11`
- [ ] Exactly one H1 per page; heading levels follow hierarchy and are not used only for styling. `ch11`
- [ ] Key answers are visible without clicking accordions, tabs or modals. `ch11`
- [ ] Comparison tables and lists are real HTML, not images. `ch11`
- [ ] Internal links are `<a href>` anchors, not JavaScript-only handlers. `ch11`
- [ ] No cookie gate or geo pop-up hides critical content from bots. `ch11`
- [ ] Each page has a canonical pointing to its intended URL. `ch11`
- [ ] Money pages are reachable in 3 clicks or fewer from the homepage. `ch11`
- [ ] Each cluster has a hub linking to every priority spoke; each spoke links back to the hub and to 2-3 related spokes. `ch11`
- [ ] Breadcrumbs exist on deeper pages and match URL structure. `ch11`
- [ ] Anchor text is descriptive and varied; no "click here" or footer-only links to key pages. `ch11`
- [ ] No important page is reachable only through search, filters or infinite scroll. `ch11`
- [ ] Key sections begin with entity-naming, self-contained passages (claim, audience, proof). `ch11`
- [ ] Organization (or LocalBusiness) schema exists on the entity home/About/Contact page. `ch11`
- [ ] Product schema appears only on genuine product/plan pages. `ch11`
- [ ] FAQPage schema is present only where Q&A is visible and matches the on-page text exactly. `ch11`
- [ ] FAQ answers are at most three sentences and put prices/timing/constraints in plain language. `ch11`
- [ ] A fact hub exists with Claim/Value/Source/Last Verified columns and is linked from pages repeating those facts. `ch11`
- [ ] Redirects are single-hop and internal links point at final URLs (carry over ch10 gates 2, 7, 8). `ch11`

## E. Topic plan, architecture & topical authority
- [ ] A keyword/topic research sheet exists with consistent columns, including Cluster, Intent, Opportunity, Status and page URL mapping. `ch09`
- [ ] Every priority keyword maps to exactly one primary URL (no two pages targeting the same intent). `ch09`
- [ ] Each target keyword has a named page type that matches the dominant SERP format. `ch09`
- [ ] A pricing/cost page exists and states current prices or ranges, plan details, trial terms. `ch09`
- [ ] Comparison and alternatives pages exist for competitors that prospects mention. `ch09`
- [ ] "Best for"/use-case pages exist for main segments. `ch09`
- [ ] FAQ and proof pages (case studies, testimonials) exist and are linked from the pillar. `ch09`
- [ ] Each commercial cluster has one identifiable pillar page that is linked from navigation or hubs. `ch09`
- [ ] Support pages link to the pillar with descriptive anchors, and the pillar links back out to them. `ch09`
- [ ] Pricing, features and terms are identical across site pages (no conflicting facts). `ch09`
- [ ] A client/brand knowledge base with proof, policies, entities, FAQs and Last Updated dates exists. `ch09`
- [ ] Search Console was reviewed for positions 2-15 queries and high-impression/low-click queries. `ch09`
- [ ] Competitor gap analysis done against 3-10 direct competitors for each target cluster. `ch09`
- [ ] Unaware/TOFU content is limited and links onward to BoF pages. `ch09`
- [ ] Each topic has a recorded decision (build now / later / don't) with a score. `ch09`
- [ ] Topic boundary (in/out of scope) is written down. `ch13`
- [ ] Content exists in all four buckets (explain, decide, implement, prove). `ch13`
- [ ] A seed list of 10-20 commercial prompts and GSC low-volume queries exists. `ch13`
- [ ] A gap matrix marks Owned/Thin/Missing for subareas. `ch13`
- [ ] Key pages have a short primary answer, 5-10 follow-up answers, and who-for/not-for plus proof. `ch13`
- [ ] An Entity Home page states brand + category, one-line description, audience, proof, official profile links. `ch13`
- [ ] Brand, product, feature and plan names are spelled identically site-wide and off-site. `ch13`
- [ ] Core positioning wording is stable across pages, bios, schema. `ch13`
- [ ] Major pages link to the entity home with consistent anchors. `ch13`
- [ ] Organization (or relevant) schema includes sameAs pointing only to controlled/representative profiles, and those profiles agree with the site. `ch13`
- [ ] Key pages show a freshness box (last updated, what changed, sources). `ch13`
- [ ] A review cadence by content type exists and is followed (check dates). `ch13`
- [ ] No duplicate-intent or keyword-variant pages split relevance. `ch13`
- [ ] Retired pages 301 to a winner; sitemap and canonicals reflect that. `ch13`
- [ ] An update log exists and is current. `ch13`

## F. Bottom-of-funnel / commercial pages
- [ ] A Pricing page exists, is crawlable, and shows prices, a range or a starting-at figure. `ch12`
- [ ] Pricing page states inclusions and extras and has a plan chooser or table. `ch12`
- [ ] Pricing, Policies/FAQ and News/Roadmap pages each open with an "In short" line. `ch12`
- [ ] Each of those pages displays Last Updated and Owner, dated within the last quarter. `ch12`
- [ ] Policies cover refunds/returns, warranty, delivery, support, security, setup in uniform Q/A format. `ch12`
- [ ] FAQPage schema exists and matches visible text exactly in meaning. `ch12`
- [ ] News/Roadmap has status labels and a change log; reviewed monthly. `ch12`
- [ ] The three official pages link to each other and appear in nav/footer. `ch12`
- [ ] A category pillar listicle ("best X for year") exists. `ch12`
- [ ] Alternatives, vs and review pages exist for the main competitors. `ch12`
- [ ] Each BoF page has a verdict box, comparison table, proof, choose-if guidance, FAQs. `ch12`
- [ ] Every satellite links to the pillar; competitor groups cross-link. `ch12`
- [ ] Anchor text patterns are consistent across the cluster. `ch12`
- [ ] Third-party sources (directories, comparison sites) do not contradict your official price/policy. `ch12`
- [ ] Each BoF page has a clear next step (demo, buy, call). `ch12`

## G. Page-level quality & underperformers
- [ ] Candidate pages identified from impressions/CTR, page 2 positions, conversion data, AI citation checks. `ch14`
- [ ] Each target page has a written job (keyword, prompt, stage, action). `ch14`
- [ ] Page type matches the dominant type in SERP and AI citations. `ch14`
- [ ] Primary keyword/variant appears in URL, title, meta description, H1, opening lines, first H2. `ch14`
- [ ] Single H1; H2s phrased as real questions/subtopics. `ch14`
- [ ] Direct answer appears near the top; no long preamble. `ch14`
- [ ] Short paragraphs, lists, tables used where helpful. `ch14`
- [ ] A competitor set (Google plus AI platforms) was compiled and de-duplicated. `ch14`
- [ ] Page covers recurring entities, subtopics, questions and objections from the set. `ch14`
- [ ] Proof, examples, author credentials and sources are visible. `ch14`
- [ ] Internal links point to the page from hubs/FAQ/comparison/cluster pages. `ch14`
- [ ] Offer, objections handling and CTA are clear. `ch14`
- [ ] Changes are logged with date, reason and expected result. `ch14`
- [ ] Success metric and review window were set before editing. `ch14`
- [ ] Only one main fix was changed per test cycle where feasible. `ch14`

## H. Media, schema, datasets & creative assets
- [ ] Every meaningful image has descriptive, non-stuffed alt text. `ch15`
- [ ] Decorative images use empty alt. `ch15`
- [ ] Charts, screenshots and diagrams have captions that state the takeaway, placed directly beneath. `ch15`
- [ ] Videos on ranking/educational/conversion pages have a transcript or at minimum a summary. `ch15`
- [ ] Transcripts were human-checked for brand, product, names, numbers, terminology. `ch15`
- [ ] Long videos have timestamps/section headers. `ch15`
- [ ] VideoObject markup has name, description, thumbnail, upload date, duration, and points to the canonical page. `ch15`
- [ ] Schema content is visible on the page and consistent with headings/captions. `ch15`
- [ ] FAQPage markup only wraps visible, useful Q&A. `ch15`
- [ ] No excessive or purposeless schema types. `ch15`
- [ ] Original datasets (if any) show date range, source/sample size, methodology, and written findings. `ch15`
- [ ] Dataset findings are reused and linked back from other pages. `ch15`
- [ ] An approved FAQ bank exists and the same answer wording appears across pages. `ch15`
- [ ] Charts are explained in text, not left bare. `ch15`
- [ ] Key pages open with a short direct answer or summary and use question-style subheads. `ch23`
- [ ] At least one comparison table or labeled stat block exists on commercial pages. `ch23`
- [ ] A public fact hub exists and matches LinkedIn, directories, and profile data (name, description, dates, locations). `ch23`
- [ ] Brand name variants and official spellings are documented. `ch23`
- [ ] A consensus kit (positioning, case studies, approved stats) exists and is shared with partners and PR. `ch23`
- [ ] Priority pages show a current date and have no outdated screenshots, pricing, or broken links. `ch23`
- [ ] Stats on the site carry a year and source. `ch23`
- [ ] An original dataset, benchmark, or study with methodology is published. `ch23`
- [ ] FAQs appear on product, service, pricing, and location pages, with answers starting with the direct answer. `ch23`
- [ ] A public change log exists (where product or service changes) with dated entries. `ch23`
- [ ] AI workflows draw from documented approved sources. `ch23`
- [ ] Trust network elements (author bios, reviews, directory listings, certifications) are present and consistent. `ch23`
- [ ] Expert-authored or expert-reviewed content is visible, with credentials. `ch23`

## I. Brand entity, consistency & profiles
- [ ] A written master brand-facts document exists and is current. `ch16`
- [ ] Brand name, URL, category, and description are identical in meaning on site, LinkedIn, GBP, Crunchbase, review sites, directories, social bios. `ch16`
- [ ] One primary category/positioning statement is used everywhere (no conflicting category labels). `ch16`
- [ ] No outdated pricing, product names, addresses, or descriptions on pages that rank for branded queries or are cited by AI. `ch16`
- [ ] Local: NAP, hours, service areas, categories match across platforms. `ch16`
- [ ] Review profile on main platform has recent (last few months), detailed reviews, not just old star ratings. `ch16`
- [ ] Reviews exist on 1-3 relevant platforms for the niche, not only one. `ch16`
- [ ] Owner responses present on reviews. `ch16`
- [ ] Recurring complaint themes have been addressed in site content (pricing, onboarding FAQs). `ch16`
- [ ] Brand mentions (listicles, podcasts, forums) have been inventoried and checked for accuracy. `ch16`
- [ ] A list of domains AI cites in the niche exists, with the brand's presence marked per domain. `ch16`
- [ ] No spammy links, junk directory submissions, or exact-match anchor patterns in the profile. `ch16`
- [ ] Founder/media bios use current positioning. `ch16`
- [ ] A profile inventory spreadsheet exists with claimed status and scores. `ch17`
- [ ] Searches for brand, brand+city, brand+founder, brand+product, brand+reviews, brand+category were run and results logged. `ch17`
- [ ] Every Tier 1 profile (GBP, LinkedIn, main review profile, About, Contact, founder bio) is green. `ch17`
- [ ] Brand name identical across all inventoried profiles. `ch17`
- [ ] Website URL on each profile is correct and live (no broken or old-domain links). `ch17`
- [ ] Category on each profile reflects the real business; no misleading extra categories. `ch17`
- [ ] Descriptions state audience + job + solution in plain language. `ch17`
- [ ] Logo/imagery is current everywhere. `ch17`
- [ ] Local: NAP matches across GBP, Bing Places, Apple Maps, Yelp, directories. `ch17`
- [ ] No duplicate listings, or merge/closure requests are filed. `ch17`
- [ ] Review profiles are complete, have recent reviews, and owner responses. `ch17`
- [ ] Website links to key profiles; Organization/LocalBusiness/Person schema has sameAs for them. `ch17`
- [ ] No links to retired social accounts or abandoned profiles. `ch17`
- [ ] A named owner and review cadence (quarterly/twice yearly) exist. `ch17`
- [ ] Founder/author bio is clear and consistent with company positioning. `ch17`

## J. Reviews
- [ ] 1-3 primary review platforms are identified and justified by buyer behavior. `ch19`
- [ ] Primary platform has recent reviews (not all old) and a steady rate rather than a single burst. `ch19`
- [ ] Reviews include specifics (service, problem, outcome), not mostly one-liners. `ch19`
- [ ] Average rating, count, and recency are recorded per platform. `ch19`
- [ ] Profiles are complete: description, category, website link, images, contact, services. `ch19`
- [ ] Business name, address, positioning match across review platforms. `ch19`
- [ ] Owner responses exist for recent positive and negative reviews, and are non-templated. `ch19`
- [ ] Negative responses are professional and offer a next step. `ch19`
- [ ] A documented request workflow exists (trigger, owner, channel, direct link, one follow-up, tracking). `ch19`
- [ ] Customers get one clear link, not a menu of platforms. `ch19`
- [ ] No evidence of review gating, incentives, scripted text, or fake reviews. `ch19`
- [ ] A review-theme analysis (praise and complaint patterns) has been done and fed into site content/operations. `ch19`
- [ ] Secondary platforms (niche directories) are maintained, not abandoned. `ch19`

## K. Links, mentions & digital PR
- [ ] A list of decision-making pages (best-of, alternatives, directories) exists for the main category and each money query. `ch20`
- [ ] Brand appears on the top-ranking best-of/alternatives pages for its category queries (check manually and in AI answers). `ch20`
- [ ] Sources cited by AI assistants for category prompts are identified, and brand presence on each is known. `ch20`
- [ ] A tracking sheet with status per target exists and is current. `ch20`
- [ ] A one-sentence description, proof points, and pricing summary are published on a clean offer page. `ch20`
- [ ] A PR kit (bio, boilerplate, logo, quotes, approved stats) is accessible at a public or shareable URL. `ch20`
- [ ] At least one link-worthy asset (study, tool, benchmark, template) exists and has a methodology note. `ch20`
- [ ] Referring domains are topically relevant; no obvious PBN/paid-link/irrelevant-directory patterns in the backlink profile. `ch20`
- [ ] Mentions without links are logged, and unlinked mentions on strong sites have been followed up. `ch20`
- [ ] Outreach follows a cadence (max ~2 follow-ups) and results are logged. `ch20`

## L. Governance, risk, crawler policy & compliance
- [ ] No personal contact details, account data, or sensitive screenshots appear on public pages. `ch21`
- [ ] Every testimonial, logo, headshot, and named case study has documented written permission. `ch21`
- [ ] Comparison/alternatives/review pages avoid accusation language and separate fact from opinion. `ch21`
- [ ] A review trigger list exists in the brief or checklist and was used on recent risky pages. `ch21`
- [ ] YMYL pages cite credible, dated sources and show reviewer/author qualifications. `ch21`
- [ ] YMYL and marketing pages avoid absolutes (guaranteed, risk-free, proven, cure) without support. `ch21`
- [ ] Images have alt text; videos have captions; audio/video have transcripts; heading hierarchy is logical. `ch21`
- [ ] robots.txt exists at root, references the sitemap, and does not block pages meant to rank or be cited. `ch21`
- [ ] Private or gated content is protected by authentication, not only robots.txt. `ch21`
- [ ] A documented crawler policy with owner and review cadence exists; staging and subdomains are handled. `ch21`
- [ ] PDFs have extractable text and an HTML landing page or summary. `ch21`
- [ ] A permissions log covers screenshots, stock/licensed images, third-party charts. `ch21`
- [ ] Contractor agreements address ownership, reuse, third-party material, and AI use. `ch21`
- [ ] Site terms address reuse of original research/templates/media. `ch21`
- [ ] An internal AI-use policy exists and defines review before publishing. `ch21`

## M. Strategy sanity (myths) & vocabulary
- [ ] Strategy documents do not assume Google traffic is irrelevant; Google organic is still tracked. `ch22`
- [ ] Core technical foundations (crawl, index, internal links, titles, speed, consistent NAP/brand data) are verified, not skipped for "AI-only" work. `ch22`
- [ ] The measurement plan tracks AI mentions/citations by prompt set, not a single "ChatGPT rank." `ch22`
- [ ] Crawler rules are intentional per bot and section; public valuable pages are not blanket-blocked, restricted content is truly protected. `ch22`
- [ ] Pages are judged on structure and completeness, not word count targets. `ch22`
- [ ] AI-assisted pages show human-added evidence (testing, pricing checks, expert input, review) before publishing. `ch22`
- [ ] The off-site footprint (reviews, directories, press, social, local citations) is audited, not only the website. `ch22`
- [ ] Backlinks, mentions, and citations are reported as three separate metrics. `ch22`
- [ ] The plan has a shared foundation plus documented per-platform notes. `ch22`
- [ ] No deliverable promises fixed AI ranks or guaranteed citations. `ch22`
- [ ] An entity home page exists and lists official name, location, leadership, offerings, descriptor. `ch04`
- [ ] Brand name, spelling and core description are identical across site, profiles and directories. `ch04`
- [ ] Organization schema present, valid, with `sameAs` to verified profiles. `ch04`
- [ ] Author pages/Person schema exist for content authors with credentials and affiliation. `ch04`
- [ ] Article pages carry headline, author, publisher, datePublished and dateModified in markup and visibly. `ch04`
- [ ] Product/Service/Review schema matches visible page content and passes Rich Results Test. `ch04`
- [ ] A fact hub exists with source, date and update history per number. `ch04`
- [ ] Key facts appear identically on third-party reputable sites (fact coverage checked). `ch04`
- [ ] Core pages contain self-contained passages naming the brand and use case near the top. `ch04`
- [ ] Passages use the brand name rather than pronouns and place proof next to claims. `ch04`
- [ ] SoV is tracked per query per platform with position and a documented weighting. `ch04`
- [ ] JSON-LD is in version control with a change log and testing step in publishing. `ch04`
- [ ] No schema claims exceed the evidence (no "schema guarantees AI visibility"). `ch04`
- [ ] The audit states which AI platforms are in scope and which classic engines are in scope. `ch00`
- [ ] The audit separates "platform-level" findings (how the answer is displayed) from "system-level" findings (what is retrieved). `ch00`
- [ ] Deliverables contain no guarantee language about rankings, citations or AI mentions. `ch00`
- [ ] Traditional SEO health (crawl, index, content, links) is assessed alongside AI-specific checks. `ch00`
- [ ] Findings are tied to evidence (screenshots, dated prompt logs, exports), not opinion. `ch00`
