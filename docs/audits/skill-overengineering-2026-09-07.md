# Audit ความซับซ้อนของ JamesSkills 2.0.3

ตรวจ 2026-09-07; baseline 659f238. อ่าน canonical SKILL.md ครบ 22, catalog, schema และส่วนบังคับ schema; เทียบ proactive-habits รุ่น 6928f69 กับปัจจุบัน และอ่าน receipt benchmark รอบก่อน. ไม่ใช่การรัน benchmark ใหม่ ไม่ได้ตรวจทุก script/reference แบบ line-by-line และไม่ยืนยันสาเหตุเชิงทดลองหรือทุก platform.

## ความหมายที่เจ้าของยืนยัน

proactive-habits เป็นโหมดทั้งห้องจนปิด; done-for-me เป็นคำสั่งจบงานครั้งเดียว ทั้งสองประกอบกันได้ ไม่ใช่ข้อยกเว้นของกันและกัน. proactive-dev ซึ่งประกาศเป็น mode ต้องตรวจความสอดคล้องแบบเดียวกัน.

## ข้อสรุป

สูง 8 / กลาง 11 / ต่ำ 3 เป็นระดับความเสี่ยงจากข้อความคำสั่ง ไม่ใช่อัตราล้มเหลว. สูง = มีข้อขัดแย้ง/เงื่อนไขที่อาจขวางผลลัพธ์โดยตรง; กลาง = ประโยชน์จริงแต่มีพิธีหรือ default กว้าง; ต่ำ = ยังไม่พบข้อบังคับเกินจำเป็นรุนแรง ไม่ได้แปลว่าไม่มี bug.

## ต้นเหตุร่วม

1. docs/SKILL-SCHEMA.md บังคับอย่างน้อยสอง exclusions ทุกชนิด และ boundary graph in-degree >= 1. การมีผู้ส่งเข้าหาไม่ได้พิสูจน์ distinct value; ทำให้ mode/standard ถูกออกแบบเหมือน workflow ที่แข่งขันกัน. เปลี่ยนเป็นทดสอบ composition และขอบเขตจริง.
2. บังคับ 2–5 principles, heading spine และ countercase routing ทุกตัว. นี่เป็น structural proof ไม่ใช่ quality proof; ควรอนุญาตรูปแบบต่างกันตามชนิด และย้าย provenance ที่ไม่ต้องใช้ตอนทำงานไป reference.
3. ข้อแก้หลังเกิดเหตุสะสมใน body แต่ description/principles/stop/handback เก่ายังสวนกัน. แก้ทั้ง contract ให้เป็นเจตนาเดียว แทนเติมข้อยกเว้นท้ายไฟล์.
4. แยก authoring/evaluation policy ของ repo ออกจากขั้นตอนที่ skill ต้องทำในงานผู้ใช้; ไม่บังคับสร้างหลักฐานรูปแบบเดียวกับทุกงาน.
5. benchmark เดิม 117 calls ส่วนใหญ่ response-only ราย skill, public cases ไม่ใช่ sealed holdout. การตรวจติดตั้งและคำตอบหนึ่ง turn ไม่พิสูจน์ว่าจะทำงานหลาย turn จบ.

## รายตัว

