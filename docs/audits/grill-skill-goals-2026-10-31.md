# Grill Me รอบ 2: เป้าหมายสกิลที่เหลือ (ตอบ offline)

เปิด `grill-skill-goals-2026-10-31.html` ในเบราว์เซอร์ ตอบครบแล้วกด "คัดลอกคำตอบ" หรือดาวน์โหลด JSON แล้ววางกลับในแชทเมื่อมีเน็ต หน้าเว็บทำงานในเครื่อง ไม่ส่งอะไรออก ถ้าเปิด HTML ไม่สะดวก ตอบเป็นข้อความตามรหัสข้อด้านล่างได้

## เคาะแล้ว 2026-10-31 (ไม่ต้องตอบซ้ำ)

1. `insight-driven-mode` = mode กับทุกงาน: ไม่เริ่มจนเข้าใจผู้ใช้/เป้าหมายจริง ขุดและถามจนเข้าใจ ออกกลยุทธ์ก่อนเสมอ ตรวจว่าตอบโจทย์จริงไม่ใช่แค่เสร็จ; เมื่อเป็นงาน marketing เพิ่มขั้น insight ต่อกลุ่มเป้าหมายตามไฟล์เดิม → เขียนใหม่ทั้งตัว
2. `proactive-habits` คนละตัวกับ insight: ตัดสินเอง ทำจนเสร็จ ข้ามจุดตัดสินแล้วมาเคาะทีเดียว ไม่รายงานกลับว่ายังไม่ทำ (7 Habits / growth mindset)
3. ทั้ง proactive-habits และ insight คิดกลยุทธ์ในตัวเอง (ไม่เรียก zoom-out) และเป็นประตูเรียก `grill-me` เมื่อเป้ายังไม่ชัดพอจะลงมือ; `grill-me` และ `zoom-out` คงแยกไว้เป็นตัวเตือนสติเมื่อ AI หลงทาง ลืมถาม หรือเรียกเฉพาะกิจ
4. ตรวจงานคง 3 ตัว: `are-you-sure` (เอกสาร) `dev-are-you-sure` (ซอฟต์แวร์ ต้องรันเทส) `is-that-the-best-you-can-do` = beyond expectation หาจุดเก็บงาน efficiency research มิติอื่น ("มึงมีปัญญาแค่นี้หรือไง") → ไฟล์ที่ห้ามขยาย scope และหยุดที่งบต้องแก้
5. `done-for-me` = ตัวเตือนสติเมื่อ AI ถามซ้ำ/หลงทาง: ทบทวนทั้งแชทและทุกจุดที่เคาะไปแล้ว (เผื่อ context หาย) แล้วลงมือทันที จุดที่ยังกำกวมก็ทำอยู่ดี โดย (ก) ทำเป็น setting ที่แก้ทีหลังได้ ไม่ hardcode หรือ (ข) บอกตรงๆ แล้วทำมา 3-5 แบบให้เลือก → เขียนใหม่
6. ลบ alias `solutionsimpact-onepagesummary` และ `solutionsimpact-meeting-summary-full` ออกจาก repo; ใส่ best practice ของ SolutionsIMPACT เป็นของทุกคนใน `one-page-pls` / `sum-meet` พร้อม footer เล็ก เทา บาง ที่ไม่กระทบการแสดงผล (ข้อความแน่นอนอยู่ในคำถาม 9)
7. งานเทคนิค P0 (ย้าย `kind` → `metadata.kind`, ปิดช่อง Codex, in-place marketplace, listing budget) ไม่ขัดกับเป้าใด ทำได้

## คำถามรอบนี้ (ตอบด้วยรหัสตัวเลือก หรือพิมพ์เอง)

1. `hand_it_off` ควรเป็นอะไร: `doc_only` ย้ายไปเป็นกฎใน AGENTS.md ไม่ติดตั้ง | `keep_hidden` ติดตั้งแต่ซ่อนจากคน | `keep_as_is`
2. `catchup_vs_standard` เมื่อ "ถึงไหนแล้ว" แล้วไฟล์สถานะล้าสมัย: `report_only` | `report_and_fix` ซ่อม STATUS เอง | `report_and_continue` ทำงานค้างต่อทันที
3. `output_trio` เมื่อ "ทำให้พร้อมส่ง" ไม่บอกรูปแบบ: `ai_picks` | `house_html` HTML สไตล์บ้านเสมอ | `ask_first` (+ มีกรณีอยาก PDF โดยไม่พิมพ์คำว่า PDF ไหม)
4. `coach_me` เมื่อ "โค้ชหน่อย ตันแล้ว": `non_directive` ถามจนเห็นเอง | `coach_then_advise` ถาม 2-3 ข้อแล้วเสนอ | `business_coach` ท้าทาย + framework
5. `evidence_trio`: `three_distinct` | `merge_research_solutions` | `baseon_is_mode` (+ framework ที่ใช้บ่อยจริง 3 เดือนนี้)
6. `never_again` เมื่อ "จำไว้เลย": `full_lesson` 3 case ทุกครั้ง | `proportional` สั้น/ยาวตามความเสียหาย | `memory_first` จำส่วนตัวก่อน เข้า repo เมื่อซ้ำ
7. `make_it_james_pair` อะไรหลุดบ่อยสุด (เลือกได้หลายข้อ): `translated_thai` | `layout_drift` | `not_triggered` ไม่โหลดเองต้องเรียกชื่อ (+ ตัวอย่างงานล่าสุด)
8. `proactive_dev` เหลือหน้าที่อะไร: `eng_discipline` test/rollback/architecture | `merge_into_habits` | `tech_lead` วางแผน 5 roles + subagent
9. `footer_text` ข้อความ footer ที่แน่นอน และใส่ทั้ง one-page-pls กับ sum-meet หรือตัวเดียว

