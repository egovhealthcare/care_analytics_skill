# emr_facilityorganization (FacilityOrganization)

app: emr | source: care/emr/models/organization.py
bases: OrganizationCommonBase (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]

JSONB shapes (`history`, `meta`, `metadata`, `cached_parent_json`): `jsonb/emr_facilityorganization.md`
