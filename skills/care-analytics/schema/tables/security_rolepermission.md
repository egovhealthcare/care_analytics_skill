# security_rolepermission (RolePermission)

app: security | source: care/security/models/role.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `role` foreign_key -> security_rolemodel [col: role_id]
- `permission` foreign_key -> security_permissionmodel [col: permission_id]
- `temp_deleted` boolean default=False
