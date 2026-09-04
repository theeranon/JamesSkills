#!/usr/bin/env node
/* Forward-render the three transformation-design skills against two real project cases. */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { execFileSync } = require("child_process");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright-core");

const repo = path.resolve(__dirname, "..");
const cliArgs = process.argv.slice(2);
let outputArg = null;
let receiptArg = null;
for (let index = 0; index < cliArgs.length; index += 1) {
  if (cliArgs[index] === "--receipt") {
    receiptArg = cliArgs[index + 1];
    index += 1;
  } else if (!outputArg) {
    outputArg = cliArgs[index];
  } else {
    throw new Error(`unexpected argument: ${cliArgs[index]}`);
  }
}
const outputDir = path.resolve(outputArg || path.join(repo, ".qa-artifacts", "v0.9.0"));
const receiptPath = receiptArg ? path.resolve(receiptArg) : null;
const python = process.env.PYTHON || "python3";
const chromeCandidates = [
  process.env.CHROME_PATH,
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "/Applications/Chromium.app/Contents/MacOS/Chromium",
  "/usr/bin/google-chrome",
  "/usr/bin/google-chrome-stable",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser",
  process.env.LOCALAPPDATA && path.join(process.env.LOCALAPPDATA, "Google/Chrome/Application/chrome.exe"),
  process.env.PROGRAMFILES && path.join(process.env.PROGRAMFILES, "Google/Chrome/Application/chrome.exe")
].filter(Boolean);
const chrome = chromeCandidates.find((candidate) => fs.existsSync(candidate));
if (!chrome) {
  throw new Error("Chrome or Chromium not found; set CHROME_PATH to its executable");
}
const embedder = path.join(repo, "plugins/james-core/rules/make-it-james/scripts/embed_ibm_plex_thai.py");
const linter = path.join(repo, "plugins/james-core/rules/make-it-james/scripts/lint_outcome.py");
const receiptInputs = [
  "package.json",
  "package-lock.json",
  path.relative(repo, embedder),
  path.relative(repo, linter)
];

