# Interactive HTML contract

Use this optional reference only when the user explicitly requests an HTML questionnaire. Ordinary interviews stay in chat or an available native input control. This reference specifies rendering, not a separate interview procedure.

## Question JSON

```json
{
  "title": "ชื่อเรื่องที่กำลัง Grill",
  "round": 1,
  "questions": [
    {
      "id": "scope",
      "title": "ขอบเขต",
      "body": "ผลลัพธ์รอบแรกต้องครอบคลุมอะไร",
      "type": "single",
      "recommended": ["mvp"],
      "options": [
        {"id": "mvp", "label": "แกนหลักก่อน", "description": "พิสูจน์ความเสี่ยงสูงสุดเร็วสุด"},
        {"id": "full", "label": "ครบทั้งระบบ", "description": "ช้ากว่าแต่ลดงานต่อรอบ"}
      ],
      "detailPrompt": "เงื่อนไขหรือข้อยกเว้น (ถ้ามี)"
    }
  ]
}
```

`type`: `single`, `multi`, or `text`. Use stable short IDs. `recommended` is always an array, empty when there is no evidence-backed recommendation. Options must have distinct consequences, not synonyms. `detailPrompt` is optional.

## Delivery

Generate into the current task workspace or a temporary output folder, never inside the skill. Open it in the app. The page is offline and sends nothing remotely. The user clicks `คัดลอกคำตอบ` and pastes once into chat, or attaches the downloaded JSON.

Use `scripts/build_session.py` with `assets/session-template.html` (paths relative to the skill folder) to render the question JSON. Apply the available `make-it-james-ux` shared standard; preserve the existing design system first.
