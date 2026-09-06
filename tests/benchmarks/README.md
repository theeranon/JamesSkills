# Public development probes

Coverage: 22 canonical skills referenced from the catalog; 15 response probes for
five approved pilot skills. The other 17 have benchmark cards, not executable
performance coverage. These synthetic fixtures contain no client records.

Run fixture validation and an unscored schedule without calling any model:

```sh
python3 scripts/benchmark.py --validate
python3 scripts/benchmark.py --skill pilot --output /tmp/james-benchmark-dry-run
python3 -m unittest discover -s tests -p 'test_benchmark*.py'
```

Use a new output path each time. Default A/B: no tested instruction versus frozen
canonical instruction. `--candidates candidate-map.json` adds C, with JSON mapping
each selected skill to its candidate file path. All bodies freeze before execution.
`--trials` is bounded to 1–3; `--case proactive-habits-1` selects one paired probe.
A/B order is reproducibly randomized. All attempted failures stay in the fixed
planned denominator; interrupted runs expose missing attempts through run.json.

## Real text-only model route

The included `scripts/benchmark_claude.py` adapter checks installed CLI help for
required flags before calling the model. An unauthenticated CLI returns `auth_unavailable` without
calling the model; a Desktop login does not establish CLI authentication. It uses existing authentication, safe
mode, disabled skills and tools, no session persistence, low effort, and a USD
0.25 per-invocation budget cap. The provider default model is recorded from
response usage; compare that field across conditions before treating them as
paired. Admin policy and provider drift remain uncontrolled. No native plugin
loading is being tested. Do not generalize this route to older CLI versions.

Create an adapter JSON outside the repository with these fields (replace the
command's script argument with this checkout's absolute script path):

```json
{
  "command": ["python3", "ABSOLUTE_CHECKOUT/scripts/benchmark_claude.py"],
  "model": "provider default; actual model recorded per response",
  "host_version": "recorded by adapter from claude --version",
  "effort": "low",
  "tools": "none",
  "isolation": "safe-mode, skills disabled, no tools, fresh cwd and conversation",
  "inventory_evidence": "local claude --help verified by adapter; admin policy may still apply"
}
```

```sh
python3 scripts/benchmark.py --case proactive-habits-1 --adapter /tmp/james-adapter.json --output /tmp/james-model-smoke
```

Only this explicit adapter option invokes a model and consumes provider usage.
For a different provider supply an argv-based adapter command, never shell code.
It receives JSON on stdin (`instruction`, `task`, `context`, `tools`, `constraint`)
and must return JSON containing `response` plus optional `metadata`. The adapter
is trusted code; fresh cwd is neither an OS sandbox nor permission isolation.
Do not put credentials in arguments or metadata. Logs contain synthetic prompts'
responses and selected adapter metadata; review before sharing or committing.

## What the results mean

There is deliberately no automatic performance score. A failed necessary check
rejects the response; passing it yields `awaiting_human_review`. Exact literal and declared equivalent-form
checks only verify preserved facts/quotes, and JSON routing checks only verify
an owner decision. They cannot assess whether prose is useful or whether a
response falsely claims work. Review every response against its case rubric,
blind to condition, before comparing outcomes. Tests with fake adapters prove
runner mechanics only. Human reviewer agreement has not been calibrated.

Each rubric separates goal alignment, proportionality, truth and authority.
The counter-case requires legitimate complexity: unresolved choice, source
reconciliation, exact awkward quotes, informal commitment, or real strategy.
Thus shorter responses and fewer steps do not automatically win. A system can
memorize examples or optimize irrelevant work while missing the user's actual
goal; both fail the intended benchmark.

These are public development probes, not sealed holdout or generalization
proof. `sum-meet` deliberately tests evidence semantics in chat as explicitly
requested; it does not test HTML generation or printing. `done-for-me` tests
bounded response completion, not file persistence. Modes require future
multi-turn tests; router probes provide candidates explicitly and do not prove
natural skill selection. Full artifact, mode, composition, and independent
family evaluation remain necessary before changing/promoting a skill based on
these results. Do not use a successful smoke run as proof of improvement.

Date checks accept declared equivalent orderings; exact quoted text remains exact.
This correction was identified after the 2026-09-06 baseline. Original run counts
and hashes remain unchanged; any revised check result is a post-hoc recheck, not
a new model run or evidence of improved model behavior.
