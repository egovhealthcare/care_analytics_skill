# emr_facilitylocationencounter (FacilityLocationEncounter)

app: emr | source: care/emr/models/location.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(25)
- `location` foreign_key -> emr_facilitylocation [col: location_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `start_datetime` datetime
- `end_datetime` datetime NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_facilitylocationencounter.md`
