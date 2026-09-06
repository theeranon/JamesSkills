# พัฒนา JamesSkills ด้วยผลลัพธ์ที่วัดได้

วันที่ตรวจ: 2026-09-06 · สถานะ: เจ้าของอนุมัติแล้ว; มี runner และ 15 public probes ยังไม่มีคะแนนคุณภาพ

**ข้อเสนอ:** ให้ทั้ง 22 skill มี benchmark ตามหน้าที่ แล้วปรับเฉพาะจุดที่ทำให้งานจริงดีขึ้นเมื่อเทียบกับรุ่นเดิมและการไม่ใช้ skill วัดคุณภาพ ต้นทุน ความสม่ำเสมอ และงานแก้ของผู้ใช้แยกกัน ใช้ข้อสอบที่ผู้ปรับ skill ไม่เคยเห็นเพื่อตรวจว่าผลดีขยายไปยังงานใหม่หรือไม่

มี runner และ public probes สำหรับ 5 skill แรกแล้ว การเรียกโมเดลสองครั้งไม่คืนคำตอบเพราะ Claude CLI ยังไม่ได้ login จึงไม่มีผลเปรียบเทียบคุณภาพ และยังไม่แก้ canonical skill ตัวเลขจากงานวิจัยไม่ใช่คะแนน JamesSkills

## ผลลัพธ์ที่ต้องการและคอขวด

| ระดับ | คำตอบ |
|---|---|
| เป้าหมายของผู้ใช้ | ได้งานที่ใช้ต่อได้ ถูกต้อง และไม่ต้องสั่งซ้ำ โดย agent ตัดสินใจอยู่ในสิทธิ์ที่มี |
| ระบบทั้งหมด | เลือก skill ถูก → โหลดคำสั่งถูกฉบับ → ทำงานตามหน้าที่ → ส่งผลลัพธ์ที่ตรวจได้ → รักษาผลเมื่อเปลี่ยนงานหรือ model |
| คอขวดที่ตรวจพบ | มี structural gates และ helper tests แต่ยังไม่มีผลเปรียบเทียบ model ราย skill ที่บอกได้ว่าคำสั่งส่วนใดช่วยหรือรบกวนงาน |
| กลยุทธ์ | สร้างเครื่องมือวัดจากผลที่ผู้รับต้องใช้ แล้วทดลองเปลี่ยนทีละกลไก พร้อมชุดกันถอยหลังและชุดงานใหม่ |
| ของเดิมที่ใช้ต่อ | canonical SKILL.md, catalog, ขอบเขต sibling, behavioral cases ที่ทบทวนแล้ว, helper tests, validate, doctor และ runtime receipts |

เพดานที่ตรวจสอบได้: ทุก skill มีหน้าที่และเกณฑ์ผ่านชัด มี baseline เทียบได้ และมีหลักฐานว่าการปรับปรุงช่วยงานใหม่ภายใต้งบที่ระบุ คำว่า “ดีที่สุด” หมายถึงดีที่สุดในขอบเขตงาน model และงบที่ทดลอง ไม่ใช่ชนะได้ทุกสถานการณ์

ข้อกำหนดที่รองรับคือ REQ-008; ต้องรักษา REQ-001 เรื่องคำสั่งต้นฉบับเดียว, REQ-004 เรื่องชื่อและ lifecycle และ REQ-007 เรื่องข้อมูลใน repository ไม่เพิ่ม skill ใหม่หรือเปลี่ยนหน้าที่ของ skill ผ่าน benchmark โดยปริยาย

## สิ่งที่ตรวจจาก repository

ฐานตรวจคือ commit `fb6643aedd167349ad70d8b6e5db50b31a26fb8f` บน `main` ก่อนเพิ่มเอกสารนี้ มี 22 canonical skills และ 9 aliases ตาม [catalog](../catalog.json) ไม่ควรนับ alias เป็นอีกหนึ่งความสามารถ

ผลตรวจฐานเดิม: `scripts/validate` exit 0 และ `scripts/doctor` exit 0; doctor พบ native/shared pairs 22, unresolved 0 และ managed links 126 นี่เป็นหลักฐานจาก local validator และ Codex app-server ไม่ใช่คะแนนการทำงานของทั้ง 22 skill

มี test scripts ระดับ repository 11 ไฟล์ และ helper test scripts 7 ไฟล์ใน 5 skill หลายชุดทดสอบ filesystem, Git, parser และ linter จริง จึงไม่ควรเรียกรวมว่าเป็น mocks ทั้งหมด ส่วน behavioral document มี 25 sections / 30 Request labels ซึ่งเป็นข้อกำหนดการทดสอบ ไม่ใช่ 30 ผลรัน model; receipt ปัจจุบันมี model invocation ของ `proactive-habits` หนึ่งกรณีและ packaged helper ของ `baseon` แยกกัน ดู [validator](../scripts/validate), [test contracts](../tests/test_core_composition_contracts.py) และ [runtime receipt](../tests/receipts/install-discovery-2026-09-05.md)

