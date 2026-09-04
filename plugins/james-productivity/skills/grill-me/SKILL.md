---
name: grill-me
kind: workflow
description: Interrogate the user through a branching interview until their own goal and requirement are sharp, then recap and confirm. Use to sharpen a plan before building; not to coach the person and not to research the answer.
---

# Grill Me

Keep asking until the requirement is sharp enough to build from.

## Scope

- Kind: workflow
- Owns: extracting and sharpening what the user actually wants — the goal, the requirement, and whatever is nagging at them — through a branching interview that ends in a confirmed decision map.
- Boundary: asks questions and records decisions. Finds every fact available from files and tools itself. Does not implement anything until the final confirmation is given.

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
4. Put a specific recommendation and its reason inside every question. A question without a recommendation transfers work to the user instead of removing it.
5. Use the host's structured input control whenever one exists, so answers are chosen rather than typed, with the recommendation placed first and a free-text field available for anything the options miss. When no such control exists, ask in plain chat with lettered options and wait for the reply. Never ask for numeric replies to questions that could have been clickable.
6. After each answer, update the tree, state any conflict with an earlier decision explicitly, and continue with whatever is newly unlocked. Preserve unanswered branches; never fill one from the recommendation.
7. Report progress each round as rounds taken, decisions settled, and branches remaining.

There is no fixed number of questions and no fixed number of rounds. Continue for as long as the user is still discovering what they want.

## Stop when

The user signals that it is now clear. Then recap the whole decision map — every decision, the answer chosen, the reason, the consequence, and any unresolved risk — and ask one final question: is this complete, correct, on target, and satisfying? If any part is not, keep asking. The interview ends only on that confirmation.

## Principles

**Socratic elicitation** — Draw the requirement out of the person through questions rather than proposing it, because a requirement they articulated is one they will recognise as wrong when it is. Source: Socratic method, as recorded by Plato
**Recognition over recall** — Offer choices to select from rather than asking the person to compose an answer from nothing; recognising is far cheaper than retrieving. Source: Jakob Nielsen, usability heuristics, 1994
**Value of information** — Ask next whatever answer would change the most downstream decisions, and skip anything whose answer changes nothing. Source: Ronald A. Howard, Information Value Theory, 1966
**Never fill a silence with an assumption** — An unanswered branch stays open and visible; quietly adopting the recommendation converts a question into a fabricated decision. Source: standing rule in this library

## Counter-case

- The user says they know exactly what they want but cannot start. The requirement is already sharp and the obstacle is personal, so `coach-me` owns it.
- The user asks to be challenged on whether a claimed best practice is real. That needs outside evidence rather than their own preferences, so `research-it` owns it.

## Hand back

The resolved decision map with every decision, chosen answer, reason, downstream consequence, and unresolved risk, plus the user's explicit confirmation that it is complete, correct, on target, and satisfying.

## Sources

Plato, Socratic dialogues. Nielsen 1994, Ten Usability Heuristics. Howard 1966, Information Value Theory.
