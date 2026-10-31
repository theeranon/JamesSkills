# JamesSkills Handbook

Choose a skill by the moment you need it. Type the slash command when you want to force a specific workflow. An agent may select the smallest matching workflow automatically when its platform loads the installed skill and supports that routing; this is not verified on every platform.

This handbook is the human navigation layer. `catalog.json` owns category, kind, lifecycle, and aliases. Each linked `SKILL.md` owns the actual behavior, and `docs/SKILL-SCHEMA.md` owns the shape every one of them must satisfy. If a summary here ever conflicts with a canonical skill, the canonical skill wins and this handbook must be repaired.

## Start in 60 seconds

1. Start or repair a project contract with `/project-standard`; return after a gap with `/catchup`.
2. Sharpen a half-formed idea with `/grill-me`; climb to strategy with `/zoom-out`.
3. Settle one doubt with `/research-it`; choose between candidates with `/give-me-solutions`.
4. Keep `/proactive-habits` on throughout; `/done-for-me` is the wake-up call that finishes the task when questions pile up.
5. Check business work with `/are-you-sure` and software with `/dev-are-you-sure`; raise a mediocre result with `/is-that-the-best-you-can-do`.

Mode and standard behavior differs from a normal workflow:

- `/i-have-adhd`, `/proactive-habits`, `/insight-driven-mode` and `/coach-me` stay active for the current conversation until explicitly disabled.
- `make-it-james` and `make-it-james-ux` apply automatically to recipient-facing outcomes; invoking one directly is useful for a wording or visual audit.
- `/hand-it-off` writes the handoff another agent, account or machine needs and pushes the records first; `/never-again` is the wake-up call when recording lapsed.


## Start or return to work

### `/project-standard`

- Canonical package: `project-standard`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Create or repair one vendor-neutral project contract so any agent or person can work without prior chat, stamped with its standard version. Use for set up project docs, AGENTS.md, context files, วางมาตรฐานโปรเจกต์, เอกสารโปรเจกต์มั่ว. Not for routine edits that change nothing durable.
- Result: The owner-document changes, requirement identifiers with acceptance/proof, visible intended-versus-actual drift, and checks actually performed. Include regenerated SRS/version only when applicable; for a requested draft, clearly identify proposed text and unverified facts instead of reporting edits or readiness.
- Do not use when: The contract exists and current state after a gap is what is unknown -> `catchup`
  - The contract exists and the work is to build against it -> `done-for-me`
  - The contract exists and engineering work must be planned and built against it -> `done-for-me`
