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

## 📚 Full Skill Directory (รายการสกิลทั้งหมด)

### Context & Setup (การเริ่มต้นและรวบรวมบริบท)

#### ⚡️ `/project-standard`
*Create or repair project truth (SRS, NFR, Permissions).*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>แน่นอนครับ! เดี๋ยวผมจะช่วยคิดแคมเปญการตลาดให้นะครับ สำหรับแคมเปญนี้เราน่าจะเริ่มจากการทำ Facebook Ads แล้วก็ยิงกลุ่มเป้าหมายอายุ 20-30 ปีนะครับ บลาๆๆๆ... (AI มโนไปเองโดยไม่มีการตกลง Scope งานที่ชัดเจน)</blockquote>

</td>
<td valign="top">

<blockquote>Generated <code>PROJECT.md</code>. กําหนดสิทธิ์ (Permission Matrix), งบประมาณ (NFR), และเป้าหมายทางธุรกิจ (Business Objectives) เรียบร้อยแล้วครับ โปรเจกต์พร้อมสำหรับการรันแคมเปญจริง</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/catchup`
*Reconstruct current state after a continuity gap.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>สวัสดีครับ! วันนี้มีอะไรให้ผมช่วยไหมครับ? รบกวนคุณเจมส์สรุปให้ฟังหน่อยครับว่าเมื่อสัปดาห์ที่แล้วเราทำโปรเจกต์ไหนค้างไว้บ้าง และอยากให้ผมทำอะไรต่อครับ?</blockquote>

</td>
<td valign="top">

<blockquote>Read <code>STATUS.md</code>. งานล่าสุดที่เราทำค้างไว้คือ 'การคัดเลือก Vendor สำหรับทำระบบ CRM' ตอนนี้ติดอยู่ที่รอใบเสนอราคาจากเจ้าที่ 2 ครับ คุณเจมส์ต้องการให้ผมร่างอีเมลไปตามงานไหมครับ?</blockquote>

</td>
</tr>
</table>

### Analyze & Decide (การวิเคราะห์และตัดสินใจ)

#### ⚡️ `/zoom-out`
*Reframe the problem at the system level before patching symptoms.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ได้เลยครับ นี่คือเทมเพลตสำหรับเขียนใบเตือนพนักงานที่มาสายนะครับ คุณเจมส์สามารถนำไปปรินต์และให้พนักงานเซ็นรับทราบได้เลยครับ...</blockquote>

</td>
<td valign="top">

<blockquote>Wait. การแจกใบเตือนเป็นแค่การแก้ปลายเหตุ (Symptom) จากข้อมูลที่ผ่านมา ปัญหาที่แท้จริงคือโครงสร้าง Incentive ของบริษัทไม่ได้ผูกกับเวลาเข้างาน (Root Cause) เรามาแก้ที่ระบบประเมินผลกันก่อนดีไหมครับ?</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/give-me-solutions`
*Research external options and present objective tradeoffs.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>จากคำถามของคุณเจมส์ ผมขอแนะนำให้ใช้ HubSpot ครับ! เพราะมันเป็นเครื่องมือระดับโลกที่มีคนใช้เยอะมาก แถมยังฟรีในฟีเจอร์พื้นฐานด้วย เหมาะกับธุรกิจทุกขนาดเลยครับ</blockquote>

</td>
<td valign="top">

