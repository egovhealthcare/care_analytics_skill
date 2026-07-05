# emr_organization (Organization)

app: emr | source: care/emr/models/organization.py
bases: OrganizationCommonBase (inherited columns: `_base_models.md`)

## Columns

- `managing_organizations` array<integer> default=list

JSONB shapes (`history`, `meta`, `metadata`, `cached_parent_json`): `jsonb/emr_organization.md`
