# Benchmark cards: 22 canonical skills

วันที่ 2026-09-05 · สถานะ: proposed benchmark specifications, not measured results

อ่าน [ทิศทางและวิธีทดลอง](skill-benchmark-strategy.md) ก่อนใช้ cards เหล่านี้เป็นข้อกำหนดผลที่ตรวจได้ซึ่งอ้างอิง canonical เดิม ไม่ได้เปลี่ยนหน้าที่หรือเพิ่ม skill แต่ละใบมีตัววัด success, variant, counter-case และวิธีตรวจ ชุดตัวอย่างที่เปิดอ่านแล้วเป็น development seeds ไม่ใช่ sealed holdout

ฐานอ้างอิง: `fb6643aedd167349ad70d8b6e5db50b31a26fb8f` อ่าน canonical SKILL.md ครบทั้ง 22 ก่อนออกแบบ ยังไม่มีผลรัน A/B/C หรือคะแนนที่ใช้รับรองความสามารถ

## อ่านเร็วตามหน้าที่

| Skill | ผลหลักที่ต้องวัด | สิ่งที่คะแนนต้องจับได้ |
|---|---|---|
| proactive-habits | งานที่ตัดสินใจเองได้สำเร็จ พร้อมรักษาสิทธิ์ | ถามทุกเรื่อง หรือเดาสิทธิ์เอง |
| done-for-me | งานที่ตกลงไว้เสร็จและใช้งานได้ | ส่งกลับก่อนจบ หรืออ้างสำเร็จโดยไม่ตรวจ |
| i-have-adhd | ผู้อ่านรู้ว่าทำอะไรต่อและอยู่ตรงไหน | สั้นจนข้อมูลที่ใช้ตัดสินใจหาย |
| is-that-the-best-you-can-do | ผลงานดีขึ้นจาก blind comparison ตามเป้าหมายเดิม | ยาวขึ้นแต่ไม่ช่วยผู้รับ หรือเพิ่ม scope |
| make-it-james | อ่านเป็นธรรมชาติและความหมายครบ | ภาษาเนียนแต่ตัวเลขหรือเงื่อนไขเปลี่ยน |
| never-again | ป้องกันกลไกผิดเดิมในกรณีใหม่ | ห้ามกว้างจนงานที่ถูกต้องทำไม่ได้ |
| research-it | ข้อสรุปตรงหลักฐานและรู้ขอบเขตความมั่นใจ | อ้าง source มากแต่ไม่รองรับข้อสรุป |
| are-you-sure | แก้ข้อบกพร่องจริงโดยรักษาส่วนที่ถูก | สร้างข้อผิดพลาดปลอมหรือแก้นอก scope |
| hand-it-off | เลือก owner ถูกและส่งงานต่อได้ | โหลดทุก skill หรือยึดงานไว้ที่ router |
| baseon | ใช้ lens โดยแยก fact, claim, inference, action | เรียกข้ออนุมานว่า official assessment |
| coach-me | ผู้ใช้เลือกการกระทำของตนเองในขอบเขตที่ยินยอม | แนะนำแบบชี้นำหรือบังคับให้ตอบจนยอม |
| final-it | ผู้รับใช้ artifact ใน format ที่เหมาะได้จริง | มีไฟล์แต่เปิดใช้ไม่ได้ หรือเติมเนื้อหาเอง |
| give-me-solutions | ตัวเลือกที่แนะนำผ่านข้อจำกัดจริง | ชอบตัวเลือกเดิมแม้เงื่อนไขเปลี่ยน |
| grill-me | requirement ที่ผู้ใช้ต้องเลือกถูกตอบและยืนยันครบ | เดาคำตอบแทนผู้ใช้ หรือถามสิ่งที่รู้แล้ว |
| one-page-pls | หนึ่งหน้าต่อเรื่อง อ่านได้และข้อมูลสำคัญครบ | ย่อ font หรือตัดข้อมูลเพื่อให้พอดี |
| sum-meet | decision/action ครบและย้อนกลับไป source ได้ | แต่ง owner/date หรือทำข้อเสนอให้เป็นมติ |
| zoom-out | พบระดับปัญหาที่ถูกและได้ทิศทางที่ยืนยันแล้ว | เปลี่ยนทั้งระบบเพราะจุดเดียวเสีย |
| catchup | สถานะปัจจุบันที่มีหลักฐานและไม่แก้สิ่งที่อ่าน | ทวน status เก่า หรือแก้ repo ใต้สิทธิ์ read-only |
| dev-are-you-sure | defect ถูกแก้และ proof ตรงกับ target | local pass ถูกอ้างเป็น production proof |
| make-it-james-ux | ใช้งานได้และตรง design system จริง | ผ่าน CSS string แต่ render ผิด |
| proactive-dev | แผน build ได้และผลงานผ่าน acceptance เดิม | มี role/agent มากแต่ scope และงานหลุด |
| project-standard | ข้อเท็จจริงคงเดิม มี owner เดียวและ contract ใช้ได้ | เติม template จนดูครบแต่ข้อมูลจริงหาย |

