---
name: prove-it
description: Verify whether a claimed result actually works for its recipient. Use before declaring code, integrations, deployments, notifications, documents, or agent work complete.
---

# Prove It

Agent reports, green health checks, screenshots of setup, and generated files are routing evidence, not completion proof.

First write the exact promise being tested and identify the target: repository, branch, commit or version, environment, account or tenant, route, data set, and recipient when relevant. A proof from another target does not transfer silently.

Derive the proof plan from that promise. Verify both semantic correctness and the layers relevant to the promised outcome:

1. Source and local checks: intended code, schema, tests, and stored state.
2. Provider boundary: authenticated event, log, API result, or delivery record.
3. User journey: real route, login, permissions, content, action, and persistence.
4. Production: deployed identity, current version, representative data, and recipient-visible result.

Exercise the happy path and at least one relevant negative, permission, stale-state, retry, or failure path. Passing mechanics with the wrong owner, meaning, ranking, recipient, or business result is still a failure.

Report each layer as passed, failed, not tested, or not applicable. Keep a short decision trace from promise to evidence to verdict. Never collapse untested into done. After a failure, state location, cause, fix, and the exact remaining gate.

For delegated implementation, verify the requirement IDs, base revision, owned paths, and produced evidence rather than accepting a worker summary. Use an independent verifier when the risk or scope justifies delegation; self-review alone is not independent proof.