- Aliases: `project-docs-standard` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-software/skills/project-standard/SKILL.md`](../plugins/james-software/skills/project-standard/SKILL.md)

### `/catchup`

- Canonical package: `catchup`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Remind the owner what has been done: reconstruct the verified state of one project after a gap and return it as one HTML page with no metacopy, the way an executive is briefed, so they can decide, instruct, continue, measure or inspect. Writes nothing else. Use for where are we, ถึงไหนแล้ว, ทวนให้หน่อยว่าทำอะไรไปแล้ว.
- Result: One HTML page briefed as to an executive: what was done, what is true now, what is open, what needs a decision, the next action; nothing else written.
- Do not use when: Ordinary progress inside an active task is being reported; let the primary workflow report it -> `done-for-me`
  - The dispute is one isolated completion claim needing verification at its boundary -> `dev-are-you-sure`
  - The project has no contract and truth was never written down -> `project-standard`
- Canonical instructions: [`plugins/james-software/skills/catchup/SKILL.md`](../plugins/james-software/skills/catchup/SKILL.md)

### `/zoom-out`

- Canonical package: `zoom-out`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Step back from implementation detail through the project goal to the strategy that should achieve it. Use for zoom out, are we solving the right problem, big picture, ถอยมามองภาพรวม, หลงทางแล้ว, ทำไปเพื่ออะไร. Not for an isolated implementation or visual fix.
- Result: The strategic reframe: project outcome, approach, how the current work contributes or distracts, and the next aligned move. Name only a genuinely new decision requiring the user. When execution was requested and authorized, carry that work forward rather than stopping at the reframe.
- Do not use when: Only layout, interaction, or visual design needs repair and the project strategy is not in question -> `make-it-james-ux`
  - The direction is settled and options must now be compared -> `give-me-solutions`
  - The direction is settled and the job is to build it -> `done-for-me`
- Canonical instructions: [`plugins/james-productivity/skills/zoom-out/SKILL.md`](../plugins/james-productivity/skills/zoom-out/SKILL.md)

### `/grill-me`

- Canonical package: `grill-me`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Interview the user one question at a time until their own goal and requirement are sharp, then proceed. Use before building, as in grill me, ask me questions first, ถามให้เคลียร์ก่อน, ซักมาเลย, ยังคิดไม่ตก. Not to coach the person and not to research the answer.
- Result: The useful decisions and remaining material questions, or the requested work when the user has instructed you to proceed. Keep routine interview bookkeeping internal.
- Do not use when: The block is the person's own hesitation rather than an unclear requirement -> `coach-me`
  - The requirement is clear and options must now be compared -> `give-me-solutions`
  - The requirement is clear and the answer lies in outside evidence -> `research-it`
- Canonical instructions: [`plugins/james-productivity/skills/grill-me/SKILL.md`](../plugins/james-productivity/skills/grill-me/SKILL.md)


## Decide

### `/research-it`

- Canonical package: `research-it`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Stop guessing and go get the information first: settle one claim with evidence that goes beyond the official spec, which overclaims, to real users, real reviews, videos, communities or the thing itself, compared and summarized. Use for is that true, prove it, จริงเหรอ, อย่าตอแหล ไปหาข้อมูลมาก่อน, เช็คข้อมูลก่อน.
- Result: The claim and verdict with official and independent evidence compared side by side, locators where available, and the material limits.
- Do not use when: Several candidates must be compared and one recommended -> `give-me-solutions`
  - The doubt is about work produced in this conversation rather than an outside claim -> `are-you-sure`
  - The doubt is about whether shipped code, data, or a deployment behaves correctly -> `dev-are-you-sure`
  - The job is a written customer insight per target group and the copy that traces to it -> `insight-driven-mode`
- Aliases: `prove-it` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-core/skills/research-it/SKILL.md`](../plugins/james-core/skills/research-it/SKILL.md)

### `/give-me-solutions`

- Canonical package: `give-me-solutions`
- Category: `james-productivity`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: When the user is out of ideas, do the homework: understand the real problem and goal, then show the ways forward in one table on one axis with one vocabulary, enum-like values, and risk, time, cost and quality now and long term, so deciding is easy but stays theirs. Use for มีทางเลือกอะไรบ้าง, ตัวไหนดีสุด, เทียบให้ที.
- Result: One comparison table on identical criteria with one vocabulary and enum-like values, the risks, time, cost and quality now and long term, and the evidence-favoured option as a recommendation the user can overrule.
- Do not use when: One claim or approach needs to be settled rather than several compared -> `research-it`
  - Which responsibility is actually failing is still unclear -> `zoom-out`
  - The choice is already made and the job is to build it -> `done-for-me`
  - Marketing, brand or copy must trace to a written insight for each target group -> `insight-driven-mode`
- Canonical instructions: [`plugins/james-productivity/skills/give-me-solutions/SKILL.md`](../plugins/james-productivity/skills/give-me-solutions/SKILL.md)

### `/baseon`

- Canonical package: `baseon`
- Category: `james-productivity`
- Kind: `knowledge-lens`
- Lifecycle: `promoted`
- Use when: Study a subject the user already has a keyword, hypothesis or insight for, wherever it lives (this chat, project, machine, connector, outside), and apply registered frameworks and books to the real case with source claims kept apart from evidence and inference. Use for อิงจากหนังสือเล่มนี้, ไปศึกษาเรื่องนี้มา.
- Result: The named subject studied where it lives and the case interpretation with source claims, facts and inference distinguishable.
- Do not use when: The source is not registered yet and the need is outside evidence about a claim -> `research-it`
  - Options must be compared and one recommended -> `give-me-solutions`
  - The problem layer itself is unclear -> `zoom-out`
- Aliases: `think-with-this`, `wealth-dynamics`, `talent-dynamics`, `wealth-spectrum` (legacy compatibility calls).
- Canonical instructions: [`plugins/james-productivity/skills/baseon/SKILL.md`](../plugins/james-productivity/skills/baseon/SKILL.md)


## Build and finish