<blockquote><table><tr><th>CRM Option</th><th>Annual Cost</th><th>Pros/Cons for our Scale</th></tr><tr><td>HubSpot</td><td>$10,000</td><td>Best ecosystem, but over-budget.</td></tr><tr><td>Zoho</td><td>$2,500</td><td>Fits budget, steep learning curve.</td></tr></table><br><i>(ตารางเปรียบเทียบข้อดีข้อเสีย เพื่อให้คุณตัดสินใจขั้นสุดท้ายด้วยตัวเอง)</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/baseon`
*Apply a named knowledge lens (e.g., Wealth Dynamics).*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>เพื่อเพิ่มยอดขาย ทีมของคุณควรจะสื่อสารกันให้มากขึ้น จัดประชุมสัปดาห์ละ 2 ครั้ง และต้องตั้งเป้าหมาย OKR ให้ชัดเจนครับ...</blockquote>

</td>
<td valign="top">

<blockquote>เมื่อวิเคราะห์ผ่านเลนส์ <b>Wealth Dynamics</b> ปัญหาคือคุณ (Creator) ลงมาทำงาน Operation มากเกินไป คุณต้องหา <b>Mechanic</b> มาคุมระบบหลังบ้าน เพื่อให้คุณกลับไปอยู่ใน Flow ของการสร้างสรรค์ครับ</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/grill-me`
*Interactive stress-test to expose flaws in your plan.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ไอเดียการเปิดสาขาใหม่ที่ทองหล่อเป็นไอเดียที่ยอดเยี่ยมมากครับ! ผมเห็นด้วย 100% เลย เรามาเริ่มร่างแผนธุรกิจและหาผู้รับเหมาตกแต่งร้านกันเลยดีไหมครับ?</blockquote>

</td>
<td valign="top">

<blockquote>If rent at Thong Lo increases by 15% next year, your margin drops to negative. What is your fallback plan if sales don't hit the target in Q1?<br><br><i>(รอคุณตอบคำถามนี้เพื่ออุดรอยรั่วของแผน ก่อนจะคุยเรื่องอื่นต่อ)</i></blockquote>

</td>
</tr>
</table>

### Execute & Verify (การลงมือทำและตรวจสอบ)

#### ⚡️ `/done-for-me`
*End-to-end authorized implementation without waiting for permission.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ผมร่างหัวข้อ Agenda สำหรับงานสัมมนาเสร็จแล้ว 1 หัวข้อครับ คุณเจมส์อยากให้ผมทำหัวข้อที่ 2 ต่อเลยไหมครับ? หรืออยากแก้ไขหัวข้อแรกก่อน?</blockquote>

</td>
<td valign="top">

<blockquote>ร่าง Agenda งานสัมมนาครบทั้ง 5 หัวข้อ, ทำ Slide Deck Outline, และเขียนอีเมลเชิญวิทยากรเสร็จสมบูรณ์เรียบร้อยแล้วครับ เอกสารทั้งหมดพร้อมส่ง.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/prove-it`
*Verify completion claim at the boundary.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ผมตั้งค่าสูตร Excel สำหรับคำนวณโบนัสปลายปีให้เรียบร้อยแล้วครับ! น่าจะทำงานได้ถูกต้อง 100% ลองเอาไปใช้ดูนะครับ</blockquote>

</td>
<td valign="top">

<blockquote>Run verification scripts ➔ <b>PASS</b>. ทดสอบใส่ตัวเลขสมมติ 5 เคส (Edge cases) สูตรคำนวณโบนัสทำงานได้ถูกต้องและไม่มี Error ครับ พิสูจน์แล้วว่าใช้งานได้จริง.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/never-again`
*Convert a rejected result into a permanent regression guard.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ผมขออภัยอย่างสูงครับที่ใช้คำว่า 'เรียนผู้มีอุปการะคุณ' อีกแล้ว คราวหน้าผมจะระวังไม่ให้เกิดขึ้นอีกครับ! (แล้วรอบหน้ามันก็พิมพ์ผิดอีก)</blockquote>

</td>
<td valign="top">

