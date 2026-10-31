# Audit พอร์ตสกิล JamesSkills 2.1.14 และความพร้อมใช้ข้ามค่าย AI

ตรวจ 2026-10-31 บน checkout `main` หลัง pull `4fa1c27` (2.1.14) โดยอ่าน canonical `SKILL.md` ครบ 23 ตัว, `catalog.json`, `docs/SKILL-SCHEMA.md`, `docs/SKILLS.md`, `scripts/install.py`, `scripts/codex_skills.py`, สถานะติดตั้งจริงบนเครื่องนี้ และเอกสารทางการของแต่ละ platform (ลิงก์ในหัวข้อ 5) เป็น audit อย่างเดียว ไม่ได้แก้พฤติกรรมสกิล ไม่ bump version ไม่ติดตั้งใหม่ และไม่ได้รัน behavioral probe

## 0. สรุปสั้น

1. โครงสร้างหลักถูกทางแล้ว: หนึ่ง `SKILL.md` ต่อสกิล ตรงกับ Agent Skills open standard ที่ 46 client รองรับ (Claude, Codex/ChatGPT, Cursor, Copilot, Gemini CLI, OpenClaw, Copilot Studio, Perplexity ฯลฯ) สิ่งที่ขวางการใช้ข้ามค่ายไม่ใช่เนื้อหา แต่เป็น frontmatter หนึ่งฟิลด์ (`kind:`) การติดตั้ง และกฎที่ซ้ำกันข้ามไฟล์
2. ตัวขวางอันดับหนึ่ง: `kind:` เป็น top-level frontmatter ซึ่ง claude.ai upload, Skills API และ `package_skill.py` รับแค่ 6 ฟิลด์ (`name, description, license, compatibility, metadata, allowed-tools`) ฟิลด์อื่นทำให้ upload ล้มด้วย hard error → ปิดทาง Cowork/claude.ai แบบ upload ทั้งหมด แก้ได้ด้วยการย้ายเป็น `metadata.kind` (เปลี่ยน schema + test + 23 ไฟล์แบบ mechanical)
3. Conflict ที่เป็นพฤติกรรมจริง 3 เรื่อง: (ก) `insight-driven-mode` ชน trigger กับ `make-it-james` และในไฟล์เดียวกันทั้ง "Works with" และ "Do not use" ชี้ไป sibling ชุดเดียวกัน (ข) installer รุ่น uncommitted (DEC-050) ลบ link ออกจาก `~/.codex/skills` และ `~/.agents/skills` เพื่อแก้ Cursor แถวซ้ำ ผลคือเครื่องนี้ Codex ไม่มี JamesSkills เลย และ doctor ยังผ่าน (ค) ชื่อ `solutionsimpact-onepagesummary` / `solutionsimpact-meeting-summary-full` เป็นทั้ง alias ใน repo และสกิลจริงในบัญชี claude.ai ที่พฤติกรรมต่างกัน
4. Efficiency: trigger surface รวม 6,364 ตัวอักษร (~1.6k token) อยู่ในงบ แต่เครื่องนี้มีสกิลจากทุกแหล่ง ~170 รายการ และ Claude Code ให้งบ listing แค่ 1% ของ context window จึงเริ่มตัด description ทิ้ง (เห็นใน session นี้แล้ว) ต้องตั้ง `skillListingBudgetFraction` หรือปิดสกิลที่ไม่ใช้
5. กฎซ้ำที่ควรมีเจ้าของเดียว: format boundary (HTML-only / PDF ต้องขอชัด) อยู่ใน 5 สกิล, `lint_outcome.py` มี 2 สำเนาที่เริ่ม drift แล้ว, ย่อหน้า delegation ซ้ำคำต่อคำใน 2 สกิล, principle ซ้ำ 4 คู่, `commands/*.md` 23 ไฟล์ซ้ำ description ทั้งหมดด้วยเหตุผลที่ DEC-037 หักล้างไปแล้ว
6. ทางที่เอกสารรองรับสำหรับ "แก้ที่เดียว อัปเดตทุก host" บน Claude: เพิ่ม marketplace จาก local path → plugin โหลด in place ไม่ต้อง bump version ไม่ต้อง symlink cache เอง (วิธีปัจจุบันใน DEC-050 symlink ทับ cache ของ Claude ซึ่งจะพังเมื่อ `claude plugin update` ครั้งถัดไป)

## 1. สิ่งที่ทำในรอบนี้

- `git fetch` พบ local ตามหลัง 1 commit (`4fa1c27` เพิ่ม `insight-driven-mode`) และมีงานค้าง uncommitted 6 ไฟล์ (DEC-049/050, installer, project_standard.py, tests) สำรอง diff ไว้ที่ scratchpad ก่อน stash → `git pull --ff-only` → stash pop
- Conflict 2 ไฟล์ แก้โดยรักษางานทั้งสองฝั่ง: upstream ใช้เลข DEC-048 ให้ `insight-driven-mode` จึง renumber งาน local เป็น DEC-049 (Cursor สองแถว) และ DEC-050 (one source tree) พร้อมแก้ pointer ใน LESSON-016 และ STATUS header เป็น 2.1.14 โดยคงข้อเท็จจริงเรื่อง cache symlink ไว้
- `./scripts/validate` ผ่านทั้งต้นไม้ (32 package, 23 canonical, 9 alias) ยังไม่ commit อะไร งาน local ยังเป็น ` M` ตามเดิม

## 2. หน้าที่แต่ละสกิล (23)

