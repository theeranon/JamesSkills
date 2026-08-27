---
name: james-project-control
description: Establish and maintain a project source of truth for requirements, architecture, decisions, status, and agent handoffs. Use when starting, restructuring, rescuing, or transferring a multi-step project.
---

# James Project Control

Keep one canonical source for each kind of truth. Do not create competing plans because another agent or vendor joins.

1. Locate existing requirement, architecture, decision, goal, status, and evidence files before creating anything.
2. Name the authority and distinguish accepted decisions from proposals.
3. Separate durable requirements, current status, append-only decisions, and execution evidence.
4. Give all agents pointers to the same canonical files through thin platform adapters such as `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`.
5. Update status only from verified work. Preserve unresolved gates visibly.

Never call work blocked merely because it is hard or incomplete. Block only on a genuine missing authority, credential, external dependency, or irreconcilable requirement.