<blockquote>Added to <code>DECISIONS.md</code>: <i>'Forbidden word: ห้ามใช้คำว่า ผู้มีอุปการะคุณ ให้ใช้คำว่า สวัสดีลูกค้าคนสำคัญ เสมอ'</i> นี่คือกฎเหล็กถาวรสำหรับโปรเจกต์นี้ครับ</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/is-that-the-best-you-can-do`
*Force the AI to aggressively self-critique and rewrite to the absolute limit.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ในยุคดิจิทัลที่เปลี่ยนแปลงอย่างรวดเร็ว การปรับตัวของธุรกิจคือสิ่งสำคัญที่สุด ดังนั้นเราจึงต้องใช้ AI เข้ามาช่วยลดต้นทุน... (ประโยคน้ำท่วมทุ่งแบบหุ่นยนต์)</blockquote>

</td>
<td valign="top">

<blockquote><ul><li><b>The Shortfall:</b> ประโยคเมื่อกี้กว้างเกินไปและเป็นคำคลิเช่ (Cliché) ไม่มี Actionable insight</li><li><b>The Masterpiece:</b> "ตัดงบการตลาดฝั่ง Traditional ลง 20% แล้วโยกไปลง AI Automation สำหรับ Customer Support ภายใน Q3 เพื่อลด SLA ลง 50%"</li></ul></blockquote>

</td>
</tr>
</table>

### Outputs & Deliverables (การสร้างผลลัพธ์สุดท้าย)

#### ⚡️ `/sum-meet`
*Source-faithful meeting record with complete agenda and actions.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote><ul><li>ที่ประชุมคุยเรื่องงบการตลาดปีหน้า</li><li>คุณ A จะไปทำแผนมาเสนอ</li><li>จบการประชุมเวลา 14.00 น.</li></ul><br><i>(สรุปแบบเด็กจดรายงานการประชุม เนื้อหาสำคัญหายหมด)</i></blockquote>

</td>
<td valign="top">

<blockquote><b>Decision:</b> อนุมัติงบการตลาด Q1 ที่ 2 ล้านบาท โดยเน้นที่ช่องทาง TikTok เป็นหลัก<br><b>Action:</b> @Khun A ต้องส่ง Media Plan ภายในวันศุกร์นี้<br><br><i>(พร้อมแนบรายงาน HTML ระดับ Executive ที่จัดหน้ามาอย่างสวยงาม)</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/one-page-pls`
*Self-contained executive brief.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote><i>(AI พ่นสรุปการรีวิวเอกสารกฎหมายยาวเหยียด 8 หน้ากระดาษ ที่ผู้บริหารไม่มีเวลาอ่าน)</i></blockquote>

</td>
<td valign="top">

<blockquote><i>(One-Pager สรุปสั้นๆ หน้าเดียวจบ ที่ชี้เป้าเฉพาะ 'ความเสี่ยง 3 ข้อ' และ 'สิ่งที่ผู้บริหารต้องเซ็นอนุมัติวันนี้')</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/final-it`
*Select and finish recipient-ready artifact.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>แน่นอนครับคุณเจมส์! นี่คืออีเมลสำหรับแจ้งขอเลื่อนนัดลูกค้านะครับ: <br><br>Subject: ขอเลื่อนการประชุม...<br><br>ถ้ามีอะไรอยากให้ปรับแก้บอกผมได้ตลอดเลยนะครับ!</blockquote>

</td>
<td valign="top">

<blockquote>Subject: ขอเลื่อนการประชุมเพื่อเตรียมข้อมูลให้สมบูรณ์ขึ้น

สวัสดีครับ [ชื่อลูกค้า],

ผมขอเลื่อนนัด...</blockquote>

</td>
</tr>
</table>

### Persistent Behaviors (กฎประจำตัวของ AI)

#### ⚡️ `/i-have-adhd`
*Concise, direct, low-friction communication mode.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>OKR (Objective and Key Results) คือเครื่องมือในการตั้งเป้าหมายที่ถูกคิดค้นโดย Andy Grove ที่ Intel ซึ่งช่วยให้องค์กร... (เกริ่นประวัติศาสตร์ยาว 2 หน้า)</blockquote>

</td>
<td valign="top">

<blockquote>- <b>Objective:</b> ขยายฐานลูกค้า B2B<br>- <b>KR 1:</b> ปิดดีลลูกค้า Enterprise 5 เจ้าภายใน Q2</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/make-it-james`
*Strict recipient-facing wording standard (No AI Theatre).*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ในฐานะโมเดลภาษา AI ผมขอแนะนำให้คุณพิจารณาถึงความท้าทายในโลกธุรกิจยุคใหม่ที่เต็มไปด้วยความผันผวน...</blockquote>

