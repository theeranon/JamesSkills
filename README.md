# JamesSkills

Canonical workflows and prompts for AI collaboration. Designed for Claude, ChatGPT, Cursor, and Gemini.

## 🚀 Highlights

### 🎯 `/grill-me` (Interactive Stress-Test)
- **EN:** Challenge an idea. The AI asks sequential questions to expose flaws and resolve dependencies before execution.
- **TH:** สั่งให้ AI ต้อนและซักถามจุดอ่อนในแผนงานทีละข้อ เพื่ออุดรอยรั่วก่อนลงมือทำ

### 💡 `/give-me-solutions` (Options & Trade-offs)
- **EN:** Research external options. Present tradeoffs without making the final choice.
- **TH:** วิเคราะห์และเปรียบเทียบข้อดีข้อเสียของแต่ละทางเลือก เพื่อประกอบการตัดสินใจ

### 🔍 `/zoom-out` (System-Level Problem Solver)
- **EN:** Reframe a problem at the system level before patching symptoms.
- **TH:** ถอยมามองภาพรวม เพื่อหาต้นตอของปัญหาระดับโครงสร้าง

### 📝 `/one-page-pls` (Executive One-Pager)
- **EN:** Turn source material into one self-contained executive page per topic.
- **TH:** สรุปเนื้อหาทั้งหมดให้อยู่ในหน้าเดียวแบบ One-Pager แยกตามวาระการประชุม

---

## 📚 Full Skill Directory (Before vs After)

### Context & Setup (การเริ่มต้นและรวบรวมบริบท)

#### ⚡️ `/project-standard`
*Create or repair project truth (SRS, NFR, Permissions).*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Of course! I'd love to help you build a new Marketing Dashboard. First, we should probably set up a React project. You can do that by running `npx create-react-app`. After that, we need to think about the design. Should we use Tailwind CSS? Also, for the database, maybe we can use Firebase...<br><br><i>(AI starts coding or guessing tools blindly without setting business rules, permissions, or requirements.)</i>

</td>
<td valign="top">

<b>[Generated <code>PROJECT.md</code> and <code>SRS.html</code>]</b><br><br>• <b>Business Goal:</b> Reduce ad-spend reporting time by 50%.<br>• <b>Permission Matrix:</b> Admins can edit, Viewers are read-only.<br>• <b>NFR:</b> Must load under 2 seconds.<br><br><i>All constraints are documented. Ready for execution.</i>

</td>
</tr>
</table>

<br>

#### ⚡️ `/catchup`
*Reconstruct current state after a continuity gap.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Hello! I am ready to help you today. Could you please remind me what we were working on yesterday? If you have any code snippets, meeting notes, or specific instructions, please paste them here so I can get up to speed!

</td>
<td valign="top">

<b>[Scanned <code>STATUS.md</code> and recent commits]</b><br><br>You left off at drafting the Q3 Investor Update email. The financial projections for Q4 were missing from the draft. I have loaded the latest Excel sheet. Shall I generate the missing paragraph?

</td>
</tr>
</table>

<br>

### Analyze & Decide (การวิเคราะห์และตัดสินใจ)

#### ⚡️ `/zoom-out`
*Reframe the problem at the system level before patching symptoms.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Great question! To fix the issue where your employees are clocking in late, you can implement a strict penalty system. Here is a template for a warning letter you can print out and make them sign: 'Dear [Employee Name], this is an official warning...'

</td>
<td valign="top">

<b>Wait.</b> Issuing warning letters patches a symptom. <br><br>The root cause is structural: your Sales team's incentive structure is tied solely to closed deals, not office hours. Before writing warning letters, let's realign their KPIs or switch them to a flexible schedule.

</td>
</tr>
</table>

<br>

#### ⚡️ `/give-me-solutions`
*Research external options and present objective tradeoffs.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Based on your needs for a CRM, I highly recommend HubSpot! It is an industry leader, very user-friendly, and has a great free tier. Many businesses love it, and it integrates well with almost everything. You should definitely go with HubSpot.

</td>
<td valign="top">

<b>Decision Matrix (Constraint: < 50-person team, B2B SaaS)</b><br><br><table><tr><th>Option</th><th>Annual Cost</th><th>Pros/Cons</th></tr><tr><td>HubSpot</td><td>$10,000+</td><td>Best ecosystem / High cost at scale</td></tr><tr><td>Pipedrive</td><td>$3,000</td><td>Great for sales / Weak marketing tools</td></tr></table><br><i>*I do not make the final choice. Please select the path.</i>

