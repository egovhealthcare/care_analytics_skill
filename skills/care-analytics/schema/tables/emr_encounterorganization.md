# emr_encounterorganization (EncounterOrganization)

app: emr | source: care/emr/models/encounter.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `organization` foreign_key -> emr_facilityorganization [col: organization_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_encounterorganization.md`
