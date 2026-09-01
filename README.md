# JamesSkills

Canonical workflows and prompts for AI collaboration. Designed for Claude, ChatGPT, Cursor, and Gemini.

## Highlights

### `/grill-me`
- **EN:** Challenge an idea. The AI asks sequential questions to expose flaws and resolve dependencies before execution.
- **TH:** สั่งให้ AI ต้อนและซักถามจุดอ่อนในแผนงานทีละข้อ เพื่ออุดรอยรั่วก่อนลงมือทำ

### `/give-me-solutions`
- **EN:** Research external options. Present tradeoffs without making the final choice.
- **TH:** วิเคราะห์และเปรียบเทียบข้อดีข้อเสียของแต่ละทางเลือก เพื่อประกอบการตัดสินใจ

### `/zoom-out`
- **EN:** Reframe a problem at the system level before patching symptoms.
- **TH:** ถอยมามองภาพรวม เพื่อหาต้นตอของปัญหาระดับโครงสร้าง

### `/one-page-pls`
- **EN:** Turn source material into one self-contained executive page per topic.
- **TH:** สรุปเนื้อหาทั้งหมดให้อยู่ในหน้าเดียวแบบ One-Pager แยกตามวาระการประชุม

## 📚 Full Skill Directory (รายการสกิลทั้งหมด)

### Context & Setup (การเริ่มต้นและรวบรวมบริบท)

#### ⚡️ `/project-standard`
*Create or repair project truth (SRS, NFR, Permissions).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

AI starts coding blindly based on a 2-line prompt. The project breaks when you hand it over to another AI because there's no central truth.

</td>
<td valign="top">

AI generates strict `PROJECT.md` and `SRS.html` files. Every rule, permission, and constraint is documented before a single line of code is written.

</td>
</tr>
</table>

#### ⚡️ `/catchup`
*Reconstruct current state after a continuity gap.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

"Hi AI, here is a 5-page explanation of what we did yesterday and what you need to do next..."

</td>
<td valign="top">

<b><i>User:</i></b> <code>/catchup</code><br><br><b><i>AI:</i></b> Scans the Git tree and instantly outputs: "You left off at fixing the Auth bug. Here is the exact file and the next step."

</td>
</tr>
</table>

### Analyze & Decide (การวิเคราะห์และตัดสินใจ)

#### ⚡️ `/zoom-out`
*Reframe the problem at the system level before patching symptoms.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "Here is the CSS fix to hide the error button on the dashboard."

</td>
<td valign="top">

<b><i>AI:</i></b> "Wait. Hiding the button doesn't fix the API failure. The root cause is your database architecture. Let's fix the schema first."

</td>
</tr>
</table>

#### ⚡️ `/give-me-solutions`
*Research external options and present objective tradeoffs.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "You should use React. It is very popular and good."

</td>
<td valign="top">

<b><i>AI:</i></b> Presents a strict 3-column table comparing React, Vue, and Svelte based on your exact server cost constraints and team size, without making the decision for you.

</td>
</tr>
</table>

#### ⚡️ `/baseon`
*Apply a named knowledge lens (e.g., Wealth Dynamics).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

AI gives generic, fortune-cookie business advice using broad MBA buzzwords.

</td>
<td valign="top">

AI analyzes your specific situation using the exact vocabulary, constraints, and mechanics of the requested framework.

</td>
</tr>
</table>

#### ⚡️ `/grill-me`
*Interactive stress-test to expose flaws in your plan.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "That is a brilliant idea! I agree completely. Let's do it!"

</td>
<td valign="top">

<b><i>AI:</i></b> "I see a massive flaw in your payment gateway logic. What happens if the webhook fails? <i>(I will wait for your answer before continuing)</i>"

</td>
</tr>
</table>

### Execute & Verify (การลงมือทำและตรวจสอบ)

#### ⚡️ `/done-for-me`
*End-to-end authorized implementation without waiting for permission.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "I wrote the first function. Should I write the second one? Let me know!"

</td>
<td valign="top">

<b><i>AI:</i></b> Writes all 10 functions, updates the tests, runs the build, and says: "Done. It's deployed."

</td>
</tr>
</table>

#### ⚡️ `/prove-it`
*Verify completion claim at the boundary.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "I fixed the bug. The code looks correct now."

</td>
<td valign="top">

<b><i>AI:</i></b> "Here is the screenshot of the passing test suite and the cURL command output proving the API returns 200 OK."

</td>
</tr>
</table>

#### ⚡️ `/never-again`
*Convert a rejected result into a permanent regression guard.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

You have to tell the AI <i>'Stop using var!'</i> every single day.

</td>
<td valign="top">

The AI writes a permanent system rule so that it, and every future AI, will never make that specific mistake in this project again.

</td>
</tr>
</table>

