# Transform registry

One file per confirmed Metabase Transform: `<slug>.md`, slug = output table
name. Human-curated; never touched by regeneration. Register a transform
only after the user has confirmed it exists in Data Studio.

Format:

```markdown
# <output_table_name>

registered: YYYY-MM-DD
metabase question: <url of the [transform] question>
refresh: <schedule, e.g. hourly / daily 02:00 IST>
grain: <one row per ...>

## Purpose

One or two sentences: what it precomputes and why live queries weren't enough.

## Columns

- `col` type — meaning

## Source SQL

​```sql
...
​```
```

Keep the SQL in sync with the transform in Data Studio — this file is what
future sessions query against, so drift here produces wrong answers.
