---
id: ch06
title: Setting Up Your AI SEO Dashboard
part: Part 2: Measuring AI SEO
tags: [GA4, channel group, regex, Looker Studio, evidence library, change log, citation rate, AI referral traffic, Search Console, calculated field, sanity checks]
use_when: Building or auditing the reporting stack for AI SEO: GA4 AI channel, evidence sheet, Looker Studio dashboard, change log, data sanity checks.
---

# ch06 — Setting Up Your AI SEO Dashboard

## Core idea
- Four pieces: a GA4 custom "AI" channel group, a screenshot/evidence sheet, a Looker Studio report, and a change log plus sanity checks.
- GA4 gives an estimate, not a full count: only visits where the AI platform passes a referrer domain are captured.
- Goal is decision support with consistent tracking, not perfect attribution.

## GA4: create an AI channel group
- Prereqs: Google account with access to GA4 property, Search Console property, and Looker Studio (wrong account = empty report).
- Steps: Admin > Data display > Channel groups > Create new channel group; name it "AI"; add channel "AI Chatbots" using dimension Session source, match type "matches regex".
- Regex shape: optional `www.` prefix, then an alternation of referrer domains, anchored with start/end. Domains in the book's list: chatgpt.com, chat.openai.com, claude.ai, perplexity.ai, gemini.google.com, bard.google.com, copilot.microsoft.com, poe.com, you.com, character.ai, meta.ai, chat.mistral.ai, huggingface.co, chat.deepseek.com, grok.com, openrouter.ai, together.ai, cohere.com, groq.com, plus a few niche ones (janitor.ai, crushon.ai, spicychat.ai, talkie-ai.com, replika.ai, cursor.sh, codeium.com, ai.google.dev). Escape dots with backslashes.
- Save the channel, then drag the AI group above other rules so it evaluates first (GA4 uses first match), Apply, Save group.
- Checkpoint: Reports > Acquisition > User acquisition, dimension "Session default channel group"; "AI Chatbots" should appear once matching traffic arrives.
- Revisit the source list periodically; add new AI platform domains as they emerge.
- Limits: not retroactive (only new sessions after save); wait at least a week; review on 28-day or longer windows; compare against Organic Search and Direct.
- It shows: which pages get AI traffic, which platforms send it, how those visitors behave vs other channels.

## Evidence library
- Shared folder "AI SEO Evidence Library" in Drive plus Google Sheet "AI SEO Tracking Sheet".
- Columns: Date Captured, AI Platform, Prompt Used, Our Brand Present (Y/N), Our URL Cited (Y/N), Answer Position (list item 3, first citation, sidebar), Screenshot URL (Drive share link), Notes.
- Weekly capture of anchor prompts (priority prompts you most want tied to your brand): e.g., "best [category] tools", "[brand] review", "[core problem] for [ideal customer]".
- Weekly steps: screenshot whole answer with citations; upload to folder; paste link into sheet; log whether your site is linked.
- Log every meaningful ship (new fact hub page, schema update, earned citation) with date, description, URLs.

