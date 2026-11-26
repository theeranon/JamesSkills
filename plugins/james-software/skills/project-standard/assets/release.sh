#!/usr/bin/env bash
# Preview by default; --push publishes only the generated branch, never a live deployment.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
exec python3 tools/release-domain.py "$@"
