# encounter_identifiers_facilityencounteridentifierconfig (FacilityEncounterIdentifierConfig)

app: encounter_identifiers | source: app/care_state_hmis/encounter_identifiers/models/FacilityEncounterIdentifierConfig.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` one_to_one -> facility_facility [col: facility_id]
- `pattern` string(128)
- `facility_code` string(16)
- `enabled_encounter_classes` jsonb default=list
- `reset_period` string(16) choices=RESET_PERIOD_CHOICES default=yearly

JSONB shapes (`history`, `meta`, `enabled_encounter_classes`): `jsonb/encounter_identifiers_facilityencounteridentifierconfig.md`
