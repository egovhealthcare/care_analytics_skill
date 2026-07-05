# security_roleassociation (RoleAssociation)

app: security | source: care/security/models/permission_association.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `user` foreign_key -> users_user [col: user_id]
- `context` string(1024)
- `context_id` integer
- `role` foreign_key -> security_rolemodel [col: role_id]
- `expiry` datetime NULL
