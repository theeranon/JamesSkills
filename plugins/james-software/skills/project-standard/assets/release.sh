#!/usr/bin/env bash
# Preview by default; --push publishes only the generated production branch.
# Where Git Manager auto-deploys production, that push starts the live deployment.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
exec python3 tools/release-domain.py "$@"