| Skill | ระดับ | หลักฐานข้อความ / ปัญหา | การปรับที่แนะนำ | คู่กรณีตรวจต่อ (ยังไม่รัน) |
|---|---|---|---|---|
| [proactive-habits](../../plugins/james-core/skills/proactive-habits/SKILL.md) | สูง | บรรทัด 5 `not for finishing one named task` — โหมดถูกแยกออกจากการจบงาน ทั้งที่ต้องทำงานร่วมกับ workflow | คงโหมดตลอดห้อง; done-for-me เพิ่มคำสั่งจบงานครั้งเดียว ไม่แทนที่โหมด | เปิดโหมด → ขอแก้ไฟล์ → ทักว่ายังไม่เสร็จ → ต้องแก้ต่อ ไม่ส่งชื่อ skill |
| [done-for-me](../../plugins/james-core/skills/done-for-me/SKILL.md) | กลาง | บรรทัด 5 `not when the plan still needs work` — การต้องมีแผนที่ตกลงแล้วอาจทำให้การตัดสินใจย่อยกลายเป็นแผนที่ต้องขอใหม่ | แยกเป้าหมายที่ตกลงแล้วจากวิธีทำที่ agent ตัดสินใจได้; คงขอบเขตการส่ง/ลบ | ให้จบงานที่เป้าหมายชัดแต่วิธีทำยังไม่ครบ ต้องตรวจแล้วทำ; draft ต้องไม่ส่ง |
| [i-have-adhd](../../plugins/james-core/skills/i-have-adhd/SKILL.md) | กลาง | บรรทัด 30 `Restate state every turn` — บังคับ action/state/time ทุกคำตอบ ทำให้ตอบคำถามธรรมดามีพิธีและข้อขัดแย้งกับ no recap | ใช้ progress เฉพาะงานหลายขั้น; คำตอบข้อเท็จจริงเริ่มด้วยคำตอบ | ถามความหมายหนึ่งคำ เทียบงานหลายขั้นที่ต้องจำสถานะ |
| [is-that-the-best-you-can-do](../../plugins/james-core/skills/is-that-the-best-you-can-do/SKILL.md) | สูง | บรรทัด 38 `Another parallel attempt no longer changes the result` — เงื่อนไขหยุดไม่จำกัดต้นทุน และต้องรายงาน ceiling/gap แม้ต้องการชิ้นงานอย่างเดียว | กำหนดเกณฑ์ประโยชน์และงบก่อนปรับ; เพิ่มรอบเฉพาะพบช่องว่างสำคัญ | ปรับ caption 20 คำ เทียบข้อเสนอสำคัญที่ต้องเพิ่มหลักฐาน |
| [make-it-james](../../plugins/james-core/skills/make-it-james/SKILL.md) | กลาง | บรรทัด 55 `plus the specific failures repaired` — มาตรฐานภาษาขอรายงานการแก้ทุกครั้ง ขัดกับการลบ production residue และ output-only | คงหลักภาษา; ไม่บังคับรายงานการแก้; ไม่ส่งต่อเมื่อข้อความทั้งผิดและเขียนไม่ดี | ขออีเมลอย่างเดียว เทียบขออธิบายสิ่งที่แก้ |
| [never-again](../../plugins/james-core/skills/never-again/SKILL.md) | กลาง | บรรทัด 28 `source and ingestion through interpretation` — บังคับไล่ระบบหลายชั้นและเพิ่มกฎเสมอ เสี่ยงสะสมข้อห้ามโดยไม่มีการลบกฎเดิม | เลือกแก้กลไก/กฎเดิมก่อนเพิ่มกฎ; วิเคราะห์เฉพาะเส้นทางจริง; คงสาม counter/transfer cases | แก้ lesson ที่ขัดกัน เทียบเหตุผิดครั้งเดียวที่ไม่ควรสร้างกฎถาวร |
| [research-it](../../plugins/james-core/skills/research-it/SKILL.md) | ต่ำ | บรรทัด 32 `A ledger is optional` — มีข้อกำหนดหลักฐานละเอียด แต่ล่าสุดมี stop และใช้ supplied source ได้ ไม่พบพิธีบังคับระดับเดียวกับกลุ่มสูง | คงหลักฐาน/ขอบเขต; รวมถ้อยคำซ้ำเมื่อมี paired proof ไม่ลบเพราะยาว | ตอบจากสองแหล่งที่ให้มา เทียบคำถามที่จำเป็นต้องหาแหล่งเพิ่ม |
| [are-you-sure](../../plugins/james-core/skills/are-you-sure/SKILL.md) | กลาง | บรรทัด 29 `sweep all five layers in order` — ทุก artifact ต้องพิจารณาอายุการใช้งานและโครงสร้าง แม้แค่ยอดรวม; มี not-applicable ช่วยแต่หลักการยังบังคับ all five | เลือกการตรวจตามความเสี่ยง; คงตรวจครบเมื่อผู้ใช้ขอ full audit | ตรวจยอดสามจำนวน เทียบแผนธุรกิจหลายปี |
| [hand-it-off](../../plugins/james-core/skills/hand-it-off/SKILL.md) | สูง | บรรทัด 89 `The named primary owner` — procedure บอกทำงานต่อ แต่ stop/handback บอกส่งชื่อ owner แล้วจบ; สำเนารายชื่อ 22 เสี่ยง drift | เป็น routing ภายในที่ไม่ตัดการทำงาน; ไม่บังคับ owner เดียวให้ mode/standard แข่ง workflow | เปิด proactive แล้วทำเอกสาร: ต้องได้เอกสาร ไม่ใช่ชื่อผู้รับงาน |
| [baseon](../../plugins/james-productivity/skills/baseon/SKILL.md) | กลาง | บรรทัด 34 `End with a reversible experiment` — ทุกคำอธิบายต้องจบด้วย experiment และจำแนก profile แม้ไม่เกี่ยวกับคน; scope สมัครแหล่งใหม่แต่ description excludes | แยกอ่าน/ประยุกต์/ลงทะเบียนตามคำขอ; experiment เฉพาะโจทย์นำไปใช้ | อธิบายแนวคิดหนึ่งข้อ เทียบประยุกต์กับกรณีทีม |
| [coach-me](../../plugins/james-productivity/skills/coach-me/SKILL.md) | สูง | บรรทัด 41 `If they ask directly for an answer` — บังคับถามกลับเมื่อขอคำตอบ; อ่าน stance และลงลึกทุกครั้งทั้งที่ countercase ยอมรับว่าคุยเบาได้ | ให้ความลึกตามความจำเป็นและยอมเปลี่ยนจาก coaching เมื่อผู้ใช้สั่ง; คงไม่วินิจฉัย | ผู้ใช้หยุด coaching ขอข้อมูลตรง ๆ เทียบผู้ใช้ต้องการสำรวจตัวเอง |
| [final-it](../../plugins/james-productivity/skills/final-it/SKILL.md) | กลาง | บรรทัด 49 `this skill delivers the email` — countercase เปลี่ยน deck ที่ผู้ใช้ขอเป็น email เอง; every rendered state ไม่จำกัดขอบเขต | เคารพรูปแบบที่ระบุ; เลือกรูปแบบเมื่อยังไม่กำหนด; ตรวจ states ที่เกี่ยวข้อง | ขอ deck โดยชัดเจน ต้องได้ deck; ไม่ระบุรูปแบบจึงเลือกได้ |
| [give-me-solutions](../../plugins/james-productivity/skills/give-me-solutions/SKILL.md) | ต่ำ | บรรทัด 33 `where they affect this choice` — มีเกณฑ์ตามบริบทและ unknown guard ดี; stop another search pass ยังเสี่ยงทำซ้ำ | จำกัดการค้นตามข้อมูลที่จะเปลี่ยนการเลือก; คงเปรียบเทียบที่เกี่ยวข้อง | เลือกสองตัวจากข้อมูลครบ เทียบซื้อระบบที่ต้นทุนยังไม่ทราบ |
| [grill-me](../../plugins/james-productivity/skills/grill-me/SKILL.md) | สูง | บรรทัด 31 `A question without a recommendation` — บังคับแนะนำทุกคำถามแม้เป็นเป้าหมาย/รสนิยมที่ไม่มีหลักฐาน และ final confirmation แม้ผู้ใช้สั่งเริ่มแล้ว | ถามเฉพาะสิ่งที่ตัดสินใจไม่ได้; recommendation เมื่อมีเหตุผล; รับคำสั่งเริ่มเป็นการจบสัมภาษณ์ | ผู้ใช้ตอบครบแล้วบอกเริ่มเลย เทียบเรื่องที่มีสองเป้าหมายขัดกัน |
| [one-page-pls](../../plugins/james-productivity/skills/one-page-pls/SKILL.md) | กลาง | บรรทัด 30 `one topic = one file` — เป้าหมายหนึ่งหน้าถูกแปลงเป็นหลายไฟล์ต่อหัวข้อและ HTML ตายตัว แม้ user ต้องการหนึ่งหน้ารวม | รักษาค่าเริ่มต้นที่อนุมัติ แต่คำขอหนึ่งหน้ารวม/รูปแบบชัดเจนต้องชนะ; coverage ภายใน | ขอหนึ่งหน้ารวมสามประเด็น เทียบขอแยกหนึ่งหน้าต่อหัวข้อ |
| [sum-meet](../../plugins/james-productivity/skills/sum-meet/SKILL.md) | กลาง | บรรทัด 15 `one canonical A4 portrait HTML` — traceability เหมาะกับ full minutes แต่ default อาจลาก summary สั้นไป HTML+ledger+render | แยก full record กับสรุปตามคำขอ; คงความครบและหลักฐานสำหรับ full record | ขอสรุปในแชทห้าบรรทัด เทียบขอ minutes ตรวจสอบย้อนหลัง |
| [zoom-out](../../plugins/james-productivity/skills/zoom-out/SKILL.md) | สูง | บรรทัด 31 `Climb at least three levels` — บังคับระดับ/ห้าม interface/ต้อง agreement แม้เป็นการถอยดู UX หรือแก้โฟกัสภายในเป้าหมายเดิม | ถอยเท่าที่พบปัญหาจริง; agreement เมื่อเปลี่ยนเป้าหมาย/ข้อผูกพัน ไม่ใช่ทุก reframe | ถอยดู flow checkout เทียบเปลี่ยนกลยุทธ์ธุรกิจที่ต้องตัดสินใจ |
| [catchup](../../plugins/james-software/skills/catchup/SKILL.md) | ต่ำ | บรรทัด 29 `Take the fast path first` — มี fast path และ chat-only แล้ว; ความเสี่ยงคงอยู่ที่ HTML default และ forensic analogy กว้าง | คง read-only สำหรับคำขอสถานะ; ถ้าสั่งทำต่อให้ workflow รับต่อโดยไม่หยุดที่รายงาน | ถามสถานะอย่างเดียว เทียบถามสถานะแล้วสั่งทำส่วนค้างต่อ |
| [dev-are-you-sure](../../plugins/james-software/skills/dev-are-you-sure/SKILL.md) | สูง | บรรทัด 31 `If no such line exists, that is the defect` — ไม่มี reset line ไม่ได้แปลว่ามี bug เสมอ เช่น derived/stateless; บังคับ 5+4 ชั้นแม้แก้เล็ก | ตรวจ invariant ตามรูปแบบโปรแกรมจริง; เลือกชั้นตามความเสี่ยงและขอบเขต | pure function/derived state ที่ถูกต้อง เทียบ async mutation ที่กดซ้ำได้ |
| [make-it-james-ux](../../plugins/james-software/skills/make-it-james-ux/SKILL.md) | กลาง | บรรทัด 35 `Replace blocking confirmations` — กฎ reduce friction แบบกว้างยังขัดกับ exceptions; font helper อาจไปบังคับ house font ทั้งที่ existing system มาก่อน | จำกัด undo ตาม reversal จริง; embed เฉพาะ font ที่เลือก; คง explicit user design requirements | ระบบใช้ฟอนต์อื่นแบบ offline เทียบงานใหม่ใช้ house font |
| [proactive-dev](../../plugins/james-software/skills/proactive-dev/SKILL.md) | สูง | บรรทัด 5 `not for executing an accepted plan` — mode ถูกเขียนให้หมดหน้าที่เมื่อเริ่ม execution; description บังคับ subagents ขัด body conditional; principles ทุก mutation ต้องแถลง | คงโหมดวิศวกรรมตลอด build/test; planning/delegation ตามงาน; ตัดหลักการที่สวน body | แก้สองบรรทัดจนทดสอบผ่าน เทียบงานย้ายฐานข้อมูลที่ต้องมี rollback |
| [project-standard](../../plugins/james-software/skills/project-standard/SKILL.md) | กลาง | บรรทัด 38 `Every project gets the same generated SRS` — เงื่อนไขสร้าง SRS และ schema อาจใหญ่เกิน status repair; one fact one place แบบเด็ดขาดต้องแยก derived view | คง source owners; render เมื่อ source ที่เกี่ยวข้องเปลี่ยน; ไม่เพิ่มเอกสารในงานเล็ก | แก้สถานะผิดหนึ่งจุด เทียบ bootstrap โครงการจริง |

