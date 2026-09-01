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

## Full Skill Directory

### Context & Setup (การเริ่มต้นและรวบรวมบริบท)

#### ⚡️ `/project-standard`
*Create or repair project truth (SRS, NFR, Permissions).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>Sure! I've updated the code for your dashboard. Here is the React component...</blockquote>

</td>
<td valign="top">

<blockquote>Generated <code>SRS.html</code> and updated <code>PROJECT.md</code>. The permission matrix is now documented. Proceeding to update the React component.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/catchup`
*Reconstruct current state after a continuity gap.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>What would you like me to do today? Please provide the code or explain where we left off.</blockquote>

</td>
<td valign="top">

<blockquote>Read <code>STATUS.md</code>. The last task was fixing the auth middleware. I've located the failing test in <code>src/auth.spec.ts</code>. Ready to patch it.</blockquote>

</td>
</tr>
</table>

### Analyze & Decide (การวิเคราะห์และตัดสินใจ)

#### ⚡️ `/zoom-out`
*Reframe the problem at the system level before patching symptoms.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>Here is the CSS to hide the overlapping error button:<br><code>display: none;</code></blockquote>

</td>
<td valign="top">

<blockquote>Wait. Hiding the button patches a symptom. The root cause is the duplicate API call in <code>UserContext</code> causing a race condition. Let's fix the data flow instead.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/give-me-solutions`
*Research external options and present objective tradeoffs.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>You should use Next.js! It's very popular, has great SEO, and is easy to learn.</blockquote>

</td>
<td valign="top">

<blockquote><table><tr><th>Framework</th><th>Cost</th><th>Verdict</th></tr><tr><td>Next.js</td><td>High</td><td>Best for SEO</td></tr><tr><td>Vite</td><td>Low</td><td>Best for Admin UI</td></tr></table><br><i>*Does not make the final choice for you.</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/baseon`
*Apply a named knowledge lens (e.g., Wealth Dynamics).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>To improve your team, you should communicate better and hold more weekly meetings.</blockquote>

</td>
<td valign="top">

<blockquote>As a <b>Creator</b> profile, your bottleneck is operations. Delegate the system-building to a <b>Mechanic</b> so you can stay in your flow state.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/grill-me`
*Interactive stress-test to expose flaws in your plan.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>That's a brilliant business idea! Let's start coding it right away. What is the first feature?</blockquote>

</td>
<td valign="top">

<blockquote>If user retention drops by 20%, what is your fallback for monetization?<br><br><i>(Waiting for your response before proceeding)</i></blockquote>

</td>
</tr>
</table>

### Execute & Verify (การลงมือทำและตรวจสอบ)

#### ⚡️ `/done-for-me`
*End-to-end authorized implementation without waiting for permission.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>I wrote the first function. Let me know if you want me to write the tests next!</blockquote>

</td>
<td valign="top">

<blockquote>Implemented the function, updated the tests, and verified the build passes. The feature is complete and ready to use.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/prove-it`
*Verify completion claim at the boundary.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>I fixed the bug. The code looks correct and it should work now!</blockquote>

</td>
<td valign="top">

<blockquote>Run <code>npm test -- auth.spec.ts</code> ➔ <b>PASS</b>. The bug is verified fixed.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/never-again`
*Convert a rejected result into a permanent regression guard.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>Sorry about that! I will remember to use UTC next time.<br><i>(Proceeds to forget it next time)</i></blockquote>

</td>
<td valign="top">

<blockquote>Added rule to <code>DECISIONS.md</code>: <i>'All timestamps must be stored in UTC'</i>. This is now a permanent constraint for this project.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/is-that-the-best-you-can-do`
*Force the AI to aggressively self-critique and rewrite to the absolute limit.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>In today's fast-paced digital world, leveraging AI is key to success...</blockquote>

</td>
<td valign="top">

<blockquote><ul><li><b>Weakness:</b> The previous draft used generic buzzwords.</li><li><b>Rewrite:</b> Here is the specific, data-backed strategy for your Q3 integration...</li></ul></blockquote>

</td>
</tr>
</table>

### Outputs & Deliverables (การสร้างผลลัพธ์สุดท้าย)

#### ⚡️ `/sum-meet`
*Source-faithful meeting record with complete agenda and actions.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote><ul><li>Discussed the new UI.</li><li>Bob will do the design.</li><li>Meeting ended at 3 PM.</li></ul></blockquote>

</td>
<td valign="top">

<blockquote><b>Decision:</b> Move to Tailwind CSS.<br><b>Action:</b> @Bob to deliver Figma mockups by Friday.<br><br><i>(Complete A4 HTML record generated)</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/one-page-pls`
*Self-contained executive brief.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote><i>(A massive 10-page wall of text summarizing everything said in a 2-hour meeting)</i></blockquote>

</td>
<td valign="top">

<blockquote><i>(A dense, highly structured 1-page executive brief containing only the core decisions and financial impact)</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/final-it`
*Select and finish recipient-ready artifact.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>Sure! Here is the email you requested:<br><br>Subject: Update<br>Hello...</blockquote>

</td>
<td valign="top">

<blockquote>Subject: Q3 System Update<br><br>Team,<br><br>The new deployment pipeline is live...</blockquote>

</td>
</tr>
</table>

### Persistent Behaviors (กฎประจำตัวของ AI)

#### ⚡️ `/i-have-adhd`
*Concise, direct, low-friction communication mode.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>HTML stands for HyperText Markup Language. To center a div, you can use flexbox, which is a layout model...</blockquote>

</td>
<td valign="top">

<blockquote>Add <code>className="flex items-center justify-center"</code> to the parent div.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/make-it-james`
*Strict recipient-facing wording standard (No AI Theatre).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>As an AI, I suggest we might want to consider perhaps optimizing the database if possible.</blockquote>

</td>
<td valign="top">

<blockquote>The database is the bottleneck. Optimize the schema before adding new features.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/make-it-james-ux`
*Visual and UI standards (IBM Plex Thai, modern layouts).*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote><i>(An ugly HTML table with default Times New Roman font and zero padding)</i></blockquote>

</td>
<td valign="top">

<blockquote><i>(A modern, responsive HTML component using IBM Plex Sans Thai with proper whitespace and contrast)</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/proactive-habits`
*Prevent passive subordinate waiting behavior.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>I have updated the file. What should I do next?</blockquote>

</td>
<td valign="top">

<blockquote>Updated <code>src/api.ts</code>. The next logical step is to update the frontend types. I'll do that now.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/proactive-dev`
*Enforce blast-radius checks before mutating code.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote><i>(Overwrites the entire file, accidentally deleting your custom logic)</i></blockquote>

</td>
<td valign="top">

<blockquote>Checked dependencies. Modifying <code>auth.ts</code> will break <code>user.spec.ts</code>. I will update both files simultaneously to prevent a broken build.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/coach-me`
*Sparring partner and root-cause behavioral coach.*

<table>
<tr>
<th width="50%">❌ Before (Normal AI Output)</th>
<th width="50%">✅ After (JamesSkills Output)</th>
</tr>
<tr>
<td valign="top">

<blockquote>Here are 5 tips to stop procrastinating: 1. Use the Pomodoro technique...</blockquote>

</td>
<td valign="top">

<blockquote>You're avoiding this task because you're afraid of looking disorganized. Let's do the backend heavy-lifting right now so you have nothing to fear.</blockquote>

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
