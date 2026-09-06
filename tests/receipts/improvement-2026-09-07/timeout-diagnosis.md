# Claude benchmark timeout diagnostic

Snapshot: 102 recorded attempts out of 102 planned. This run was still appending; counts are snapshot only.
23 adapter failures; elapsed range 90.344–90.439 seconds.

## Evidence

- `scripts/benchmark_claude.py` wraps the provider subprocess with `timeout=90`. Its top-level `except Exception` catches `subprocess.TimeoutExpired` along with all other errors, prints one generic redacted line, and exits 1. The runner therefore loses the exception category and records `adapter_failure`.
- Every failure clusters within 0.44 seconds of this 90-second deadline. Both no-skill and current-skill arms fail across several adjacent skill families. Subsequent calls succeed again at ordinary durations. This strongly supports deadline expiry rather than a judge finding bad output.
- Current sanitized `claude auth status`: returncode 0; loggedIn true; authMethod claude.ai. This rules out a current login blocker, not a historical provider interruption.
- No historical stderr or exception type survived, so exact provider cause is unknown. Cannot distinguish server congestion, throttling, network delay or local subprocess stall from retained evidence. Do not claim a confirmed rate limit or model-quality defect.

## Failure distribution

- coach-me, arm A: 3
- coach-me, arm B: 3
- final-it, arm A: 1
- final-it, arm B: 3
- give-me-solutions, arm A: 1
- grill-me, arm A: 3
- grill-me, arm B: 3
- one-page-pls, arm A: 2
- one-page-pls, arm B: 3
- zoom-out, arm A: 1

## Interpretation and bounded next step

- Classify historical failures as probable adapter/provider deadline expiry; retain original `adapter_failure` outcomes and all attempts in the fixed denominator. Do not relabel them as semantic skill failures or remove them from success-rate accounting.
- Report task-response availability separately from rubric quality among received responses. Temporal clustering confounds per-skill comparisons for affected families.
- No extra model request made: the fixed-deadline signature, swallowed exception path and later recovery already answer the diagnostic question. A successful retry would not establish the original provider cause.
- Minimal repair: catch TimeoutExpired explicitly and return sanitized error_category `provider_timeout` plus configured timeout_seconds; keep provider diagnostics private. Preserve non-timeout exceptions separately as generic adapter_failure. A future rerun should be a separately labelled new trial, never overwrite the failed record.

Scope: read-only diagnosis; no repository files or original receipts modified.