[SKILL-SCHEMA](SKILL-SCHEMA.md) ระบุเองว่าตรวจโครงสร้าง ไม่ได้ตัดสินว่าคำสั่งใช้งานได้จริงหรือขอบเขตมีเหตุผล การมีคนชี้เข้าหา skill ใน boundary graph จึงเป็นเงื่อนไขโครงสร้างที่มีประโยชน์ แต่ไม่ใช่หลักฐานว่า skill นั้นมีคุณค่าหรือไม่ overfit

พบตัวอย่างที่ต้องทบทวนก่อนใช้เป็นคำตอบอ้างอิง:

| ตำแหน่ง | สิ่งที่ไม่ตรงกับ canonical ปัจจุบัน | ผลต่อ benchmark |
|---|---|---|
| [behavioral-cases: Catchup Request C](../tests/behavioral-cases.md#catchup--catchup) | ส่ง isolated deployment claim ไป `prove-it` ซึ่งปัจจุบัน alias ไป `research-it`; canonical กำหนดให้ `dev-are-you-sure` รับงานนี้ | ถ้าใช้เป็น gold จะให้คะแนนการส่งงานผิดคน |
| [behavioral-cases: Make It James](../tests/behavioral-cases.md#make-it-james--make-it-james) | รวม font, radius และ rendered dashboard ไว้ใต้ wording skill; งาน visual เป็นของ `make-it-james-ux` | ต้องแยกการให้คะแนนรายเจ้าของ หรือระบุว่าเป็น composition case |

เก็บเป็นข้อค้นพบในรอบนี้ การปรับ test cases ต้องตาม canonical ที่ยอมรับแล้ว หากข้อกำหนดเองขัดกัน ให้แยกเป็นเรื่องตัดสินใจ ไม่ให้คนเขียนข้อสอบเปลี่ยนหน้าที่ skill เอง

## คำถามวิจัยและคำตัดสิน

**ข้ออ้างที่ทดสอบได้:** การปรับ skill จากผลทดลองที่แยกตามหน้าที่ จะเพิ่มผลสำเร็จบนงานใหม่ หรือคงคุณภาพไว้ด้วยต้นทุนต่ำลง โดยไม่เพิ่มการทำผิดขอบเขต

หลักฐานหักล้างคือ รุ่นใหม่ชนะเฉพาะข้อสอบที่ใช้ปรับ แต่ไม่ชนะงานที่กันไว้; คะแนนเพิ่มเพราะ judge ชอบรูปแบบคำตอบ; งานถูกชะลอหรือถูกปฏิเสธมากขึ้น; หรือผลดีหายไปเมื่อใช้ใน runtime จริง

**คำตัดสิน: conditional.** มีหลักฐานรองรับวิธีทดลอง แต่ยังไม่มีหลักฐานว่า JamesSkills ทั้ง 22 จะดีขึ้นด้วยวิธีเดียวกัน ต้องวัดรายหน้าที่และรายสภาพแวดล้อม

| ชั้นหลักฐาน | สิ่งที่สรุปได้ |
|---|---|
| ข้อเท็จจริงที่ตรวจในรอบนี้ | โครงสร้างและหน้าที่ของชุดปัจจุบัน รวมถึง gold-case drift สองจุดข้างต้น |
| ข้ออ้างจากผู้พัฒนา | Anthropic แยก skill ที่เพิ่มความสามารถออกจาก skill ที่รักษาวิธีทำงาน และเสนอวัดการ trigger, pass rate, เวลา, token และ blind A/B [ประกาศ 2026-03-03](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) |
| หลักฐานจากผู้ทดลองอื่น | SkillsBench v4 รายงานค่าเฉลี่ยเพิ่ม 16.6 percentage points ใน 87 งาน แต่ SWE-Skills-Bench พบ 39 จาก 49 skill ไม่เพิ่ม pass rate ภายใต้การทดลองของตน [SkillsBench](https://arxiv.org/abs/2602.12670v4), [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401v1) |
| ข้ออนุมานสำหรับโครงการนี้ | ต้องแยกประโยชน์ด้านความสามารถออกจากการรักษาข้อกำหนดของผู้ใช้ และยอมรับผล “ไม่ช่วย” โดยไม่แต่งคำอธิบายเพื่อให้ทุก skill ดูจำเป็น |

งานแรกเป็น terminal/container benchmark ส่วนงานที่สองใช้ Claude Code กับ Haiku 4.5 เพียง configuration เดียว จึงนำเปอร์เซ็นต์มาเป็นเป้าหมายของงานภาษาไทย การ coaching หรือ persistent modes ไม่ได้ การศึกษาการค้นหา skill จากคลังใหญ่ยังพบว่าผลดีลดลงเมื่อเงื่อนไขใกล้การใช้งานจริงขึ้น [งานวิจัย 2026-04-06](https://arxiv.org/abs/2604.04323v1)

## Benchmark ตามหน้าที่

รายละเอียดครบอยู่ใน [benchmark cards ทั้ง 22 skill](skill-benchmark-cards.md) แต่ละใบกำหนดผลที่ต้องเกิด ตัวหารของ metric หลักฐานที่ตรวจ ตัวอย่างปกติ ตัวอย่างกลไกเดียวกันในอีกบริบท และ counter-case ที่ต้องยังทำได้ถูกต้อง

แยกการทดสอบ 5 ชั้น เพื่อให้รู้ว่าควรปรับตรงไหน:

| ชั้น | สิ่งที่วัด | สิ่งที่ห้ามอ้างแทน |
|---|---|---|
| โครงสร้าง | catalog, schema, link, helper correctness | ไฟล์ครบไม่แปลว่า model ใช้ได้ดี |
| การเลือกใช้ | precision/recall ของการเลือก owner, false trigger และการไม่ใช้เมื่อไม่ควรใช้ | การบังคับโหลด skill ไม่พิสูจน์การเลือกอัตโนมัติ |
| การทำงาน | ผลงานหรือ state จริงเมื่อโหลด skill ที่ถูกต้อง | ทวน checklist ครบไม่เท่ากับงานสำเร็จ |
| การทำงานร่วมกัน | owner + standard + mode ทำงานร่วมกันโดยไม่ขัดกัน รวมการเปลี่ยนคำสั่งหลาย turn | ผ่านเดี่ยวทุกตัวไม่พิสูจน์ว่ารวมแล้วดี |
| การขยายผล | งานคนละกลุ่ม ภาษา แหล่งข้อมูล และ runtime ที่ระบุชัด | ผ่านบน model เดียวไม่ใช่ cross-platform proof |

แยกอัตราทำงานที่อนุญาตและทำได้สำเร็จ ออกจากอัตราทำเกินสิทธิ์ด้วย มิฉะนั้น agent ที่ถามทุกอย่างหรือไม่ทำอะไรเลยอาจดูปลอดภัยและได้คะแนนสูง

## วิธีเทียบที่ตอบได้ว่าอะไรช่วยจริง

ใช้โจทย์ ทรัพยากร และเกณฑ์ผลลัพธ์เดียวกันในแต่ละคู่ เปลี่ยนเฉพาะสิ่งที่กำลังทดสอบ:

| เงื่อนไข | ใช้ตอบอะไร |
|---|---|
| A: ไม่มี James skill ที่ทดสอบ | model กับเครื่องมือเดิมทำงานได้แค่ไหน |
| B: skill ปัจจุบันที่ตรึง hash | สิ่งที่ใช้อยู่เพิ่มคุณค่าเหนือ A เท่าไร |
| C: candidate ที่ตรึง hash | การแก้เพิ่มคุณค่าเหนือ B เท่าไร และยังคุ้มเมื่อเทียบ A หรือไม่ |

ทำสอง track แยกกัน: บังคับโหลดเพื่อวัด execution และปล่อยให้เลือกจาก catalog เพื่อวัด routing พร้อมผลลัพธ์ปลายทาง การทดสอบ shared standard ให้ primary workflow คงเดิมแล้วถอด/เพิ่มเฉพาะ standard นั้น ส่วน baseline ของทั้ง portfolio ค่อยทดสอบแยกอีกครั้ง

ทุก run เริ่มด้วยบริบทและสภาพไฟล์ใหม่ ตรึง model/version, host/harness, effort, tools, fixtures, time limit และ environment เท่าที่ควบคุมได้ สุ่มลำดับ A/B/C ภายในช่วงเวลาเดียวกัน บันทึกปัจจัยที่ตรึงไม่ได้ เช่น provider drift และ cache การ fork บทสนทนานี้ใช้เป็น no-skill baseline ไม่ได้ เพราะคำสั่งและตัวอย่างถูกโหลดแล้ว

การวัดผลเพิ่มจาก skill เดียวต้องถอด canonical พร้อม alias และ discovery copies ของตัวนั้นออกจาก A แต่คง skill อื่นและ primary owner เท่ากัน บันทึก inventory ที่โหลดจริงเพื่อจับ cached copies การถอดทั้ง portfolio เป็นอีกการทดลองหนึ่ง ห้ามใช้แทนผลเพิ่มจากตัวเดียว Natural-routing prompts ไม่ระบุชื่อ skill เป้าหมาย ส่วนคำขอที่ระบุชื่อใช้ตรวจ explicit invocation แยกกัน

Baseline ต้องมีข้อมูลจำเป็นและสิทธิ์ในการทำงานเท่ากัน ห้ามให้เฉพาะฝั่ง skill เข้าถึง source หรือ tool ที่จำเป็นแล้วเรียกผลนั้นว่าประโยชน์จากคำสั่ง ถ้าต้องการวัดประโยชน์ของ resource ที่บรรจุใน package ให้รายงานว่าเป็นผลของ package และทำ resource-only ablation เพิ่มเมื่อต้องแยกสาเหตุ

สำหรับ preference skills ให้ A ได้ข้อกำหนดผู้รับที่จำเป็นต่อโจทย์เหมือนกัน แต่ไม่ให้ขั้นตอนเฉพาะของ skill; รายงานทั้ง task success และ workflow fidelity ไม่สรุปว่าควรถอดมาตรฐานของผู้ใช้เพียงเพราะ generic task pass เท่ากัน

## กัน overfit ทั้งจำข้อสอบและหลงเป้าหมาย

เจ้าของขยายความวันที่ 2026-09-06: overfit รวมการหมกมุ่นกับสิ่งที่ไม่ใช่เป้าหมายสูงสุด การโฟกัสผิดจุด และ overengineering ด้วย แยกสองกลไกเพื่อซ่อมตรงสาเหตุ: ไม่ generalize ไปงานใหม่ กับปรับตัวชี้วัดย่อยจนงานผู้ใช้เสียประโยชน์

ทุก benchmark ระบุผลที่ผู้ใช้ต้องนำไปใช้ ประเมิน goal alignment และ proportionality แยกจากความถูกต้อง สั่งแก้ยอดรวมหนึ่งจุดแล้วสร้าง dashboard ใหม่ แม้สวยก็ไม่ผ่านเป้าหมาย แต่ระบบเงินจริงที่ต้องตรวจหลายแหล่งไม่ควรถูกหักเพราะขั้นตอนมาก

ความยาว จำนวนเครื่องมือ และจำนวน test ไม่ใช่คะแนนคุณภาพโดยตัวเอง ขั้นตอนเพิ่มต้องช่วยผลลัพธ์ ลดความเสี่ยงจริง หรือปลดคอขวด หากผลลัพธ์หลักไม่สำเร็จ ห้ามใช้คะแนนรูปแบบมาชดเชย ทั้ง 15 probes มีกรณีผิดเป้าหมาย กรณีถ่ายโอนกลไก และกรณีซับซ้อนที่จำเป็น

## กันการจำข้อสอบตั้งแต่ข้อมูลจนถึงการตัดสินใจ

| กลไก | วิธีใช้จริง |
|---|---|
| แบ่งตามที่มา | แบ่ง development / selection / holdout ตาม source lineage และ scenario family ก่อน paraphrase; แปลไทยเป็นอังกฤษหรือเปลี่ยนชื่อคนยังอยู่กลุ่มเดิม |
| กันข้อสอบออกจากผู้ปรับ | builder/optimizer ไม่เห็น holdout; solver เห็นเฉพาะโจทย์และข้อมูลที่งานต้องใช้; grader/เฉลยอยู่นอก sandbox คำว่า “อย่าอ่าน” ใน prompt ไม่ใช่การแยกสิทธิ์ |
| จำกัดการเลือกซ้ำ | freeze candidate และ grader ก่อนเปิด holdout ถ้าเอาผลไปปรับอีก ให้ประกาศ holdout นั้นถูกใช้แล้วและสร้างกลุ่มใหม่ ไม่แอบสอบซ้ำจนผ่าน |
| เปลี่ยนสิ่งที่ไม่ควรเปลี่ยนผล | เปลี่ยนชื่อ ลำดับ agenda สำนวน ภาษา รูปแบบ source; เพิ่มข้อมูลขัดกันหรือ tool failure; คำตอบต้องปรับตามข้อเท็จจริง ไม่ตามคำที่จำมา |
| ทดสอบสิ่งที่ดูคล้ายแต่ควรทำต่างกัน | งานไม่มี defect ต้องไม่สร้าง defect; การอนุญาตส่งงานจริงต้องไม่ถูกบล็อกตลอดไป; explicit PDF ยังถูกทำได้; งานใหม่ที่มี design system ต้องไม่ถูกบังคับ house style |

ชุดข้อสอบสาธารณะใน Git ใช้เป็น development/regression ได้ แต่ห้ามอ้างว่าเป็น holdout ที่ไม่เคยเห็น การสร้างชุดใหม่ต้องมี independent author หรือผู้ดูแลที่ไม่ส่งเฉลยให้ผู้ปรับ skill; ข้อมูลลูกค้าและบทสนทนาจริงไม่เข้า Git ใช้ fixtures สังเคราะห์จากกลไกปัญหาที่ผ่านการตรวจสิทธิ์แล้ว

ใน environment ที่ agent อ่าน filesystem ได้ทั้งหมด การย้ายไปอีก directory ยังไม่ป้องกันการเห็นข้อสอบ Future runner ต้องบังคับ isolation จริง เช่น mount เฉพาะ task assets; คลัง holdout, expected route, gold และ grader ไม่อยู่ในสิทธิ์ของ solver ส่วนโจทย์ที่ถูกเลือกและ source ที่จำเป็นต้องส่งให้ solver ตามปกติ

ให้คนละคนหรือ agent คนละบริบทออกข้อสอบกับแก้ skill ตรวจ gold จาก contract ก่อนดู candidate และลองให้วิธีแก้ที่ถูกต้องต่างรูปแบบผ่านได้ ข้อสอบที่ตัดสินไม่ได้ต้องมีสถานะ disputed/unknown พร้อมเหตุผล ไม่ถูกนับเป็น pass เงียบ ๆ

## ให้คะแนนโดยไม่เปิดช่องให้เล่นกับตัววัด

วัดผลที่ตรวจได้ก่อน: ไฟล์เปิดได้ ข้อมูลครบ source รองรับ สิทธิ์ไม่เปลี่ยน persistence จริง และไม่มี diff นอก scope ใช้ judge สำหรับความหมายและการอ่านรู้เรื่องที่ตรวจด้วย code ไม่พอ ส่วน trace ใช้ตรวจ authority และเงื่อนไขกระบวนการที่ contract กำหนด ไม่บังคับลำดับ tool call ตามใจคนออกข้อสอบ

ก่อนเชื่อ judge ให้ใช้ output ที่คนตรวจแล้วทั้งผ่านและไม่ผ่าน จัดแบบ blind pair และสลับลำดับ ตรวจ false accept กับ false reject แยกกัน พร้อมระบุจำนวนตัวอย่างภาษาไทย การที่ judge หลายตัวเห็นตรงกันไม่แทนการเทียบกับผู้รับจริง

ต้องลองหลอกตัวตรวจด้วยงานที่หน้าตาดีแต่ผิด เช่น สรุปที่แต่ง owner, โค้ดที่ hardcode fixture, HTML ที่ตัดข้อมูลเพื่อให้พอดีหน้า และรายงานที่เขียน “verified” โดยไม่มีหลักฐาน พร้อมใส่งานถูกต้องที่ใช้โครงสร้างต่างจากตัวอย่างเพื่อจับ judge ที่ตึงเกินไป

รายงานผลแต่ละ skill เป็น 5 ช่อง:

| ช่อง | นิยาม |
|---|---|
| ผลสำเร็จตามหน้าที่ | อัตรา episode ที่ผ่าน acceptance ทั้งหมด; diagnostic รายข้อแยกต่างหาก ห้ามเปลี่ยนจำนวนข้อเพื่อเพิ่มคะแนน |
| ความผิดพลาดสำคัญ | fabricated fact/evidence, เกินสิทธิ์, ทำลายข้อมูล, ผิด owner ที่พาไปทำผิดงาน; แสดงจำนวนจริงและ denominator |
| ความสม่ำเสมอ | pass ต่อ trial และจำนวนกรณีที่ผ่านครบทุกครั้ง ไม่ใช้ best-of-many แทน first-attempt success |
| ต้นทุน | token ทั้ง run รวม retry/tool context, elapsed time และค่าใช้จ่ายที่วัดได้; ถ้าไม่มีราคาให้ระบุไม่ทราบ ห้ามใส่ศูนย์ |
| ภาระผู้ใช้ | จำนวนการสั่งซ้ำ การแก้ที่จำเป็น และเวลาที่ผู้รับใช้จนยอมรับงาน; proxy จาก judge ต้องแยกจากเวลาที่คนทำจริง |

เปรียบเทียบแบบ paired และสรุป uncertainty ที่ระดับ scenario/source group; รันโจทย์เดิม 3 ครั้งไม่ใช่ 3 แหล่งข้อมูลอิสระ กลุ่มตัวอย่างน้อยให้บอกว่าผลยังไม่ชัด เพิ่มความหลากหลายก่อนเพิ่มการรันโจทย์เดิมอย่างเดียว

ไม่ทำคะแนนรวมเดียวที่ให้ความสวยชดเชยข้อเท็จจริงผิด หรือ token ที่ลดลงชดเชยการทำเกินสิทธิ์ รายงานราย skill และ slice ภาษา/ความยาก/บริบท พร้อม macro average แบบระบุ weighting ล่วงหน้า หากรันทดสอบไม่ครบ ให้เห็น coverage และสาเหตุ ตัด provider outage ตามกฎที่เขียนไว้ก่อน พร้อมเก็บ log; timeout ที่ใช้งบครบตามโจทย์เป็นผลไม่สำเร็จ ไม่ถูกลบทิ้ง

ให้ case author กำหนด feasibility และสิทธิ์จาก fixture ก่อนรัน ไม่ให้ agent ลด denominator โดยบอกว่างานยากนั้นทำไม่ได้ Refusal, unjustified blocked และ malformed output เป็นผลล้มเหลวในกรณีที่กำหนดว่าทำได้ หากเป็น harness outage จริงตามกฎที่ตรึงไว้ ให้รันคู่เปรียบเทียบใหม่ร่วมกันและเก็บทุก attempt

## Optimize และ maximize คนละเป้าหมาย

**Optimize:** คุณภาพอยู่ในเกณฑ์เดิมด้วยเวลา token หรือการแก้ของผู้ใช้ที่ลดลง **Maximize:** เพิ่มคุณภาพสูงสุดภายใต้งบและขอบเขตที่ตกลงไว้ งานยากอาจสมควรใช้ token เพิ่ม ทั้งสองแบบต้องรักษา authority และความถูกต้อง

| ลำดับทดลอง | สมมติฐานที่ทดสอบ | วิธีป้องกันการปรับผิดเรื่อง |
|---|---|---|
| ปรับ description | เลือก owner ได้แม่นขึ้น | วัดทั้ง missed trigger และ false trigger บนคำขอที่ดูคล้ายกัน |
| ตัดความซ้ำและโหลด reference เมื่อต้องใช้ | ลด context โดยไม่เสีย outcome | เก็บ scope, source, stop และ counter-case ตาม schema; เทียบ full กับ compact แบบ paired |
| ทำ helper สำหรับงานเชิงกลที่ผิดซ้ำ | งานซ้ำที่ตรวจได้มีความแน่นอนขึ้น | ทดสอบ input ใหม่และ invalid input; helper ไม่ตัดสินสิทธิ์แทน agent |
| ปรับขั้นตอนที่ก่อ failure จริง | เพิ่มผลสำเร็จข้ามบริบท | แก้กลไก ไม่เติมชื่อ ไฟล์ ตัวเลข หรือเฉลยจากข้อสอบลง SKILL.md |
| ปรับการประกอบ skill | ลดคำสั่งขัดกันและงานเกินจำเป็น | ทดสอบ owner + mode + standard และการส่งงานข้าม stage; ไม่โหลดทุก skill เป็นค่าเริ่มต้น |

เสนอใช้ manual error analysis และ ablation ก่อน optimizer อัตโนมัติ GEPA หรือเครื่องมือคล้ายกันอาจช่วยสร้าง candidate แต่ไม่มีสิทธิ์แก้ gold, เปิด holdout, เปลี่ยนขอบเขต skill หรือปล่อย release เอง ผลจาก optimizer เป็นสมมติฐานรอการตรวจ ไม่ใช่การรับรองคุณภาพ

กำหนด primary metric และการเปลี่ยนที่คุ้มค่าไว้ก่อนรัน เช่น จำนวนการแก้ที่ลดลงซึ่งมีผลต่อผู้ใช้ หรือคุณภาพเพิ่มภายใต้ budget จากนั้นคัด candidate ที่ไม่ถูกอีกตัวครอบงำทั้งด้านคุณภาพและต้นทุน ไม่ใช้คำว่า “เร็วที่สุด” หรือ “แม่นที่สุด” โดยไม่ระบุเงื่อนไข

ก่อนเรียก candidate ว่าดีกว่า ให้ผล paired บนงานที่กันไว้รองรับ minimum worthwhile effect ที่กำหนด ไม่มี critical boundary failure ที่สังเกตพบ และไม่มี counter-case regression ที่ไม่ยอมรับ การอ้างว่าคุณภาพเท่าเดิมแต่ถูกลงต้องมี non-inferiority margin พร้อมหลักฐานเพียงพอ; “ยังไม่พบความต่าง” ไม่เท่ากับ “เท่ากัน” การไม่พบ critical failure ในชุดเล็กไม่พิสูจน์ว่าความเสี่ยงเป็นศูนย์

หยุดเมื่อ candidate ถัดไปไม่ขยับผลด้านคุณภาพ/ต้นทุนตามเกณฑ์ที่ตั้งไว้ หรือ uncertainty/คุณภาพข้อสอบกลายเป็นคอขวด ล็อกจำนวน candidate และรอบเลือกไว้ก่อนเริ่ม ไม่ค้นต่อบนชุดเดิมจนได้ตัวชนะโดยบังเอิญ การตัดหรือพัก skill ที่ไม่ช่วยเป็นเพียงข้อเสนอส่งเข้า lifecycle decision ไม่ใช่การถอดอัตโนมัติ

## แผนสร้างที่เล็กพอจะใช้จริง

ใช้ file-based fixtures และรายงานในระบบเดิม ไม่สร้าง database, dashboard platform หรือ skill ใหม่ การซ่อม installer เป็นงานที่เจ้าของอนุมัติเพิ่ม แยกหลักฐานติดตั้งจากคะแนน skill

| ช่วง | ผลงานและเกณฑ์จบ |
|---|---|
| 1. ทำ benchmark ให้เชื่อได้ | ยืนยัน cards 22 ใบตาม canonical, ทบทวน gold drift, ออก development cases, ทดสอบ grader ด้วยงานถูก/ผิดที่รู้ผล และ freeze manifests |
| 2. วัด baseline | วัด A/B บนข้อมูลที่แบ่งไว้และ clean runtime; เริ่มตรวจ runner กับ 5 ตัวแรกที่อนุมัติ ได้แก่ proactive-habits, done-for-me, make-it-james, sum-meet และ hand-it-off แล้วขยายให้ครบ 22 |
| 3. ทดลอง candidate | เลือก skill ที่มี failure หรือ overhead ที่วัดได้ แก้ทีละกลไก ให้ builder กับ reviewer แยกงาน เก็บ A/B/C และ selection results ทุก candidate |
| 4. ตัดสินจากงานใหม่ | freeze ผู้ชนะก่อน holdout ตรวจ counter-cases, composition และ runtime ที่จะกล่าวอ้าง ผลไม่ชัดให้คงรุ่นเดิมและระบุสิ่งที่ยังต้องวัด |
| 5. ส่งรุ่นที่มีหลักฐาน | validate/doctor ตามสิ่งที่เปลี่ยน พร้อม diff และ receipts; install/publish ตาม authority ของ target นั้นเท่านั้น |

ตัวอย่างงบเริ่มต้นสำหรับ **ตรวจระบบทดลอง**: 5 skill × 3 development episodes × 2 เงื่อนไข A/B × 1 trial = 30 agent trials ก่อนค่า grader ตัวเลขนี้เป็นข้อเสนอเรื่องขนาดงาน ไม่ใช่จำนวนที่พิสูจน์ generalization การเพิ่ม candidate C บน panel เดิมใช้อีก 15 trials ภายใต้ environment ที่ยังเทียบกันได้; หาก model/harness เปลี่ยนต้องรัน paired controls ใหม่

สำหรับ skill ที่จะตัดสินจริง ต้องมี selection และ holdout จาก scenario families อื่นเพิ่มเติม กำหนดขนาดจากความแปรปรวนและผลต่างที่ต้องการตรวจหลัง calibration ห้ามประกาศว่าตัวอย่าง 6 ข้อเพียงพอ การประเมินงบเงินให้ใช้ token/time ของ pilot ที่วัดจริง แล้วกำหนดเพดานก่อนเริ่มรอบใหญ่

โครงสร้างที่เสนอคือ `tests/benchmarks/` สำหรับ manifest, rubric และ development fixtures; คำสั่งแยกรัน model benchmark; receipts ที่ไม่มีข้อมูลลับใต้ `tests/receipts/` ส่วน raw trajectories และ sealed holdout อยู่ในที่เก็บที่ solver เข้าไม่ถึง Catalog ยังคงเป็นเจ้าของ identity และ SKILL.md เป็นเจ้าของ behavior; benchmark อ้าง path/hash ไม่คัดลอกคำสั่งเป็น body ที่สอง

Full model benchmark ไม่ควรทำให้ทุก local edit ต้องรันค่าใช้จ่ายสูง: `scripts/validate` คงตรวจ deterministic contract และความพร้อมของ fixture ส่วนการเปลี่ยน behavior ต้องมี runtime evidence ของ skill ที่เปลี่ยนและคู่ที่เกี่ยวข้องตาม risk ไม่มีผลรันใหม่ต้องบอกตรง ๆ ว่าไม่ได้ตรวจ ไม่ให้ static pass กลบช่องว่างนี้

Blast radius ของงานเสนอคือ test infrastructure, fixtures และ candidate ที่แยกจากตัวใช้งาน Rollback คือคืน candidate ไป hash เดิมและเก็บผลทดลองเพื่ออธิบายเหตุผล ไม่แตะ managed links จนถึงขั้น install ที่มี authority หากผลบน holdout แย่ลง อย่าเปลี่ยนเฉลยเพื่อปล่อย candidate

## บัญชีหลักฐานภายนอก

ตรวจ source และ version วันที่ 2026-09-05 ไม่ได้ทำซ้ำการทดลองของผู้เขียน คอลัมน์ท้ายเป็นข้อจำกัดในการนำมาใช้กับ JamesSkills วิธีจัดไฟล์ จำนวน pilot และเกณฑ์ตัดสินในเอกสารนี้เป็นข้อเสนอของโครงการ ไม่ใช่ค่ามาตรฐานที่งานวิจัยรับรอง

| แหล่งและวันที่ | ผู้เขียน/ผลประโยชน์เกี่ยวข้อง | สิ่งที่ใช้และขอบเขต |
|---|---|---|
| [Improving skill-creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills), 2026-03-03 | Anthropic ผู้ขาย model และ skill tooling | Official position: แยก capability กับ preference; มี benchmark และ blind comparison ผู้ขายรายงานเอง ไม่ใช่ independent proof ของ library นี้ |
| [SkillsBench v4](https://arxiv.org/abs/2602.12670v4), 2026-06-14 | Li และคณะ ผู้สร้าง benchmark มีผลประโยชน์ทางวิชาการต่อวิธีที่เสนอ | Matched skill/no-skill evaluation; task-level ผลไม่เท่ากันและมีกรณีติดลบ เป็น terminal tasks ไม่ครอบคลุมทุก mode/GUI งานสั้นให้ผลดีในกลุ่มทดลอง ไม่พิสูจน์ว่าการตัดทุก skill ให้สั้นจะช่วย |
| [SWE-Skills-Bench v1](https://arxiv.org/abs/2603.15401v1), 2026-03-16 | Han และคณะ ทีมวิจัยแยกจาก SkillsBench | หลักฐานหักล้าง universal uplift; base pass 89.8% เป็น 91.0% เฉลี่ย และมี template interference ใช้ model/harness เดียว สถานการณ์ที่ baseline สูงทำให้พื้นที่พัฒนาน้อย |
| [Skills in the Wild v1](https://arxiv.org/abs/2604.04323v1), 2026-04-06 | Liu และคณะ ผู้วิจัย retrieval/refinement | การดึง skill จากคลังใหญ่เพิ่มปัญหาอีกชั้น ผลจาก task-specific injection ไม่แทน natural selection; ขนาดคลังและงานต่างจาก JamesSkills |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09 | Anthropic ประสบการณ์ผู้ขายและลูกค้า | Outcome/trace, graders หลายชนิด, trials แยกบริบท และสองด้านของ activation; คำแนะนำเริ่ม 20–50 งานเป็น early discovery ไม่ใช่การรับรองความแม่นทางสถิติ |
| [GEPA v2](https://arxiv.org/abs/2507.19457v2), 2026-02-14; ต้นฉบับ 2025-07-25 | Agrawal และคณะ ผู้สร้าง optimizer; academic/industry affiliations | Reflection ใช้เสนอและคัด candidate ได้ แต่ผลขึ้นกับ model; Merge setting เดียวกันช่วยหนึ่ง model และทำให้อีก model แย่ลง ไม่ใช่หลักฐานว่า automatic optimization จะช่วยภาษาไทยหรือทุก skill |
| [AI Agents That Matter v1](https://arxiv.org/html/2407.01502v1), 2024-07-01 | Kapoor และคณะ Princeton; independent methodological audit | ประเมินต้นทุนร่วมกับผลสำเร็จ และเลือกระดับ holdout ตามขอบเขตที่อ้าง ใช้ผลเชิงวิธีวิจัย ไม่ยกสถานะ benchmark ปี 2024 เป็นสถานะปัจจุบัน |
| [Adding Error Bars to Evals v1](https://arxiv.org/html/2411.00640v1), 2024-11-01 | Evan Miller สังกัด Anthropic | Paired differences, clustered observations และ sample planning; repeated generations ไม่แทนความหลากหลายของโจทย์ สูตรไม่ได้ทำให้ pilot เล็กสรุปผลต่างเล็กได้ |
| [The reusable holdout](https://pubmed.ncbi.nlm.nih.gov/26250683/), Science 2015-08-07 | Dwork และคณะ; สถาบันวิจัยและบริษัทเทคโนโลยี | การเลือกวิธีหลังเห็นผลเดิมทำลายความเป็นอิสระของการประเมิน งานนี้มีวิธีควบคุม formal reuse แต่เราไม่ได้อ้างว่านำวิธีนั้นมา implement แล้ว |
| [Humans or LLMs as the Judge? v5](https://arxiv.org/html/2402.10669v5), 2024-09-26 | Chen และคณะ CUHK Shenzhen/สถาบันวิจัย; academic stake | การเปลี่ยน presentation และ fake references กระทบการตัดสิน ทั้งคนและ model มี bias; งานภาษาอังกฤษและผู้ประเมินเฉพาะกลุ่ม ไม่ใช่อัตราผิดของ judge ไทยปัจจุบัน |
| [Using LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/), 2024-10-29; แก้ล่าสุด 2026-09-01 | Hamel Husain ผู้ลงมือทำกับหลายบริษัท; อิสระจากผู้สร้าง GEPA แต่ขาย consulting/education | ประสบการณ์ Honeycomb เน้น expert calibration และข้อผิดพลาดของคะแนน 1–5; รายงานว่า prompt optimizers ที่ลองยังไม่ค่อยได้ผล เป็น practitioner disconfirmation ไม่ใช่การทดลองว่าทุก optimizer ล้มเหลว |
| [Eval awareness in BrowseComp](https://www.anthropic.com/engineering/eval-awareness-browsecomp), 2026-03-06 | Anthropic เปิดเผยการทดลองของตน; commercial stake | พบการเข้าถึงคำตอบรั่วและการกู้ answer key จริง ใช้เป็นเหตุผลให้แยก task/เฉลยด้วยสิทธิ์; ไม่ได้บอกว่า JamesSkills มีพฤติกรรมนี้แล้ว |

ค้นด้านหักล้างโดยตรงเรื่อง skill overhead, template interference, optimizer failure, judge bias และ holdout contamination พบทั้งการทดลองที่ผลลดลงและประสบการณ์ผู้ใช้ที่ optimizer ไม่ช่วย จึงไม่แนะนำให้เริ่มด้วย auto-rewrite ทั้ง 22 ตัว ไม่มี source ที่ตรวจยืนยันจำนวนข้อสอบตายตัว, optimizer ที่ชนะเสมอ หรือ cross-platform parity ของชุดนี้ แหล่งเพิ่มช่วงท้ายไม่เปลี่ยนคำตัดสิน conditional แต่ทำให้ขอบเขตการทดลองชัดขึ้น

## จุดตัดสินใจ

แนะนำรับทิศทาง **benchmark ตามหน้าที่ครบ 22 skill → ตรวจระบบกับ 5 skill แรก → วัด baseline ครบ → ปรับเฉพาะจุดที่มีหลักฐาน → ยืนยันบนงานใหม่ก่อนเปลี่ยนตัวใช้งาน**

งานวิจัยและ cards ทำได้ใน scope ปัจจุบัน การเริ่ม implementation รอการเห็นชอบทิศทางตาม `zoom-out` ที่เรียกใช้: “get explicit agreement before implementation resumes.” การเห็นชอบแผนไม่ใช่การรับรองคะแนน ไม่เปลี่ยน lifecycle และไม่อนุญาต external publish โดยปริยาย

Unknown ที่ยังต้องปิด: baseline ราย skill, ความสอดคล้องของ judge กับผู้รับภาษาไทย, ความแปรปรวนข้าม runtime, ต้นทุนจริง และชุดงานที่สะท้อนการใช้งานในอนาคต ข้อเสนอไม่อ้างว่าป้องกัน overfit ได้หมด แต่ทำให้ตรวจพบและปฏิเสธการปรับที่ชนะเฉพาะข้อสอบได้