| สกิล | kind | หน้าที่ | ขอบเขตที่ประกาศ |
|---|---|---|---|
| proactive-habits | mode | ตัดสินเองในสิ่งที่อยู่ในอำนาจ ถามเฉพาะเรื่องที่ผลลัพธ์ต้องการจริง ทำให้จบ | ไม่ขยาย authorization ไม่ส่ง/publish/จ่ายเงินเอง |
| insight-driven-mode | mode | งาน marketing/brand/copy ต้องมี insight เขียนไว้ต่อกลุ่มเป้าหมายก่อนเขียนทุกบรรทัด | ไม่แต่ง quote/ตัวเลข ไม่แทนเจ้าของ wording/evidence/deliverable |
| done-for-me | workflow | พางานที่ตกลงแล้วไปจนเสร็จและ verify เองโดยไม่หยุดถาม | ไม่ push/deploy/send/publish/spend นอก authorization |
| i-have-adhd | mode | คำตอบก่อน ขั้นตอนเป็นเลข ไม่ให้ผู้อ่านต้องจำ state | เปลี่ยนแค่การนำเสนอ ไม่ตัดข้อมูลที่จำเป็น |
| is-that-the-best-you-can-do | workflow | ยกงานที่ถูกแต่ธรรมดาขึ้นถึงเพดานที่ควรเป็น ด้วย effort ตามสัดส่วน | ไม่ใช้กับ defect หรืองานไม่เสร็จ |
| make-it-james | shared-standard | ภาษาที่คนอ่านต้อง "เขียน" ไม่ใช่ "แปล" ตัด metacopy เสียงเป็นคน + lint gate | ไม่เลือก format ไม่เติม fact |
| never-again | workflow | เปลี่ยนความผิดพลาดซ้ำเป็น lesson แคบที่ค้นพบได้ + 3 regression | ไม่ใช่การแก้ output เดียว |
| research-it | workflow | ตัดสิน claim เดียวด้วยหลักฐานภายนอกที่ตรวจย้อนได้ | ไม่เทียบตัวเลือก ไม่ตรวจงานตัวเอง |
| are-you-sure | workflow | ตรวจซ้ำ artifact ธุรกิจที่ส่งแล้วด้วย 5 เลนส์ ซ่อมใน surface ที่ประกาศ | ไม่ใช่โค้ด ไม่ใช่ทำให้ดีขึ้น |
| hand-it-off | internal-routing | fallback เลือกเจ้าของงานเมื่อไม่มีสกิลตรง + ถือ Candidate Card gate | ไม่ผลิต deliverable |
| baseon | knowledge-lens | ใช้/เทียบ framework ที่ลงทะเบียนกับ case จริง แยก source claim / evidence / inference | ไม่ตัดสินแทน ไม่ blend framework |
| coach-me | workflow | พาคนไปสู่เป้าหมายตัวเองด้วยคำถามและการสะท้อน ลึกเท่าที่เขาต้องการ | ไม่วินิจฉัย เปลี่ยนเป็นตอบ/ทำเมื่อถูกขอ |
| final-it | output | เลือก format ที่รับใช้ผู้รับแล้วทำให้เสร็จจริง เมื่อไม่มี output skill ที่แคบกว่า | ไม่เติม fact; HTML-only เว้นแต่ขอ PDF ชัด |
| give-me-solutions | workflow | เทียบตัวเลือกจริงกับบริบทโปรเจกต์ ชี้ตัวที่ชนะ + เงื่อนไขที่ทำให้พลิก | ไม่ซื้อ/สมัคร/migrate แทน |
| grill-me | workflow | สัมภาษณ์ทีละคำถามผ่าน native popup จนเป้าหมายและ requirement ชัด แล้วลงมือ | ไม่ coach ไม่ research แทน |
| one-page-pls | output | บีบเนื้อหาเป็น brief หน้าเดียว (default A4 landscape HTML, 1 topic/หน้า) | ไม่ซ่อนการตัดเนื้อหา ไม่ใช่ meeting record |
| sum-meet | output | บันทึกประชุมฉบับตรวจย้อนได้ ทุก agenda ในไฟล์เดียว แยก evidence/interpretation | ไม่ตัดสินสิ่งที่ห้องไม่ได้ตัดสิน |
| zoom-out | workflow | ถอยจากรายละเอียดไปถึงเป้าหมายโปรเจกต์และ strategy แล้วเลือก move ถัดไป | ไม่แก้ UI/implementation เดี่ยว |
| catchup | workflow | สร้างสถานะจริงของโปรเจกต์หลังหายไป แบบ read-only เป็นหน้า catchup มาตรฐาน | ไม่ซ่อม ไม่ทำต่อใน workflow นี้ |
| dev-are-you-sure | workflow | ตรวจซ้ำซอฟต์แวร์ที่ส่งแล้ว เลือก check ตาม risk ซ่อมใน surface ที่ประกาศ | ไม่ใช่ artifact ธุรกิจ |
| make-it-james-ux | shared-standard | ออกแบบจาก real flow → reading order → perfect grid; สี/ฟอนต์ตามโปรเจกต์ + format boundary | ไม่เลือก format ไม่ authorize PDF |
| proactive-dev | mode | วิศวกรรมเชิงรุกตั้งแต่เข้าใจ goal → build → test → deliver (5 roles เป็นวิธีคิด) | ไม่เพิ่ม store/identity path ใหม่โดยไม่มี decision + rollback |
| project-standard | workflow | สร้าง/ซ่อม project contract vendor-neutral (PROJECT/STATUS/AGENTS/DECISIONS + SRS) | ไม่ overwrite ด้วย template ไม่รายงาน intended เป็น implemented |

ขนาดและงบ (วัดจากไฟล์จริง): description เฉลี่ย 277 ตัวอักษร (cap 320) รวม 6,364; body รวม ~145k ตัวอักษร (~36k token) ทุกตัวอยู่ใต้ line cap ของ schema ตัวใหญ่สุด `grill-me` ~3.5k token, `make-it-james-ux` ~2.3k token + `references/standard.md` อีก ~3k token ที่สั่งให้อ่านทั้งไฟล์ก่อนตัดสินใจ

## 3. Conflict และ overlap ที่พบ

ระดับ = ผลต่อพฤติกรรมหรือความถูกต้อง ไม่ใช่อัตราล้มเหลว หลักฐานอ้างชื่อไฟล์และ section

### สูง

**C1. `insight-driven-mode` ชน `make-it-james` และขัดกับ schema ของตัวเอง**
- description ปิดท้ายว่า "or when copy sounds generic or translated" ซึ่งเป็น trigger หลักของ `make-it-james` ("sound written rather than translated", ภาษาแข็ง, อ่านแล้วเหมือน AI) → เมื่อผู้ใช้บ่นว่าสำนวนเหมือนแปล model มีสองเจ้าของให้เลือก
- `## Works with` และ `## Do not use this when` ชี้ไป sibling ชุดเดียวกัน 4 ตัว (`research-it`, `give-me-solutions`, `i-have-adhd`, `proactive-habits`) คือ "ประกอบกับ X" และ "อย่าใช้เมื่อ X" ในไฟล์เดียว ขัด `docs/SKILL-SCHEMA.md` ("modes do not exclude workflows they accompany") และ LESSON-004
- ชื่อลงท้าย `-mode` เป็นสกิลเดียวที่เอาชื่อหมวดมาเป็นชื่อ ขัดกฎใน `AGENTS.md` ("Name the mental move, not an internal department") และ DEC-048 ระบุว่า "the requesting instruction... is the naming and promotion authority" ซึ่งไม่ใช่ถ้อยคำอนุมัติของเจ้าของตาม REQ-004 ควรยืนยันว่า James อนุมัติชื่อและ scope นี้เอง

**C2. DEC-050 (uncommitted) แลก Cursor แถวซ้ำกับการหาย Codex coverage**
- `scripts/install.py` รุ่น local: เมื่อมี Claude plugin ติดตั้ง จะลบ link ของสกิลนั้นออกจาก `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`, `~/.cursor/skills` ทั้งหมด แต่ Codex อ่านสองโฟลเดอร์หลัง ไม่ได้อ่าน Claude plugin
- บนเครื่องนี้: `~/.codex/config.toml` ไม่มี marketplace `james-skills`, `~/.codex/skills` มีแค่ `chronicle` และ `solutionsimpact-keynote-style`, `~/.agents/skills` ว่าง → Codex ไม่มี JamesSkills สักตัว และ `scripts/doctor` ผ่านเพราะ `codex` ไม่อยู่บน PATH จึง SKIP
- หลักฐาน runtime (ไม่ใช่แค่ไฟล์): ถาม app-server ของ Codex binary ที่ bundled ใน ChatGPT.app (0.166.0-alpha.5.1) ด้วย `skills/list` แบบอ่านอย่างเดียว ได้สกิลทั้งหมด 14 รายการ (plugin ของ OpenAI 6 + `~/.codex/skills` และ `.system`) และ JamesSkills = 0
- `ai-context/STATUS.md` ของ 2.1.14 (เขียนจาก checkout ที่ไม่มีงาน local นี้) รายงาน "128 managed links รวม `.agents`, `.codex`, `.claude`, `.cursor`" ซึ่งสวนทางกับ DEC-050 ตรงๆ → ต้องเลือกหนึ่งสายก่อน commit (ดูข้อเสนอ P0-1)
- แนวทางที่สอดคล้องกับหลักฐานในหัวข้อ 5.1.1: คง DEC-050 (ไม่ใช้ shared dir) แต่ปิดช่องว่าง Codex ด้วย native plugin (`codex plugin marketplace add` ตาม README) และให้ doctor หา binary ที่ bundled ใน ChatGPT.app; doctor ต้อง fail เมื่อ host ที่ประกาศว่าครอบคลุมมีสกิลเป็นศูนย์ ไม่ใช่ SKIP

