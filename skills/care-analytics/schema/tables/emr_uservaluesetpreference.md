# emr_uservaluesetpreference (UserValueSetPreference)

app: emr | source: care/emr/models/valueset.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `user` foreign_key -> users_user [col: user_id]
- `valueset` foreign_key -> emr_valueset [col: valueset_id]
- `favorite_codes` jsonb default=list

JSONB shapes (`history`, `meta`, `favorite_codes`): `jsonb/emr_uservaluesetpreference.md`

## Model meta

```json
{
 "unique_together": [
  "user",
  "valueset"
 ]
}
```