#### ⚡️ `/is-that-the-best-you-can-do`
*Force the AI to aggressively self-critique and rewrite to the absolute limit.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

AI outputs a generic, safe, boilerplate response. You have to manually point out every weak paragraph.

</td>
<td valign="top">

AI roasts its own previous draft, performs deep research, and produces a highly-polished, boundary-pushing masterpiece.

</td>
</tr>
</table>

### Outputs & Deliverables (การสร้างผลลัพธ์สุดท้าย)

#### ⚡️ `/sum-meet`
*Source-faithful meeting record with complete agenda and actions.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

A short, bulleted list that misses half the context and forgets who was assigned what task.

</td>
<td valign="top">

A pristine A4 HTML document with full context, exact decisions made, and a tracked action register.

</td>
</tr>
</table>

#### ⚡️ `/one-page-pls`
*Self-contained executive brief.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

A 10-page wall of text that no executive will ever read.

</td>
<td valign="top">

One single, perfectly formatted page containing only the absolute core decisions, risks, and next steps.

</td>
</tr>
</table>

#### ⚡️ `/final-it`
*Select and finish recipient-ready artifact.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "Sure, here is the email you asked for: <br> Subject: Hello..."

</td>
<td valign="top">

Outputs ONLY the raw email text. No 'Sure!', no 'Let me know if you need changes!', no conversational filler.

</td>
</tr>
</table>

### Persistent Behaviors (กฎประจำตัวของ AI)

#### ⚡️ `/i-have-adhd`
*Concise, direct, low-friction communication mode.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

Huge paragraphs explaining the history of HTML before giving you a <div> tag.

</td>
<td valign="top">

No fluff. Bullet points. Just the exact code and where to put it.

</td>
</tr>
</table>

#### ⚡️ `/make-it-james`
*Strict recipient-facing wording standard (No AI Theatre).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

"As an AI language model, I recommend..." or "In today's fast-paced digital world..."

</td>
<td valign="top">

Sharp, decisive, professional human tone. Sounds exactly like an expert consultant.

</td>
</tr>
</table>

#### ⚡️ `/make-it-james-ux`
*Visual and UI standards (IBM Plex Thai, modern layouts).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

Ugly, generic HTML with Times New Roman and zero padding.

</td>
<td valign="top">

Production-ready, beautiful UI components with proper fonts, spacing, and accessible contrast.

</td>
</tr>
</table>

#### ⚡️ `/proactive-habits`
*Prevent passive subordinate waiting behavior.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

AI acts like an intern waiting for explicit step-by-step orders.

</td>
<td valign="top">

AI acts like a senior partner: it predicts the next step, warns you of edge cases, and moves the project forward automatically.

</td>
</tr>
</table>

#### ⚡️ `/proactive-dev`
*Enforce blast-radius checks before mutating code.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

AI overwrites your entire file and accidentally deletes your custom logic.

</td>
<td valign="top">

AI checks dependencies, isolates the change, and guarantees no collateral damage before editing.

</td>
</tr>
</table>