**C3. ชื่อเดียว สองพฤติกรรม ข้าม surface**
- `aliases/solutionsimpact-onepagesummary` และ `aliases/solutionsimpact-meeting-summary-full` ชี้ไป `one-page-pls` / `sum-meet`
- บัญชี claude.ai ของ James มีสกิลชื่อเดียวกันเป็นสกิลจริง (Bento grid, สี Downriver/Supernova, แบรนด์ SolutionsIMPACT) ซึ่ง Claude Desktop โหลดเป็น plugin `anthropic-skills` (83 สกิล) ใน Code และ Cowork → ใน Claude เรียกชื่อนี้ได้ของเก่า ใน Gemini/Antigravity ได้ alias ที่พาไป `one-page-pls` ซึ่งหน้าตาต่างกัน
- alias ระบุว่า "expires after the migration window" แต่ไม่มีวันหมดอายุหรือเกณฑ์ปิด

**C4. Cache symlink (DEC-050) ฝืนกลไก versioned cache ของ Claude Code**
- สภาพปัจจุบัน: `installed_plugins.json` บันทึก 2.1.13 @ `63a4512`, แต่ `~/.claude/plugins/cache/james-skills/*/2.1.13` เป็น symlink ไป repo ที่เป็น 2.1.14 แล้ว, marketplace clone ค้างที่ `719a977` (2.1.13)
- `claude plugin update` ครั้งถัดไปจะเห็น 2.1.14 บน GitHub แล้วสร้างโฟลเดอร์ 2.1.14 เป็นสำเนาจริง → symlink กลายเป็น orphan และ drift กลับมา
- เอกสารทางการมีทางที่รองรับ: marketplace ที่เพิ่มจาก local path ทำให้ plugin "loads in place... edits take effect at the next session start or /reload-plugins, and you don't need to increase the version" (code.claude.com/docs/en/plugins/loading)

**C5. `kind:` ใน frontmatter ปิดทาง claude.ai / Cowork upload / Skills API**
- ทุก `SKILL.md` มี `kind:` เป็น top-level field ตาม `docs/SKILL-SCHEMA.md`
- เอกสาร Claude Code: นอก Claude Code ใช้ได้เฉพาะ `name, description, license, compatibility, metadata, allowed-tools`; ฟิลด์อื่น "packaging or upload fails with a hard error" (code.claude.com/docs/en/skills, หัวข้อ Using skill frontmatter outside Claude Code) spec ของ Agent Skills ก็กำหนด `metadata` เป็น string→string map ซึ่งรับ `kind: workflow` ได้พอดี
- ผล: ส่งเข้า claude.ai Skills, Skills API, Copilot Studio/Perplexity validator เข้มๆ ไม่ได้จนกว่าจะย้าย ส่วน Cowork ผ่านทาง marketplace ยังไม่พบเอกสารว่าเข้มเท่ากัน ถือเป็นความเสี่ยงที่ยังไม่ปิด

### กลาง

**C6. `are-you-sure` / `dev-are-you-sure` คือ mental move เดียว สองไฟล์** — ทั้งคู่ใช้ 5 เลนส์โครงเดียวกัน (Integrity / Structure↔Architecture / Residue↔Hygiene / Recipient↔Interface / Longevity) principle ซ้ำ (Swiss cheese model) และ counter-case ของแต่ละตัวคือการชี้ไปอีกตัว เป็นการแยกตาม artifact ที่เจ้าของเคยยืนยัน จึงไม่ใช่ bug แต่คือต้นทุน maintenance สองเท่า ทางเลือกคือสกิลเดียว + lens table สองชุดใน `references/` (ต้อง James อนุมัติชื่อ/scope) หรือคงสองชื่อแต่ย้ายเลนส์ร่วมไป reference เดียว

**C7. กลุ่ม "ทำให้จบ" สามตัวมีข้อความซ้อน** — ย่อหน้า delegation ("same requirement identifiers, base revision, owned paths, allowed actions, forbidden external effects, and acceptance evidence") อยู่คำต่อคำใน `done-for-me` และ `proactive-dev`; principle "Begin with the end in mind" (Covey) อยู่ทั้ง `proactive-habits` และ `proactive-dev`; "Two-way and one-way doors" (Bezos) ใน `proactive-habits` กับ "Reversibility decides authority" (Bezos) ใน `done-for-me` คือกฎเดียวกัน schema เองระบุว่า principle ที่ใส่ sibling ได้เท่ากันคือ padding (DEC-032 ยืนยันแล้วว่าสามตัวนี้ compose กัน ประเด็นจึงอยู่ที่ข้อความซ้ำ ไม่ใช่หน้าที่ซ้ำ)

**C8. Format boundary มี 5 สำเนา และ `AGENTS.md` ชี้เจ้าของผิดไฟล์** — กฎ HTML-only / PDF เมื่อขอชัดเท่านั้น อยู่ใน `make-it-james-ux` (เจ้าของหลัง DEC-046), `final-it`, `one-page-pls`, `sum-meet`, `catchup` ด้วยถ้อยคำต่างกันเล็กน้อย ขณะที่ `AGENTS.md` ยังเรียกว่า "the `make-it-james` format boundary" ทั้งที่กฎย้ายไป `make-it-james-ux` แล้ว

**C9. Script ซ้ำและ dependency ข้าม pillar** — `lint_outcome.py` มี 2 สำเนา (`make-it-james` 10,693 B และ `make-it-james-ux` 10,620 B) ต่างกัน 1 regex แล้ว ซึ่งเป็น class เดียวกับ LESSON-013; `embed_ibm_plex_thai.py` อยู่ใน `james-software` แต่ `one-page-pls` และ `sum-meet` (`james-productivity`) ต้องโหลด `make-it-james-ux` เพื่อหามัน → ติดตั้ง pillar เดียวหรือ upload แยกสกิล gate นี้ล้มทันที; `proactive-dev` อ้าง Wealth Spectrum pack ที่อยู่ใน `james-productivity`

**C10. `hand-it-off` จ่ายค่า listing ทุก turn เพื่อบอกว่า "อย่าเลือก"** — description 284 ตัวอักษร resident ทุก host รวม host ที่ไม่มี auto-routing; Candidate Card gate เป็น policy ของ repo (`AGENTS.md` มีอยู่แล้ว) ไม่ใช่ runtime behavior ตัวเลือก: `user-invocable: false` บน Claude, ไม่ติดตั้งแต่เก็บใน repo, หรือย้าย gate ไป docs

**C11. `commands/*.md` 23 ไฟล์ ซ้ำ description ทั้งหมด** — เหตุผลเดิม (DEC-035: picker ไม่โชว์ skill) ถูก DEC-037 หักล้างว่าสาเหตุจริงคือ marketplace ไม่ลงทะเบียนกับ binary ของ Desktop; เอกสารปัจจุบัน: "Commands: Flat Markdown command files. Prefer skills/ for new plugins" และ plugin skill เรียกเป็น `/plugin-name:skill-name` ได้ตรง (bare name ใช้ได้เมื่อไม่ชนชื่ออื่น) `scripts/package-plugins` ยังมี comment ยืนยันความเชื่อเก่า ควร verify กับ Desktop binary (2.1.309) ก่อนลบ

**C12. เอกสารจัด `coach-me` เป็น mode แต่ catalog เป็น workflow** — `docs/SKILLS.md` อยู่ใต้ "Modes and standards", README อยู่ใต้ "Persistent Interaction Modes" ขณะที่ `catalog.json` และ frontmatter คือ `workflow`

**C13. Roster ไม่เท่ากันข้าม host** — alias 9 ตัวติดตั้งเฉพาะ host ที่ใช้ user-dir links (`~/.gemini/config/skills` มี 31 รายการ = 22 สกิล + 9 alias ก่อน install รอบใหม่) แต่ plugin route (Claude/Cursor/Codex) เห็น 23 ไม่มี alias

