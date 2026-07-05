# users_plugconfig (PlugConfig)

app: users | source: care/users/models.py
bases: models.Model (inherited columns: `_base_models.md`)

## Columns

- `slug` string(255) UNIQUE
- `meta` jsonb default=dict

JSONB shapes (`meta`): `jsonb/users_plugconfig.md`
