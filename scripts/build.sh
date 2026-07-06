#!/usr/bin/env bash
# Build the sharded schema catalog into skills/care-analytics/schema/.
#
# Thin wrapper: all logic (cloning care, cloning ADDITIONAL_PLUGS/plugs.json
# plugs, scanning, writing shards + PROVENANCE) lives in
# scripts/generate_ai_analytics_schema.py — run that directly if you prefer.
#
# Env (all optional, consumed by the python script):
#   CARE_ROOT        existing care checkout; default: clone into .care/
#   CARE_REPO        care git URL (default: https://github.com/ohcnetwork/care)
#   CARE_REF         branch/tag/SHA for the clone (default: develop)
#   ADDITIONAL_PLUGS care-style plug JSON; falls back to plugs.json at repo root
#   PYTHON           python executable (default: python3, needs 3.13+)
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
exec "${PYTHON:-python3}" "$REPO_DIR/scripts/generate_ai_analytics_schema.py"
