# emr_facilitylocationorganization (FacilityLocationOrganization)

app: emr | source: care/emr/models/location.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `location` foreign_key -> emr_facilitylocation [col: location_id]
- `organization` foreign_key -> emr_facilityorganization [col: organization_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_facilitylocationorganization.md`