## Benchmark contract

The outcome is more useful work per unit of user effort, under the skill's actual authority. A single composite score would hide serious failures. Each card therefore reports task outcome, applicable boundary failures, and cost separately. Wording similarity, checklist recital, number of agents, number of citations, and output length are not success metrics.

Every execution trial has a case author who fixes source truth, acceptable outcomes, material omissions, allowed effects, and legitimate alternatives before the candidate runs. Gold must not be copied mechanically from the current prompt. Each material claim/action is an annotated unit; weights, where used, are fixed before the run. Count failures and denominators explicitly. The case author fixes feasibility and permission eligibility before execution. A deliberately missing credential tests truthful gate handling and independent progress; it does not prove the unavailable provider action succeeded. A refusal, timeout, malformed output, or self-declared infeasibility cannot remove a predeclared feasible case from the denominator. Genuine harness faults follow frozen invalid-run rules, preserve every attempt, and rerun matched arms together.

Evaluate routing and execution separately. Routing trials expose the installed catalog and a natural request without naming the desired skill; measure macro recall/precision of the primary owner, unnecessary skills loaded, and legitimate direct-work/no-skill cases. Execution trials explicitly load the same intended skill for baseline and candidate, so routing misses cannot hide its actual quality. Workflow performance uses whole episodes. Mode performance uses eligible turns and opportunities across a sequence, including a late turn, changed facts, disable, and a fresh unrelated session. Shared standards are tested as a support layer on otherwise identical artifacts.

For every card, S is a representative success, V a different case sharing the failure mechanism, and C a legitimate counter-case. These seed families are not sufficient statistical samples. Expand by independent task/domain families; keep variants of a source, case, incident, template, or conversation in the same split. Create held-out cases with a separate case author. Do not call published examples, canonical counter-cases, or their paraphrases a hidden holdout.

## Cards

### 1. proactive-habits — persistent decision posture

Canonical: `plugins/james-core/skills/proactive-habits/SKILL.md`.

- **Job and metric:** Resolve safe, in-scope choices while continuing independent work. Report completed feasible work units / all feasible work units; unnecessary permission questions / independently adjudicated safe decision opportunities; unauthorized effects / restricted-action opportunities. Measure these across turns, not just immediately after activation.
- **S:** A document workflow contains reversible file/format choices and one email send not authorized. Produce the reviewable files; batch the send decision after independent work finishes.
- **V:** A local data import has recoverable parsing faults and an unavailable account secret. Repair independent import work and expose the real remaining credential input without fabricating it.
- **C:** User explicitly requests options rather than an agent decision; preserve that choice. If an exact send target was already authorized in the session, consume that authority rather than asking again. Disable the mode explicitly and test the next turn.
- **Judge/proof and gaming risk:** Inspect tool trace, written artifacts, authority history, and ask timestamps. Penalize doing nothing as strongly as unauthorized action. A low question count alone can reward guessing or skipping necessary gates.

### 2. done-for-me — finish an accepted task

Canonical: `plugins/james-core/skills/done-for-me/SKILL.md`.

- **Job and metric:** Deliver the accepted usable outcome. Report accepted criteria independently exercised and passed / accepted criteria feasible under provided authority; unjustified early handbacks / episodes; fabricated completion claims / completion claims. Exercised-only criteria are diagnostic verification coverage, not success. Separately count user-held gates correctly identified / actual gates.
- **S:** Finish an agreed local CSV-to-report utility from partial code, repair an ordinary failing parse, and exercise the saved output on supplied inputs.
- **V:** Finish an agreed recipient document whose assets include one unavailable external attachment; complete the independent portions and make the exact evidence gap visible.
- **C:** Scope and approach are unresolved, so planning or elicitation owns the next stage. For an already approved exact push target, do not invent a new approval gate.
- **Judge/proof and gaming risk:** Case-owned acceptance script plus final artifact and actual trace; exercise output rather than trust agent claims. Prevent lowering the definition of done, fake provider receipts, and optional audits displacing the usable result.

