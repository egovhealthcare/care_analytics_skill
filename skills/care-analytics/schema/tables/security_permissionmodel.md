# security_permissionmodel (PermissionModel)

app: security | source: care/security/models/permission.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `slug` string(1024) UNIQUE
- `name` string(1024)
- `description` string
- `context` string(1024)
- `temp_deleted` boolean default=False