## Looker Studio build (4 pages)
- Open lookerstudio.google.com with the same Google account. Copy the provided AI SEO Tracking report template (More menu > Make a copy > Copy report). Note: template is separate from the tracking sheet; sheet stores evidence, template charts it.
- Page 1 (GA4 visibility): Add data > select GA4 property. Verify via Resource > Manage added data sources. Add a calculated field "AI Platform" to the GA4 source that maps referral source to a platform label (formula is on the book's companion site; write your own CASE on Session source such as chatgpt.com -> ChatGPT). Charts then break AI traffic down by platform.
- Page 2 (landing pages): auto-populates from GA4; shows top landing pages from AI Chatbots, pages gaining AI sessions, content that attracts AI referrals.
- Page 3 (Search Console prompt-like queries): add the Search Console source; create calculated field "AI Prompt Bucket" with CASE logic:
  - Commercial terms (buy, purchase, for sale, order, pricing, cost, deal) AND 10+ words -> "Extreme Long-Tail Commercial"
  - 10+ words AND starts with question/guide word (how, what, why, who, where, when, best way to, guide, steps to, tutorial, explain, examples) -> "Extreme Long-Tail Informational"
  - Starts with give me / show me / help me / explain / list / step by step -> "Instructional Prompt"
  - else "Other"
  - Tune word-count and keyword patterns to your niche.
- Page 4 (evidence): add Google Sheets source; point each scorecard to it; create "Citation Rate" = count of "YES" in Our URL cited / count of rows marked YES or NO (return 0 when denominator is 0). Match the exact column header name.
- Dashboard questions it should answer: which platforms send traffic, which pages receive it, which queries feel prompt-like, how often AI answers link to you.

## Weekly cadence (about 10 minutes)
- Monday: update sheet with new screenshots; refresh report; review AI Chatbots trend and top pages, AI Platform breakdown, Citation Rate and prompt-bucket shifts; write 1-2 notes in change log.

## Change log and sanity checks
- Change log columns: Date, Type of Change (content, schema, links, product, algorithm news), Short Description, URLs Affected, Person Responsible. Keep as a sheet tab or linked doc.
- Turns charts into a story ("citation rate rose the week the fact hub shipped"; "AI traffic dropped after nav change").
- Pre-report 5-minute checks: channel totals add up vs total users; date range matches narrative; odd one-day spikes (bots, internal testing, tracking bugs); freshness of GA4, GSC, Sheet data.
- Investigate anomalies before claiming a win or panicking.

## Templates & prompts
- Tracking sheet header: Date Captured | AI Platform | Prompt Used | Our Brand Present? | Our URL Cited? | Answer Position | Screenshot URL | Notes
- Change log header: Date | Type | Description | URLs | Owner
- Report map: P1 AI traffic by platform; P2 AI landing pages; P3 prompt buckets from GSC; P4 citation rate from sheet.

## Audit checks
- [ ] GA4 has a custom channel group containing an "AI Chatbots" channel.
- [ ] The AI channel regex covers at least chatgpt.com, perplexity.ai, claude.ai, gemini.google.com, copilot.microsoft.com, and escapes dots.
- [ ] The AI group sits above default rules in priority.
- [ ] AI channel appears in User acquisition report with data.
- [ ] Data window used for AI reporting is 28+ days.
- [ ] A shared evidence folder and tracking sheet exist with the listed columns.
- [ ] Anchor prompts are captured on a regular schedule with screenshots.
- [ ] Looker Studio report is connected to GA4, Search Console, and the sheet.
- [ ] "AI Platform" and "AI Prompt Bucket" calculated fields exist.
- [ ] Citation Rate formula returns a sensible value and ignores blank rows.
- [ ] A change log exists and has recent entries.
- [ ] A sanity-check routine runs before reports are shared.

## Actions
- Create the AI Chatbots channel group and move it to top priority. [Quick win]
- Review GA4 referral sources for AI domains missing from the regex and extend it. [Ongoing]
- Set up the evidence folder, sheet, and weekly capture routine. [Foundation]
- Build the four-page Looker Studio report and wire the calculated fields. [Foundation]
- Add a Change Log tab and require entries for every shipped change. [Foundation]
- Add a recurring Monday review slot. [Ongoing]

## Pitfalls
- Claiming GA4 AI channel equals total AI influence; many platforms and apps strip referrers.
- Expecting historical data to be reclassified.
- Putting the AI group below a rule that already claims the traffic.
- Wrong Google account, producing empty charts.
- Reporting from a 7-day or spike-affected window.
- Column header mismatch breaking the Citation Rate field.
- Skipping the change log, then not knowing why numbers moved.

## Related
- ch03 (evidence library intro), ch05 (what to measure, prompt buckets), ch07 (competitor tracking), ch08 (experiment change logs), ch16 (signals).