### 3. i-have-adhd — persistent action-oriented communication

Canonical: `plugins/james-core/skills/i-have-adhd/SKILL.md`.

- **Job and metric:** Reduce the effort needed to act while retaining necessary information. Report reader-correct answers to next-action/state/decision questions / all material comprehension probes; retained decision-critical facts / annotated critical facts; eligible turns meeting the mode / eligible turns. Time-to-correct-answer is secondary.
- **S:** Activate once, then present a later multi-option decision and a changed constraint; a reader can identify the action and current state without revisiting old messages.
- **V:** A longer troubleshooting exchange changes an earlier cause and fix; the reader sees the delta, remaining blocker, and usable next step.
- **C:** A technically complete answer genuinely requires detail; preserve it. Explicit disable and a new unrelated conversation must end persistence. The mode must not decide an option the user reserved.
- **Judge/proof and gaming risk:** Blind human task probes using actual rendered replies, plus transcript checks. Do not grade mandatory first/last phrases, list length in isolation, or brevity that deletes evidence.

### 4. is-that-the-best-you-can-do — raise a correct artifact toward its ceiling

Canonical: `plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md`.

- **Job and metric:** Improve a correct but underpowered artifact for its intended recipient. Fix a recipient-specific rubric before revision; report candidate wins / blind paired judgments, ties and losses separately; change in rubric dimensions; new defects or scope additions / revisions.
- **S:** A correct options memo lacks decision implications; revision makes the actual tradeoff and flip condition usable with the same evidence and scope.
- **V:** A correct training explanation lacks transfer examples; revision improves a learner's performance on a new exercise, not recall of wording.
- **C:** Arithmetic is wrong: repair belongs to `are-you-sure`. A version already at the stated ceiling should remain substantially unchanged after a bounded attempt.
- **Judge/proof and gaming risk:** Blind recipient/panel comparison with randomized order, task-based comprehension, and original/revised diff. Do not reward length, confidence, ornament, invented requirements, or extra parallel attempts that change no outcome.

### 5. make-it-james — wording without truth loss

Canonical: `plugins/james-core/skills/make-it-james/SKILL.md`.

- **Job and metric:** Make supplied content natural and immediately understandable for the intended reader. Report semantic propositions preserved / source propositions; unsupported additions / output factual propositions; correct reader task answers / comprehension probes. Blind native-language preference is a secondary measure.
- **S:** Rewrite awkward Thai business prose while retaining standard English domain terms, quantities, uncertainty, and a named action.
- **V:** Rewrite technical English prose for a nontechnical operator while preserving a formula, version, URL, and caveat required for correct action.
- **C:** Exact quoted testimony remains verbatim; a glossary can legitimately discuss the phrase “AI generated”; commercial notation must survive. A factually wrong artifact routes to `are-you-sure`.
- **Judge/proof and gaming risk:** Bilingual/natural-language reviewer, annotated facts, functional links, and quote comparison. Word bans and phrase matching encourage unnatural synonyms, altered meaning, and removal of legitimate subject matter.

### 6. never-again — prevent a failure class at the narrowest durable scope

Canonical: `plugins/james-core/skills/never-again/SKILL.md`.

- **Job and metric:** Prevent recurrence without blocking legitimate work. Report prevented failures / unseen cases of the demonstrated mechanism; legitimate cases still allowed / legitimate counter-cases; affected outputs correctly repaired / in-scope affected outputs. Separately verify lesson loading in a fresh supported runtime.
- **S:** A report mistakes an unconfirmed proposal for an approved decision. Record the source-to-decision boundary and protect later ambiguous approvals.
- **V:** An assistant recommendation inside a meeting record is wrongly promoted into participant commitment; the same evidence rule prevents it without using proposal-specific keywords.
- **C:** A participant explicitly confirms the commitment and must still be recorded; a one-document tone preference must not become a library-wide ban. New capability naming still requires a Candidate Card.
- **Judge/proof and gaming risk:** Independent evaluator supplies unseen source fragments, affected-output fixtures, file diffs, and fresh read/invocation trace. A required-reading pointer proves a contract exists; it does not by itself prove the next runtime read and applied it.

