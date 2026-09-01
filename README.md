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

### Context & Setup
| Skill | Function | Without | With |
|---|---|---|---|
| `/project-standard` | Create or repair project truth (SRS, NFR, Permissions) | Scattered logic, lost context | Documented boundaries, AI continuity |
| `/catchup` | Reconstruct current state after a continuity gap | Repetitive context briefing | Immediate execution baseline |

### Analyze & Decide
| Skill | Function | Without | With |
|---|---|---|---|
| `/zoom-out` | Reframe the system boundary | Fixing the wrong symptom | Structural root cause identified |
| `/give-me-solutions` | Research options and present tradeoffs | AI picks randomly | Objective comparison matrix |
| `/baseon` | Apply a named knowledge lens | Generic assumptions | Specific vocabulary and analysis |
| `/grill-me` | Interactive stress-test | Unchallenged logic flaws | Bulletproof execution plan |

### Execute & Verify
| Skill | Function | Without | With |
|---|---|---|---|
| `/done-for-me` | End-to-end authorized implementation | Piecemeal execution and waiting | Finished, usable outcome |
| `/prove-it` | Verify completion claim at the boundary | Trusting AI hallucinations | Hard proof of correctness |
| `/never-again` | Convert rejected result to regression guard | Recurring identical mistakes | Permanent system correction |

### Outputs
| Skill | Function | Without | With |
|---|---|---|---|
| `/sum-meet` | Source-faithful meeting record | Missing decisions and actions | Complete A4 HTML agenda |
| `/one-page-pls` | Self-contained executive brief | Bloated, mixed topics | Concise single-page topic |
| `/final-it` | Select and finish recipient-ready artifact | Meta-copy and AI theatre | Clean delivery format |

### Persistent Standards
| Skill | Function | Without | With |
|---|---|---|---|
| `/i-have-adhd` | Concise, direct communication mode | Wordy prose | Bullet points |
| `/make-it-james` | Recipient-facing wording standard | AI boilerplate | Direct, professional tone |
| `/make-it-james-ux` | Visual and UI standards (IBM Plex Thai) | Default generic styles | Production-ready UI |
| `/proactive-habits` | Prevent subordinate waiting behavior | Waiting for permission | Proactive momentum |
| `/proactive-dev` | Enforce blast-radius checks before code | Broken dependencies | Safe execution |
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
