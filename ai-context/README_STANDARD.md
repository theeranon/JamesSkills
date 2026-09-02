# JamesSkills README Standard & Architecture

Last verified: 2026-09-03
Status: Enforced

## Purpose
`README.md` is the public front door and human onboarding surface of the repository. It is designed for human developers, business owners, and technical operators browsing GitHub. 

It is **not** the exhaustive technical reference manual (which is strictly governed by `docs/SKILLS.md` and individual `SKILL.md` files under `DEC-006`).

## Benchmarks & Principles
Benchmarked against top-tier open-source agent frameworks (Anthropic Skills, Fabric, vLLM, shadcn/ui):
1. **Scannable in 30 Seconds:** A developer or operator must grasp the core value proposition, scan all available capabilities, and find install commands without endless scrolling.
2. **Anti-Bloat Law:** Prohibit 40KB+ walls of repetitive HTML tables and auto-generated decorative images on the landing page.
3. **No AI Theater:** Strictly eliminate meta-copy, conversational residue, and juvenile tags (e.g. `❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)`). Maintain a sharp, direct operator tone (`make-it-james`).
4. **Iconic Showcase:** Use 3–4 high-impact Before/After showcases to provide immediate proof of agency, then direct full reference lookups to the Scannable Catalog Table and `docs/SKILLS.md`.

## Required Section Hierarchy
1. **Hero Header:** Title, one-sentence value proposition, and verification badges.
2. **Operating Philosophy ("Why This Exists"):** Sharp contrast between passive chat prompts and executable agentic skills.
3. **60-Second Quickstart:** One-line install command for terminal users + zero-terminal instructions.
4. **Iconic Showcase:** 3–4 representative Before/After comparisons demonstrating core breakthroughs (`/grill-me`, `/are-you-sure`, `/make-it-james-ux`, `/done-for-me`).
5. **Full Skill Directory (Scannable Matrix):** A single, compact table covering all canonical skills with commands, bilingual summaries, categories, and direct links to their handbook entries.
6. **Architecture & Boundaries:** Progressive disclosure model, category taxonomy, and local validation gates.
7. **Complete Handbook Pointer:** Direct link to `docs/SKILLS.md` for deep composition and lifecycle rules.
