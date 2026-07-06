# Metabase connector quirks

2026-07-05

- Pivot display (`display: "pivot"`) works only on MBQL (notebook) queries —
  never native SQL. Needs ≥2 breakouts, and `pivot_table.column_split` in
  `visualization_settings` assigns breakouts to rows/columns/values.
- Division of labor with transforms: put the native-SQL complexity **inside
  the transform**, then query its output table with MBQL. That keeps the
  full visualization surface (pivots, drill-through, brush filters) usable
  downstream. Don't query transform outputs with native SQL when a
  visualization is the deliverable.
- The MCP connector cannot create or edit transforms (write path absent;
  see SKILL.md for the save-as-question handoff procedure).