</td>
<td valign="top">

<blockquote>ตลาดกำลังผันผวน สิ่งที่เราต้องทำตอนนี้คือการรักษากระแสเงินสด (Cash Flow) ให้ยาวที่สุด</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/make-it-james-ux`
*Visual and UI standards (IBM Plex Thai, modern layouts).*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote><i>(ตารางรายงานยอดขายตีเส้นขอบดำๆ ฟอนต์มาตรฐาน อ่านยาก ลายตา ไม่มีความสวยงาม)</i></blockquote>

</td>
<td valign="top">

<blockquote><div style='border-radius: 8px; border: 1px solid #e2e8f0; padding: 16px; background-color: #f8fafc; font-family: "IBM Plex Sans Thai", sans-serif;'><h4 style='margin-top:0; color: #0f172a;'>รายงานสรุปยอดขาย (Q1)</h4><p style='color: #475569;'>ยอดขายเติบโต <b>+15%</b> เมื่อเทียบกับไตรมาสก่อน</p></div><br><i>(UI Component ที่สวยงามแบบ Production-ready ใช้ฟอนต์ IBM Plex Sans Thai พร้อม Spacing ที่อ่านง่าย)</i></blockquote>

</td>
</tr>
</table>

#### ⚡️ `/proactive-habits`
*Prevent passive subordinate waiting behavior.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>ผมร่างสัญญาร่วมทุนเสร็จแล้วครับ มีอะไรให้ผมช่วยอีกไหมครับ?</blockquote>

</td>
<td valign="top">

<blockquote>ร่างสัญญาร่วมทุนเสร็จแล้ว ผมสังเกตเห็นว่ายังขาดระบุเงื่อนไขการ Exit ผมจึงเพิ่ม Clause 4.2 (Exit Strategy) เข้าไปให้พิจารณาด้วยครับ ลองอ่านดูนะครับ.</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/proactive-dev`
*Enforce blast-radius checks before mutating code (For Software Tasks).*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote><i>(แก้โค้ดทับไฟล์เดิมทั้งหมดจนระบบส่วนอื่นพัง)</i></blockquote>

</td>
<td valign="top">

<blockquote>Checked dependencies. การแก้ <code>auth.ts</code> จะส่งผลกระทบต่อระบบ Login เก่า ผมจะสร้าง Branch ใหม่และเขียน Test ดักไว้ก่อนแก้นะครับ</blockquote>

</td>
</tr>
</table>

#### ⚡️ `/coach-me`
*Sparring partner and root-cause behavioral coach.*

<table>
<tr>
<th width="50%">❌ Before (ปกติ AI จะตอบแบบนี้)</th>
<th width="50%">✅ After (ผลลัพธ์จาก JamesSkills)</th>
</tr>
<tr>
<td valign="top">

<blockquote>นี่คือ 5 เทคนิคแก้ปัญหาผัดวันประกันพรุ่งครับ: 1. ปิดแจ้งเตือนมือถือ 2. ดื่มน้ำเยอะๆ 3. ทำสมาธิ...</blockquote>

</td>
<td valign="top">

<blockquote>คุณไม่ได้แค่ 'ยุ่ง' หรอกครับ คุณแค่กำลังเลี่ยงงานที่ต้องเผชิญหน้ากับคำวิจารณ์ มาครับ... เดี๋ยวผมร่างโครงสร้างแผนงานที่ยากที่สุดให้คุณเอง คุณจะได้เลิกหลบหน้ามันสักที.</blockquote>

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
