# emr_deviceencounterhistory (DeviceEncounterHistory)

app: emr | source: care/emr/models/device.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `device` foreign_key -> emr_device [col: device_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `start` datetime
- `end` datetime NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_deviceencounterhistory.md`
