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

1. Start the interview in this reply. Use the existing conversation to identify the first unresolved goal or decision, then call the available in-app question tool with one self-contained question and selectable choices. A plain-text question is not a substitute for a working native question tool. An invocation such as "Grill Me กัน" is a request to begin, not an answer to earlier questions. Never respond only with acknowledgement, instructions to answer above, or a promise to ask later. If a previous question was broad or compound, narrow it instead of repeating the burden.
2. Separate the desired outcome from the proposed solution. When the goal is unclear, ask what needs to change, why it matters now, or for a concrete recent incident. Do not require a polished vision, complete requirements, or a list of pain points to begin. If the user has already established the goal, start at the unresolved decision rather than reopening it. A named solution is not proof that its underlying goal is clear; an explicitly settled choice is not an invitation to relitigate it.
3. Keep a private decision tree of goals, evidence, user decisions and unresolved assumptions. Read relevant available files and tools for factual answers; do not make the user repeat them or perform an exhaustive audit before the first useful question. A fact about the current system does not establish what the user wants next.
4. Present exactly one focused question per in-app popup, chosen for how much its answer changes what comes next. Wait for the user's answer before opening the next popup; do not queue a second question or treat a preselected choice or elapsed time as a submitted answer. Batch only if the user explicitly requests it. Do not hide several dependent questions inside one sentence. Keep routine rounds, branch counts and method explanations internal unless requested.
5. Use the host's available, permitted native question control for every interview question, including the opening goal question. Inspect tool availability rather than guessing from the host name. For example, use `request_user_input_async` when available in the current mode, `request_user_input` when that tool is permitted in the current mode, or `AskUserQuestion` when exposed by the host. These are capability examples, not assumed universal APIs. Supply one question with 2-3 short, distinct choices plus the host's free-text escape. Choices for an unclear goal are plausible directions to react to, not invented facts or a diagnosis; let the user qualify them or say they do not fit. Narrow an abstract question into a concrete choice instead of dropping the choices. Do not output a chat question, HTML page, or promised popup when the native tool is callable. If one native tool call fails, report that exact error and check the remaining permitted question tools before falling back; one failed call is not proof that the host lacks popups. In Default mode, use an available asynchronous question tool rather than a Plan-only tool. Do not ask the user to switch modes just to obtain a popup when a permitted route already exists. Only when no permitted native route remains, state the specific limitation once and use one chat question with lettered choices and room for free text; do not claim a popup appeared. An explicit user request for text-only questions overrides the popup default.
6. Offer a specific recommendation and reason only when evidence supports one, labelled `(แนะนำ)` in a structured control. Ask neutrally about goals or preferences only the user can choose. Do not infer complexity, cost or impact solely from frequency or urgency. Name material uncertainty in a provisional recommendation. A free-text detail qualifies or overrides a selected option; intentional multi-selection is different from no selection. Never treat a default, silence or agreement with your wording as a decision the user has not made.
7. Follow the answer, not a questionnaire. Briefly reflect the part that changes your understanding, then probe its consequence, a concrete example, a trade-off, a success criterion or an apparent contradiction, whichever unlocks the next decision. Use the user's words and make a possible insight a hypothesis they can correct. Challenge unsupported assumptions with a reason; do not manufacture disagreement, psychological labels or adversarial pressure. State conflicts with earlier decisions explicitly and preserve unresolved branches.
8. When the user says "I don't know", reduce the abstraction: ask about one recent event or offer a small contrast grounded in what they said. If talking cannot establish the answer, identify the missing evidence or smallest useful trial instead of repeatedly rephrasing. Preserve that uncertainty; carry out a trial only within existing authorization. Do not turn an interview into an unsolicited research project or prototype build.

For an explicitly requested HTML questionnaire only, read [the optional rendering contract](references/interactive-html.md).

There is no question quota or fixed sequence of topics. Depth comes from what each answer reveals, not from exhausting every imaginable branch. Keep going while a material uncertainty can usefully be resolved through conversation.

## Stop when

The goal, meaningful success criteria and decisions needed for the next authorized step are clear, or the user tells you to stop or start. Do not demand implementation details that do not affect that step. A request to start is authorization already given, not a reason to ask for a confirmation word. Summarize material decisions only when useful; proceed with authorized work. Ask further only for an unresolved decision that materially changes the outcome, authority or commitment.

## Principles

**Socratic elicitation** — Draw the requirement out of the person through questions rather than proposing it, because a requirement they articulated is one they will recognise as wrong when it is. Source: Socratic method, as recorded by Plato
**Recognition over recall** — Offer choices to select from rather than asking the person to compose an answer from nothing; recognising is far cheaper than retrieving. Source: Jakob Nielsen, usability heuristics, 1994
**Value of information** — Ask next whatever answer would change the most downstream decisions, and skip anything whose answer changes nothing. Source: Ronald A. Howard, Information Value Theory, 1966
**Never fill a silence with an assumption** — An unanswered branch stays open and visible; quietly adopting the recommendation converts a question into a fabricated decision. Source: standing rule in this library

## Counter-case

- The user says they know exactly what they want but cannot start. The requirement is already sharp and the obstacle is personal, so `coach-me` owns it.
- The user has already settled the goal and says "start building the agreed draft". Proceed within that scope; do not restart discovery or demand another confirmation.
- The user asks to be challenged on whether a claimed best practice is real. That needs outside evidence rather than their own preferences, so `research-it` owns it.

## Hand back

During the interview, deliver the next question through the native question tool with choices, then wait. Put the necessary context inside the question so the user need not reread chat. A text-only answer is a failed interview turn when a permitted native control exists, except when the user explicitly requested text-only. At a useful stopping point, briefly capture the goal, settled choices and reasons, and material unknowns or risks; allow correction without requiring a ritual approval round. When instructed to proceed, deliver the authorized work. Keep routine interview bookkeeping internal.

## Sources

Plato, Socratic dialogues. Nielsen 1994, Ten Usability Heuristics. Howard 1966, Information Value Theory.

Design reference: Matt Pocock, [The /grill-me Skill](https://www.aihero.dev/skills-grill-me), updated 2026-08-24, reviewed 2026-09-10. Used for dependency-aware inquiry and recognizing questions that need a trial. This James adaptation uses original wording: immediate conversational entry, one-question default, native choice-based discovery, and existing execution authority. The article is a design source, not an instruction to install its package or adopt its full workflow.

Implementation source checked 2026-09-10: [grill-me entrypoint](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) delegates to [grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md), which specifies text rounds with recommendations. The native popup with one question and choices is the owner-required James interaction, not a claim about upstream behavior.
