---
name: prove-it
description: Verify whether a claimed result actually works for its recipient. Use before declaring code, integrations, deployments, notifications, documents, or agent work complete.
---

# Prove It

Agent reports, green health checks, screenshots of setup, and generated files are routing evidence, not completion proof.

Verify the layers relevant to the promised outcome:

1. Source and local checks: intended code, schema, tests, and stored state.
2. Provider boundary: authenticated event, log, API result, or delivery record.
3. User journey: real route, login, permissions, content, action, and persistence.
4. Production: deployed identity, current version, representative data, and recipient-visible result.

Report each layer as passed, failed, not tested, or not applicable. Never collapse untested into done. After a failure, state location, cause, fix, and the exact remaining gate.
