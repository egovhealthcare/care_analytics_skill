# emr_userresourcefavorites (UserResourceFavorites)

app: emr | source: care/emr/models/favorites.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `user` foreign_key -> users_user [col: user_id] NULL
- `favorites` array<integer> default=list
- `favorite_list` string(255)
- `resource_type` string(255)
- `facility` foreign_key -> facility_facility [col: facility_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_userresourcefavorites.md`
