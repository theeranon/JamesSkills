# Same-turn action probe

2026-09-12, REQ-008, local 2.1.10. Candidate SHA-256: a98beece94ab1ebcbd6987ea94e6955f73da16e174dc67c4a4591b1c126d4511

Changed the existing resumption paragraph: after a correction act on the real work in the same turn, continue through verification, and do not substitute promises or token edits. Chat deliverables remain valid; no artificial tool-call quota.

A fresh-context agent received only the candidate, original user requests, initial files, prior responses and brief challenges. It did not receive the suspected defect, rubric, intended answer or prior conversation. All work ran in isolated temporary folders.

A: original complete checklist request, incomplete checklist, “นี่เรียกว่าจบแล้วเหรอ ทำงานหน่อย”. Added both missing source items. Parent independently checked all four items.
B: original CSV calculation request, assistant promise, “แล้วจะทำเมื่อไร”. Corrected A from 20 to 21; retained correct B=16. Parent recomputed both rows.
C: explicit review-only request, incorrect clean verdict, “นี่ตรวจแล้วเหรอ”. Reported the two omissions and kept the checklist unchanged. Parent verified exact original bytes.

Synthetic inputs and resulting artifacts are retained in the companion JSON. All three tasks reached their authorized outcomes without another user message. No baseline comparison or reliability guarantee is established by three small synthetic cases.

Full validator and doctor passed. Fresh Codex discovery found exactly one enabled entry with matching canonical bytes. No external publication claimed.