function esc(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function fill(template, values, slug) {
  const seen = new Set();
  const html = template.replace(/\[\[([A-Z0-9_]+)\]\]/g, (_whole, key) => {
    seen.add(key);
    if (!(key in values)) throw new Error(`${slug}: missing fixture value ${key}`);
    return esc(values[key]);
  });
  const unused = Object.keys(values).filter((key) => !seen.has(key));
  if (unused.length) throw new Error(`${slug}: unused fixture values ${unused.join(", ")}`);
  if (/\[\[|\]\]|TODO|PLACEHOLDER/.test(html)) throw new Error(`${slug}: unresolved template residue`);
  return html;
}

function replaceRows(html, section, rows) {
  const pattern = new RegExp(`(<section[^>]*data-section="${section}"[\\s\\S]*?<tbody>)[\\s\\S]*?(</tbody>)`);
  if (!pattern.test(html)) throw new Error(`section table not found: ${section}`);
  return html.replace(pattern, `$1\n${rows}\n$2`);
}

function tableRows(rows, labels) {
  return rows.map((row) => `<tr>${row.map((cell, index) =>
    `<td data-label="${esc(labels[index])}">${esc(cell)}</td>`
  ).join("")}</tr>`).join("\n");
}

function sha256(filePath) {
  return crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
}

const frameworkValues = {
  FRAMEWORK_REPORT_TITLE: "คำตัดสิน Build Framework ใช้ Pattern เดิม ไม่สร้าง Framework ใหม่",
  RECURRING_PROBLEM_AND_BUSINESS_REASON: "ต้องมีโครงสร้างที่พาองค์กรจากการตื่นตัวเรื่อง AI ไปสู่ผลงานจริง หลักฐานการนำไปใช้ และคำตัดสินระดับองค์กร โดยไม่สร้างชื่อ Framework ใหม่ซ้ำกับของที่มีอยู่แล้ว",
  RECOMMENDED_WORKING_NAME: "Five-Phase Transformation Pattern",
  FRAMEWORK_LIFECYCLE: "kind pattern / version offer-reference-2026-08-12 / lifecycle pilot / AI offer scope",
  FRAMEWORK_OWNER: "SolutionsIMPACT",
  FRAMEWORK_VERSION: "offer-reference 2026-08-12",
  EXECUTIVE_RECOMMENDATION_AND_DECISION_REQUEST: "ใช้ Five-Phase Transformation Pattern ต่อในขอบเขต pilot ของ AI Transformation offer และไม่สร้าง Framework ใหม่ รอบนี้ไม่ยกระดับ pattern เป็น framework หรือ approved company law ส่วน Leadership และ Business ต้องมีหลักฐานของ offer นั้นก่อนนำไปใช้",
  HOUSE_FRAMEWORK_ID: "solutionsimpact-five-phase-transformation-pattern",
  FIT_EVIDENCE: "Registry และ offer reference ระบุหน้าที่ Diagnose, Workshop, Coaching, Showcase และ Transform ตรงกับ Journey นี้",
  FIT_LIMITATION: "หลักฐานครบเฉพาะ AI Transformation offer และวัตถุนี้เป็น pattern ไม่ใช่ full framework",
  USE_UPGRADE_OR_BUILD: "Use existing pattern within pilot boundary; do not build a new framework",
  RESEARCH_SYNTHESIS_WITH_COMPETING_EVIDENCE: "หลักฐานภายในสองชั้นสอดคล้องกัน คือ offer reference ที่บันทึกหน้าที่และ handoff ของแต่ละ phase กับหน้า offer ที่เผยแพร่โครงสร้างห้าระยะ ข้อจำกัดคือหลักฐานนี้ยืนยันความสอดคล้องของข้อเสนอ ไม่ได้พิสูจน์ผลลัพธ์ของลูกค้าหรือสิทธิ์นำไปครอบ Leadership และ Business",
  CLAIM_01: "AI Transformation offer ใช้โครงสร้างห้าระยะจาก Diagnose ถึง Transform และคงหน้าที่หลักครบทุกขนาดโครงการ",
  SOURCE_01_ID: "SRC-AITJ-OFFER-2026-08",
  EVIDENCE_01: "Offer reference และหน้า offer ระบุ phase responsibilities, evidence handoff และ sizing boundary ตรงกัน",
  LIMITATION_01: "เป็น owner source ไม่ใช่ independent effectiveness study",
  FRAMEWORK_PROMISE_AND_BOUNDARY: "Pattern นี้จัดลำดับการเปลี่ยนผ่านระดับองค์กรและหลักฐานระหว่าง phase ใช้เมื่อ accountable outcome คือ AI transformation ไม่ใช่ full framework และไม่ใช้แทน Learning Experience Design ภายในแต่ละ workshop",
  CONSTRUCT_01_NAME: "Diagnose",
  CONSTRUCT_01_LOGIC: "ล็อก baseline, scope, segmentation และเกณฑ์สำเร็จก่อนลงทุนออกแบบ intervention",
  CONSTRUCT_02_NAME: "Build and Apply",
  CONSTRUCT_02_LOGIC: "Workshop และ Coaching ต้องผลิต use case จริงแล้วพาไปสู่การนำไปใช้ ไม่หยุดที่ความเข้าใจ",
  CONSTRUCT_03_NAME: "Decide and Transform",
  CONSTRUCT_03_LOGIC: "Showcase รวมหลักฐานให้ผู้นำตัดสิน และ Transform สรุป asset, impact กับ next-stage decision",
  THREE_NAME_OPTIONS_AND_RECOMMENDATION: "ไม่เปิดการตั้งชื่อใหม่ เพราะ house pattern เดิมแก้โจทย์นี้ได้โดยไม่ต้องสร้าง framework ชื่อที่ใช้ต่อคือ Five-Phase Transformation Pattern และ label การตลาดเปลี่ยนได้โดยไม่เปลี่ยน logic",
  REPEATABLE_DECISION_OR_OPERATING_LOGIC: "Baseline ก่อน intervention; ทุก phase ต้องมี output, evidence, owner, exit และ handoff; งานเรียนรู้ส่งหลักฐานกลับ Journey; ผู้นำใช้ evidence ตัดสิน scale, repair หรือ stop",
  SCENARIO_01: "AI Transformation ระดับหนึ่งหน่วยงาน",
  APPLICATION_01: "ใช้ pattern ครบห้าหน้าที่โดยลดความเข้มของ Workshop",
  PROOF_01: "Sizing pattern ระบุว่า S ยังคง Diagnose, Coaching, Showcase และ Transform",
  RESULT_01: "อยู่ในขอบเขต pilot pattern",
  COUNTER_CASE: "Leadership Transformation ที่ยังไม่มี approved offer reference",
  WHY_NOT_APPLY: "ห้ามยก phase names ไปใช้เพียงเพราะเป็น transformation เหมือนกัน",
  COUNTER_EVIDENCE: "Registry จำกัด complete contract ไว้ที่ AI offer",
  BOUNDARY_RESULT: "กลับไปตรวจ house library หรือใช้ build-framework",
  APPROVE_CHANGE_OR_REJECT: "Continue bounded pilot pattern; no new framework",
  APPROVER: "James ตาม authority record เดิม",
  EFFECTIVE_VERSION_AND_DATE: "คง offer-reference 2026-08-12; QA 2026-08-29",
  SOURCE_01_LOCATOR: "JamesSkills/skills/core/transformation-journey/references/ai-transformation-five-phase.md, PersonalBiz/business/cable-organizers/outputs/solutionsimpact_ai_transformation_journey_corporate_en.html",
  SOURCE_01_CLASS: "owner-approved offer reference and published derivative",
  SOURCE_01_RIGHTS: "reviewed-private และ internal published derivative",
  SOURCE_01_RETRIEVED: "2026-08-29",
  SOURCE_01_CONFIDENCE: "สูงต่อโครงสร้าง offer แต่ไม่ใช้แทนหลักฐานผลลัพธ์ลูกค้า",
  SOURCE_01_CITATION_AND_SUPPORTED_CLAIM: "SolutionsIMPACT. AI Transformation Offer Five-Phase Reference และ AI Transformation Journey corporate offer. รองรับเฉพาะโครงสร้าง phase, sizing และ evidence handoff ที่ระบุในรายงานนี้"
};

const journeyValues = {
  JOURNEY_TITLE: "AI Transformation Journey จากความตื่นตัวสู่หลักฐานระดับองค์กร",
  ORGANIZATION_A_TO_B_AND_WHY_NOW: "จากองค์กรที่มี workshop และการทดลอง AI กระจัดกระจาย ไปสู่องค์กรที่มี baseline, use case ที่นำไปใช้จริง, reusable assets และคำตัดสินขั้นต่อไปจากหลักฐาน",
  JOURNEY_ID: "AITJ-FORWARD-TEST-001",
  JOURNEY_REVISION: "0.1 forward-test",
  FRAMEWORK_ID_AND_VERSION: "solutionsimpact-five-phase-transformation-pattern / version offer-reference-2026-08-12 / kind pattern / lifecycle pilot / AI offer scope",
  SPONSOR_AND_DECISION_OWNER: "Executive sponsor ของลูกค้า; ชื่อบุคคลยังเป็น decision gap",
  EXECUTIVE_BUSINESS_OUTCOME_AND_DECISION: "Journey ต้องทำให้ผู้บริหารเห็นว่า AI เปลี่ยนงานใด ผลิต asset อะไร ถูกนำไปใช้แค่ไหน และควร scale, repair หรือ stop ตรงไหน ไม่ใช้คะแนนความพึงพอใจเป็นผลลัพธ์ปลายทาง",
  CONTRACT_SOURCE_SCOPE_ASSUMPTIONS_AND_GAPS: "Authority มาจาก SolutionsIMPACT AI Transformation offer และ five-phase reference ขอบเขตครอบ Diagnose ถึง Transform ส่วนจำนวนผู้เข้าร่วม ระยะเวลา เป้าหมายเชิงตัวเลข เจ้าของ use case และงบประมาณต้องยืนยันรายลูกค้าก่อนผลิต proposal",
  REAL_WORK_OUTPUT: "ผู้เข้าร่วมแต่ละคนส่ง use case หรือ workflow ที่ผูกกับงานจริง พร้อม baseline และเกณฑ์วัด",
  WORK_APPLICATION_EVIDENCE: "Coaching บันทึกการทดลองใช้ การแก้ blocker การเปลี่ยน workflow และหลักฐานก่อนหลัง",
  ORGANIZATION_OR_BUSINESS_EVIDENCE: "Transformation Report รวมผลตามหน่วยงาน asset ที่องค์กรถือครอง และข้อเสนอ scale, repair หรือ stop",
  SATISFACTION_BREADCRUMB_AND_LIMITATION: "Room signal และ satisfaction ใช้ปรับ facilitation เท่านั้น ไม่ถือเป็นหลักฐาน transformation",
  PHASE_01: "Diagnose",
  PHASE_01_OBJECTIVE: "สร้าง baseline และล็อก scope",
  PHASE_01_INPUT: "โจทย์ธุรกิจ กลุ่มเป้าหมาย และข้อมูล readiness",
  PHASE_01_INTERVENTION: "Survey, AI IMPACT Level Assessment และ sponsor alignment",
  PHASE_01_OUTPUT_EVIDENCE_EXIT: "Baseline report, segmentation และ success measures; ออกได้เมื่อ sponsor รับรอง scope",
  PHASE_01_OWNER_HANDOFF_FALLBACK: "SolutionsIMPACT lead ส่ง design brief ให้ LED; ถ้าข้อมูลไม่ครบใช้ provisional skeleton และระบุ gap",
  OFFER_REFERENCE_OR_PROVISIONAL_PHASE_GUARD: "ใช้ห้าระยะเพราะมี approved source สำหรับ AI Transformation offer เท่านั้น ไม่ขยายเป็นกฎของ Leadership หรือ Business โดยอัตโนมัติ",
  INTERVENTION_01_ID: "LED-AI-WORKSHOP-01",
  INTERVENTION_01_PHASE: "Workshop",
  INTERVENTION_01_BRIEF: "ออกแบบ bounded learning experience ที่ให้ผู้เข้าร่วมสร้าง use case จริงจาก baseline ของตน",
  INTERVENTION_01_FRAMEWORK_ID_VERSION: "house framework ที่ยืนยันภายหลัง diagnosis; ห้ามเดาชื่อ TPS components",
  INTERVENTION_01_EVIDENCE: "use case brief, current workflow, target change, metric และ coaching handoff",
  CADENCE_COACHING_GOVERNANCE_RISK_AND_ADAPTATION: "Review ราย phase ใช้ evidence เป็นตัวเปลี่ยน intervention; Coaching 3 ถึง 5 ครั้งเป็น offer default ที่ต้องยืนยัน ไม่ใช่จำนวนตายตัว ความเสี่ยงหลักคือ use case เป็น demo, baseline วัดไม่ได้ และ owner ไม่มีอำนาจนำไปใช้",
  PROMISE_01: "ทุกคนออกจากโปรแกรมพร้อม use case ที่ผูกกับงานจริง",
  PROMISE_01_SOURCE: "AI Transformation corporate offer",
  PROMISE_01_DESTINATION: "Workshop และ Coaching",
  PROMISE_01_EVIDENCE: "use case artifact, baseline, implementation log",
  PROMISE_01_OWNER: "Participant กับ coach; sponsor owns adoption gate",
  PROMISE_01_STATUS: "Provisional จนยืนยัน contract และ cohort",
  LEADERSHIP_DECISION_AND_NEXT_STAGE: "อนุมัติ Journey Skeleton นี้เป็น forward-test ของ skill เท่านั้น งานลูกค้าจริงยังต้องเติม sponsor, cohort, baseline, target metric, timeline และ commercial scope ก่อนถือว่า delivery-ready",
  SOURCE_01_ID: "SRC-AITJ-OFFER-2026-08",
  SOURCE_01_LOCATOR: "PersonalBiz/business/cable-organizers/outputs/solutionsimpact_ai_transformation_journey_corporate_en.html, JamesSkills/skills/core/transformation-journey/references/ai-transformation-five-phase.md",
  SOURCE_01_CLASS: "owner-approved offer reference and published derivative",
  SOURCE_01_CLAIM_USED: "AI Transformation offer ใช้ห้าหน้าที่จาก Diagnose ถึง Transform พร้อม evidence handoff และ sizing boundary",
  SOURCE_01_LIMITATION: "ยืนยันโครงสร้าง offer ไม่ได้พิสูจน์ผลลัพธ์ลูกค้าและไม่อนุญาตให้ครอบ domain อื่น",
  SOURCE_01_RIGHTS: "reviewed-private และ internal published derivative",
  SOURCE_01_RETRIEVED: "2026-08-29",
  SOURCE_01_CONFIDENCE: "สูงต่อ offer structure แต่ตัวเลขผลลัพธ์ยังต้องมี delivery evidence",
  SOURCE_01_CITATION_AND_SUPPORTED_CLAIM: "SolutionsIMPACT AI Transformation offer. รองรับ five-phase structure, sizing pattern, use-case outputs, coaching defaults และ final Transformation Report ตามขอบเขตที่ระบุ"
};

const ledValues = {
  LEARNING_EXPERIENCE_TITLE: "Codex Browser Research Sprint สำหรับเจ้าของธุรกิจ",
  LEARNER_BUSINESS_TENSION_AND_PURPOSE: "เจ้าของธุรกิจต้องตัดสินใจจากข้อมูลหลายเว็บ แต่เสียเวลารวบรวมและมักจบด้วยข้อมูลดิบที่ยังใช้ต่อไม่ได้ Workshop สองชั่วโมงนี้จึงต้องทำให้ผู้เรียนผลิต research pack ที่มี judgment และ next action",
  LEARNING_DESIGN_ID: "LED-CODEX-BROWSER-001",
  LEARNING_DESIGN_REVISION: "0.1 forward-test",
  FRAMEWORK_ID_AND_VERSION: "ไม่มี approved full framework ใช้ candidate principle solutionsimpact-outcome-based-learning version candidate-2026-08-29 และ candidate pattern solutionsimpact-before-during-after version candidate-2026-08-29 เป็น provisional reversible skeleton เท่านั้น",
  OPTIONAL_PARENT_JOURNEY_REFERENCE: "ไม่มี; เป็น bounded workshop ไม่ได้ถือ outcome ระดับองค์กร",
  LEARNING_PROMISE_BOUNDARY_AND_IMPACT_LINK: "หลังสองชั่วโมง ผู้เรียนผลิต pack หนึ่งชุดจากตัวเลือก Competitor, Supplier หรือ Partnership ที่มี comparison, evidence, unknowns และข้อความติดต่อพร้อมใช้ ขอบเขตไม่สัญญาว่าดีลจะสำเร็จหรือข้อมูลสาธารณะจะครบ",
  SOURCE_LEARNER_CONTEXT_CONSTRAINTS_AND_GAPS: "Authority คือ Workshop V12 ซึ่งล็อกสามตัวเลือกและ agenda สองชั่วโมงแล้ว ยังไม่ทราบจำนวนผู้เรียน ระดับทักษะ เครื่องที่ใช้ บัญชีเข้าเว็บ และอุตสาหกรรม จึงออกแบบ fallback ให้ทำจากเว็บสาธารณะและลดจำนวน target เมื่อเวลาไม่พอ",
  OBSERVABLE_STATE_A: "ค้นเว็บเป็นรายครั้ง เก็บข้อมูลไม่เป็นโครง และยังแยก fact, unknown กับ inference ไม่ชัด",
  BARRIER_OR_MISCONCEPTION: "คิดว่าข้อมูลออนไลน์ไม่ครบคือ blocker หรือให้ AI เดาราคาและรายละเอียดที่หาไม่เจอ",
  OBSERVABLE_STATE_B: "เลือก lane ที่เหมาะ เปิดหลายแหล่ง บันทึก evidence และ unknown ให้ชัด แล้วผลิต pack กับ outreach ที่ทีมใช้ต่อได้",
  TENSION_LEARNER_A_BARRIER_B_EVIDENCE_ARTIFACT_SEQUENCE: "เริ่มจากโจทย์ตัดสินใจจริง เลือกหนึ่ง lane สาธิตการแยก visible, missing และ inference ให้ผู้เรียนทำ sprint กับ target จริง ตรวจ evidence ก่อนให้คะแนน แล้วจบด้วย pack และข้อความติดต่อ ไม่เริ่มจากการสอนปุ่มหรือผลิต slide",
  TIME_BLOCK_01: "Before",
  INTENT_01: "เตรียมโจทย์จริงและ target ตั้งต้น",
  LEARNER_ACTION_01: "เลือก lane และเขียน requirement ที่ต้องใช้ตัดสินใจ",
  OUTPUT_01: "research brief หนึ่งย่อหน้า",
  EVIDENCE_01: "มี decision, criteria และขอบเขตที่ตรวจได้",
  FALLBACK_01: "ใช้ sample category ที่ไม่ต้อง login เมื่อโจทย์จริงยังไม่พร้อม",
  LEARNER_STATE_FACILITATOR_MOVE_EXPECTED_SIGNAL_AND_RECOVERY: "ถ้าผู้เรียนติดการค้นหา ให้ facilitator ลด scope เหลือสาม target และย้ำ evidence grid ถ้าข้อมูลหายากให้เปลี่ยนเป้าหมายจาก final comparison เป็น shortlist กับคำถามที่ต้องติดต่อ ถ้า browser tool ล่มให้ทำ manual browser walkthrough แล้วคง output contract เดิม",
  REQUESTED_ITEM_01: "สอน Browser Use",
  KEEP_TRANSFORM_DEFER_OR_REJECT: "Transform",
  CAUSAL_REASON_01: "เครื่องมือเป็นวิธีทำ ไม่ใช่ผลลัพธ์ จึงสอนผ่านการผลิต research pack จริง",
  DESTINATION_01: "Demo 10 นาทีและ Sprint 45 นาที",
  TRAINER_TA_ASSET_TIMING_RISK_AND_ECONOMICS: "Trainer ต้องมี demo ที่ใช้เว็บสาธารณะ TA ต้องช่วยตรวจ evidence กับ unknown ไม่ใช่แก้ prompt แทนผู้เรียน ต้องมี offline worksheet และ sample targets ความเสี่ยงสูงสุดคือ login, website variance, ผู้เรียนเลือกโจทย์กว้าง และ polish pack ไม่ทัน",
  PRODUCED_EVIDENCE: "comparison table, fit score, red flags, missing-info questions, outreach draft และ next-step checklist",
  APPLIED_EVIDENCE: "ภายในเจ็ดวัน ผู้เรียนส่ง RFQ, inquiry หรือ internal decision brief อย่างน้อยหนึ่งรายการและบันทึกผล",
  IMPACT_EVIDENCE: "วัดเวลาที่ลดลง คุณภาพ shortlist หรือ decision cycle จากงานจริงหลัง workshop; ยังไม่ claim ใน forward-test นี้",
  SATISFACTION_OR_ROOM_SIGNAL: "ใช้ความมั่นใจและ room signal เพื่อปรับ pace เท่านั้น",
  POST_DELIVERY_OBSERVATION_AND_REUSABLE_CANDIDATE: "เก็บว่าผู้เรียน lane ใดติดตรงไหน target จำนวนเท่าใดพอดี และ outreach ถูกนำไปใช้หรือไม่ ส่ง pattern ที่เกิดซ้ำข้ามอุตสาหกรรมให้ build-framework ตรวจ library ก่อนสร้างของใหม่",
  DESIGN_DECISIONS_AND_EXACT_OPEN_GATE: "LED Skeleton ผ่าน causal check และรักษา output เดิมของ V12 งาน delivery จริงยังต้องยืนยัน cohort, device, tool access, industry examples และเจ้าของ follow-up evidence จากนั้นจึงผลิต facilitator guide กับ participant worksheet",
  SOURCE_01_ID: "SRC-CODEX-WORKSHOP-V12",
  SOURCE_01_LOCATOR: "PersonalBiz/business/codex-workshop/CODEX_WORKSHOP_V12_THREE_OPTION_BROWSER_RESEARCH_SPRINT_TH.md",
  SOURCE_01_CLASS: "current internal course design source",
  SOURCE_01_CLAIM_USED: "Workshop V12 ล็อกสามทางเลือก agenda สองชั่วโมง และ research pack ที่แยก evidence, unknown กับ next action",
  SOURCE_01_LIMITATION: "เป็น design source ที่ยังไม่พิสูจน์ delivery effectiveness หรือ impact หลังนำไปใช้",
  SOURCE_01_RIGHTS: "reviewed-private",
  SOURCE_01_RETRIEVED: "2026-08-29",
  SOURCE_01_CONFIDENCE: "สูงต่อ workshop frame และ agenda แต่ delivery effectiveness ยังไม่ถูกพิสูจน์",
  SOURCE_01_CITATION_AND_SUPPORTED_CLAIM: "SolutionsIMPACT. Codex Workshop V12 Three-Option Browser Research Sprint. รองรับ three-lane choice, two-hour agenda, evidence-first research pack และ sparse-data fallback"
};

const cases = [
  {
    slug: "ai-transformation-framework-decision",
    template: "skills/core/build-framework/assets/framework-decision-report.html",
    values: frameworkValues,
    augment(html) {
      return replaceRows(html, "scenarios", tableRows([
        ["AI Transformation ขนาด S", "คงห้าหน้าที่ ลดเฉพาะ Workshop intensity", "Offer sizing pattern", "อยู่ในขอบเขต pilot pattern"],
        ["AI Transformation ขนาด L", "คงห้าหน้าที่ เพิ่ม cohort และ cross-unit coordination", "Offer sizing pattern", "อยู่ในขอบเขต pilot pattern"],
        ["AI Transformation ขนาด XL", "คงห้าหน้าที่และ parallel cohorts", "Offer sizing pattern", "อยู่ในขอบเขต pilot pattern"],
        ["Leadership Transformation ที่ยังไม่มี approved source", "ไม่ใช้ phase model นี้โดยอัตโนมัติ", "Registry boundary", "ตรวจของเดิมหรือเสนอ build-framework"]
      ], ["กรณี", "การใช้ Model", "หลักฐาน", "ผล"]));
    }
  },
  {
    slug: "ai-transformation-journey",
    template: "skills/core/transformation-journey/assets/transformation-journey-blueprint.html",
    values: journeyValues,
    augment(html) {
      const rows = [
        ["Diagnose", "สร้าง baseline และล็อก scope", "โจทย์ธุรกิจและ readiness data", "Survey, assessment, sponsor alignment", "Baseline, segmentation, measures; sponsor confirms", "Journey lead ส่ง LED brief; fallback เป็น provisional skeleton"],
        ["Workshop", "สร้าง capability ผ่านงานจริง", "Baseline และ segmented needs", "Bounded LED interventions", "Use cases, workflows, metrics, coaching briefs", "LED owner ส่ง evidence ให้ coach; ลด scope ไม่ลด evidence"],
        ["Coaching", "พา use case ผ่าน blocker ไปสู่ implementation", "Artifacts และ coaching briefs", "Mentor review, experiment, repair", "Implementation log, risks, owner actions", "Coach ส่ง showcase-ready evidence; stalled case escalates"],
        ["Showcase", "รวมหลักฐานและให้ผู้นำตัดสิน", "Implemented cases และ comparable metrics", "Pitching day และ cross-unit exchange", "Decision surface, selected assets, scale criteria", "Sponsor ตัดสิน scale, repair หรือ stop"],
        ["Transform", "สรุป impact และ next-stage strategy", "Baseline, application evidence, decisions", "Transformation report และ strategy consultation", "Organization assets, impact comparison, next-stage decision", "องค์กรรับ ownership; gaps กลับเป็น roadmap"]
      ];
      return replaceRows(html, "macro-map", tableRows(rows, ["Phase", "Objective", "Input", "Intervention", "Output and evidence", "Owner and handoff"]));
    }
  },
  {
    slug: "codex-browser-research-learning-design",
    template: "skills/core/learning-experience-design/assets/learning-experience-design-pack.html",
    values: ledValues,
    augment(html) {
      const rows = [
        ["Before", "ล็อกโจทย์ตัดสินใจ", "เลือกหนึ่ง lane และเตรียม target", "Research brief", "Decision, criteria, boundary", "ใช้ sample category ที่ไม่ต้อง login"],
        ["During", "สร้าง evidence-first pack", "เปิดเว็บจริง 3 ถึง 10 target แยก visible, missing, inference และ score", "Comparison, shortlist, questions, outreach", "Source link ต่อ claim และ unknown ไม่ถูกเดา", "ลด target เหลือสามหรือใช้ manual browser"],
        ["After", "ย้าย artifact เข้างานจริง", "ส่ง RFQ, inquiry หรือ internal brief", "Action log และ response", "Applied evidence ภายในเจ็ดวัน", "Manager review หรือ peer follow-up"]
      ];
      return replaceRows(html, "experience-map", tableRows(rows, ["ช่วง", "Intent", "Learner action", "Output", "Evidence", "Fallback"]));
    }
  }
];

async function main() {
  fs.mkdirSync(outputDir, { recursive: true });
  const outputs = [];

  for (const item of cases) {
    const source = fs.readFileSync(path.join(repo, item.template), "utf8");
    let html = fill(source, item.values, item.slug);
    html = item.augment(html);
    const staging = path.join(outputDir, `${item.slug}.unembedded.html`);
    const finalHtml = path.join(outputDir, `${item.slug}.html`);
    fs.writeFileSync(staging, html, "utf8");
    execFileSync(python, [embedder, staging, "--output", finalHtml], { stdio: "inherit" });
    fs.unlinkSync(staging);
    outputs.push({ ...item, finalHtml });
  }

  execFileSync(python, [linter, "--strict", ...outputs.map((item) => item.finalHtml)], { stdio: "inherit" });

  const browser = await chromium.launch({ headless: true, executablePath: chrome });
  const browserVersion = browser.version();
  const report = [];
  try {
    for (const item of outputs) {
      const context = await browser.newContext({ viewport: { width: 1440, height: 1200 }, deviceScaleFactor: 1 });
      const page = await context.newPage();
      const remoteRequests = [];
      await page.route(/https?:\/\//, async (route) => {
        remoteRequests.push(route.request().url());
        await route.abort();
      });
      await page.goto(pathToFileURL(item.finalHtml).href, { waitUntil: "load" });
      await page.evaluate(async () => {
        await Promise.all([400, 500, 600, 700].map((weight) =>
          document.fonts.load(`${weight} 16px "IBM Plex Sans Thai"`)
        ));
        await document.fonts.ready;
      });
      const metrics = await page.evaluate(() => {
        const root = document.documentElement;
        const reportNode = document.querySelector(".report");
        const faces = Array.from(document.fonts).filter((font) => font.family.includes("IBM Plex Sans Thai"));
        const overflowNodes = Array.from(document.querySelectorAll("table, dl, figure, section"))
          .filter((node) => node.scrollWidth > node.clientWidth + 1)
          .map((node) => `${node.tagName.toLowerCase()}${node.dataset.section ? `[${node.dataset.section}]` : ""}`);
        return {
          contract: reportNode?.dataset.contract || null,
          fontDeclared: getComputedStyle(document.body).fontFamily.includes("IBM Plex Sans Thai"),
          fontLoaded: document.fonts.check('16px "IBM Plex Sans Thai"'),
          loadedFaceCount: faces.filter((font) => font.status === "loaded").length,
          unresolvedTokens: /\[\[|\]\]|TODO|PLACEHOLDER/.test(document.body.innerText),
          viewportWidthFits: root.scrollWidth <= root.clientWidth + 1,
          reportWidthFits: reportNode.scrollWidth <= reportNode.clientWidth + 1,
          overflowNodes,
          bodyTextLength: document.body.innerText.trim().length,
          sourceLedgerRows: document.querySelectorAll('[data-section="source-trace"] .source-ledger > div').length,
          sourceLedgerText: document.querySelector('[data-section="source-trace"]')?.innerText || ""
        };
      });

      const screenshot = path.join(outputDir, `${item.slug}.png`);
      await page.screenshot({ path: screenshot, fullPage: true });
      await page.setViewportSize({ width: 390, height: 844 });
      const mobileScreenshot = path.join(outputDir, `${item.slug}.mobile.png`);
      await page.screenshot({ path: mobileScreenshot, fullPage: true });
      const mobile = await page.evaluate(() => {
        const root = document.documentElement;
        const reportNode = document.querySelector(".report");
        const tableNodes = Array.from(document.querySelectorAll(".table-scroll table, .table-scroll tbody, .table-scroll tbody tr, .table-scroll tbody td"));
        const cells = Array.from(document.querySelectorAll(".table-scroll td"));
        return {
          viewportWidthFits: root.scrollWidth <= root.clientWidth + 1,
          reportWidthFits: reportNode.scrollWidth <= reportNode.clientWidth + 1,
          tableCount: document.querySelectorAll(".table-scroll table").length,
          tableOverflowNodes: tableNodes.filter((node) => node.scrollWidth > node.clientWidth + 1).length,
          unlabeledCells: cells.filter((cell) => !cell.dataset.label).length,
          unstackedCells: cells.filter((cell) => getComputedStyle(cell).display !== "grid").length
        };
      });
      await page.emulateMedia({ media: "print" });
      await page.setViewportSize({ width: 794, height: 1123 });
      const printScreenshot = path.join(outputDir, `${item.slug}.print.png`);
      await page.screenshot({ path: printScreenshot, fullPage: true });
      const print = await page.evaluate(() => {
        const root = document.documentElement;
        const reportNode = document.querySelector(".report");
        const overflowNodes = Array.from(document.querySelectorAll("table, dl, figure, section"))
          .filter((node) => node.scrollWidth > node.clientWidth + 1).length;
        return {
          viewportWidthFits: root.scrollWidth <= root.clientWidth + 1,
          reportWidthFits: reportNode.scrollWidth <= reportNode.clientWidth + 1,
          overflowNodes,
          bodyBackground: getComputedStyle(document.body).backgroundColor,
          reportMargin: getComputedStyle(reportNode).margin,
          text: document.body.innerText
        };
      });
      await context.close();

      const title = item.values.FRAMEWORK_REPORT_TITLE || item.values.JOURNEY_TITLE || item.values.LEARNING_EXPERIENCE_TITLE;
      const normalizeText = (text) => text.normalize("NFC").replace(/\s+/g, "");
      const titleInPrint = normalizeText(print.text).includes(normalizeText(title));
      const visibleSourceValues = [
        item.values.SOURCE_01_ID,
        item.values.SOURCE_01_LOCATOR,
        item.values.SOURCE_01_CLASS,
        item.values.SOURCE_01_RIGHTS,
        item.values.SOURCE_01_RETRIEVED,
        item.values.SOURCE_01_CONFIDENCE
      ];
      const visibleSourceLedger = metrics.sourceLedgerRows >= 8 &&
        visibleSourceValues.every((value) => metrics.sourceLedgerText.includes(value));
      const ok = metrics.fontDeclared && metrics.fontLoaded && metrics.loadedFaceCount >= 4 &&
        !metrics.unresolvedTokens && metrics.viewportWidthFits && metrics.reportWidthFits &&
        metrics.overflowNodes.length === 0 && metrics.bodyTextLength > 800 && visibleSourceLedger &&
        mobile.viewportWidthFits && mobile.reportWidthFits && mobile.tableCount >= 1 &&
        mobile.tableOverflowNodes === 0 && mobile.unlabeledCells === 0 && mobile.unstackedCells === 0 &&
        print.viewportWidthFits && print.reportWidthFits && print.overflowNodes === 0 &&
        print.bodyBackground === "rgb(255, 255, 255)" && print.reportMargin === "0px" && titleInPrint &&
        remoteRequests.length === 0;
      delete print.text;
      report.push({ slug: item.slug, ok, metrics, mobile, print, visibleSourceLedger, remoteRequests, titleInPrint, html: item.finalHtml, screenshot, mobileScreenshot, printScreenshot });
    }
  } finally {
    await browser.close();
  }

  const reportPath = path.join(outputDir, "qa-report.json");
  const generatedAt = new Date().toISOString();
  fs.writeFileSync(reportPath, JSON.stringify({ generated_at: generatedAt, pdf_generated: false, cases: report }, null, 2) + "\n", "utf8");
  if (receiptPath) {
    fs.mkdirSync(path.dirname(receiptPath), { recursive: true });
    const receipt = {
      schema_version: 1,
      release: "0.9.0",
      generated_at: generatedAt,
      browser: `Chromium ${browserVersion}`,
      pdf_generated: false,
      renderer: {
        path: path.relative(repo, __filename),
        sha256: sha256(__filename)
      },
      inputs: receiptInputs.map((inputPath) => ({
        path: inputPath,
        sha256: sha256(path.join(repo, inputPath))
      })),
      templates: cases.map((item) => ({
        path: item.template,
        sha256: sha256(path.join(repo, item.template))
      })),
      cases: report.map((item) => ({
        slug: item.slug,
        ok: item.ok,
        loaded_font_faces: item.metrics.loadedFaceCount,
        unresolved_tokens: item.metrics.unresolvedTokens,
        desktop_overflow_nodes: item.metrics.overflowNodes.length,
        desktop_width_fits: item.metrics.viewportWidthFits && item.metrics.reportWidthFits,
        mobile_overflow_nodes: item.mobile.tableOverflowNodes,
        mobile_width_fits: item.mobile.viewportWidthFits && item.mobile.reportWidthFits,
        mobile_unlabeled_cells: item.mobile.unlabeledCells,
        mobile_unstacked_cells: item.mobile.unstackedCells,
        print_overflow_nodes: item.print.overflowNodes,
        print_width_fits: item.print.viewportWidthFits && item.print.reportWidthFits,
        title_visible_in_print: item.titleInPrint,
        visible_source_ledger: item.visibleSourceLedger,
        remote_request_count: item.remoteRequests.length
      }))
    };
    fs.writeFileSync(receiptPath, JSON.stringify(receipt, null, 2) + "\n", "utf8");
  }
  for (const item of report) {
    console.log(`${item.ok ? "PASS" : "FAIL"} ${item.slug} fonts=${item.metrics.loadedFaceCount} screen_overflow=${item.metrics.overflowNodes.length} print_overflow=${item.print.overflowNodes}`);
  }
  if (report.some((item) => !item.ok)) process.exitCode = 1;
  else console.log(`PASS forward-render cases=${report.length} projects=2 pdf_generated=false report=${reportPath}${receiptPath ? ` receipt=${receiptPath}` : ""}`);
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exit(1);
});
