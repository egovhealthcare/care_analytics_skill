#!/usr/bin/env bash
# Build the sharded schema catalog into skills/care-analytics/schema/.
#
# Env:
#   CARE_ROOT        path to an existing care checkout. If unset: uses ../..
#                    when this repo sits inside care, otherwise clones care
#                    into .care/ (gitignored).
#   CARE_REPO        care git URL for the clone fallback
#                    (default: https://github.com/ohcnetwork/care)
#   CARE_REF         branch/tag/SHA to check out in the clone (default: develop)
#   ADDITIONAL_PLUGS same JSON format as care's ADDITIONAL_PLUGS env
#                    (plugs/manager.py): a JSON array of Plug kwargs, e.g.
#                    [{"name":"care_scribe",
#                      "package_name":"git+https://github.com/ohcnetwork/care_scribe.git",
#                      "version":"@main"}]
#                    Falls back to plugs.json at the repo root if unset.
#                    git+ package_names are cloned into $CARE_ROOT/app/<name>;
#                    local-path package_names (e.g. app/...) are assumed
#                    present; bare pip package names are skipped with a
#                    warning (no source to scan).
#   PYTHON           python executable (default: python3, needs 3.13+)
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PYTHON="${PYTHON:-python3}"
CARE_REPO="${CARE_REPO:-https://github.com/ohcnetwork/care}"
CARE_REF="${CARE_REF:-develop}"

if [[ -z "${CARE_ROOT:-}" ]]; then
  if [[ -d "$REPO_DIR/../../care" && -f "$REPO_DIR/../../manage.py" ]]; then
    CARE_ROOT="$(cd "$REPO_DIR/../.." && pwd)"  # dev convenience: nested in care
  else
    CARE_ROOT="$REPO_DIR/.care"
    if [[ -d "$CARE_ROOT/.git" ]]; then
      git -C "$CARE_ROOT" fetch --quiet
    else
      git clone --quiet "$CARE_REPO" "$CARE_ROOT"
    fi
    git -C "$CARE_ROOT" checkout --quiet "$CARE_REF"
    git -C "$CARE_ROOT" pull --quiet --ff-only origin "$CARE_REF" 2>/dev/null || true
  fi
fi

if [[ ! -d "$CARE_ROOT/care" ]]; then
  echo "error: no usable care checkout at $CARE_ROOT (set CARE_ROOT)" >&2
  exit 1
fi
echo "care: $CARE_ROOT @ $(git -C "$CARE_ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)"

PLUGS_JSON="${ADDITIONAL_PLUGS:-}"
if [[ -z "$PLUGS_JSON" && -f "$REPO_DIR/plugs.json" ]]; then
  PLUGS_JSON="$(cat "$REPO_DIR/plugs.json")"
fi

if [[ -n "$PLUGS_JSON" ]]; then
  # Parse care's ADDITIONAL_PLUGS JSON into "name<TAB>url<TAB>ref" lines
  # (git+ packages only; local paths assumed present; pip names skipped).
  while IFS=$'\t' read -r kind name url ref; do
    case "$kind" in
      git)
        dest="$CARE_ROOT/app/$name"
        if [[ -d "$dest/.git" ]]; then
          git -C "$dest" fetch --quiet
        else
          git clone --quiet "$url" "$dest"
        fi
        if [[ -n "$ref" ]]; then
          git -C "$dest" checkout --quiet "$ref"
        fi
        echo "plug: $name @ $(git -C "$dest" rev-parse --short HEAD)"
        ;;
      local)
        echo "plug: $name (local path $url — assumed present in care tree)"
        ;;
      pip)
        echo "warning: plug $name is a pip package ($url) — no source to scan, skipped" >&2
        ;;
    esac
  done < <(PLUGS_JSON="$PLUGS_JSON" "$PYTHON" - <<'PYEOF'
import json, os
for plug in json.loads(os.environ["PLUGS_JSON"]):
    name = plug["name"]
    pkg = plug.get("package_name", name)
    ref = plug.get("version", "").lstrip("@")
    if pkg.startswith("git+"):
        print(f"git\t{name}\t{pkg.removeprefix('git+')}\t{ref}")
    elif "/" in pkg:
        print(f"local\t{name}\t{pkg}\t")
    else:
        print(f"pip\t{name}\t{pkg}\t")
PYEOF
)
fi

# Vendored generator: scans the care tree, writes into this repo.
CARE_SOURCE_ROOT="$CARE_ROOT" AI_SCHEMA_OUTPUT_DIR="$REPO_DIR" \
  "$PYTHON" "$REPO_DIR/scripts/generate_ai_analytics_schema.py"

{
  echo "care_sha: $(git -C "$CARE_ROOT" rev-parse HEAD 2>/dev/null || echo unknown)"
  echo "plugs: ${PLUGS_JSON:-none}"
  echo "generated_at: $(date -u +%FT%TZ)"
} > "$REPO_DIR/skills/care-analytics/schema/PROVENANCE"

echo "schema written to skills/care-analytics/schema/"