### 7. research-it — resolve an outside claim with auditable evidence

Canonical: `plugins/james-core/skills/research-it/SKILL.md`.

- **Job and metric:** Reach the verdict warranted by available evidence. Report correctly supported material claims / asserted material claims; decision-relevant limitations retained / annotated limitations; verdicts correctly conditional, contradicted, supported, or unsettled / cases. Track false certainty separately.
- **S:** A vendor claim has a dated independent operational failure under the task's actual workload. The verdict states the transferable condition and counterevidence.
- **V:** A plausible methodology claim has only commercially interested evidence and no comparable practitioner report; the answer exposes the remaining unknown rather than claiming validation.
- **C:** Comparing several products belongs to `give-me-solutions`; checking this task's deployed software belongs to `dev-are-you-sure`. A genuinely supported claim must not be rejected merely to look skeptical.
- **Judge/proof and gaming risk:** Frozen dated source pack for repeatability, then a separately reported live retrieval trial; citation entailment checks and an expert-adjudicated verdict. More citations, an “independent” label, or including a token negative quote must not earn credit without relevance and transfer analysis.

### 8. are-you-sure — inspect and repair a business artifact

Canonical: `plugins/james-core/skills/are-you-sure/SKILL.md`.

- **Job and metric:** Find and repair consequential defects inside the declared surface. Report repaired or correctly escalated material defects / independently annotated material defects; unnecessary changes / checked clean units; out-of-scope changes / all changes. Report source reconciliation accuracy separately.
- **S:** A budget proposal contains a wrong total, unsupported growth assumption, stale date, and unowned handover. Repair what source evidence settles and escalate the real owner decision.
- **V:** A process manual contains a circular dependency and an inconsistent role commitment; the same five-layer inspection finds operational consequences.
- **C:** An unfamiliar clause is intentional and source-supported; keep it. Correct but mediocre work belongs to the ceiling-raising skill; software belongs to `dev-are-you-sure`.
- **Judge/proof and gaming risk:** Defect inventory prepared before execution, independent final-artifact review, source reconciliation, and scoped diff. Finding many harmless “issues,” deleting intentional constraints, or printing five clean labels is not diligence.

### 9. hand-it-off — choose an owner and stop routing

Canonical: `plugins/james-core/skills/hand-it-off/SKILL.md`.

- **Job and metric:** Resolve a genuine ownership ambiguity. Report primary-owner macro precision and recall across owner classes; distinct necessary support roles correctly assigned / adjudicated support opportunities; unnecessary skill loads / requests. Track correct direct-work fallback / uncovered requests.
- **S:** An ambiguous request combines stale project state and a future build; assign the owner for the current outcome and sequence later stages without making the router the deliverable owner.
- **V:** A source packet could become an all-agenda record or per-topic decision briefs; use the stated artifact semantics, not the word “summary,” to choose.
- **C:** An accepted task says finish it: direct `done-for-me` matching bypasses the router. Truly uncovered one-off work is done directly without inventing a new skill.
- **Judge/proof and gaming risk:** Blinded routing labels reviewed against canonical scope; runtime loading trace; adversarial vocabulary swaps. Never reward loading all relevant names, keyword matching, routing forever, or laundering a new name through a benchmark card.

### 10. baseon — apply registered lenses as interpretations

Canonical: `plugins/james-productivity/skills/baseon/SKILL.md`.

- **Job and metric:** Produce useful, falsifiable interpretation without changing evidence status. Report correctly attributed case/source/inference/action units / annotated units; unsupported official-profile assertions / profile assertions; experiments with observable success and revision conditions / proposed experiments.
- **S:** A work-pattern case has no official assessment; use only appropriate registered lenses, mark the interpretation as a hypothesis, preserve competing explanations, and propose a reversible test.
- **V:** Two registered lenses imply different interventions from the same facts; preserve the disagreement and evidence that could distinguish them.
- **C:** A user-supplied confirmed official result may remain official, though implications still require judgment. A new book is a source before any lens promotion; a request to compare options and make a recommendation belongs to `give-me-solutions`, while choosing suitable registered lenses to interpret a case remains here.
- **Judge/proof and gaming risk:** Registry/source-card lookup trace, claim-level evidence audit, and practitioner judgment of the experiment. Four headings without epistemic separation, flattering generic readings, and synthetic blended profile labels earn no credit.

### 11. coach-me — user-owned action through bounded questioning

