---
name: grill-me
description: Stress-test James's plan, decision, or idea through a branching interview with mouse-first inline controls or a text-chat fallback. Use when James says grill me, asks to sharpen thinking, or wants a decision tree challenged.
---

# Grill Me — James Edition

Reach shared understanding before implementation. Keep the decision-tree rigor of `grilling`; replace its type-a-number interaction with the fastest available mouse-first UI.

## Interview logic

1. Build a private design tree. A decision may unlock later decisions.
2. Ask only the current **frontier**: unresolved decisions whose prerequisites are settled.
3. Find facts yourself. Never ask James for information available from files or tools.
4. Every question contains a specific recommendation and its reason.
5. After each response, update the tree, expose conflicts or trade-offs, and continue with the newly unlocked frontier.
6. Finish only when no meaningful branch remains. Show the resolved decision map and ask for final confirmation before acting.

Do not use a fixed question count. Do not ask dependent questions in the same round. Do not turn the interview into a generic survey.

## Choose the interaction

### Inline controls — default for 1–3 independent questions

Use the host's structured user-input control when available. Make every option clickable, place the recommendation first and label it `(แนะนำ)`, and use the control's free-form `Other` field for detailed answers.

- Ask one question at a time when its answer changes the next question.
- Ask up to three together only when genuinely independent.
- Keep 2–3 mutually exclusive choices per inline question.
- Never ask James to reply with `1`, `2`, `A/B`, question IDs, or comma-separated choices when clickable controls exist.

### Text-Chat Fallback — when inline controls are unavailable

If native interactive popup tools (like `request_user_input` or `ask_question`) are unavailable on the current platform (e.g., Claude), **DO NOT generate HTML forms or artifacts**. 

Fallback to Text-Chat mode:
- Ask ONE concise question at a time directly in the chat.
- Provide clear, numbered, or bulleted options.
- Wait for James's text reply before proceeding to the next question.
- Do not output large JSON or HTML files. Keep the interview flowing naturally in the chat window.

## Response handling

- Treat `detail` as an override or qualification.
- Distinguish `all selected intentionally` from `no selection`.
- If an answer conflicts with an earlier decision, show the exact conflict and ask only what resolves it.
- Preserve unanswered branches; never silently fill them from the recommendation.
- Report progress as `รอบ N · ตัดสินใจแล้ว X · เหลือ Y สาขา`.

## Completion output

Return a compact decision map: decision, chosen answer, reason/detail, downstream consequence, and unresolved risk. Then ask: `ยืนยันแผนนี้และให้เริ่มทำเลยไหม?`
