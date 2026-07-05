# encounter_identifiers_encounteridentifierallocation (EncounterIdentifierAllocation)

app: encounter_identifiers | source: app/care_state_hmis/encounter_identifiers/models/EncounterIdentifierAllocation.py
bases: models.Model (inherited columns: `_base_models.md`)

## Columns

- `encounter` one_to_one -> emr_encounter [col: encounter_id]
- `facility` foreign_key -> facility_facility [col: facility_id]
- `identifier` string(100)
- `bucket` string(16)
- `sequence` integer
- `pattern` string(128)
- `reset_period` string(16)
- `allocated_at` datetime idx

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['identifier'], name='unique_hmis_encounter_identifier'), models.UniqueConstraint(fields=['facility', 'bucket', 'sequence'], name='unique_hmis_encounter_identifier_seq')]"
}
```
