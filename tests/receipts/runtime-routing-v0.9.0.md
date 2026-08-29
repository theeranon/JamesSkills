# Runtime Routing Receipt — 0.9.0

Date: 2026-08-29
Mode: fresh ephemeral, read-only, no repository edits

| Runtime | Version and mode | Recurring company method | Macro organization transformation | Bounded workshop | Explicit build-framework |
|---|---|---|---|---|---|
| Codex CLI | 0.147.0, gpt-5.6-luna, low | `build-framework` | `transformation-journey` | `learning-experience-design` | house-library search, then reuse-first |
| Claude Code | 2.1.220, Haiku, low | `build-framework` | `transformation-journey` | `learning-experience-design` | loaded `build-framework`; house-library search, then reuse-first |

Commands:

```bash
codex exec -m gpt-5.6-luna -c 'model_reasoning_effort="low"' -s read-only --ephemeral -C '<repo>' '<prompt>'
claude -p --model haiku --effort low --permission-mode plan --tools Read,Glob,Grep --no-session-persistence '<prompt>'
```

Result: Codex implicit 3/3 plus explicit behavior passed. Claude implicit 3/3 passed. Claude explicit behavior passed in two isolated reruns and the tool trace read the installed `build-framework` package. One earlier parallel Claude sample produced the correct reuse-first behavior but mislabeled the route as `james-skill-router`; retained as a low-severity stochastic-label warning rather than hidden.

Scope: evidence covers these two runtimes and these four routing cases only. It does not claim Gemini, Antigravity, every model, or universal future parity.