### `/done-for-me`

- Canonical package: `done-for-me`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Wake-up call when the agent keeps asking after enough insight and decisions were given. Re-read the whole conversation and every settled decision, then act at once; build what is still ambiguous as a changeable setting or as three to five variants. Use for just do it, stop asking, ทำให้จบ, ทำสักที, พอแล้วถามอยู่นั่น.
- Result: The finished, exercised outcome; every formerly open point turned into a changeable setting or three to five variants; only gates the user genuinely holds.
- Do not use when: The work is finished and its diligence is what is in doubt -> `are-you-sure`
  - The work is finished and its diligence is what is in doubt -> `are-you-sure`
  - Delivered code needs a layered sweep and boundary check -> `dev-are-you-sure`
- Canonical instructions: [`plugins/james-core/skills/done-for-me/SKILL.md`](../plugins/james-core/skills/done-for-me/SKILL.md)

## Check the work

### `/are-you-sure`

- Canonical package: `are-you-sure`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Re-check a finished plan, document, deck, budget or analysis and repair the real defects found. Use when delivered work is in doubt, as in are you sure, double-check this, ตรวจอีกรอบ, แน่ใจนะ, เช็คให้ชัวร์. Not for code, and not for making good work better.
- Result: The repaired artifact, or the requested clean-result confirmation. A request to return the corrected artifact gets that artifact alone; keep surface, layer labels and repair bookkeeping internal unless the user asks for the inspection report. When an inspection report is requested, include the surface and actual findings, with clean, repaired, escalated, not-applicable or unverified status as warranted. Name only the decisions genuinely needed to finish.
- Do not use when: The artifact is code, schema, data, or a deployment -> `dev-are-you-sure`
  - The doubt is about an outside claim rather than work produced here -> `research-it`
  - The work is correct and clean but unambitious, and needs a higher ceiling -> `is-that-the-best-you-can-do`
- Canonical instructions: [`plugins/james-core/skills/are-you-sure/SKILL.md`](../plugins/james-core/skills/are-you-sure/SKILL.md)

### `/dev-are-you-sure`

- Canonical package: `dev-are-you-sure`
- Category: `james-software`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Re-inspect delivered software with checks matched to its risks and repair findings inside a declared surface. Use when code looks done but may not be, as in are you sure it works, did you test it, โค้ดชัวร์ไหม, เทสแล้วเหรอ, เช็คโค้ดอีกรอบ. Not for business artifacts or outside claims.
- Result: The repaired outcome, checks actually performed, and material unresolved findings with the evidence still needed. Include the complete layer/boundary inventory when a full audit was requested; keep inspection notes internal for a code-only response.
- Do not use when: The artifact is a plan, document, model, or business decision -> `are-you-sure`
  - The doubt is whether an outside approach or library claim is sound -> `research-it`
  - The code is correct and clean but the solution is mediocre -> `is-that-the-best-you-can-do`
- Canonical instructions: [`plugins/james-software/skills/dev-are-you-sure/SKILL.md`](../plugins/james-software/skills/dev-are-you-sure/SKILL.md)

### `/is-that-the-best-you-can-do`

- Canonical package: `is-that-the-best-you-can-do`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Push a correct result beyond expectation: find what can still be polished in efficiency, evidence, depth, usefulness and dimensions the brief never named, and deliver that. Use for is that the best you can do, make it better, level this up, ดีกว่านี้ได้ไหม, ยังไม่ว้าว, เอาให้สุด, มีปัญญาแค่นี้เหรอ. Not for defects.
- Result: The result raised beyond the brief across depth, evidence, efficiency, usefulness and unnamed dimensions, with a short account of what was raised and left alone.
- Do not use when: The work contains actual defects, shortcuts, or residue -> `are-you-sure`
  - The defects are in delivered code -> `dev-are-you-sure`
  - The work is unfinished rather than unambitious -> `done-for-me`
- Canonical instructions: [`plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md`](../plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md)

### `/never-again`

