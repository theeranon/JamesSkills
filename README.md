# JamesSkills

> **Production-grade agentic workflows and execution laws for Claude Code, Cursor, Antigravity, and Gemini.**

[![Canonical Skills](https://img.shields.io/badge/Canonical%20Skills-21-blue.svg)](catalog.json)
[![Local Test Gates](https://img.shields.io/badge/Local%20Gates-100%25%20Passing-success.svg)](scripts/validate)
[![Standard](https://img.shields.io/badge/Standard-ai--context%20v2-orange.svg)](ai-context/PROJECT.md)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 💡 Why JamesSkills?

Most AI tools treat large language models like polite chat assistants: they ask for permission after every single file edit, hallucinate dependencies, sugarcoat flawed ideas, and litter codebases with dead temporary code.

**JamesSkills turns AI into an autonomous, high-agency operator.**  
Every skill in this repository is an executable workflow grounded in five iron principles:

1. **Zero AI Theater:** No flattering conversational residue, robotic apologies, or filler intros. Output goes directly to recipient-ready deliverables.
2. **Autonomous Execution (`/done-for-me`):** Executes multi-step implementations end-to-end through verified completion without pausing for trivial micro-approvals.
3. **Ruthless Quality Gates (`/are-you-sure`, `/prove-it`):** Evaluates work across a 5-layer OCD framework to eradicate hardcodes, broken layouts, and legacy junk before declaring victory.
4. **Root-Cause Problem Solving (`/zoom-out`):** Forces the model to step back and reframe architectural and business constraints before touching symptoms.
5. **Bilingual Operator Reality:** Speaks both English and Thai with field-tested business, financial, and engineering rigor.

---

## ⚡️ 60-Second Quickstart

### Terminal Users (Claude Code, Cursor, Codex, Antigravity)
Install and link all canonical skills directly into your local agent discovery directories with one idempotent command:

```bash
git clone https://github.com/theeranon/JamesSkills.git "$HOME/.james-skills"
"$HOME/.james-skills/scripts/install"
```

*The installer links skills into `~/.claude/skills`, `~/.codex/skills`, `~/.agents/skills`, and configured Gemini/Antigravity roots while configuring zero-cost local pre-commit and pre-push test gates.*

### Zero-Terminal Users (ChatGPT Web & Claude Projects)
Browse the [`skills/`](skills/) folder, open the `SKILL.md` file of any workflow, and copy-paste its instructions directly into your Claude Project knowledge or ChatGPT Custom Instructions.

---

## 🌟 Iconic Showcase (Before vs. After)

### 🎯 `/grill-me` (Interactive Plan Stress-Test)
*Challenges your strategy, exposing blind spots and resolving critical dependencies before building.*

<table width="100%">
<tr>
<th width="50%">❌ Standard AI Behavior</th>
<th width="50%">✅ JamesSkills Outcome</th>
</tr>
<tr>
<td valign="top">

"Opening a premium specialty matcha bar in Thong Lo sounds like a wonderful and profitable venture! Thong Lo has high purchasing power and loves Japanese culture. Here is a 5-step marketing plan to launch your cafe..."<br><br>
<i>(AI เอาใจผู้ใช้ เออออห่อหมก และกระโดดเขียนแผนธุรกิจโดยไม่สนต้นทุนจริง)</i>

</td>
<td valign="top">

<b>[Stress Test: Question 1 of 3]</b><br><br>
"Prime retail rent in Thong Lo averages 180,000 THB/month. At an 80 THB gross margin per cup, your breakeven volume is 75 cups/day before labor, electricity, or marketing.<br><br>
<b>What is your proven unfair distribution advantage to secure that foot traffic on Day 1 against the 4 existing matcha bars within 500 meters?</b>"<br><br>
<i>(ต้อนถามจุดบอดทีละข้อ บังคับให้ตอบตัวเลขจริงก่อนเริ่มลงมือ)</i>

</td>
</tr>
</table>

<br>

### 🛡 `/are-you-sure` (The Zero-Tolerance OCD QA)
*Runs a 5-layer audit (Integrity, Anti-Laziness, Hygiene, OCD UX, Longevity) to eliminate sloppy shortcuts.*

<table width="100%">
<tr>
<th width="50%">❌ Standard AI Behavior</th>
<th width="50%">✅ JamesSkills Outcome</th>
</tr>
<tr>
<td valign="top">

"I have finished building the user profile page! All unit tests are passing and the layout looks great. Let me know what you'd like me to build next!"<br><br>
<i>(AI อ้างว่างงานเสร็จ แต่ทิ้ง Hardcoded strings, ปล่อย CSS margin เบี้ยว 2px, และทิ้งไฟล์ <code>temp_test.js</code> ค้างไว้ใน repo)</i>

</td>
<td valign="top">

<b>[OCD QA 5-Layer Audit & Auto-Remediation]</b><br><br>
• <b>Layer 1 (Integrity):</b> Patched missing JWT token expiration boundary in auth middleware.<br>
• <b>Layer 2 (Anti-Laziness):</b> Extracted hardcoded hex colors (`#333`) into CSS custom variables.<br>
• <b>Layer 3 (Hygiene):</b> Purged orphaned <code>temp_auth.ts</code> and cleaned dangling <code>console.log</code> calls.<br>
• <b>Layer 4 (Sensory UX):</b> Realigned misaligned flexbox icon padding (2px jump on hover fixed).<br>
• <b>Layer 5 (Longevity):</b> Documented session invalidation contract in <code>ai-context/DECISIONS.md</code>.<br><br>
<i>"Every defect caught has been autonomously repaired. Zero technical debt remains. Work is genuinely complete."</i>

</td>
</tr>
</table>

<br>

### 💡 `/give-me-solutions` (Objective Trade-off Matrix)
*Researches external tools and presents evidence matrices without usurping the user's executive decision.*

<table width="100%">
<tr>
<th width="50%">❌ Standard AI Behavior</th>
<th width="50%">✅ JamesSkills Outcome</th>
</tr>
<tr>
<td valign="top">

"You should definitely use HubSpot CRM! It is the market leader, very user-friendly, and has great marketing automation. Everyone loves it, so it's the right choice for your business."<br><br>
<i>(AI ตัดสินใจแทนผู้ใช้ แนะนำแอปตามกระแสโดยไม่เช็คงบประมาณหรือข้อจำกัดของทีม)</i>

</td>
<td valign="top">

<b>[Decision Matrix: CRM Options (Constraint: &lt; 20 seats, Budget $3,000/yr)]</b><br><br>
<table>
<tr><th>Option</th><th>Est. Cost</th><th>Pros & Tradeoffs</th></tr>
<tr><td><b>Pipedrive</b> <i>(Front-runner)</i></td><td>$3,360/yr</td><td>Focused sales pipeline, fast onboarding; lacks native email marketing.</td></tr>
<tr><td><b>HubSpot Pro</b></td><td>$10,800/yr</td><td>Industry standard ecosystem; exceeds current budget constraint by 3.6x.</td></tr>
<tr><td><b>Zoho CRM</b></td><td>$2,400/yr</td><td>Within budget, extensive feature set; steeper learning curve for team.</td></tr>
</table><br>
<i>*ทางเลือกสุดท้ายขึ้นอยู่กับคุณ — แจ้งหมายเลขที่ต้องการเพื่อเริ่มคอนฟิก</i>

</td>
</tr>
</table>

<br>

### 🎨 `/make-it-james-ux` (Visual Standards & UX Law)
*Enforces strict aesthetic standards: IBM Plex Sans Thai typography, restrained contrast, and zero AI dashboard clutter.*

<table width="100%">
<tr>
<th width="50%">❌ Standard AI Behavior</th>
<th width="50%">✅ JamesSkills Outcome</th>
</tr>
<tr>
<td valign="top">

<i>Generates generic, spacious AI dashboard templates with oversized cards, random neon gradients, heavy borders, and unreadable default system fonts.</i>

</td>
<td valign="top">

<img src="assets/ux-preview.png" alt="JamesSkills UX Preview" width="100%" style="border-radius: 8px; border: 1px solid #e2e8f0;"><br><br>
<i>Compact density, zero-waste layout, pixel-perfect alignment, and native <code>IBM Plex Sans Thai</code> font integration.</i>

</td>
</tr>
</table>

---

## 📚 Full Skill Directory (21 Canonical Skills)

Open [`docs/SKILLS.md`](docs/SKILLS.md) for detailed lifecycles, composition patterns, and trigger conditions for each skill.

| Command | Category | Purpose & Description (English & Thai) | Handbook |
|:---|:---|:---|:---:|
| **`/done-for-me`** | `core` | Autonomous end-to-end execution through verified completion without pausing for micromanagement.<br>*(สั่งทำงานชิ้นใหญ่ให้จบครบม้วนเดียวโดยไม่ต้องรอคอนเฟิร์มขั้นตอนย่อย)* | [`SKILL.md`](skills/core/done-for-me/SKILL.md) |
| **`/give-me-solutions`** | `core` | Researches external options, presents objective trade-offs and cost matrices without making the final choice.<br>*(วิเคราะห์เปรียบเทียบข้อดีข้อเสียของทางเลือกต่างๆ พร้อมตารางประกอบการตัดสินใจ)* | [`SKILL.md`](skills/core/give-me-solutions/SKILL.md) |
| **`/baseon`** | `core` | Applies named business frameworks (Wealth Dynamics, Talent Dynamics, Wealth Spectrum) with strict epistemic separation.<br>*(วิเคราะห์โจทย์ธุรกิจผ่านเลนส์กรอบความคิดระดับสากลอย่างเป็นระบบ)* | [`SKILL.md`](skills/core/baseon/SKILL.md) |
| **`/never-again`** | `core` | Converts a rejected output into a permanent regression guard and durable system rule.<br>*(เปลี่ยนความผิดพลาดให้กลายเป็นกฎเหล็กถาวร เพื่อไม่ให้ AI ทำผิดซ้ำเดิมอีก)* | [`SKILL.md`](skills/core/never-again/SKILL.md) |
| **`/prove-it`** | `core` | Verifies completion claims against objective boundaries and real execution receipts.<br>*(ตรวจสอบหลักฐานการทำงานจริงก่อนอนุมัติว่างานเสร็จสิ้น ไม่รับคำอ้างลอยๆ)* | [`SKILL.md`](skills/core/prove-it/SKILL.md) |
| **`/zoom-out`** | `core` | Reframes problems at the system and outcome level before picking tools or patching symptoms.<br>*(ถอยมามองภาพรวมระดับโครงสร้าง เพื่อแก้ปัญหาที่ต้นตอจริงไม่ใช่แก้ที่ปลายเหตุ)* | [`SKILL.md`](skills/core/zoom-out/SKILL.md) |
| **`/catchup`** | `core` | Reconstructs verified project state after a context wipe, continuity gap, or agent handoff.<br>*(กู้คืนบริบทและสถานะล่าสุดของโปรเจกต์อย่างแม่นยำหลังเปลี่ยนหน้าแชท)* | [`SKILL.md`](skills/core/catchup/SKILL.md) |
| **`/grill-me`** | `core` | Interactive stress-test that grills your plan with sequential, high-impact questions.<br>*(ซักฟอกและท้าทายแผนงานเพื่ออุดรอยรั่วและขจัดข้อสมมติฐานที่ผิดพลาด)* | [`SKILL.md`](skills/core/grill-me/SKILL.md) |
| **`/is-that-the-best-you-can-do`** | `core` | Forces the AI to aggressively self-critique and rewrite draft outputs to their absolute limit.<br>*(รีดประสิทธิภาพงานเขียนและโค้ดให้เฉียบคมที่สุด ฉีกกรอบคำตอบระดับมาตรฐาน)* | [`SKILL.md`](skills/core/is-that-the-best-you-can-do/SKILL.md) |
| **`/are-you-sure`** | `core` | 5-layer zero-tolerance OCD quality gate that purges hardcodes, visual bugs, and technical debt.<br>*(มือปราบความมักง่าย สแกนและซ่อมแซมจุดบกพร่องทั้ง 5 ชั้นอย่างละเอียดกริบ)* | [`SKILL.md`](skills/core/are-you-sure/SKILL.md) |
| **`/i-have-adhd`** | `modes` | Persistent concise communication mode that batches interruptions and presents clear choices.<br>*(โหมดสื่อสารกระชับ ตรงประเด็น เห็นความคืบหน้าชัดเจน ไม่เวิ่นเว้อ)* | [`SKILL.md`](skills/modes/i-have-adhd/SKILL.md) |
| **`/proactive-habits`** | `modes` | Enforces proactive partnership mode: bans passive waiting, excuses, and conversational recaps.<br>*(โหมดผู้ช่วยเชิงรุก ลงมือแก้ปัญหาทันที ไม่ทำตัวเป็นผู้ตามที่คอยแต่รับคำสั่ง)* | [`SKILL.md`](skills/modes/proactive-habits/SKILL.md) |
| **`/coach-me`** | `modes` | Sparring partner and root-cause behavioral coach that unblocks procrastination while executing backend work.<br>*(โค้ชทลายจุดติดขัดทางจิตวิทยาและการผัดวันประกันพรุ่ง พร้อมลุยงานหลังบ้าน)* | [`SKILL.md`](skills/modes/coach-me/SKILL.md) |
| **`/final-it`** | `outputs` | Formats and finishes requested work into recipient-ready HTML, Markdown, or clean documents.<br>*(ปรับแต่งผลลัพธ์สุดท้ายให้อยู่ในฟอร์แมตที่พร้อมส่งมอบให้ผู้รับทันที)* | [`SKILL.md`](skills/outputs/final-it/SKILL.md) |
| **`/sum-meet`** | `outputs` | Transforms transcripts or notes into complete, source-faithful, print-ready A4 meeting records.<br>*(จัดทำรายงานบันทึกการประชุมฉบับสมบูรณ์พร้อมพิมพ์ แยกวาระและมติชัดเจน)* | [`SKILL.md`](skills/outputs/sum-meet/SKILL.md) |
| **`/one-page-pls`** | `outputs` | Synthesizes complex source material into one self-contained executive brief per topic.<br>*(สรุปเนื้อหาสำคัญให้อยู่ในกระดาษหน้าเดียวแบบ One-Pager สำหรับผู้บริหาร)* | [`SKILL.md`](skills/outputs/one-page-pls/SKILL.md) |
| **`/make-it-james`** | `standards` | Enforces James's Final Word law: natural Thai/English phrasing, zero AI fluff, and direct operator tone.<br>*(ขัดเกลาสำนวนภาษาให้เป็นธรรมชาติแบบมืออาชีพ ตัดคำฟุ่มเฟือยของ AI ทิ้งทั้งหมด)* | [`SKILL.md`](skills/standards/make-it-james/SKILL.md) |
| **`/make-it-james-ux`** | `standards` | Applies strict UX/UI standards: IBM Plex Sans Thai typography, restrained contrast, and compact density.<br>*(ควบคุมมาตรฐานความสวยงามของ UI ให้เป็นระเบียบ สะอาดตา และอ่านง่าย)* | [`SKILL.md`](skills/standards/make-it-james-ux/SKILL.md) |
| **`/project-standard`** | `standards` | Bootstraps and repairs single-source-of-truth project contracts (`ai-context/`, SRS, NFRs, permissions).<br>*(วางโครงสร้างเอกสารโครงการและข้อกำหนดทางเทคนิคให้เป็นมาตรฐานสากล)* | [`SKILL.md`](skills/standards/project-standard/SKILL.md) |
| **`/proactive-dev`** | `standards` | Mandates blast-radius safety checks and architecture verification before any code mutation.<br>*(ตรวจสอบผลกระทบลูกโซ่ก่อนแก้โค้ด ป้องกันระบบพังจากความมักง่าย)* | [`SKILL.md`](skills/standards/proactive-dev/SKILL.md) |
| **`skill-router`** | `internal` | Deterministic internal routing matrix that assigns single-workflow ownership to complex requests.<br>*(ระบบประมวลผลภายในสำหรับจัดสรรคำสั่งไปยังสกิลที่รับผิดชอบโดยตรง)* | [`SKILL.md`](skills/internal/skill-router/SKILL.md) |

---

## 🏗 System Architecture & Boundaries

```
JamesSkills/
├── ai-context/        # Project truth, SRS spec, and architecture decision records (ADRs)
├── catalog.json       # Authoritative canonical skill index and lifecycle status
├── skills/            # Canonical skill instruction packages (SKILL.md)
│   ├── core/          # Bounded reasoning and execution workflows
│   ├── modes/         # Persistent conversational behaviors
│   ├── outputs/       # Recipient-facing deliverable formatters
│   ├── standards/     # Automatically enforced quality and engineering laws
│   └── internal/      # Dispatch routing matrices
├── docs/SKILLS.md     # Full human navigation handbook
├── scripts/           # Idempotent install, update, validate, and doctor tools
└── tests/             # Structural, regression, and behavioral verification suites
```

- **Progressive Disclosure:** Skills are not dumped into system prompts all at once. Agents discover and load only the specific `SKILL.md` needed for the task, keeping context windows lean.
- **Local Git Test Gates:** Every commit and push runs `scripts/validate` locally (zero paid cloud runners required). Commits are rejected if skills mismatch the catalog, contracts fail, or repository boundaries are breached.
- **Safe Fast-Forward Updates:** `scripts/update` verifies candidate trees in a detached temporary workspace before touching your active installation.

---

## 📖 Complete Documentation

Read the full handbook at [`docs/SKILLS.md`](docs/SKILLS.md) for deep dives into lifecycle management, compatibility aliases, and multi-skill composition patterns.
