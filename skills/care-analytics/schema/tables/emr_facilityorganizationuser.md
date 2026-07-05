# emr_facilityorganizationuser (FacilityOrganizationUser)

app: emr | source: care/emr/models/organization.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `organization` foreign_key -> emr_facilityorganization [col: organization_id]
- `user` foreign_key -> users_user [col: user_id]
- `role` foreign_key -> security_rolemodel [col: role_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_facilityorganizationuser.md`
