# JamesSkills README Standard & Architecture

Last verified: 2026-09-03
Status: Enforced

## Purpose
`README.md` is the public front door and human onboarding surface of the repository. It is designed for human developers, business owners, and technical operators browsing GitHub. 

It is **not** the exhaustive technical reference manual (which is strictly governed by `docs/SKILLS.md` and individual `SKILL.md` files under `DEC-006`).

## Benchmarks & Principles
Benchmarked against user requirements and preferences:
1. **Visual and Engaging:** The user explicitly prefers the README to be visual ("เบื้องหลังการทำงานมันเป็นประมาณไหน"), showing background processes and flow diagrams.
2. **Before/After Outcomes for ALL Skills:** Every skill must have a concrete, literal Before/After table in both English and Thai. Do not just describe concepts; show literal outcomes.
3. **No AI Theater:** Strictly eliminate meta-copy, conversational residue, and juvenile tags. Maintain a sharp, direct operator tone (`make-it-james`).
4. **Curated Illustrations:** Provide image illustrations (PNGs) for the most complex or impactful skills (e.g., `/done-for-me`, `/grill-me`, `/are-you-sure`, `/make-it-james-ux`, `/project-standard`, `/proactive-dev`, etc.) while keeping the rest as Before/After tables to balance visual flair and file size.

## Required Section Hierarchy
1. **Hero Header:** Title, one-sentence value proposition, and verification badges.
2. **Operating Philosophy ("Why This Exists"):** Sharp contrast between passive chat prompts and executable agentic skills.
3. **60-Second Quickstart:** One-line install command for terminal users + zero-terminal instructions.
4. **Full Skill Directory (Before vs After):** A complete section covering all canonical skills grouped by category. Each skill MUST include:
   - Command and brief description
   - A curated flow diagram or illustration (for selected complex skills)
   - A Before/After comparison table with concrete, literal examples in both English and Thai.
5. **Architecture & Boundaries:** Progressive disclosure model, category taxonomy, and local validation gates.
6. **Complete Handbook Pointer:** Direct link to `docs/SKILLS.md` for deep composition and lifecycle rules.
