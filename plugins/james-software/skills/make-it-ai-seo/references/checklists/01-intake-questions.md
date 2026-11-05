---
id: intake
title: Intake — goal, positioning, branding, keywords
tags: [intake, goals, positioning, branding, keywords, audience, competitors, questions, brief]
use_when: Start of every project, before auditing. Collect the user's goal in ONE batch.
---

# Intake — ถามเป้าหมายก่อนเสมอ (ครั้งเดียว ครบทุกข้อ)

## How to run the intake
- First infer what you can from the repo / live site (About page, homepage H1, title tags, existing schema, pricing, footer NAP, GA/GSC files). Pre-fill answers as a "draft brief".
- Then ask the user ONCE, in Thai, showing the pre-filled guesses as choices to confirm or correct. Never interview one question at a time.
- Questions the user skips → use the default in brackets and mark `assumed` in the brief.
- Save the answers to `seo-brief.md` in the project root (template below). Every later decision traces back to it.

## The questions (batch)
1. **ธุรกิจ/เว็บนี้ขายอะไร ให้ใคร** — product/service, ICP (who buys, B2B/B2C), geography & language(s). [from site]
2. **Positioning** — อยากให้ AI และ Google จำแบรนด์ว่าเป็น "ที่สุดของอะไร" ในประโยคเดียว: `<Brand> is the <category> for <audience> that <differentiator>`. Pick one primary category to own.
3. **Branding / tone** — บุคลิกแบรนด์ (expert, friendly, premium, budget), ชื่อแบรนด์ที่ถูกต้อง (spelling, ไทย/อังกฤษ), founder/expert ที่จะเป็นหน้าตา (E-E-A-T author).
4. **เป้าหมายธุรกิจ** — leads / sales / bookings / sign-ups / brand awareness? KPI หลัก 1 ตัว + ตัวเลขเป้า + กรอบเวลา. [leads, 90 days]
5. **คีย์เวิร์ด/คำถามที่อยากติด** — 5-20 seed keywords + คำถามที่ลูกค้าถาม AI จริง (prompts), แยก bottom-of-funnel ("best X for Y", "X vs Y", "X price", "X review") กับ informational.
6. **คู่แข่ง** — 3-5 คู่แข่งธุรกิจจริง + เว็บที่ติดอันดับ/ถูก AI อ้างถึงแทนเรา (ถ้ารู้).
7. **แพลตฟอร์มเป้าหมาย** — Google (SERP + AI Overviews/AI Mode), ChatGPT, Perplexity, Gemini, Claude, Copilot. [all, prioritize Google + ChatGPT]
8. **Asset ที่มีอยู่** — GBP/Google Maps, review platforms, social profiles, YouTube, data/case studies, press, partners.
9. **สิทธิ์และขอบเขต** — เข้าถึงโค้ด/CMS ได้ไหม (stack?), GA4/GSC access, อนุญาตให้แก้โค้ดและ commit/deploy เองแค่ไหน, งาน off-site (รีวิว, PR, outreach) ให้ร่างอย่างเดียวหรือส่งเองได้. [code edits OK; no publish/send/deploy without approval]
10. **ข้อจำกัด** — งบ, ทีม, กฎหมาย/อุตสาหกรรม YMYL (การเงิน สุขภาพ กฎหมาย), สิ่งที่ห้ามพูด.

## seo-brief.md template
```markdown
# SEO Brief — <brand> (<date>)
- Business / offer:
- ICP & market (geo, language):
- Positioning statement: <Brand> is the <category> for <audience> that <differentiator>
- Brand facts (canonical name, founder/experts, founding year, locations, contact):
- Tone:
- Primary KPI + target + deadline:
- Target platforms (priority order):
- Seed keywords / prompts (BOFU):
- Seed keywords / prompts (MOFU/TOFU):
- Competitors (business):
- Competitors (search/AI citations):
- Existing assets:
- Access & permissions (code, CMS, GA4, GSC, deploy, off-site):
- Constraints (budget, YMYL, legal):
- Assumed (not confirmed):
```

## Related
- ch01 (who AI SEO is for), ch03 (30-day plan), ch09 (topic plan), ch16-17 (brand/entity consistency)