</td>
</tr>
</table>

<br>

#### ⚡️ `/baseon`
*Apply a named knowledge lens (e.g., Wealth Dynamics).*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

To scale your business, you need to communicate better with your co-founder. Make sure to hold weekly sync meetings, set clear OKRs, and foster a culture of transparency and continuous feedback.

</td>
<td valign="top">

<b>Lens Applied: Wealth Dynamics</b><br><br>You are a <b>Creator</b>. Your co-founder is a <b>Lord</b>. The friction isn't 'communication'—it's mechanics. You need a <b>Mechanic</b> in the middle to translate your big-picture ideas into the analytical systems your co-founder needs.

</td>
</tr>
</table>

<br>

#### ⚡️ `/grill-me`
*Interactive stress-test to expose flaws in your plan.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Opening a new coffee shop in Thong Lo sounds like an amazing and highly profitable idea! Thong Lo has great foot traffic and high purchasing power. Let me help you write a business plan and a menu right away!

</td>
<td valign="top">

<b>Stress Test: Q1</b><br><br>Commercial rents in Thong Lo average 150k THB/month. To maintain a 20% margin, you need to sell 300 cups a day. If a new competitor opens next door, what is your unfair advantage to retain foot traffic?<br><br><i>(Waiting for your response before proceeding to Q2)</i>

</td>
</tr>
</table>

<br>

### Execute & Verify (การลงมือทำและตรวจสอบ)

#### ⚡️ `/done-for-me`
*End-to-end authorized implementation without waiting for permission.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

I have drafted the first slide for your pitch deck regarding the market size. Would you like me to continue and draft the second slide about the business model? Let me know if you need any adjustments!

</td>
<td valign="top">

<b>[Execution Complete]</b><br><br>1. Drafted all 12 slides of the Pitch Deck.<br>2. Formatted the financial projections into a markdown table.<br>3. Wrote the speaker notes for each slide.<br><br><i>The artifact is ready for delivery.</i>

</td>
</tr>
</table>

<br>

#### ⚡️ `/prove-it`
*Verify completion claim at the boundary.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

I have updated the Excel formula for the commission calculation. It should now correctly handle the tiered percentages. You can copy and paste it into your sheet. Let me know if it works!

</td>
<td valign="top">

<b>[Verification Passed]</b><br><br>Tested against 3 edge cases:<br>• Sales = $5k ➔ Commission: $500 (10%)<br>• Sales = $15k ➔ Commission: $2,250 (15%)<br>• Sales = $50k ➔ Commission: $10,000 (20%)<br><br><i>Math is verified correct.</i>

</td>
</tr>
</table>

<br>

#### ⚡️ `/never-again`
*Convert a rejected result into a permanent regression guard.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

I apologize profusely for using the term 'Dear Valued Customer' again. You are right, it sounds very corporate and robotic. I will make sure to remember to use 'Hi [Name]' in all future interactions!

</td>
<td valign="top">

<b>[System Rule Updated]</b><br><br>Appended to <code>DECISIONS.md</code>:<br><i>'Forbidden word constraint: Never use "Dear Valued Customer". Always default to "Hi [First Name]".'</i><br><br>This regression guard is now permanent for all agents.

</td>
</tr>
</table>

<br>

#### ⚡️ `/is-that-the-best-you-can-do`
*Force the AI to aggressively self-critique and rewrite to the absolute limit.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

In today's fast-paced digital era, leveraging artificial intelligence is absolutely crucial for modern businesses aiming to stay ahead of the curve and maximize their operational efficiency...

</td>
<td valign="top">

<b>[Self-Critique & Rewrite]</b><br>• <b>Weakness:</b> The previous draft relied on generic, meaningless buzzwords.<br>• <b>Elevated Rewrite:</b> <i>"Automating your Level 1 Customer Support via AI will cut SLA response times from 4 hours to 3 seconds, saving $40k annually in headcount scale."</i>

</td>
</tr>
</table>

<br>

### Outputs & Deliverables (การสร้างผลลัพธ์สุดท้าย)

#### ⚡️ `/sum-meet`
*Source-faithful meeting record with complete agenda and actions.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Here is the summary of your meeting:<br>- We talked about the Q3 budget.<br>- The marketing team needs to spend less on ads.<br>- Sarah will send the report later.<br>- Meeting adjourned at 4:00 PM.

</td>
<td valign="top">

