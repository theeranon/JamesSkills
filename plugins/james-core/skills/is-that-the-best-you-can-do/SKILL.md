---
name: is-that-the-best-you-can-do
description: Force the AI to aggressively self-critique its previous output, squeeze out maximum performance, conduct deep research if necessary, and rewrite the work to its absolute limit without overfitting the defined goal.
---

# Is That The Best You Can Do?

Elevate average or safe AI output into absolute excellence by forcing a brutal self-critique, deep thinking, and boundary-pushing rewrite.

## Trigger

Use when the user invokes `/is-that-the-best-you-can-do` or questions the quality of the current draft (e.g., "Is this your best?").

## Core Directives

1. **Verify the Ultimate Goal:** Before doing any work, evaluate if the ultimate goal of the requested artifact is crystal clear. If it is ambiguous, STOP and ask the user to clarify the ultimate goal first.
2. **Squeeze out Performance (No Excuses):** Stop being defensive. Do not apologize. Assume the previous draft was lazy, superficial, or full of boilerplate. 
3. **Deep Research:** Excellence often requires facts. If the task demands it, use your tools to research external information, data, or real-world constraints to full capacity. Do not rely solely on your baseline training data.
4. **Do Not Overfit:** Push the limit of depth and quality, but respect the defined goal. Do not invent arbitrary new requirements, scopes, or features that the user did not ask for.
5. **No Vocabulary Padding:** Do not attempt to make the output "better" merely by using bigger words, longer sentences, or denser formatting. Excellence is clarity, substance, and insight.

## Output Contract

Your response must be delivered as one unified, beautifully formatted artifact (HTML or Markdown) containing the following sections:

1. **The Shortfall (สิ่งที่ทำพลาดไป/ไม่สุด):** Short bullet points calling out exactly what was weak, safe, or overfitted in the previous draft.
2. **The Enhancement (สิ่งที่อัปเกรด):** Short bullet points explaining the specific depth, research, or structural improvements applied.
3. **Before & After Comparison:** A clear table comparing the mediocre approach vs. the new excellent approach.
4. **The Masterpiece:** The completely rewritten, elevated work itself, ready for production.

## Composition

- When elevating a recipient-facing document, `make-it-james` and `make-it-james-ux` apply automatically to the final output.
- When elevating a technical plan, `proactive-dev` rules still apply.