เมื่อได้คำตอบ ขั้นต่อไปคือเขียนใหม่ 5 ตัวที่เคาะแล้ว (insight-driven-mode, proactive-habits, done-for-me, is-that-the-best-you-can-do, ลบ alias + footer) และปรับตัวที่เหลือตามคำตอบรอบนี้ ก่อนงานเทคนิค P0

## คำตอบรอบ 2 (James, 2026-10-31) และข้อสรุป

- `hand_it_off` → เปลี่ยนหน้าที่เป็น handoff: ทำให้ AI ตัวอื่น ค่ายอื่น หรือตัวเดิมที่ย้ายบัญชี/เครื่อง เข้าใจทุกอย่างของการคุยครั้งนี้เป็นคำสั่งสั่งต่อได้ รวมงานค้างและแผนที่ยังไม่ทำ และบันทึก decision, skill, ai-context ลง GitHub; Candidate Card gate ย้ายไป AGENTS.md
- `catchup_vs_standard` → catchup = ทวนว่าทำอะไรไปแล้ว ไม่เขียนอะไรใหม่ ตอบเป็น HTML 1 หน้าไม่มี metacopy แบบผู้บริหารถาม "ถึงไหนแล้ว"; project-standard = ใช้บ่อย บังคับ format/directory ของการจดทุกอย่าง
- `output_trio` → final-it: เจ้าของลืมว่าไว้ทำอะไร (เตรียมปลด); one-page-pls = วิธีคิดสรุปใจความ 1 หน้า ตาม design system เดิม ยอม override เล็กน้อย มี default style เช็คและลบ metacopy; sum-meet = หลักเดียวกันแต่ครบถ้วน (ครบ ≠ ยาว) แยก agenda/topic ชัด HTML ไฟล์เดียว: สรุปรวม → สารบัญ → รายหัวข้อ
- `coach_me` → เป็น mode ถามอย่างเดียว ไม่คิดแทน ไม่เสริม ไม่ตอบ ขุดภูเขาน้ำแข็งลงไปเรื่อยๆ ถามด้วยคำของผู้ใช้ จดได้ เปิดด้วยเป้าหมายสูงสุดของการโค้ชครั้งนี้ คำตอบไม่ตรงเป้าแรกแต่ได้คำตอบชีวิตก็ถือว่าสำเร็จ
- `evidence_trio` → คนละงาน คงสามตัว: research-it = "อย่าตอแหล ไปหาข้อมูลมาก่อน" ไม่เอาแค่ official spec ต้องมีคนจริง รีวิวจริง; give-me-solutions = ทำการบ้านแล้วเสนอทางออกไม่ตัดสินแทน ตารางเดียว แกนเดียว คำเดียวกัน หัวตารางแม่น ค่าแบบ enum มอง Time/Cost/Quality ทั้งสั้นและยาว; baseon = "ไปศึกษาเรื่อง ___ มา" มี keyword/สมมติฐานชัดแล้ว หาจากแชท/โปรเจกต์/เครื่อง/MCP/ข้างนอก
- `never_again` → ตัวเตือนสติเมื่อหยุดจด md นานจนเริ่มลืม context; กฎถาวร: ทุก insight, learning, decision, context, skill.md, ผลงานทุก version → อัปเดต GitHub เสมอโดยไม่ต้องรอสั่ง
- `make_it_james_pair` → เจ้าของให้ตัดสินแทน: คงแยก 2 ตัว (checklist ต่างกัน โหลดต่างสถานการณ์); make-it-james = copywriting, NO THAI AI SLOP, NO METACOPY; make-it-james-ux แยก 2 ส่วน UX (real user flow ทุกกลุ่ม, don't make me think, ลด step, เลี่ยง modal, ซ้ายไปขวา บนลงล่าง, grid เป๊ะ, component เหมาะ, compact) และ UI (ล็อค font/weight/radius, default ขาว clean minimal IBM Plex Sans Thai ≤ semi-bold, ห้าม accent border, หน้าไม่เด้ง, nav/expand ไม่เด้ง, card/row/table สูงคงที่, ไม่ nested, คิด desktop + mobile)
- `proactive_dev` → ไม่จำเป็นถ้า proactive-habits ใช้ได้ทุกสายงาน → ปลดใน release ถัดไป
- `footer_text` → `Researched by SolutionsIMPACT, Developed by James Theeranon` ทั้ง one-page-pls และ sum-meet

บันทึกเป็น DEC-051 และ LESSON-017 ใน `ai-context/`

คำตอบดิบทุกข้อความของ James (ทั้งรอบสัมภาษณ์และรอบ 2) อยู่ใน `skill-purpose-raw-answers-2026-10-31.md` ไฟล์นี้คือข้อสรุป ไฟล์นั้นคือต้นฉบับ
