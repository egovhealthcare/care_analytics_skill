# emr_devicelocationhistory (DeviceLocationHistory)

app: emr | source: care/emr/models/device.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `device` foreign_key -> emr_device [col: device_id]
- `location` foreign_key -> emr_facilitylocation [col: location_id]
- `start` datetime
- `end` datetime NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_devicelocationhistory.md`
