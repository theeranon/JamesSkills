
# 🚀 JamesSkills (AI Hero Edition)

Welcome to **JamesSkills**! A curated collection of powerful, production-ready AI skills and prompts used by James Theeranon. Designed to supercharge your workflow on Claude, ChatGPT, Cursor, and Gemini. 

ยินดีต้อนรับสู่ **JamesSkills**! คลังคำสั่ง (Skills) และ Prompt ระดับมืออาชีพที่ออกแบบมาเพื่อช่วยให้คุณทำงานกับ AI (Claude, ChatGPT, Cursor) ได้เหมือนมีผู้เชี่ยวชาญส่วนตัวนั่งอยู่ข้างๆ ครับ

---

## 🌟 Highlight Skills (สกิลยอดฮิตที่แนะนำให้ลอง)

### 1. 🎯 `/grill-me` (Stress-Test & Decision Maker)
* **🇬🇧 EN:** Have an idea or a plan? Use this skill to let the AI "grill" you. It acts as an interviewer, asking you sharp, step-by-step questions to expose flaws and refine your plan before execution.
* **🇹🇭 TH:** มีไอเดียหรือแผนงานในหัว? ใช้สกิลนี้สั่งให้ AI "สัมภาษณ์และต้อนคุณให้มุม" มันจะถามคำถามเจาะลึกทีละข้อ เพื่ออุดรอยรั่วและทำให้แผนของคุณเฉียบคมที่สุดก่อนลงมือทำจริง

### 2. 💡 `/give-me-solutions` (Options & Trade-offs Researcher)
* **🇬🇧 EN:** Stop getting generic lists. This skill forces the AI to research real tools, compare them against your constraints, and present the strongest options with pros/cons without making the final choice for you.
* **🇹🇭 TH:** เลิกให้ AI สุ่มรายชื่อแอปมาให้! สกิลนี้จะสั่งให้ AI วิเคราะห์หา "ทางเลือกที่ดีที่สุด" มาเทียบข้อดีข้อเสียให้คุณดูอย่างละเอียด โดยเว้นช่องว่างให้คุณเป็นคนตัดสินใจขั้นตอนสุดท้ายเอง

### 3. 🔍 `/zoom-out` (System-Level Problem Solver)
* **🇬🇧 EN:** When you're stuck in the weeds, use this to step back. The AI will reframe the problem at a macro level, helping you see the big picture before you waste time fixing the wrong symptom.
* **🇹🇭 TH:** เวลาแก้ปัญหาแล้วรู้สึกหลงทาง ให้ใช้สกิลนี้ AI จะช่วย "ถอยหลังออกมามองภาพรวม" เพื่อหาต้นตอของปัญหาจริงๆ ก่อนที่คุณจะเสียเวลาไปแก้ผิดจุด

### 4. 📝 `/one-page-pls` (Executive One-Pager)
* **🇬🇧 EN:** Turn chaotic meeting notes, transcripts, or scattered files into a pristine, actionable one-page executive summary.
* **🇹🇭 TH:** สกิลสำหรับยุบรวมไฟล์บันทึกการประชุม หรือแชทที่คุยกันยืดยาว ให้กลายเป็นสรุป One-page สั้นๆ กระชับๆ ที่พร้อมส่งให้ผู้บริหารอ่านทันที

---

## 🚀 How to Install (วิธีติดตั้ง)

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

## 🛠 For Developers & Maintainers (ส่วนจัดการระบบ)
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
- use `/build-framework`, `/transformation-journey`, and `/learning-experience-design` for reusable method, macro transformation, and bounded learning respectively;
- use `/prove-it` before accepting a completion claim;
- use `/sum-meet`, `/one-page-pls`, or `/final-it` for recipient-facing outcomes; `make-it-james` applies automatically.

This release has no pilot packages. Compatibility aliases keep older calls working without creating another instruction body. `james-skill-router` is installed internal support, not a recommended human command.

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