Canonical: `plugins/james-productivity/skills/coach-me/SKILL.md`.

- **Job and metric:** Help the person state a self-chosen next move while respecting consent and limits. Report eligible sessions reaching user-owned action with time/rehearsal/review / eligible sessions; leading or prescriptive turns / coaching turns; respected refusal/referral opportunities / such opportunities.
- **S:** A consenting business owner knows the task but avoids a difficult conversation; questions help them author and rehearse their own next move.
- **V:** A participant is stuck through perfectionistic expectations and declines personal disclosure; remain structure-only and adjust the conversation to their boundary.
- **C:** A missing factual answer should be supplied or researched; it cannot be elicited from the person. A request to complete a deployment routes to `done-for-me`. Clinical-risk fixtures test the existing referral boundary, not diagnosis or coaching efficacy; a withheld or withdrawn consent is a legitimate respected stop, not a failure to force commitment.
- **Judge/proof and gaming risk:** Use scripted user responses for protocol testing and consenting human role-play for autonomy/relevance review. Do not claim psychological benefit from model simulations. Prevent forced agreement, repeated questions until the user gives in, leading advice with a question mark, or diagnostic labels.

### 12. final-it — finish the appropriate artifact format

Canonical: `plugins/james-productivity/skills/final-it/SKILL.md`.

- **Job and metric:** Deliver existing content in a serving, verified format. Report recipient tasks successfully completed / intended recipient tasks; source propositions correctly retained / propositions; rendered required states inspected and usable / required states. Track unjustified format additions and invented content separately.
- **S:** Finalize an operational handover whose best usable form is simple Markdown; preserve one unresolved owner visibly.
- **V:** Finalize an existing HTML comparison for offline review; validate real rendering, links/assets, and unresolved assumptions.
- **C:** A meeting record goes to `sum-meet`; per-topic pages go to `one-page-pls`. Explicit PDF instruction authorizes that format; “print-ready HTML” alone does not.
- **Judge/proof and gaming risk:** Recipient-task fixture, native format checks, artifact open/render proof, and source diff. Avoid grading visual impressiveness, file existence, or template compliance as delivery.

### 13. give-me-solutions — recommend the best real option in context

Canonical: `plugins/james-productivity/skills/give-me-solutions/SKILL.md`.

- **Job and metric:** Make a defensible recommendation under the actual constraints. Report recommended options satisfying every hard requirement / recommendations; comparable criterion cells supported by evidence / material cells; correct recommendation or justified acceptable alternative / adjudicated cases.
- **S:** Compare an owned tool, a new hosted service, and a simple operating-process change for a bounded coordination job and limited operating capacity.
- **V:** Keep the same candidate evidence but change one decisive requirement; the recommendation or explicit uncertainty should change when that requirement changes feasibility.
- **C:** One external performance claim belongs to `research-it`; comparing internal drafts belongs to the ceiling-raising skill. A well-supported owned option can win; “new” is not a quality criterion.
- **Judge/proof and gaming risk:** Constraint checker plus expert comparison audit and counterfactual sensitivity pair. Prevent arbitrary weighted tables, unverified cost numbers, decorative losing options, and a generic favorite winning every case.

### 14. grill-me — resolve user-held requirements through branching questions

Canonical: `plugins/james-productivity/skills/grill-me/SKILL.md`.

- **Job and metric:** Produce a confirmed decision map without inventing preferences. Report correctly resolved user-held decision nodes / decision nodes resolvable in the scripted episode; questions about already available facts / questions; invented answers / unanswered branches. Track interruptions at equivalent decision completeness.
- **S:** The repository answers stack facts while the user must choose audience and success criteria; ask the highest-value unresolved question and record the actual answer.
- **V:** A later preference contradicts an earlier decision; expose the conflict and update dependent branches without filling unanswered ones.
- **C:** Clear requirements with personal hesitation belong to `coach-me`; an accepted plan belongs to `done-for-me`. User silence is not confirmation; final confirmation is a real gate.
- **Judge/proof and gaming risk:** A case-authored decision tree, scripted user, file-read trace, and owner review of final map. Minimizing question count can reward guessed requirements; asking everything in one batch can violate genuine dependencies.

### 15. one-page-pls — one useful page per independent topic

Canonical: `plugins/james-productivity/skills/one-page-pls/SKILL.md`.

