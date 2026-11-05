---
id: ch15
title: Making Images, Video, and Data Work for You
part: Part 3: Building Content That Gets Chosen
tags: [alt text, captions, transcripts, video, VideoObject, ImageObject, FAQPage schema, dataset, original data, FAQ bank, media SEO, accessibility]
use_when: Auditing or improving media on a page: image alt/captions, video transcripts and schema, original datasets, and reusable FAQ answers.
---

# ch15 — Making Images, Video, and Data Work for You

## Core idea
- Media does not explain itself. Search engines and AI need nearby text stating what the asset is, what it shows and why it matters.
- Captions, transcripts and alt text turn media into retrievable, citable evidence; schema reinforces what is already visible.
- Original datasets and a reusable FAQ bank compound value across the whole site when pages link back to a single source of truth.

## Captions
- Formula: what this is + what it shows + why it matters. Weak captions merely label ("dashboard"); strong ones state the takeaway.
- A caption should explain the main point, tell the reader what to notice, tie the visual to the page's argument, or add context not visible in the image.
- Match to type: screenshot = the feature/issue visible; chart = trend or comparison; diagram = process or relationship; product/service image = what matters to the buyer.
- Place directly below the asset so proximity gives context.

## Video transcripts
- AI may not watch video but can read text; a transcript frees content trapped in the player, aids accessibility, gives engines readable text, and feeds reuse.
- Include a transcript for any video on a page meant for search visibility, education or conversion. Skip for decorative clips, brand montages, short social snippets not meant to rank, teach or answer.
- Full vs cleaned: use full/verbatim for webinars, interviews, compliance-sensitive or exact-wording content; use cleaned (filler removed) for demos, educational or thought-leadership videos.
- Enhance with: short summary on top, timestamps on long videos, section headers, pull quotes or takeaways.
- Auto-generated transcripts (YouTube, LinkedIn) contain errors; review immediately, checking first: brand names, product names, proper nouns, numbers, industry terms. On LinkedIn treat the transcript as part of the post.
- Repurpose one video into: transcript, recap article, checklist, several FAQs, captioned screenshots, summary block for other pages.

## Alt text
- Primary purpose is accessibility (for screen readers or failed loads); also gives context to engines.
- Describe meaningful content, not file type. Weak: "graph", "screenshot", "SEO chart". Better pattern: chart type + what it shows (e.g., line chart of citation coverage rising after FAQ sections were added).
- By type: decorative = empty alt (alt=""), only when the image adds no meaning; photo = relevant subject; screenshot = visible feature or key point; chart = trend/comparison; diagram = flow/relationship.
- Test question: if someone cannot see this, what must they know to understand the page?
- Do not stuff keywords; a plain description beats a keyword jumble.

## Media schema
- First make the visible page clear: topic, media present, what it shows, main task/claim. Fix headings, labels, captions, summaries before markup, since engines compare markup against what users see.
- Types: VideoObject (embedded video), ImageObject (stand-alone valuable images such as infographics, product image sets, original diagrams), FAQPage (visible Q&A), Article/BlogPosting (editorial), plus Product/Service/Organization as fitting. Example combo: tutorial with video and FAQs = Article + VideoObject + FAQPage.
- VideoObject basics: name, description, thumbnail, upload date, duration, canonical page location.
- For images, strong captions and surrounding copy often matter more than elaborate image markup.
- Title, heading, caption and markup should all convey the same meaning.
- Common errors: marking up content not visible; leaving outdated titles/descriptions in markup; FAQ schema on low-value or hidden content; piling on unneeded types.

## Public datasets
- A dataset is original data others can reference. Small and focused is fine: pricing benchmarks, customer surveys, usage trends, service timelines, local market comparisons, before/after results.
- Dataset page elements: clear title; short summary on top; date range; source or sample size; plain-English methodology; charts or tables; written explanation of findings (one or two sentences per chart stating the point).
- Reuse findings across blog posts, service pages, comparison pages, fact hubs, outreach pitches, webinar decks, FAQ sections; link those back to the dataset page as source of truth.

## FAQ bank
- Build a small set of approved, reusable answers on brand, products, services, niche (e.g., what it does, who it serves best, setup time, what makes it different, replaces or complements another tool).
- Place the same approved wording on product, service, pricing, comparison and support pages; pair answers with supporting media (chart, screenshot, clip, dataset).
- Answer formula: direct answer + qualifier + next step or context.
- Danger: five pages answering the same question five ways lets the weaker version get retrieved.
- Weak FAQs are generic, ramble, change wording across pages, and feel like an afterthought.

## Templates & prompts
- Caption: "This [asset] shows [observation], which [why it matters]."
- Alt text: "[Chart/screenshot type] showing [key content or trend]".
- Video page layout: player, 2-3 line summary, timestamped transcript, takeaway callout, related FAQ, VideoObject markup.
- Dataset page outline: Title / Summary / Date range / Source and sample / Method / Charts / Findings in plain English / Reuse links.
- FAQ entry: Q (customer wording) -> Direct answer + qualifier + next step -> optional media link -> owner and date.
- Pre-publish media check: Does each asset clarify, prove or simplify? Caption? Alt text? Transcript or summary? Reusable elsewhere?

## Audit checks
- [ ] Every meaningful image has descriptive, non-stuffed alt text.
- [ ] Decorative images use empty alt.
- [ ] Charts, screenshots and diagrams have captions that state the takeaway, placed directly beneath.
- [ ] Videos on ranking/educational/conversion pages have a transcript or at minimum a summary.
- [ ] Transcripts were human-checked for brand, product, names, numbers, terminology.
- [ ] Long videos have timestamps/section headers.
- [ ] VideoObject markup has name, description, thumbnail, upload date, duration, and points to the canonical page.
- [ ] Schema content is visible on the page and consistent with headings/captions.
- [ ] FAQPage markup only wraps visible, useful Q&A.
- [ ] No excessive or purposeless schema types.
- [ ] Original datasets (if any) show date range, source/sample size, methodology, and written findings.
- [ ] Dataset findings are reused and linked back from other pages.
- [ ] An approved FAQ bank exists and the same answer wording appears across pages.
- [ ] Charts are explained in text, not left bare.

## Actions
- Rewrite weak alt text and add captions to top 20 pages' key visuals. [Quick win]
- Review and correct auto-generated transcripts on key videos; publish with summary and timestamps. [Quick win]
- Add VideoObject (and FAQPage where visible Q&A exists) with accurate fields. [Foundation]
- Create the FAQ bank and roll approved answers into product, service, pricing, comparison, support pages. [Foundation]
- Publish a small original dataset page with method note and reuse it across the site. [Foundation]
- Repurpose each important video into a recap article, checklist and FAQs. [Ongoing]
- Re-run the media check before publishing significant pages. [Ongoing]

## Pitfalls
- Bare charts or screenshots with no explanation.
- Publishing unchecked auto-transcripts that misspell brand or numbers.
- Alt text with keyword lists or file-type labels.
- Schema describing hidden or outdated content.
- Inconsistent FAQ wording across pages.
- Datasets without method or sample, or never reused.

## Related
- ch04 (schema glossary), ch10 and ch11 (foundations), ch12 (FAQ and policies pages), ch13 (consistency, fact hubs), ch16 (signals), ch17 (cross-platform presence), ch20 (data for citations).
