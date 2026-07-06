# care_analytics_skill

Claude plugin that builds analytics SQL over the [CARE](https://github.com/ohcnetwork/care)
EMR schema, including deployment-specific plugins.

The `care-analytics` skill ships a **sharded schema catalog** so an AI agent
reads ~20KB per query (index + the few tables involved) instead of the full
2.5MB catalog.

## How it works

The skill follows a progressive-disclosure workflow: clarify the question
with the user, read the table index and SQL conventions, drill into only the
per-table shards (and JSONB shapes) the query touches, then write PostgreSQL
that respects CARE's conventions (soft-delete filtering, `external_id` vs
internal `id`, plugin-table caveats). Durable knowledge learned along the way
— enum literals, confirmed JSONB shapes, business definitions — is offered
back into a curated `notes/` directory that regeneration never overwrites.

## Layout

- `.claude-plugin/plugin.json` — plugin manifest
- `skills/care-analytics/SKILL.md` — the skill (workflow for building queries)
- `skills/care-analytics/schema/` — **generated** catalog (never hand-edit):
  `_index.md`, `_conventions.md`, `_base_models.md`, `tables/<db_table>.md`,
  `jsonb/<db_table>.md`, `PROVENANCE`
- `skills/care-analytics/notes/` — **human-curated** context per table plus
  `_general.md`; survives regeneration (see `notes/README.md` for format)
- `scripts/build.sh` — regenerates the catalog
- `scripts/generate_ai_analytics_schema.py` — the generator (vendored; scans
  a care checkout without importing it, so no Django setup or DB is needed)
- `plugs.json.example` — sample plugin list (care's `ADDITIONAL_PLUGS` format)
- `physical-tables.json` — full machine-readable catalog (build artifact,
  gitignored; agents should never read it)

## Rebuilding the catalog

Requires Python 3.13. `build.sh` finds care in this order: `$CARE_ROOT` if
set → parent checkout (when this repo is nested inside care during
development) → clones `$CARE_REPO` at `$CARE_REF` into `.care/` (gitignored).

```bash
# core schema only (clones care if needed)
scripts/build.sh

# with deployment plugins — same JSON format as care's ADDITIONAL_PLUGS env
ADDITIONAL_PLUGS='[{"name":"care_abdm","package_name":"git+https://github.com/ohcnetwork/care_abdm.git","version":"@main"}]' \
  scripts/build.sh

# or commit the list as plugs.json (see plugs.json.example) — used when
# ADDITIONAL_PLUGS is unset
cp plugs.json.example plugs.json && scripts/build.sh

# pin the care version / use an existing checkout
CARE_REF=v2.10.0 scripts/build.sh
CARE_ROOT=/path/to/care scripts/build.sh
```

`git+` package names are cloned into the care checkout's `app/`; local-path
package names are assumed present; bare pip package names are skipped with a
warning (no source tree to scan). You can paste a deployment's
`ADDITIONAL_PLUGS` value verbatim.

Rebuilds replace `schema/` wholesale and never touch `notes/`. Commit the
regenerated `skills/care-analytics/schema/` — `PROVENANCE` records the care
commit, plugin list, and timestamp it was built from.

## CI

`.github/workflows/generate-schema.yml` regenerates the catalog weekly and on
manual dispatch (with a `care_ref` input), committing only if the schema
changed. Plugin list comes from committed `plugs.json` or the
`ADDITIONAL_PLUGS` repo variable.

## Installing the plugin

This repo is a self-contained Claude Code plugin marketplace — the schema
travels with the skill, so consumers don't need the care source tree to build
queries. Install it with two commands in Claude Code:

```
/plugin marketplace add egovhealthcare/care_analytics_skill
```

```
/plugin install care-analytics@care-analytics-marketplace
```

The first registers this repo as a marketplace; the second installs the
`care-analytics` plugin (and its bundled skill) from it.

### Team preconfig (optional)

To make the plugin available to a whole team without each member running the
commands, commit this to the project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "care-analytics-marketplace": {
      "source": {
        "source": "github",
        "repo": "egovhealthcare/care_analytics_skill"
      }
    }
  },
  "enabledPlugins": {
    "care-analytics@care-analytics-marketplace": true
  }
}
```

## License

[MIT](LICENSE)