### ต่ำ

**C14. `grill-me` ผูกกับเครื่องมือ host เฉพาะ** — ชื่อเครื่องมือ `request_user_input_async`, `request_user_input`, `AskUserQuestion` และกลไก wait/yield ของ Codex อยู่ใน body (มี fallback เป็น chat) บน host ที่ไม่มี native popup (Cowork, OpenClaw, ChatGPT) จะตก fallback ทุกครั้ง และ body ขนาด ~3.5k token โหลดทุกครั้งที่สัมภาษณ์

**C15. ชื่อผลิตภัณฑ์และระบบส่วนตัวใน public body** — `proactive-dev` ระบุ Base44/Supabase/Vercel (DEC-045 ตั้งใจคงไว้); `catchup` และ `hand-it-off` อ้าง JamesOS ซึ่ง `PROJECT.md` ประกาศเป็น out of scope ของ repo สาธารณะ

**C16. ข้อความซ้ำย่อย** — "On Windows invoke the same helper with `python`..." ซ้ำ 4 สกิล (`baseon`, `catchup`, `make-it-james-ux`, `project-standard`)

**C17. README บอก invoke ด้วย bare name เท่านั้น** — เอกสารปัจจุบันระบุ plugin skill เป็น `/plugin-name:skill-name` และ bare name ใช้ได้เมื่อไม่มีคำสั่งอื่นใช้ชื่อนั้น ควรเขียนทั้งสองรูป (DEC-036/LESSON-014 บันทึกไว้จากรุ่นเมื่อกันยายน)

## 4. Optimize และ efficiency

**E1. Skill listing budget บนเครื่องนี้ล้นจริง** — Claude Code ให้งบ listing = 1% ของ context window และเมื่อล้นจะตัด description ของสกิลที่ใช้น้อยสุดก่อน (code.claude.com/docs/en/skills, Skill descriptions are cut short) เครื่องนี้มี `anthropic-skills` 83 + JamesSkills 23 (+23 commands) + user skills 9 + plugin อื่น รวม ~170 รายการ ใน session นี้เห็นสกิลหลายสิบตัวถูกตัด description แล้ว ทางแก้ที่ไม่ต้องแก้ repo: ตั้ง `skillListingBudgetFraction` (เช่น 0.02), ใช้ `skillOverrides` เป็น `name-only` กับสกิลที่ไม่ใช้, เช็คด้วย `/doctor` และ `/skill-doctor` ทางแก้ฝั่ง repo: ตัดส่วน exclusion ยาวใน description ที่ไม่ช่วย match (เช่น `hand-it-off`) และตัด `commands/` ที่ซ้ำ

**E2. `proactive-habits` โหลดสองทาง** — `~/.claude/CLAUDE.md` @import body ทั้งไฟล์ (~8 KB ≈ 2k token) ทุก session และ plugin ยังใส่ description ใน listing อีก ถ้า import ไว้แล้ว รายการใน listing ซ้ำ ตั้ง name-only ได้ ส่วนความ "always-on" บน host อื่นทำแยกกันคนละวิธี (Codex: `~/.codex/AGENTS.md` เขียนมือ, Cursor/Gemini/Antigravity: ไม่มี) ควรเป็น adapter ที่ generate จากต้นทางเดียว (ดูหัวข้อ 6)

**E3. กฎซ้ำ → เจ้าของเดียว + pointer** — format boundary ×5, delegation ×2, Windows helper line ×4, `lint_outcome.py` ×2, principle ×4 คู่ (C6–C9, C16) ลดทั้ง token ตอนโหลดและโอกาส drift

**E4. Body ขนาดใหญ่ที่จ่ายทุกครั้ง** — `make-it-james-ux` + `references/standard.md` ≈ 5.3k token ต่องาน visual ทุกงาน; `grill-me` 3.5k token รวม host-specific tool rules ที่ย้ายไป `references/` ได้ (Claude Code หลัง compaction เก็บแค่ส่วนต้นของสกิล จึงควรให้กฎที่ผูกมัดอยู่บนสุดของ body ทุกตัว)

**E5. Installer** — จุดแข็ง: `--plan`, rollback, ไม่ overwrite ของจริง, reconcile Codex ผ่าน app-server จุดอ่อน: verify บน macOS เท่านั้น, Windows ไม่เคยรัน, ไม่มี adapter สำหรับ Cowork/claude.ai, OpenClaw, Copilot, Windsurf, OpenCode, Kiro; path ของ Antigravity ที่ใช้ (`~/.gemini/config/skills`, `~/.gemini/antigravity/custom/skills`) ต้องเทียบกับเอกสารปัจจุบัน (หัวข้อ 5)

**E6. Release gate** — pre-commit บังคับ bump VERSION เมื่อแก้ content (LESSON-005) ยังจำเป็นสำหรับผู้ใช้ทาง GitHub marketplace แต่ถ้าเครื่อง James ใช้ local-path marketplace (in-place) การแก้ไฟล์มีผลทันทีโดยไม่ต้อง bump ลดรอบ "แก้ → bump → push → update → restart" เหลือ `/reload-plugins`

## 5. Research: skill format และ discovery ของแต่ละค่าย (ณ 2026-10-31)

เกรดหลักฐาน: OFFICIAL = เอกสารผู้ผลิต, PRACTITIONER = รายงานผู้ใช้, NOT FOUND = หาไม่พบ ห้ามอนุมาน path/คำสั่งที่ไม่มีแหล่ง (LESSON-001)

### 5.1 Coding agents

