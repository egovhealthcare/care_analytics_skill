# emr_deviceservicehistory (DeviceServiceHistory)

app: emr | source: care/emr/models/device.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `device` foreign_key -> emr_device [col: device_id]
- `serviced_on` datetime NULL
- `note` string NULL
- `edit_history` jsonb default=list

JSONB shapes (`history`, `meta`, `edit_history`): `jsonb/emr_deviceservicehistory.md`
