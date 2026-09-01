# Interactive HTML contract

Use HTML when the frontier needs multi-select, Select All, more than three independent questions, or detailed answers without repeated chat turns.

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

`type`: `single`, `multi`, or `text`. Use stable short IDs. `recommended` is always an array. Options must have distinct consequences, not synonyms. `detailPrompt` is optional.

## Delivery

Generate into the current task workspace or a temporary output folder, never inside the skill. Open it in the app. The page is offline and sends nothing remotely. James clicks `คัดลอกคำตอบ` and pastes once into chat, or attaches the downloaded JSON.

Apply `make-it-james-ux`: IBM Plex Sans Thai, dense hierarchy, 6px radius, one blue accent, semantic colors only, no decorative rails, gradients, or card soup.