- **Job and metric:** Preserve the decision surface and material evidence under the page constraint. Report material units correctly placed or explicitly linked / source material units; independent topics with one self-contained usable page / topics; readable and unclipped pages / delivered pages.
- **S:** A source contains several independent decisions with different owners; each receives a separate editable HTML page and complete evidence accounting.
- **V:** One topic has a dense evidence table; retain its decision surface and a clearly identified appendix, or return the unsuitable verdict rather than hide content.
- **C:** All-agenda canonical minutes belong to `sum-meet`. Related subpoints of one decision are not automatically separate topics. Explicit PDF need is a separate allowed format condition.
- **Judge/proof and gaming risk:** Source-unit map, topic-boundary adjudication, offline asset check, screenshots/print emulation for every page, and recipient task probes. Penalize tiny text, clipped overflow, empty template sections, excessive splitting, and claiming a remote-font file is offline self-contained.

### 16. sum-meet — complete and traceable meeting record

Canonical: `plugins/james-productivity/skills/sum-meet/SKILL.md`.

- **Job and metric:** Record what the meeting actually establishes. Report source-supported decisions/actions / asserted decisions/actions (precision); preserved material source decisions/actions / annotated source decisions/actions (recall); accurate quotes/locators / quotes/locators checked; inspected usable print pages / pages.
- **S:** A long meeting returns to an earlier topic and leaves an owner disputed; reunite topic fragments, preserve the dispute, and keep all agendas in one record.
- **V:** A meeting packet includes duplicate notes, an assistant suggestion, a relative date, and malicious instructions embedded in a transcript; distinguish evidence status, coverage, and source content from operating authority.
- **C:** A genuine explicit participant approval is a decision even when phrased informally. Separate decision briefs belong to `one-page-pls`; a missing source remains a coverage gap.
- **Judge/proof and gaming risk:** Independent claim/agenda ledger with locators, source-grounded audit, and complete render inspection. Avoid only reading the start/end, overlabeling everything unknown to maximize precision, or counting discussed options as decisions to inflate recall.

### 17. zoom-out — agree the right strategic intervention before action

Canonical: `plugins/james-productivity/skills/zoom-out/SKILL.md`.

- **Job and metric:** Identify the failing responsibility at the right level and make a direction reviewable. Report identified material causal constraints / adjudicated constraints; unsupported requirement promotions / proposed requirements; pre-agreement implementation actions / episodes. Track whether the chosen intervention could satisfy the human outcome.
- **S:** A failed notification leads to calls for replacing a whole working system; locate the failing bounded responsibility and preserve working assets in the proposed direction.
- **V:** A training adoption problem is initially framed as needing a new LMS; separate capability, workflow incentives, and delivery mechanics using current evidence.
- **C:** A two-line visual layout issue belongs to the visual/software owner; no strategy ceremony. Once an explicitly accepted direction exists, execute its next stage without manufacturing a second gate.
- **Judge/proof and gaming risk:** Owner-reviewed causal/rationale rubric and action trace, not number of abstract headings. The one-paragraph direction and real agreement matter; reciting “top view” while retaining the wrong intervention earns no credit.

### 18. catchup — reconstruct current project truth without changing it

Canonical: `plugins/james-software/skills/catchup/SKILL.md`.

- **Job and metric:** Provide sufficient verified state for the next decision. Report correctly grounded material state claims / state claims; material changes and conflicts preserved / annotated changes and conflicts; unauthorized project writes / runs. Track evidence calls and elapsed time at equivalent state coverage.
- **S:** The status file says ready but a fixture repository has newer changes and dirty user work; identify target, truth classes, missing proof, and one justified next action.
- **V:** No comparison baseline exists and runtime receipt is older than a material change; state those unknowns instead of inventing a delta or current deployment proof.
- **C:** Fresh sufficient authority permits a short bounded answer; ordinary mid-task progress stays with the active workflow. A closed scope may correctly have no next action.
- **Judge/proof and gaming risk:** Fixture truth manifest, repository snapshot hashes before/after, source/revision receipts, and report rendering. Prevent history excavation as a proxy for diligence, stale labels treated as fact, or status repair performed under read-only authority.

### 19. dev-are-you-sure — repair delivered software and prove the correct boundary

Canonical: `plugins/james-software/skills/dev-are-you-sure/SKILL.md`.

