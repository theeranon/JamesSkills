---
id: action-plan
title: Audit report + action plan output format
tags: [report, action plan, roadmap, prioritization, quick wins, 90 day, impact effort, deliverable]
use_when: Writing the audit result and the prioritized action plan after the checklist is scored.
---

# Output format — Audit report + Action plan

## Scoring each checklist item
- Status: ✅ pass · ⚠️ partial · ❌ fail · ❓ cannot verify (say what access is needed).
- Evidence: URL / file:line / screenshot / prompt-test result. No evidence → ❓, never ✅.
- Impact (H/M/L) on the brief's primary KPI · Effort (S/M/L) · Owner (me-in-code / user / dev / content / PR).
- Priority = fix blockers first (crawl/index/render), then high-impact-low-effort, then foundations, then ongoing.

## Report skeleton (write to `seo-audit.md` in the project root)
```markdown
# AI SEO Audit — <brand> — <date>
## 1. Goal recap (from seo-brief.md)
## 2. Baseline snapshot
- Google: indexed pages, top queries, clicks (GSC) · AI: prompt-test coverage %, position, share of voice, citations
## 3. Scorecard by area
| Area | ✅ | ⚠️ | ❌ | ❓ |
## 4. Checklist results (bullets, grouped by area)
### A. Crawl & index
- ❌ <item> — evidence — impact H / effort S — fix: <one line>
...
## 5. Top 10 priorities (ranked)
## 6. Action plan
## 7. Measurement plan (prompts to track, dashboard, change log)
```

## Action plan skeleton
```markdown
### Now — Week 1-2 (Quick wins / blockers)
- [ ] <verb> <what> — where — owner — done when <observable check>
### Weeks 3-4 (Foundations)
### Days 31-90 (Authority & content)
### Ongoing (monthly)
- Re-run prompt protocol, update change log, refresh top pages, reviews, PR/mentions
```

## Execution rules
- Do every item owned by "me-in-code" now (HTML, meta, schema, robots/sitemap, internal links, page drafts, FAQ, fact hub), verify each, and log it in `seo-changelog.md` (date, change, URL, expected effect).
- Off-site items (reviews, PR pitches, profile updates, outreach emails) → produce ready-to-use drafts; sending, publishing, deploying or changing third-party accounts needs the user's explicit OK.
- Never invent facts, stats, reviews, testimonials, credentials or dates in content or schema. Unknown → placeholder `TODO(user): ...`.

## Related
- ch03 (90-day roadmap), ch05-06 (metrics, dashboard), ch08 (experiments), ch10 (fix-first logic)
