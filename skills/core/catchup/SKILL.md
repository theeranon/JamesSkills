---
name: catchup
description: Reconstruct the verified current state of one existing project or workstream after a continuity gap, agent handoff, or suspected stale status. Use for catch-me-up or where-are-we-now requests; do not activate for ordinary progress inside an active task or for verifying one isolated completion claim.
---

# Catchup

Return a decision-ready current state, not a history dump and not a confident summary of stale documents.

## Boundary

- Own one bounded project or workstream. Separate multiple targets instead of blending their state.
- Read only by default. Do not repair files, change state, continue implementation, send messages, or update external systems unless that work is separately authorized.
- Do not create a missing project contract, run a full system audit, or inspect unrelated personal history.
- During an active implementation turn, let the primary workflow report its own progress. Route one isolated completion claim to `prove-it` instead of reconstructing the whole project.
- Use JamesOS or another live-context adapter only when the requested state genuinely depends on current cross-channel commitments, people, queues, or an explicit request for that system.

## Workflow

1. Identify the target and comparison point: project root or workstream, branch or environment when relevant, and the last known checkpoint if one exists. Never invent a baseline; label `comparison point not established` when it cannot be recovered cheaply.
2. Take the fast path first. If the current request and accepted project sources already contain fresh, sufficient state, answer from them without excavating chat or history.
3. Gather the smallest current evidence set:
   - for a local project, run `python3 scripts/project_snapshot.py <project-root> --checkpoint <known-checkpoint>` from this skill directory when the comparison point is known; omit `--checkpoint` rather than inventing one;
   - read the current project contract and status owners that actually exist;
   - inspect only the runtime, provider receipt, task system, or recent history needed to resolve a material state claim.
4. Reconcile four truth classes instead of merging them:
   - **Intended:** accepted requirements and decisions say what should exist.
   - **Actual:** source, Git, tests, runtime, and provider evidence say what currently exists.
   - **Active:** dirty work, in-progress tasks, blockers, and current owner state say what is moving now.
   - **Historical:** prior chat and old reports explain a delta only when current sources cannot.
5. Stop when the user can safely continue: current truth, meaningful delta, open work, material conflict or unknown, evidence freshness, and the next action or explicit no-action verdict are all clear.

## Output contract

Keep the first view compact:

1. **ตอนนี้:** verified current state and target identity.
2. **เปลี่ยนจากจุดไหน:** material delta from a named checkpoint, or state that no comparison point is established.
3. **ยังค้าง:** open work, blocker, owner, and proof gap.
4. **ขัดกันหรือยังไม่รู้:** only material conflicts and unknowns.
5. **ทำต่อ:** one concrete next action, or `ไม่มี action เพิ่มใน scope นี้` when the bounded work is genuinely closed. Never invent follow-up work to fill the section.

Use only the sections that materially help a narrow direct question; do not manufacture empty sections merely to satisfy the template.

Attach a short evidence locator and freshness signal to every material claim. A file modification time, status label, agent summary, generated artifact, or green local test is routing evidence, not universal proof.

## Failure guards

- Preserve dirty and untracked user work. Never clean, stash, reset, or rewrite it during catchup.
- Do not treat the current branch, upstream, environment, account, or deployed version as obvious; identify the target that the evidence covers.
- Do not upgrade intended architecture into implemented reality or let newer current evidence erase accepted requirements.
- Do not widen a bounded status question into an audit of the whole portfolio.
- If durable project truth is missing or contradictory, finish the best evidence-backed catchup first, then recommend `project-standard` as a separate repair workflow.
- Use `prove-it` only when a disputed completion claim needs deeper verification; do not load it for every ordinary state summary.

Completion means a fresh agent can continue the bounded work without relying on hidden chat history and without mistaking unknown, stale, intended, or unverified state for current fact.