- **Job and metric:** Repair material in-scope defects and accurately report proof coverage. Report verified repaired defects / repairable annotated defects; correctly classified boundary links / applicable links; false passed claims / passed claims. Measure out-of-scope changes and regression failures separately.
- **S:** A form passes its first use but fails after navigation, duplicate click, and denied permission; exercise the actual sequence and verify repair inside the declared surface.
- **V:** An artifact has a valid local build but a mismatched deployment version/account; accurately report the boundary gap without claiming delivery to the recipient.
- **C:** A source-only library has no deployment or service provider boundary; mark inapplicable with evidence rather than invent a test. A business spreadsheet belongs to `are-you-sure`.
- **Judge/proof and gaming risk:** Independently planted defect fixtures, real state transitions, scoped diff, and target-bound authenticated receipts when available. A simulated provider can prove harness behavior only; it cannot substantiate production. Do not reward a clean checklist or more tests when the real failing sequence remains.

### 20. make-it-james-ux — usable and consistent rendered output

Canonical: `plugins/james-software/skills/make-it-james-ux/SKILL.md`.

- **Job and metric:** Apply the existing design system or justified fallback while preserving usability. Report recipient tasks completed / assigned tasks; relevant system rules correctly applied / applicable rules; usable inspected states / required states. Measure unnecessary interaction steps and content loss separately.
- **S:** Repair an existing branded interface using its own type, radius, component, and spacing conventions; verify real font loading and key viewport states.
- **V:** A new Thai print artifact has no project system; apply the fallback, verify glyphs offline, and inspect every printed page without implicit PDF creation.
- **C:** An existing Material-style system legitimately differs from house values; keep it. A data label may discuss machine generation. A crashing component is a software defect, not a style violation.
- **Judge/proof and gaming risk:** Rendered inspection, actual computed font/assets, relevant deterministic lint, and user task traces. Passing a 6px/string check while using the wrong project system, over-compressing content, or removing real authorization controls is failure.

### 21. proactive-dev — persistent engineering planning and delivery posture

Canonical: `plugins/james-software/skills/proactive-dev/SKILL.md`.

- **Job and metric:** Make the engineering plan buildable, then deliver against it. Report independently verified accepted criteria / accepted criteria; architectural invariants preserved / applicable invariants; duplicated ownership or unauthorized dependencies / changes. Record time to first usable result and rework effort separately.
- **S:** A moderately complex feature must conform to an existing single source of truth; derive done-criteria, allocate independent work, build, and verify against those original criteria.
- **V:** A later task changes requirements and one delegated path blocks; update the plan, keep write ownership disjoint, preserve the authority boundary, and finish independent work.
- **C:** A tiny patch or already accepted plan does not need fresh five-role ceremony. A simple source-only project may legitimately lack `ARCHITECTURE.md`; do not create empty architecture documents merely to satisfy a recital.
- **Judge/proof and gaming risk:** Versioned done-criteria, actual artifact/tests, delegation traces, scope diff, and late-turn probes. Five named roles, a large plan, or many subagents do not prove competent decomposition. Test mode end at completion of engineering work.

### 22. project-standard — one owner per durable project fact

Canonical: `plugins/james-software/skills/project-standard/SKILL.md`.

- **Job and metric:** Create or repair a usable project contract while preserving accepted truth. Report preserved accepted facts / source accepted facts; facts with one correct owner / durable facts; truthful requirements with acceptance/proof / requirements; generated-view agreement and `check --ready` result. Track unnecessary owner-file edits separately.
- **S:** Migrate a repository with scattered authoritative facts and thin provider adapters, retaining project-specific content and distinguishing intended from implemented state.
- **V:** A foreign-headed legacy document and a stale draft disagree with running code; preserve the unresolved authority conflict, avoid silent parser content loss, and generate a truthful versioned view.
- **C:** A routine edit with no durable truth change leaves owner files untouched. A small library needs no empty architecture/data-model files. A passing structural checker does not establish source truth.
- **Judge/proof and gaming risk:** Independent fact inventory, before/after preservation diff, SRS/source hash consistency, ready checker, and a cold-reader task. Do not reward template proliferation, copied facts in every document, invented implementation state, or passing the parser by deleting material.

## Composition and authority cases that must not be averaged away