- Canonical package: `never-again`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Wake-up call when the agent stopped recording and starts forgetting: write the missed lessons, decisions and context into ai-context and push, then keep recording every insight, decision, skill change and version unasked. Use for never again, จำไว้เลย, อย่าให้เกิดอีก, ลืมอีกแล้ว, อย่าเป็นคนขยันแต่โง่.
- Result: The missed insights, decisions and lessons written to their owner documents and pushed; a lesson with three regressions for a repeated mistake; recording resumed.
- Do not use when: The single bad output needs repairing and nothing durable is at stake -> `are-you-sure`
  - The defect is in delivered code and the sweep is what is wanted -> `dev-are-you-sure`
  - The project has no contract yet and truth is scattered rather than wrong -> `project-standard`
- Canonical instructions: [`plugins/james-core/skills/never-again/SKILL.md`](../plugins/james-core/skills/never-again/SKILL.md)


## Deliver an artifact

### `/sum-meet`

- Canonical package: `sum-meet`
- Category: `james-productivity`
- Kind: `output`
- Lifecycle: `promoted`
- Use when: Summarize a meeting or long material completely (every point kept, not long): topics clearly separated in one HTML file ordered summary, table of contents, then each topic, evidence apart from interpretation, project design system with a quiet default, no metacopy. Use for สรุปประชุม, ทำ minutes, meeting minutes.
- Result: The requested short summary, or the full rendered meeting record with source coverage and traceability. Keep verification bookkeeping internal unless requested or material; show unknown or disputed facts where relevant.
- Do not use when: Each agenda must become its own separate page -> `one-page-pls`
  - Project state must be reconstructed from the repository rather than a transcript -> `catchup`
- Canonical instructions: [`plugins/james-productivity/skills/sum-meet/SKILL.md`](../plugins/james-productivity/skills/sum-meet/SKILL.md)

### `/one-page-pls`

- Canonical package: `one-page-pls`
- Category: `james-productivity`
- Kind: `output`
- Lifecycle: `promoted`
- Use when: Summarize the essentials onto one page: choose what a decision-maker needs, in the project's design system with small user overrides accepted and a quiet default style, metacopy checked and removed. One page per topic by default. Use for one page please, one-pager, สรุปหน้าเดียว, ขอ one page.
- Result: The requested page or chat brief. Keep coverage and inspection bookkeeping internal unless requested; disclose any material omission, linked appendix or delivery limitation the reader needs.
- Do not use when: Every agenda must live in one record together -> `sum-meet`
  - Current project state must be reconstructed rather than summarised -> `catchup`
- Canonical instructions: [`plugins/james-productivity/skills/one-page-pls/SKILL.md`](../plugins/james-productivity/skills/one-page-pls/SKILL.md)

## Modes and standards

### `/i-have-adhd`

- Canonical package: `i-have-adhd`
- Category: `james-core`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Shape every reply so it can be acted on at once without holding state in memory, with the answer first and steps numbered. Use for I have ADHD, too long, keep it simple, สั้นๆ, ยาวไป, สรุปให้ทำตามได้เลย. Changes presentation only and never drops needed information.
- Result: A reply that is easy to understand and act on, with progress only when relevant. Preserve the requested artifact format; no mandatory action or status footer.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-core/skills/i-have-adhd/SKILL.md`](../plugins/james-core/skills/i-have-adhd/SKILL.md)

### `/proactive-habits`

- Canonical package: `proactive-habits`
- Category: `james-core`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Decide what is yours to decide, think strategically first, carry the work to completion, skip undecidable points and batch them into one question, and never report back that something is still undone. Activate once for the whole conversation with be proactive, stop asking me, ไม่ต้องถาม, คิดเองทำเองเลย, ทำงานเชิงรุก.
- Result: The completed requested deliverable, or an observed blocker after independent work is finished. Repeated invocation during unfinished work resumes execution immediately; an explicit audit-only request still returns findings.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-core/skills/proactive-habits/SKILL.md`](../plugins/james-core/skills/proactive-habits/SKILL.md)

### `/insight-driven-mode`

- Canonical package: `insight-driven-mode`
- Category: `james-core`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Understand the real user and goal before any work starts, in every kind of task: dig, ask and research until clear, set strategy first, then check the result serves the need, not just that it is done. Marketing: one written insight per group. Activate with insight first, เริ่มจากอินไซต์, เข้าใจก่อนทำ, อย่าเพิ่งลงมือ.
- Result: The deliverable preceded by the understanding and strategy it rests on and followed by the check that it serves the real need; for marketing, every piece traces to one insight line per group.
- Do not use when: The only job is to settle one outside claim, with no customer-facing marketing or copy -> `research-it`
  - The only job is to compare options and recommend one -> `give-me-solutions`
  - The reader needs a shorter reply and no marketing, brand or copy sequence is in play -> `i-have-adhd`
  - The missing piece is who decides the next action, not which insight the copy traces to -> `proactive-habits`