<b>[Meeting Record: Executive Summary]</b><br><br><b>Decision:</b> Q3 Ad Spend capped at 500k THB. Reallocating 200k THB to SEO.<br><b>Action:</b> @Sarah to deliver revised SEO media plan by Friday EOD.<br><br><i>(Full HTML A4 transcript generated)</i>

</td>
</tr>
</table>

<br>

#### ⚡️ `/one-page-pls`
*Self-contained executive brief.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

<i>(A massive 15-page wall of text summarizing every single word, joke, and tangent spoken during a 3-hour strategic planning workshop.)</i>

</td>
<td valign="top">

<i>(A highly structured 1-page executive brief containing only the Core Decisions, Financial Impact, Risk Matrix, and Next Steps. Ready for CEO sign-off.)</i>

</td>
</tr>
</table>

<br>

#### ⚡️ `/final-it`
*Select and finish recipient-ready artifact.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Certainly! I'd be happy to help you draft that email to your investors. Here is the text you requested:<br><br>Subject: Q3 Update...<br><br>I hope this helps! Please let me know if you need any revisions.

</td>
<td valign="top">

Subject: Q3 Revenue Update & Q4 Projections

Investors,

We closed Q3 at $1.2M ARR (20% QoQ growth)...

</td>
</tr>
</table>

<br>

### Persistent Behaviors (กฎประจำตัวของ AI)

#### ⚡️ `/i-have-adhd`
*Concise, direct, low-friction communication mode.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

The VLOOKUP function in Excel stands for 'Vertical Lookup'. It is a very powerful tool used to search for a certain value in a column in order to return a value from a different column in the same row. To use it, you...

</td>
<td valign="top">

`=VLOOKUP(A2, Sheet2!A:C, 3, FALSE)`

</td>
</tr>
</table>

<br>

#### ⚡️ `/make-it-james`
*Strict recipient-facing wording standard (No AI Theatre).*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

As an AI language model, I suggest that we might want to carefully consider optimizing the onboarding process, as it could potentially lead to better retention rates.

</td>
<td valign="top">

User drop-off is highest at Day 1. Simplify the onboarding flow to 3 steps to fix retention.

</td>
</tr>
</table>

<br>

#### ⚡️ `/make-it-james-ux`
*Visual and UI standards (IBM Plex Thai, modern layouts).*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

<i>(An ugly HTML table with default Times New Roman font, rigid borders, and zero padding.)</i>

</td>
<td valign="top">

<i>(A responsive, modern UI component using IBM Plex Sans Thai, soft shadows, rounded borders, and perfectly balanced whitespace.)</i><br><br><img src='https://raw.githubusercontent.com/theeranon/JamesSkills/main/assets/make-it-james-ux-preview.png' alt='UI Example' width='100%' style='border-radius: 8px; border: 1px solid #e2e8f0;'>

</td>
</tr>
</table>

<br>

#### ⚡️ `/proactive-habits`
*Prevent passive subordinate waiting behavior.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

I have finished analyzing the competitor's pricing model. What would you like me to do next?

</td>
<td valign="top">

Competitor pricing analyzed. I noticed their premium tier lacks API access. I have preemptively drafted a new landing page copy highlighting our open API as a competitive advantage. Review it below.

</td>
</tr>
</table>

<br>

#### ⚡️ `/proactive-dev`
*Enforce blast-radius checks before mutating code.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

<i>(AI overwrites your core `auth.ts` file without checking dependencies, breaking the entire login flow and crashing the app.)</i>

</td>
<td valign="top">

<b>[Blast-Radius Check]</b><br>Modifying `auth.ts` will break 3 downstream services (`billing`, `profile`, `api_keys`). I will execute the refactor across all 4 files simultaneously to maintain a green build.

</td>
</tr>
</table>

<br>

#### ⚡️ `/coach-me`
*Sparring partner and root-cause behavioral coach.*

<table width="100%">
<tr>
<th width="50%">❌ Before (AI วิ่งเล่นทุ่งลาเวนเดอร์)</th>
<th width="50%">✅ After (JamesSkills Outcome)</th>
</tr>
<tr>
<td valign="top">

Here are 5 generic tips to stop procrastinating: 1. Use the Pomodoro technique. 2. Break tasks into smaller steps. 3. Remove distractions. 4. Drink water. 5. Get enough sleep.

</td>
<td valign="top">

You are not 'too busy'—you are avoiding this launch because you fear public criticism. I am doing the backend heavy-lifting right now. I've deployed the staging server. You have no excuses left. Press launch.

</td>
</tr>
</table>

<br>

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