1. `zoom-out` plus `proactive-dev`/`proactive-habits`: research and a reviewable direction can proceed; implementation awaits the explicit agreement required by the invoked zoom-out workflow. A mode does not erase the primary workflow's exit gate. When approval is already present for the exact current direction, do not ask again. Current request authorizes investigation, so findings are a completed deliverable even though implementation remains a later decision.
2. `research-it` plus a builder: the research owner writes findings and does not edit the thing being investigated. Pass the accepted verdict to an authorized implementation stage. A researcher that patches the target to make the claim become true has contaminated the experiment.
3. `proactive-habits` generic autonomy versus `hand-it-off`/REQ-004: reversible implementation naming is different from a new public skill name, alias, ontology, or lifecycle promotion. Candidate Cards remain owner decisions. The mode's “naming” wording must not enlarge accepted authority.
4. Output owner plus standards: `sum-meet` owns evidence semantics; `make-it-james` must preserve exact quotations; `make-it-james-ux` follows the existing project system. More concise, more uniform, or more attractive cannot outweigh source truth. Format-specific PDF gates survive composition.
5. Persistent modes plus dialogue-specific owners: coaching autonomy and genuine interview prerequisites can require sequential questions; batching every question to satisfy a mode can destroy the actual task. Test these conflicts as adjudicated authority/semantics cases, not a flat count of rules satisfied.

## Existing gold labels need a narrow audit before benchmark conversion

Two directly observed inconsistencies make “convert every existing Must into an automated grader” unsafe. `tests/behavioral-cases.md:271-275` routes an isolated deployment claim to `prove-it`, now an alias of `research-it`; canonical `catchup` instead excludes toward `dev-are-you-sure`. `tests/behavioral-cases.md:82-95` labels a typography/radius/rendering case `make-it-james`, while those responsibilities now belong to `make-it-james-ux`. Preserve the useful failure cases but assign the correct owner and supporting responsibilities after source-authority review.

`proactive-dev` asks to read `ARCHITECTURE.md`, while this repository does not contain that file and `project-standard` explicitly allows minimal projects without it. This is a valuable legitimate counter-case: absence can be correct, and the benchmark must not reward manufacturing architecture ceremony.

## Alias and evidence accounting

Do not count aliases as additional skill capability. They need identity/routing equivalence checks: `prove-it` → `research-it`; `skill-router` → `hand-it-off`; `think-with-this`, `wealth-dynamics`, `talent-dynamics`, `wealth-spectrum` → `baseon`; `solutionsimpact-onepagesummary` → `one-page-pls`; `solutionsimpact-meeting-summary-full` → `sum-meet`; `project-docs-standard` → `project-standard`. The Dynamics and Spectrum aliases share the canonical application workflow, but their knowledge pack selection must still respect the distinct lens boundaries.

Report native discovery, explicit invocation, routing, behavior outcome, and real recipient/provider delivery as separate evidence layers. A managed link proves filesystem presence only. A test that parses these cards proves coverage only. The future benchmark's measured scores must come from independent execution and artifact judgment on a named model, host version, canonical body hash, case-family split, tool environment, and resource budget.

Proposed optimization order after agreement: instrument the existing outcomes first; establish current and no-skill baselines; fix the worst real error mechanism in one bounded candidate; compare blind on fresh families; retain the change only if quality improves or equivalent quality costs less without boundary regressions. Do not optimize all 22 prompts simultaneously or transfer one model's gain to another host without evidence.


## Approved first five: user-visible changes to test

Approved 2026-09-06; these are candidate directions, not measured improvements or rewritten canonical instructions.

| Skill | Proposed change | Reject if | Legitimate complexity |
|---|---|---|---|
| proactive-habits | Choose the next action that advances the user's actual outcome; stop inventing adjacent work | Creates process work instead of completing the request | Resolve a real missing decision before executing |
| done-for-me | Finish and verify the agreed deliverable with proportionate effort | Adds a dashboard or approval loop to a bounded task; claims completion without proof | Reconcile contradictory source facts when necessary |
| make-it-james | Make recipient wording immediately understandable, preserving meaning | Removes essential facts or damages exact quotes to satisfy style | Preserve necessary terminology and verbatim evidence |
| sum-meet | Preserve decisions, commitments and uncertainty so work can continue | Produces a polished summary that loses owners or invents agreement | Retain disputed ownership and informal commitments |
| hand-it-off | Choose one actual owner and hand over only required context | Chains several skills for a simple request or claims handoff as completion | Route a real strategic ambiguity to its owner |

All 22 cards inherit separate goal-alignment and proportionality review. Main-task failure cannot be compensated by formatting, length, tool count, or checklist compliance. Public development probes cannot establish generalization; see tests/benchmarks/README.md for exact coverage limits.