- Canonical instructions: [`plugins/james-core/skills/insight-driven-mode/SKILL.md`](../plugins/james-core/skills/insight-driven-mode/SKILL.md)

### `/coach-me`

- Canonical package: `coach-me`
- Category: `james-productivity`
- Kind: `mode`
- Lifecycle: `promoted`
- Use when: Ask questions that dig to the core of what the person is working through, in performance, life or purpose, so they find their own answer; never think for them, add, complete or advise. Activate with coach me, I feel stuck, โค้ชหน่อย, ตันแล้ว, ไม่รู้จะเริ่มยังไง. Ends when they ask for an answer or a task.
- Result: The next question or a reflection in the person's own words until they reach their own next step; notes if wanted; no advice.
- Do not use when: The person wants the task done rather than to be moved -> `done-for-me`
  - What is unclear is the requirement rather than the person -> `grill-me`
  - The person wants options researched and compared -> `give-me-solutions`
- Canonical instructions: [`plugins/james-productivity/skills/coach-me/SKILL.md`](../plugins/james-productivity/skills/coach-me/SKILL.md)

### `/make-it-james`

- Canonical package: `make-it-james`
- Category: `james-core`
- Kind: `shared-standard`
- Lifecycle: `promoted`
- Use when: Copywriting pass on anything a person will read: human language against the checklist, no Thai AI slop, no translated syntax, no metacopy anywhere in the outcome. Applies automatically to recipient-facing work; also use for humanize it, ภาษาแข็ง, อ่านแล้วเหมือน AI, เกลาคำ. Does not choose format or supply content.
- Result: The reworded output. Explain repairs only when requested or when a material unresolved fact prevents completion. Do not append editing commentary to an artifact-only request.
- Do not use when: Not a replacement for the task workflow. Composes with active workflows and standards.
- Canonical instructions: [`plugins/james-core/skills/make-it-james/SKILL.md`](../plugins/james-core/skills/make-it-james/SKILL.md)

### `/make-it-james-ux`

- Canonical package: `make-it-james-ux`
- Category: `james-software`
- Kind: `shared-standard`
- Lifecycle: `promoted`
- Use when: No slop in UX, UI and web app design, as principles a user or project design system may override. UX: real flow of every user group, fewer steps, no needless modal, left to right, top to bottom, exact grid. UI: locked type and radius, no accent border, nothing jumps, fixed heights. Use for UI รก, จัดหน้าให้เป๊ะ.
- Result: The requested code or rendered artifact. For a rendered deliverable, report the system followed, actual lint/render evidence and material open gates. For code-only output, return exclusively code; keep verification notes internal.
- Do not use when: The rules needed are about wording rather than presentation -> `make-it-james`
  - The interface is defective rather than inconsistent -> `dev-are-you-sure`
- Canonical instructions: [`plugins/james-software/skills/make-it-james-ux/SKILL.md`](../plugins/james-software/skills/make-it-james-ux/SKILL.md)


## Hand over

### `/hand-it-off`

- Canonical package: `hand-it-off`
- Category: `james-core`
- Kind: `workflow`
- Lifecycle: `promoted`
- Use when: Hand this conversation's work to another agent, vendor, account or machine: record every decision, skill and ai-context change in the repository, push it, and write instructions that let the next agent continue pending and planned work without this chat. Use for hand it off, ส่งต่องาน, ให้ AI ตัวอื่นทำต่อ, ย้ายเครื่อง.
- Result: The paste-ready block for the next agent, the handoff file path under docs/handoffs/, and the commit carrying the recorded decisions, state and lessons.
- Do not use when: The user wants to be reminded what has been done, with no transfer -> `catchup`
  - Recording lapsed but the same agent continues -> `never-again`
- Aliases: `skill-router` (legacy compatibility call).
- Canonical instructions: [`plugins/james-core/skills/hand-it-off/SKILL.md`](../plugins/james-core/skills/hand-it-off/SKILL.md)
