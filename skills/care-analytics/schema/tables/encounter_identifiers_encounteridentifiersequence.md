# encounter_identifiers_encounteridentifiersequence (EncounterIdentifierSequence)

app: encounter_identifiers | source: app/care_state_hmis/encounter_identifiers/models/EncounterIdentifierSequence.py
bases: models.Model (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `bucket` string(16)
- `last_value` integer default=0

## Model meta

```json
{
 "unique_together": [
  [
   "facility",
   "bucket"
  ]
 ]
}
```
