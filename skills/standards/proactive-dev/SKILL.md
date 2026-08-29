---
name: proactive-dev
description: Strict engineering protocols for safe, evidence-based development. Prevents architectural hallucination, ensures execution boundaries are respected, and mandates blast-radius checks before mutating code or infrastructure.
---

# Proactive Dev (Engineering Standard)

When this skill is active, you must adhere to the following strict engineering and diagnostic protocols to guarantee system stability and prevent rogue AI actions.

## 1. The 3 Guarantees (Trust & Execution Protocols)
- **Evidence-Based Diagnosis:** NEVER hallucinate a bug's root cause. You MUST extract and verify the exact Source Code lines, schema constraints, or terminal Logs as concrete evidence BEFORE writing any fix.
- **Strict Architectural Boundaries:** ALWAYS respect the execution boundaries defined by the specific project (e.g., strict isolation for BaaS backends like Base44, flexible for local Supabase/Vercel). Never use rogue local hacks to bypass intended architecture.
- **Mandatory Blast Radius Check:** Before executing any fix or configuration change, you MUST internally evaluate the business and security impact (Blast Radius). Ensure the technical fix does not violate core project rules, open financial loopholes, or compromise security.

## 2. Knowledge Hygiene (Map Before Writing)
- NEVER blindly dump bug summaries, technical fixes, or localized logic into high-level foundational files (like `AGENTS.md` or `RULES.md`). 
- Before saving any project knowledge, you MUST proactively scan the repository structure (e.g., looking inside `.agents/skills/` or `docs/`) to find the most specific, appropriate location for it. 
- Respect Separation of Concerns: High-level files are for cross-cutting workflows; granular files are for domain-specific knowledge (e.g., specific troubleshooting guides).
