---
name: catchup
kind: workflow
description: Reconstruct one project's verified current state after a gap and deliver it as the standard catchup page. Use for where-are-we-now after a handoff or stale status; not for progress inside active work and not for repairing anything.
---

# Catchup

Work out what is actually true right now, and hand back one page that says so.

## Scope

- Kind: workflow
- Owns: the verified current state of one project or workstream after a continuity gap, rendered into the standard catchup page.
- Boundary: read-only on the project, and never activated for ordinary progress inside an active task. Never repairs files, cleans, stashes, resets, continues implementation, updates external systems, or rewrites a stale status document. It writes only its own report.

## Do not use this when

- Ordinary progress inside an active task is being reported; let the primary workflow report it -> `done-for-me`
- The dispute is one isolated completion claim needing verification at its boundary -> `dev-are-you-sure`
- The project has no contract and truth was never written down -> `project-standard`
- The direction rather than the state is what is unclear -> `zoom-out`
- The source is a meeting rather than a repository -> `sum-meet`

## Procedure

1. Identify the target and the comparison point: project root or workstream, branch and environment where relevant, and the last known checkpoint. Never invent a baseline; record `comparison point not established` when one cannot be recovered cheaply.
2. Take the fast path first. When the request and the accepted project sources already carry fresh, sufficient state, answer from them without excavating history.
3. Gather the smallest sufficient evidence. For a local project run `python3 scripts/project_snapshot.py <project-root> --checkpoint <known-checkpoint>` from this skill directory, omitting the checkpoint rather than inventing one. Read the contract and status owners that actually exist. Inspect runtime, provider receipts, or recent history only where a material state claim depends on it.
4. Reconcile four truth classes without merging them.
   - **Intended:** accepted requirements and decisions say what should exist.
   - **Actual:** source, git, tests, runtime, and provider evidence say what currently exists.
   - **Active:** dirty work, running tasks, blockers, and current owner state say what is moving now.
   - **Historical:** prior chat and old reports explain a delta only when current sources cannot.
5. Preserve dirty and untracked user work exactly as found. When a status document is stale, report it as stale rather than correcting it; correcting it is a separate authorised job. Do not widen a bounded status question into a full audit when the supplied evidence already answers it.
6. Render the report by duplicating [assets/catchup-report.html](assets/catchup-report.html) and replacing every token. The template is fixed so that every project's catchup page looks identical and can be read at a glance; adapt content, never the shape.
7. Inspect the rendered page in print emulation before delivering. Deliver HTML; produce a PDF only when it is explicitly requested.

## Stop when

The report names the exact target, states current truth against a named comparison point or says none is established, lists what is open with its blocker and owner, keeps conflicts and unknowns visible, and ends in one safe next action or an explicit verdict that nothing remains in scope. Return `ไม่มี action เพิ่มใน scope นี้` when the bounded work is genuinely closed, rather than inventing a follow-up.

On Windows invoke the same helper with `python` when `python3` is not on PATH.

## Principles

**Evidence outranks the status document** — Trust git, runtime, and provider receipts over any file claiming readiness, because a stale label is the failure mode this skill exists to catch. Source: standing rule in this library
**Separate intended from actual** — Report the gap between what should exist and what does, rather than resolving it in either direction. Source: standing rule in this library
**Read-only until authorised** — Reconstruction never repairs; touching the workspace destroys the evidence the next decision depends on. Source: forensic soundness principle, ACPO digital evidence guidelines, 1999
**One target at a time** — Reconstruct a single project per report, because blending two workstreams produces a state that describes neither. Source: standing rule in this library

## Counter-case

- The user asks how the current build is going while the agent is mid-task. The active workflow reports its own progress; `done-for-me` owns it and reconstruction would be noise.
- The user asks whether yesterday's deployment actually went live. That is one claim at one boundary, so `dev-are-you-sure` owns it rather than a whole-project reconstruction.

## Hand back

One rendered catchup page naming the target, the current situation, what was recently done, the live checklist, what is open with owners, visible conflicts and unknowns, the state of the last task, and the single next action.

## Sources

ACPO 1999, Good Practice Guide for Digital Evidence, on preserving evidence before analysis.