#### ⚡️ `/coach-me`
*Sparring partner and root-cause behavioral coach.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI)</th>
<th width="50%">✅ After (With JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<b><i>AI:</i></b> "Here is a 30-day generic roadmap to stop procrastinating."

</td>
<td valign="top">

<b><i>AI:</i></b> "You're avoiding this task because you're afraid of looking stupid. Let's do the backend heavy-lifting right now so you have nothing to fear."

</td>
</tr>
</table>

## Installation

**For Mac/Linux Users (ติดตั้งแบบบรรทัดเดียวจบ):**
Open your terminal and run:
```bash
git clone https://github.com/theeranon/JamesSkills.git "$HOME/.james-skills"
"$HOME/.james-skills/scripts/install"
```
*This will safely link the skills to your local AI environments.*
*(คำสั่งนี้จะติดตั้งและผูกสกิลเข้ากับ Claude/Cursor ในเครื่องคุณให้แบบอัตโนมัติ)*

> **No terminal? No problem! (สำหรับคนไม่อยากลงโค้ด):**
> Simply browse the `skills/` folder in this repository, open the `SKILL.md` of the skill you want, and copy-paste the text into your ChatGPT's "Custom Instructions" or Claude's "Projects"!
> (ใครไม่อยากยุ่งกับ Terminal แค่กดเข้าไปดูในโฟลเดอร์ `skills/` ก๊อปปี้ข้อความในไฟล์ `SKILL.md` ไปแปะในแชท AI ก็ใช้งานได้เลยครับ!)

---

## Developers
*(The following sections are technical architecture notes for maintainers)*

```bash
git clone https://github.com/theeranon/JamesSkills.git "$HOME/.james-skills"
"$HOME/.james-skills/scripts/install"
"$HOME/.james-skills/scripts/doctor"
```

The installer links the canonical skills into the discovery directories available on the machine, including `~/.codex/skills`, `~/.agents/skills`, `~/.claude/skills`, and configured Gemini or Antigravity roots. It never overwrites a real directory or file; a legacy name collision fails visibly so an outdated duplicate cannot stay active unnoticed.
It also activates repository-owned `pre-commit` and `pre-push` gates. Every commit and push runs `scripts/validate` locally, without GitHub Actions or paid runners.

The tracked browser-render receipt is reproducible without PDF export:

```bash
npm ci
npm run qa:transformation
```

The QA command uses an installed Chrome or Chromium browser. Set `CHROME_PATH` only when it is not in a standard platform location.

## Update

```bash
"$HOME/.james-skills/scripts/update"
```

Update fetches a fast-forward candidate, validates it in a detached temporary worktree before moving the active checkout, then refreshes links. An invalid candidate cannot replace the working version. Skill behavior never silently changes in the background.

## Boundaries

- `catalog.json`: canonical package category, promotion state, and compatibility aliases
- `skills/core`: bounded reasoning and execution workflows
- `skills/modes`: persistent conversation behavior
- `skills/standards`: automatically applied James-wide output law
- `skills/outputs`: reusable recipient-facing artifact workflows
- `skills/internal`: routing and composition mechanics
- `packs`: optional brand or domain references with no live state or client data
- `adapters`: vendor-specific metadata only; never duplicate core instructions
- `tests`: structural and outcome regression gates
- `scripts`: idempotent install, update, validation, and diagnosis
- `.githooks`: free local validation before every commit and push

Private by default. Review every file before publishing any subset.

## Skill handbook

Open [`docs/SKILLS.md`](docs/SKILLS.md) to choose a skill by the moment you need it. The handbook covers every canonical package, slash command, lifecycle state, alias, bounded result, do-not-use case, and common composition in one place.

The short rule:

- use `/project-standard` to establish or repair project truth;
- use `/catchup` to return after a continuity gap;
- use `/give-me-solutions` to research choices and `/done-for-me` after the owner decides;
- use `/prove-it` before accepting a completion claim;
- use `/sum-meet`, `/one-page-pls`, or `/final-it` for recipient-facing outcomes; `make-it-james` and `make-it-james-ux` apply automatically.

This release has no pilot packages. Compatibility aliases keep older calls working without creating another instruction body. `skill-router` is installed internal support, not a recommended human command.

## Knowledge library

`baseon` owns the application workflow. Sources and lenses live separately under `packs/knowledge` so a new book does not create another skill or inflate `SKILL.md`.

```bash
python3 skills/core/baseon/scripts/knowledge_library.py list
python3 skills/core/baseon/scripts/knowledge_library.py validate
```

The first reviewed-private lenses are `wealth-dynamics` and `wealth-spectrum`. `talent-dynamics` resolves to the same Dynamics lens because it is the team adaptation of the same model. Wealth Spectrum remains a separate model with the same creator lineage. Their full source PDFs remain outside Git. Source cards keep version, rights posture, SHA-256 when applicable, and locators; lens files contain original paraphrase, applications, and limitations.

Direct calls are available as `/baseon`, `/wealth-dynamics`, `/talent-dynamics`, and `/wealth-spectrum`. The framework shortcuts only preselect a lens; they contain no duplicate knowledge or reasoning rules. `/think-with-this` remains a compatibility alias.

The transformation-design portfolio has three approved calls. `/build-framework` searches the house library before upgrading or creating reusable company IP. `/transformation-journey` owns macro organization transformation. `/learning-experience-design` owns a bounded learning intervention. TPS is one house framework available inside LED; it is not LED itself or the macro journey timeline.

The framework registry lives at `packs/frameworks/registry.json`. Lifecycle and source gaps remain visible so an agent cannot turn an incomplete internal model or one successful activity into approved company law.

Clone the full repository when moving machines. A detached copy of `baseon` alone intentionally has no duplicated knowledge library; set `JAMES_SKILLS_ROOT` to the full clone if a platform cannot use the installer links.

Skill names are phrases people naturally say when they need the capability. Workflow skills complete a bounded job; mode skills remain active for the conversation after one invocation.

## Candidate lifecycle

Discovery comes before packaging. A new skill remains a pilot until its Candidate Card shows repeated cross-project need, non-duplication, source confidence, representative failures, legitimate counter-cases, and James approves the exact name and scope. General permission to improve this repository does not approve a candidate's name or ontology.

The current cross-history portfolio audit selected and promoted `catchup` after clean, dirty, stale-status, scoped-workstream, Git-error, and already-clear forward tests. `learn-this`, `audit-this`, and `systemize-it` remain Candidate Cards, not installed skills. See `research/2026-08-29-skill-portfolio-audit.md`.
