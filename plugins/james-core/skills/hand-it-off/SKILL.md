---
name: hand-it-off
license: CC-BY-NC-4.0
metadata:
  kind: workflow
description: Hand this conversation's work to another agent, vendor, account or machine: record every decision, skill and ai-context change in the repository, push it, and write instructions that let the next agent continue pending and planned work without this chat. Use for hand it off, ส่งต่องาน, ให้ AI ตัวอื่นทำต่อ, ย้ายเครื่อง.
---

# Hand It Off

Write down everything the next agent needs, push it, and give them the order to continue.

## Scope

- Kind: workflow
- Owns: the handoff of this conversation's work: the recorded state in the repository and one instruction document a different agent can act on without reading this chat.
- Boundary: writes to the project's `ai-context/` owner documents and a dated handoff file, commits and pushes under the project's standing rule. Never claims work is done that was not verified, never includes credentials, chat exports or client data, and never changes the work itself.

## Do not use this when

- The user wants to be reminded what has been done, with no transfer -> `catchup`
- Recording lapsed and a lesson must be written, but the same agent continues -> `never-again`
- The project has no contract and nothing durable has ever been written -> `project-standard`, then return here

## Procedure

1. Re-read the whole conversation and the project's `ai-context/`. Separate what is verified from what was only discussed.
2. Record first, in the owner documents the project uses: decisions into `ai-context/DECISIONS.md`, current verified state and the next move into `ai-context/STATUS.md`, lessons into `ai-context/LESSONS.md`, changed skills into their `SKILL.md`. Nothing goes into the handoff file that is not also in its owner document.
3. Write the handoff as `docs/handoffs/<date>-<topic>.md`, or the project's equivalent, with these parts in this order: what the goal is and for whom; what happened and what was verified, with commit references; pending work in execution order, each item with its acceptance; planned work the owner agreed but has not started; decisions the next agent must not reopen, in the owner's own words; blockers and the exact input each needs; the owner's working preferences that shape every step; which files to read first.
4. Write every instruction so an agent from any vendor can run it: no tool names that exist only here, no paths outside the repository, no assumption that this chat is visible.
5. Validate with the project's checks, commit, and push. State the commit and the remote branch in the handoff.
6. Return a short paste-ready block the owner can give the next agent: the repository, the handoff file path, and the first command to run.

## Stop when

The owner documents and the handoff file are pushed, the handoff names every pending and planned item with its acceptance, and the paste-ready block exists. Unverified items are marked unverified, never dropped.

## Principles

**Write for the stranger** — A record that needs this conversation to be understood is not a record. Source: standing rule in this library
**One fact, one owner** — The handoff points at the owner document; it never becomes a second copy that drifts. Source: standing rule in this library
**Verified, unverified, planned** — Keep the three apart; a plan written as a result is the most expensive lie a handoff can tell. Source: standing rule in this library

## Counter-case

- The owner asks where the project stands and intends to continue in this chat. That is a status read, so `catchup` owns it and nothing is pushed.
- Everything is already recorded and pushed and only the paste-ready block is missing. Write the block; do not rewrite the records to show effort.

## Hand back

The paste-ready block, the handoff file path, and the commit that carries the records. No summary of the chat beyond that.

## Sources

Standing rules of this library, recorded in `ai-context/DECISIONS.md` DEC-051 and `ai-context/LESSONS.md` LESSON-017.
