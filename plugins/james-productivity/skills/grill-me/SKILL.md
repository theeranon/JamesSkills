---
name: grill-me
kind: workflow
license: CC-BY-NC-4.0
description: Interrogate the user through a branching interview until their own goal and requirement are sharp, then proceed when the necessary decisions are clear. Use to sharpen a plan before building; not to coach the person and not to research the answer.
---

# Grill Me

Keep asking until the requirement is sharp enough to build from.

## Scope

- Kind: workflow
- Owns: extracting and sharpening what the user actually wants — the goal, the requirement, and whatever is nagging at them — through a focused interview that resolves the decisions needed to proceed.
- Boundary: asks questions and records decisions. Finds every fact available from files and tools itself. Uses existing implementation authorization; an instruction to start ends the interview when no material decision remains.

## Do not use this when

- The block is the person's own hesitation rather than an unclear requirement -> `coach-me`
- The requirement is clear and options must now be compared -> `give-me-solutions`
- The requirement is clear and the answer lies in outside evidence -> `research-it`
- The requirement is clear and the job is to build it -> `done-for-me`
- The problem is that the work is aimed at the wrong layer entirely -> `zoom-out`

## Procedure

1. Build a private decision tree. Some decisions unlock others; most do not matter yet.
2. Find every fact yourself first. Never ask for something a file, a repository, or a tool already answers.
3. Ask only the current frontier: unresolved decisions whose prerequisites are already settled. Ask one at a time when the answer changes the next question; ask up to three together only when they are genuinely independent.
4. Offer a specific recommendation and reason when evidence supports one. For goals or preferences only the user can choose, ask neutrally. Do not infer implementation complexity, cost or expected impact solely from frequency or urgency. When the evidence supports only a provisional preference, name the material uncertainty rather than inventing a stronger rationale. Never invent a recommendation to satisfy the question format.
5. Use the host's structured input control whenever one exists, so answers are chosen rather than typed, with the recommendation placed first and a free-text field available for anything the options miss. When no such control exists, ask in plain chat with lettered options and wait for the reply. Never ask for numeric replies to questions that could have been clickable.
6. After each answer, update the tree, state any conflict with an earlier decision explicitly, and continue with whatever is newly unlocked. Preserve unanswered branches; never fill one from the recommendation.
7. Report progress when it helps the ongoing interview, using only decisions and rounds actually established. If the user asks for the next question only, return only that question, with a recommendation if supported; keep the dependency tree private.

There is no fixed number of questions and no fixed number of rounds. Continue for as long as the user is still discovering what they want.

## Stop when

The decisions needed for the requested work are clear, or the user tells you to stop or start. A request to start is authorization already given, not a reason to ask for a confirmation word. Summarize material decisions only when useful; proceed with authorized work. Ask further only for an unresolved decision that materially changes the outcome, authority or commitment.

## Principles

**Socratic elicitation** — Draw the requirement out of the person through questions rather than proposing it, because a requirement they articulated is one they will recognise as wrong when it is. Source: Socratic method, as recorded by Plato
**Recognition over recall** — Offer choices to select from rather than asking the person to compose an answer from nothing; recognising is far cheaper than retrieving. Source: Jakob Nielsen, usability heuristics, 1994
**Value of information** — Ask next whatever answer would change the most downstream decisions, and skip anything whose answer changes nothing. Source: Ronald A. Howard, Information Value Theory, 1966
**Never fill a silence with an assumption** — An unanswered branch stays open and visible; quietly adopting the recommendation converts a question into a fabricated decision. Source: standing rule in this library

## Counter-case

- The user says they know exactly what they want but cannot start. The requirement is already sharp and the obstacle is personal, so `coach-me` owns it.
- The user asks to be challenged on whether a claimed best practice is real. That needs outside evidence rather than their own preferences, so `research-it` owns it.

## Hand back

The useful decisions and remaining material questions, or the requested work when the user has instructed you to proceed. Keep routine interview bookkeeping internal.

## Sources

Plato, Socratic dialogues. Nielsen 1994, Ten Usability Heuristics. Howard 1966, Information Value Theory.