## ตรวจแก้แล้วต้องพิสูจน์อะไร

ใช้ model/settings/tools/งบเดียวกัน เทียบ no-skill, รุ่นก่อน rewrite, 2.0.3 และ candidate. วัดงานเสร็จจริง/ความถูกต้องก่อน จำนวนหยุดให้ผู้ใช้เข็น จำนวนคำถามซ้ำ เวลาหรือ token และผลข้างเคียงเป็นคนละมิติ. ไม่ใช้ความสั้นชดเชยงานไม่เสร็จ.

ชุดหลาย turn ต้องมี: เปิด mode → ทำงาน → ผู้ใช้แก้ไข → ทำต่อ → ตรวจ artifact; mode + done-for-me + standard; ขอแค่ draft ห้ามส่ง; คำขอ full audit ที่ความละเอียดจำเป็น; เปลี่ยนเป้าหมายจริงที่ต้องถาม. จองกรณีใหม่ไม่ให้ผู้แก้ skill เห็นไว้ตรวจทั่วไป และไม่ทิ้ง timeout/failed run.

## สถานะงานนี้

Audit ครบ canonical 22/22; ยังไม่แก้ behavior ไม่ bump version ไม่ติดตั้ง และไม่เผยแพร่ผล audit. ข้อเสนอปรับ format/lifecycle ที่เป็นความตั้งใจเดิมต้องยืนยันจาก requirement ก่อนเปลี่ยน ไม่ถือว่าทุกกฎเฉพาะตัวเป็นความผิด.