| Platform | project path | user/global path | frontmatter / ลิมิต | เรียกใช้ | plugin / marketplace | symlink | แหล่ง (fetched 2026-10-31) | เกรด |
|---|---|---|---|---|---|---|---|---|
| Claude Code | `.claude/skills/<name>/` (cwd ถึง repo root, nested โหลดเมื่อแตะไฟล์, `--add-dir`); `.claude/commands/*.md` ยังใช้ได้ skill ชนะเมื่อชื่อชน; **ไม่อ่าน `.agents/skills`** | `~/.claude/skills/`; claude.ai sync → `~/.claude/skills/synced/`; plugin `<plugin>/skills/<name>/` เรียก `/plugin:skill` | ~20 ฟิลด์ (`disable-model-invocation`, `user-invocable`, `paths`, `hooks`, `context`…); unknown key ถูก ignore ใน Claude Code แต่ hard error บน claude.ai/API; listing budget 1% ของ context; `description+when_to_use` ตัดที่ 1,536 | `/name`, auto จาก description | `.claude-plugin/plugin.json` + `marketplace.json`; cache `~/.claude/plugins/cache/<m>/<p>/<version>/`; version = manifest → entry → commit SHA; local-path marketplace โหลด in place | รองรับที่ skill entry (โหลดครั้งเดียวแม้หลายที่ชี้ target เดียว); plugin: link นอก marketplace ถูกทิ้งตอน copy; `claude plugin validate` ไม่ตาม symlink | code.claude.com/docs/en/skills, /plugins/manifest-reference, /plugins/loading, /plugins/host-marketplace (อ้าง v2.1.310) | OFFICIAL |
| OpenAI Codex (CLI, ChatGPT app, IDE) | `.agents/skills` (walk-up ถึง repo root) | **`~/.agents/skills` (primary)**; `~/.codex/skills` ยังโหลดแต่ source ระบุ "Deprecated... kept for backward compatibility"; admin `/etc/codex/skills` | `name, description` บังคับ; sidecar `agents/openai.yaml` (`interface`, `policy.allow_implicit_invocation`); listing ≤2% context หรือ 8,000 chars; `skills.max_context_tokens` ≤10,000; สกิลชื่อซ้ำสอง root ถูกเก็บทั้งคู่ | `$skill-name`, `/skills`, implicit | Agent Plugins root `plugin.json` (+ `.codex-plugin/plugin.json` fallback); marketplace `.agents/plugins/marketplace.json`, `~/.agents/plugins/marketplace.json`, **legacy `.claude-plugin/marketplace.json` (desktop อ่าน)**; cache `~/.codex/plugins/cache/`; `codex plugin marketplace add|list|upgrade|remove`; app-server `skills/list` มีจริง | ตาม symlink; dedupe root ตาม path ไม่ใช่ชื่อสกิล | learn.chatgpt.com/docs/build-skills, /docs/plugins, developers.openai.com/codex/plugins/build; source `codex-rs/ext/skills/src/host_roots.rs` | OFFICIAL (docs+source) |
| Cursor | `.agents/skills/`, `.cursor/skills/`; compat `.claude/skills/`, `.codex/skills/` | `~/.agents/skills/`, `~/.cursor/skills/`; compat `~/.claude/skills/`, `~/.codex/skills/`; **Claude plugin cache ไม่อยู่ในรายการทางการ** (แต่ DEC-049 สังเกตว่าเห็น); เฉพาะ `~/.cursor/skills` sync ไป Cloud Agents | `name` (ตัวเล็ก/ขีด = โฟลเดอร์), `description` บังคับ; `paths`, `disable-model-invocation`, `icon`, `color`, `metadata` | auto; `/` picker (ใช้ครั้งเดียว); "Use as Mode" Option+Enter (ตลอด session) | rules `.cursor/rules/*.mdc`; AGENTS.md; plugin `.cursor-plugin/plugin.json` หรือ Agent Plugins root `plugin.json`; marketplace ต้อง review และ open source; local dev `~/.cursor/plugins/local/<p>` | ไม่ระบุ | cursor.com/docs/context/skills, /docs/context/rules, /docs/plugins; changelog 2.4 (2026-01-22) | OFFICIAL |
| Google Antigravity (App, CLI, IDE) | `<workspace>/.agents/skills/` (App/CLI อ่าน parent ถึง repo root); legacy `.agent/skills` | **`~/.gemini/config/skills/` (canonical ปัจจุบัน, ตรงกับ repo)**; CLI เพิ่ม `~/.gemini/antigravity-cli/skills/`, `~/.gemini/skills/`; IDE legacy `~/.gemini/antigravity/skills/`; plugin `~/.gemini/config/plugins/<p>/skills/`; **`~/.gemini/antigravity/custom/skills` ไม่มีในเอกสาร** | `name` optional (default โฟลเดอร์), `description` บังคับ; v2.25.0 (2026-10-20) แก้ bug colon ใน description | auto ทุก turn; App `/<name>`; CLI ทุกสกิลเป็น slash + `/skills reload`; IDE เมนู Customizations | rules: workspace `AGENTS.md`/`GEMINI.md`/`.agents/rules/*.md`; global `~/.gemini/AGENTS.md|GEMINI.md`, `~/.gemini/config/rules/*.md`; plugin marketplace ใน Customizations (v2.18.1, 2026-09-28); Antigravity CLI แทน Gemini CLI สำหรับผู้ใช้ฟรี/Google One ตั้งแต่ 2026-06-18 | ไม่ระบุ; PRACTITIONER: IDE เคยไม่อ่าน symlink ใน legacy path (vercel-labs/skills#633, 2026-03-14) แก้ด้วย Settings → Skill Custom Paths | antigravity.google/docs/skills, /docs/rules/, /docs/changelog (ล่าสุด 2026-10-29) | OFFICIAL (symlink: PRACTITIONER) |
| Gemini CLI | `.gemini/skills/` หรือ alias `.agents/skills/` | `~/.gemini/skills/` หรือ `~/.agents/skills/` | ไม่ระบุในหน้า | model เรียก `activate_skill` + consent; `gemini skills list|install|uninstall`; `/skills link <path>` | extensions รวมสกิล; GEMINI.md | `/skills link` มีให้ | geminicli.com/docs/cli/skills/ (2026-04-30) | OFFICIAL |
| GitHub Copilot (CLI, VS Code, GitHub) | `.github/skills`, `.claude/skills`, `.agents/skills` | `~/.copilot/skills`, `~/.agents/skills`; VS Code Local เพิ่ม `~/.claude/skills` | `name` ≤64 ตัวเล็ก = โฟลเดอร์ (ผิด = เงียบไม่โหลด); `description` ≤1,024; `user-invocable`, `disable-model-invocation`, `context: fork` | auto; `/skill-name`; CLI `/skills reload`, `copilot skill`, `gh skill` | AGENTS.md ใกล้สุดชนะ; `CLAUDE.md`/`GEMINI.md` ที่ root; Agent Plugins รองรับ; VS Code Customization Marketplace (Preview) | ไม่ระบุ | docs.github.com about-agent-skills; code.visualstudio.com agent-skills (2026-10-28) | OFFICIAL |
| Windsurf → Devin Local | `.devin/skills/` (legacy `.windsurf/skills/`), `.agents/skills/` | `~/.config/devin/skills/`, `~/.agents/skills/` | `name, description` | `/skill-name`; auto | — | ไม่ระบุ | docs.devin.ai/desktop/cascade/skills (docs.windsurf.com redirect) | OFFICIAL |
| OpenCode | `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` | `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | `name` 1–64 ตาม regex spec, `description` 1–1,024; unknown key ignore | tool `skill` เท่านั้น (ไม่มี slash); `permission.skill` | — | ไม่ระบุ | opencode.ai/docs/skills/ (2026-10-30) | OFFICIAL |
| Amp | `.agents/skills/`, `.claude/skills/` | `~/.config/agents/skills/`, `~/.agents/skills/`, `~/.config/amp/skills/`, `~/.claude/skills/`, **`~/.claude/plugins/cache/`**; recursive 5 ชั้น; ชื่อแรกชนะ | `name`(= dir), `description`, `mcpServers` | auto; plugin skill `<plugin>:<skill>` | `amp.skills.disableClaudeCodeSkills`, `amp.skills.disableGlobalAgentsSkills`; plugins `~/.config/amp/plugins/` | ไม่ระบุ | ampcode.com/docs/customize/skills | OFFICIAL |
| Kiro | `.kiro/skills/` เท่านั้น | `~/.kiro/skills/` | `name` ≤64 = โฟลเดอร์; `description` ≤1,024; `license/compatibility/metadata` | auto; `/name` | Agent Plugins | ไม่ระบุ | kiro.dev/docs/skills/ (2026-10-21) | OFFICIAL |
| Factory Droid | `.factory/skills/`; compat `.agents/skills/**`, `.agent/skills/**` | `~/.factory/skills/`, `~/.agents/skills/**`, `~/.agent/skills/**` | `name, description`, `allowed-tools`(metadata), `enabled`, `user-invocable`, `disable-model-invocation` | `/skill-name`; `/skills`; auto | — | ไม่ระบุ | docs.factory.com/cli/configuration/skills | OFFICIAL |
| JetBrains Junie | `.junie/skills/`, `.agents/skills/`; ตรวจพบ `.claude/.cursor/.codex` แล้วเสนอ import | `~/.junie/skills/`, `~/.agents/skills/` | `name` บังคับ; `description` optional | `/<name>`, `$<name>`, `/skills`; auto | — | ไม่ระบุ | junie.jetbrains.com/docs/agent-skills.html (2026-10-30) | OFFICIAL |
| Roo Code | `.roo/skills/`, `.agents/skills/` | `~/.roo/skills/`, `~/.agents/skills/` | `name` 1–64 = dir **หรือชื่อ symlink**; `description` 1–1,024 | auto เท่านั้น | — | รองรับ ใช้ชื่อ symlink | roocodeinc.github.io/Roo-Code/features/skills (2026-05-15) | OFFICIAL |
| Cline | `.cline/skills/`, `.clinerules/skills/`, `.claude/skills/` (**ไม่มี `.agents`**) | `~/.cline/skills/`; global ชนะ project | `name` = dir; `description` ≤1,024 | tool `skills`; `/name` | — | ไม่ระบุ | docs.cline.bot/features/skills | OFFICIAL (ขัดกับตาราง Vercel) |
| Agent Skills spec | `SKILL.md` + `scripts/ references/ assets/` | — | `name` 1–64 ตัวเล็ก/ขีดเดี่ยว = dir; `description` 1–1,024; `license`; `compatibility` ≤500; `metadata` string→string; `allowed-tools` (experimental); SKILL.md <500 บรรทัด, body <5,000 token; validator `skills-ref` | — | Showcase 46 client (self-declared) รวม Claude Code, Claude, ChatGPT & Codex, Cursor, Copilot, VS Code, Gemini CLI, Amp, OpenCode, Kiro, Factory, Junie, Roo, OpenClaw; **ไม่มี Antigravity, Windsurf, Cline** | — | agentskills.io/specification, /clients (repo สร้าง 2025-12-16, push ล่าสุด 2026-08-09) | OFFICIAL |
| Vercel `skills` CLI | `./<agent>/skills/` | `~/<agent>/skills/` ด้วย `-g` | — | `npx skills add <owner/repo> [--skill x] [-a agent] [-g] [--copy]`; `find/list/update/remove/check`; Node ≥22.20 | 75+ agents; canonical `~/.agents/skills` + symlink ต่อ agent (อยู่ใน source/issues ไม่ใช่ README) | ใช้ symlink เป็น default; issues: Codex โชว์ซ้ำ (#1056), Copilot ซ้ำ (#1200), universal-agent skip (#1874), พังเมื่อ skills dir เป็น symlink (#481) | github.com/vercel-labs/skills docs/commands.md, docs/agents.md | OFFICIAL docs / PRACTITIONER issues |
| `.agents/skills` convention | ผู้อ่านตามเอกสาร: Codex (primary), Cursor, Antigravity (workspace), Gemini CLI (alias), Copilot, OpenCode, Amp, Roo, Factory, Devin, Junie, OpenClaw; **ไม่อ่าน: Claude Code, Kiro, Cline** | ชุดเดียวกันสำหรับ `~/.agents/skills` | — | — | Codex marketplace ที่ `.agents/plugins/marketplace.json` | — | แหล่งข้างบน | OFFICIAL |

### 5.1.1 ข้อค้นพบที่กระทบ repo โดยตรง

- **`~/.agents/skills` เป็น hub ร่วมของอย่างน้อย 11 tools** และ host ส่วนใหญ่ยังอ่าน private dir ของตัวเองพร้อมกัน (Cursor อ่าน 8 โฟลเดอร์, Amp อ่าน Claude plugin cache ด้วย) การวาง link ที่ hub จึงหมายถึงโชว์ซ้ำกับ host ที่มี native plugin หรือ private copy อยู่แล้ว เท่ากับยืนยันทิศของ DEC-050: ใช้ **private dir ต่อ host หรือ native plugin เท่านั้น ไม่ใช้ shared dir** แต่ต้องปิดช่องว่างที่ C2 เปิดไว้ (Codex)
- **Codex**: `~/.codex/skills` (ที่ installer ใช้เป็น `codex_target`) ถูก source ระบุว่า deprecated; ทาง native plugin ตาม README ยังถูกต้องเพราะ desktop อ่าน `.claude-plugin/marketplace.json`; binary ของ Codex บนเครื่องนี้อยู่ที่ `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex` (0.166.0-alpha.5.1) ไม่อยู่บน PATH จึงทำให้ `scripts/doctor` SKIP Codex ทุกครั้ง (กลไกเดียวกับ LESSON-015 ของ Claude Desktop) → doctor ต้องหา binary นี้เอง
- **Cursor**: เอกสารไม่ระบุว่าอ่าน Claude plugin cache แต่ DEC-049 สังเกตได้ว่าเห็น; route ที่เป็นทางการคือ local plugin `~/.cursor/plugins/local/<p>` ด้วย Agent Plugins root `plugin.json`; path `.codex/skills` ที่ Cursor ยังอ่านคือ path ที่ Codex เลิกใช้แล้ว
- **Antigravity**: `~/.gemini/config/skills` ยืนยันเป็น canonical (repo ถูกอยู่แล้ว); `~/.gemini/antigravity/custom/skills` ไม่มีในเอกสาร ควรตัดจาก installer; มีรายงานผู้ใช้ว่า IDE เคยไม่โหลด symlink จึงต้อง verify การโหลดจริง (ไม่ใช่แค่เมนู Customizations); always-on adapter วางได้ที่ `~/.gemini/AGENTS.md` หรือ `~/.gemini/config/rules/*.md`
- **Agent Plugins (root `plugin.json`, agent-plugins.org)**: Codex/ChatGPT, Cursor, Copilot, Kiro, VS Code รองรับ → เพิ่ม root `plugin.json` ต่อ pillar ควบคู่ `.claude-plugin/plugin.json` จะได้ plugin ข้ามค่ายโดยไม่ซ้ำ body (ต้อง verify schema ก่อน ตาม LESSON-001)
- **Frontmatter ผ่านลิมิต spec ทั้งหมด**: ชื่อ ≤64 ตาม regex, description ≤1,024, ไม่มี colon ใน description, ทุกไฟล์ <500 บรรทัด เหลือตัวขวางเดียวคือ `kind:` (C5)
- **Symlink ไม่ใช่ universal**: Claude Code โหลดได้แต่ `claude plugin validate` ไม่ตาม; Codex ตาม; Roo ใช้ชื่อ symlink; Antigravity IDE มีรายงานไม่โหลด; Vercel CLI พังเมื่อ dir เป็น symlink → installer ต้องมี copy mode ต่อ host (เหมือน `--copy` ของ Vercel)
- **`npx skills add theeranon/JamesSkills`** ใช้เป็น installer สำรองสำหรับ host ที่ยังไม่มี adapter ได้ แต่มันวาง canonical ที่ `~/.agents/skills` + symlink ต่อ agent ซึ่งสร้างแถวซ้ำแบบเดียวกับที่ DEC-050 แก้ (issues #1056, #1200)

### 5.2 Non-coding และ general assistant

| ผลิตภัณฑ์ | สกิลเข้าทางไหน | แชร์กับ Claude Code? | กฎ frontmatter / ลิมิต | เรียกใช้ | Registry | แหล่ง | เกรด |
|---|---|---|---|---|---|---|---|
| Claude Cowork | Customize › Plugins: Discover, **Add marketplace** (`owner/repo` GitHub ได้), หรือ upload `.zip`/`.plugin`; ≤200 MB, ≤5,000 ไฟล์ | ใช่ ทางเดียวผ่านบัญชี: plugin ที่เปิดในบัญชีลงมา Claude Code เป็น `<name>@synced` (v2.1.273+); Cowork **ไม่อ่าน** `~/.claude/skills` | รูปแบบ plugin เดียวกับ Claude Code; skills/commands/agents/hooks/remote MCP โหลด; `bin/` ระดับบนทำให้ติดตั้งไม่ได้ | อัตโนมัติจาก description หรือเมนู `/` | Anthropic directory + Git-repo marketplaces | claude.com/docs/cowork/guide/plugins, claude.com/docs/plugins/platform-support, code.claude.com/docs/en/plugins/loading | OFFICIAL |
| claude.ai chat / Desktop | Customize › Skills › Upload ZIP ที่ชั้นบนสุดเป็น `<skill-name>/SKILL.md` (SKILL.md ที่ root ไม่รับ) | ทางเดียวลง `~/.claude/skills/synced/` | **6 ฟิลด์เท่านั้น** `name, description, license, compatibility, metadata, allowed-tools`; ฟิลด์อื่น = hard error; `name` ≤64 ตัวพิมพ์เล็ก/ขีด; `description` ≤1,024 | อัตโนมัติ / เมนู `/` | ผ่าน plugin directory เท่านั้น | support.claude.com/en/articles/12512180, code.claude.com/docs/en/skills | OFFICIAL |
| Claude Developer Platform (Skills API) | `POST /v1/skills` (zip หรือไฟล์; ≤30 MB; ≤20 สกิล/คำขอ), versions เป็น snapshot เต็ม | แยก workspace ไม่แชร์กับ claude.ai/Code | 6 ฟิลด์เดิม; ต้องเปิด code execution; mount ที่ `/skills/{name}/` | `container.skills[]` ใน `/v1/messages` | ไม่มี registry สาธารณะ | platform.claude.com/docs/en/build-with-claude/skills-guide | OFFICIAL |
| OpenClaw (เดิม Clawdbot → Moltbot) | roots เรียงลำดับ: `<workspace>/skills`, `<workspace>/.agents/skills`, **`~/.agents/skills`**, `~/.openclaw/skills`, bundled, `skills.load.extraDirs`; `openclaw skills install @owner/slug [--global]`; `clawhub install` / `clawhub skill publish` | ไม่อ่าน `.claude/skills`; อ่าน `~/.agents/skills` ร่วมกับ Codex | บังคับ `name, description`; เพิ่มได้ `user-invocable`, `disable-model-invocation`, `command-dispatch`; `metadata.openclaw` เป็น map ซ้อน (requires.bins/env, install, os) ซึ่งเกินกฎ string→string ของ spec | `$skill-name` ใน composer (ไม่ใช่ `/`) | ClawHub (clawhub.ai) | docs.openclaw.ai/tools/skills, docs.openclaw.ai/tools/clawhub | OFFICIAL (ประวัติเปลี่ยนชื่อ: PRACTITIONER) |
| ChatGPT (web/desktop) | Skills › Create › upload หรือ `@skill-creator`; beta สำหรับ Business/Enterprise/Edu; plugins รวมสกิล | แยก ไม่ sync ข้ามผลิตภัณฑ์ | `name, description`; ส่วนเพิ่มของ OpenAI อยู่ใน sidecar `agents/openai.yaml` ไม่ใช่ frontmatter | `@skill` หรืออัตโนมัติ (Codex: `$`, `/skills`) | ไม่พบ registry สาธารณะ | learn.chatgpt.com/docs/build-skills, academy.openai.com (2026-09-17) | OFFICIAL (help-center บางส่วนจาก snippet) |
| Microsoft Copilot Studio | Build › Skills › Upload `.md` หรือ ZIP ที่มี `SKILL.md` **ที่ root** | แยก | ล้มเมื่อ YAML ผิด, ขาด name/description, description ยาวเกิน (ไม่ระบุตัวเลข), ชื่อซ้ำ | เลือกอัตโนมัติเท่านั้น | ต่อ agent | learn.microsoft.com/.../skills-add-existing (2026-10-21) | OFFICIAL |
| Perplexity Computer | Plugins › Add custom › upload `.md`/`.zip` (SKILL.md ที่ root; ≤20 MB, ≤100 ไฟล์) | แยก | ตาม spec | อัตโนมัติเท่านั้น | ต่อบัญชี | perplexity.ai/help-center/en/articles/13914413 | OFFICIAL |
| Manus / Mastra / CrewAI / LangChain deepagents / Microsoft Agent Framework | รับโฟลเดอร์ SKILL.md ตาม spec (Manus: upload/GitHub URL; Mastra/CrewAI/deepagents: path ใน code; Agent Framework: `SkillsProvider`) | แยก | ตาม spec; Agent Framework ข้าม `metadata` ที่ซ้อน | ต่างกัน | CrewAI มี registry ของ org | manus.im/docs, mastra.ai/docs/skills, docs.crewai.com, docs.langchain.com, learn.microsoft.com/agent-framework (2026-10-23) | OFFICIAL |
| Agent Skills standard (agentskills.io) | โฟลเดอร์ + `SKILL.md` (+ `scripts/ references/ assets/`); SKILL.md < 500 บรรทัด | n/a | `name` 1–64 `a-z0-9-` ต้องเท่าชื่อโฟลเดอร์; `description` 1–1,024; `license`; `compatibility` ≤500; `metadata` string→string; `allowed-tools` (experimental) | progressive disclosure | Client showcase 46 ราย; validator `skills-ref` | agentskills.io/specification, agentskills.io/clients (repo push ล่าสุด 2026-08-09) | OFFICIAL |
| Notion / Zapier / n8n / Genspark | Notion export เป็น SKILL.md ได้แต่ไม่ import; Zapier publish สกิลแต่ไม่พบว่า Zapier Agents โหลด; n8n เป็น feature request; Genspark ไม่พบ import | — | — | — | — | notion.com/help/skills-for-notion-agent, zapier.com/blog/agent-skills | NOT FOUND (runtime) |

### 5.3 สิ่งที่ยังยืนยันไม่ได้

- รูปแบบไฟล์ `.plugin` ของ Cowork นอกจาก "รับคู่กับ `.zip`"
- Cowork ที่ติดตั้งผ่าน marketplace เข้มกับฟิลด์ frontmatter นอก spec เท่า claude.ai upload หรือไม่ (เอกสารระบุรายการฟิลด์เฉพาะทาง upload/API)
- OpenAI help center ตอบ 403; รายละเอียดแผน/วันเปิด default มาจาก snippet
- ประวัติชื่อ Clawdbot → Moltbot → OpenClaw (ม.ค. 2026) มีแต่แหล่งรอง เอกสารทางการยืนยันผ่าน `metadata.clawdbot` legacy เท่านั้น

## 6. สถาปัตยกรรมที่เสนอ: body เดียว adapter บาง installer แยก host

หลักการ: `plugins/<pillar>/skills/<name>/SKILL.md` เป็น body เดียว (เหมือนเดิม) ทุก host ได้ไฟล์เดียวกันผ่าน link/copy ส่วนที่ต่างกันต่อ host อยู่ใน adapter ที่ generate ได้ ไม่ใช่สำเนา body

| ชั้น | สิ่งที่ทำ | หมายเหตุ |
|---|---|---|
| 0. Canonical body | frontmatter เหลือ 6 ฟิลด์ตาม spec; `kind`, `pillar`, `schema` ย้ายเข้า `metadata` (string ทั้งหมด); `scripts/` อ้างด้วย path สัมพัทธ์ภายในสกิลตัวเอง; ถ้อยคำเรียกใช้ใน body เป็นกลาง (Claude `/`, ChatGPT `@`, OpenClaw `$`, Copilot Studio/Perplexity อัตโนมัติ) | ปลดล็อก claude.ai, Skills API, Copilot Studio, Perplexity, ChatGPT ในครั้งเดียว |
| 1. Claude family | GitHub marketplace เดิมสำหรับคนอื่น + Cowork (Add marketplace `theeranon/JamesSkills`); เครื่อง James ใช้ local-path marketplace ให้โหลด in place; ลบ `commands/` หลัง verify; ตรวจไม่มี `bin/` ระดับบน | Cowork และ Claude Code ได้ของเดียวกันผ่านบัญชี (`@synced`) |
| 2. Agent Skills hosts (Codex, Cursor, Antigravity, Gemini CLI, Copilot, Devin/Windsurf, OpenCode, Amp, Kiro, Factory, Junie, Roo, Cline, OpenClaw) | installer เดิมขยายเป็น table ของ host → **private dir หรือ native plugin ที่เอกสารรับรอง** (เช่น Codex plugin, `~/.cursor/plugins/local`, `~/.gemini/config/skills`, `~/.copilot/skills`, `~/.kiro/skills`, `~/.openclaw/skills`) พร้อม copy mode สำรองสำหรับ host ที่ไม่ตาม symlink และ evidence column (filesystem / UI / invocation) ต่อ host; Agent Plugins root `plugin.json` ต่อ pillar สำหรับ host ที่รับ plugin | ไม่ใช้ `~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills` ที่หลาย tool สแกนพร้อมกัน; `npx skills add` เป็นทางสำรองเฉพาะ host ที่ไม่มี adapter และต้องยอมรับความเสี่ยงแถวซ้ำ |
| 3. Packagers | `scripts/package` หนึ่งตัวมี `--layout`: `name/SKILL.md` (claude.ai), `SKILL.md` ที่ root (Copilot Studio, Perplexity, Skills API), pillar zip (OpenAI portal เดิม); OpenClaw: generate `SKILL.md` ที่เติม `metadata.openclaw` เมื่อจำเป็น (ไม่ symlink ของเดิม) หรือ publish ClawHub | ซ้ำกับ `scripts/package-plugins` และ `scripts/export` บางส่วน รวมเป็นตัวเดียวได้ |
| 4. Always-on parity | `adapters/` (ตอนนี้ว่าง) เก็บตัว generate: `CLAUDE.md` import, `~/.codex/AGENTS.md` block, Cursor User Rules, `GEMINI.md`, OpenClaw `AGENTS.md`/`SOUL.md` จากต้นทางเดียว (`proactive-habits` + กฎ "คำบ่น = คำสั่งแก้") | ตอนนี้ Codex ใช้ไฟล์เขียนมือ, Cursor/Gemini/Antigravity ไม่มี |
| 5. Doctor | รายงานต่อ host เป็น 3 คอลัมน์ (ไฟล์มี / UI เห็น / เรียกแล้วทำงาน) และ fail เมื่อ host ที่ประกาศว่าครอบคลุมไม่มีสกิลเลย (กรณี C2) | ตรงกับ `docs/ecosystem-installation.md` ที่เขียนไว้แล้วแต่ยังไม่ได้ทำ |

## 7. ลำดับงานที่เสนอและสิ่งที่ต้องให้ James ตัดสิน

**P0 ทำได้เลย ไม่เปลี่ยนชื่อ/scope สกิล**
1. Reconcile งาน local (DEC-049/050) กับ STATUS 2.1.14 แล้ว commit เป็นชุดเดียว พร้อมปิดช่องว่าง Codex: ติดตั้ง Codex native plugin บนเครื่องนี้, ให้ `codex_skills.reconcile` หา binary ที่ bundled ใน ChatGPT.app เมื่อ `codex` ไม่อยู่บน PATH, และให้ doctor fail (ไม่ใช่ SKIP) เมื่อ Codex มี JamesSkills เป็นศูนย์; ตัด `~/.gemini/antigravity/custom/skills` ที่ไม่มีในเอกสารออกจาก installer
2. ย้าย `kind:` → `metadata.kind` ทั้ง 23 ไฟล์ + `docs/SKILL-SCHEMA.md` + `tests/test_skill_schema.py` + `scripts/validate` แล้วรัน `claude plugin validate plugins/<pillar>` และ `skills-ref validate`
3. แก้ `insight-driven-mode`: ตัด "generic or translated" ออกจาก description, ยุบ "Do not use" ที่ซ้ำกับ "Works with" (C1)
4. เครื่อง James: เพิ่ม marketplace จาก local path แล้วติดตั้งใหม่ให้โหลด in place; ถอด symlink ที่ทับ cache (C4)
5. ตั้ง `skillListingBudgetFraction` และ name-only ให้สกิลที่ไม่ใช้; รัน `/doctor` ดูต้นทุน listing (E1)

**P1 ลด duplicate (ไม่เปลี่ยนพฤติกรรม)**
6. Format boundary เหลือเจ้าของเดียวใน `make-it-james-ux` ตัวอื่นชี้ไป; แก้ `AGENTS.md` ให้เรียกชื่อเจ้าของถูก (C8)
7. `lint_outcome.py` เหลือสำเนาเดียว ให้อีกสกิลเรียกผ่านการโหลดสกิลเจ้าของ เหมือนที่ทำกับ font helper (C9)
8. ย่อหน้า delegation และ Windows line เหลือที่เดียว (C7, C16); แก้หมวด `coach-me` ใน docs/README (C12); README ระบุทั้ง `/plugin:skill` และ bare name (C17)
9. Verify บน Desktop binary ว่า plugin skills ขึ้น picker โดยไม่มี `commands/` แล้วลบ 23 ไฟล์ + comment ใน `package-plugins` (C11)

**P2 ต้องการคำตัดสินของเจ้าของ (REQ-004)**
- A. ชื่อและ scope ของ `insight-driven-mode` (คงชื่อ / เปลี่ยนเป็นวลีธรรมชาติ เช่น `insight-first`) และยืนยันว่าอนุมัติเอง
- B. alias `solutionsimpact-*`: ปลดออกจาก repo (ให้บัญชี claude.ai เป็นเจ้าของชื่อ) หรือลบสกิลในบัญชีแล้วให้ alias ชนะ (C3)
- C. `hand-it-off`: คงติดตั้ง / `user-invocable: false` / เก็บเป็น docs อย่างเดียว (C10)
- D. รวม `are-you-sure` + `dev-are-you-sure` เป็นตัวเดียวสอง lens หรือคงสองชื่อ (C6)
- E. host ที่ต้อง "ครอบคลุม" ใน 2.2: Cowork, Codex, Cursor, Antigravity, Gemini CLI, OpenClaw, Copilot, ChatGPT ตัวไหนบ้าง และยืนยันยุทธศาสตร์ private dir / native plugin ต่อ host (ต่อยอด DEC-050) โดยไม่ใช้ `~/.agents/skills` ซึ่งหลักฐานในหัวข้อ 5.1.1 ชี้ว่าจะโชว์ซ้ำกับ Cursor และ Amp
- F. อนุมัติให้สร้าง `scripts/package --layout` และ `adapters/` generator ตามหัวข้อ 6

## 8. ขอบเขตและข้อจำกัดของ audit นี้

- อ่านไฟล์และเอกสารเป็นหลัก ไม่ได้รัน behavioral probe ตัวเลขทั้งหมดเป็นขนาดไฟล์/จำนวนรายการ ไม่ใช่อัตราทริกเกอร์
- สถานะติดตั้งตรวจบนเครื่องนี้เครื่องเดียว (macOS, Claude Desktop binary 2.1.308/2.1.309, Cursor.app, ChatGPT.app ที่มี Codex, ไม่พบ Antigravity.app แต่มี `~/.gemini/antigravity` และ `~/.gemini/config/skills`)
- ค่าใน `skills-doc` ของ Claude Code อ่านจากหน้าเอกสาร ณ วันนี้ เวอร์ชันเปลี่ยนเร็ว ควร re-check ก่อนทำ P0-4
- ข้อเสนอในหัวข้อ 6–7 เป็นข้อเสนอ ไม่ใช่การตัดสินใจ ตาม `AGENTS.md` การเปลี่ยนชื่อ ขอบเขต lifecycle หรือ alias ต้องผ่าน Candidate Card และการอนุมัติของเจ้าของ
