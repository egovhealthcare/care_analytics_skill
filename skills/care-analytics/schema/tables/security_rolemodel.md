# security_rolemodel (RoleModel)

app: security | source: care/security/models/role.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(1024)
- `description` string
- `is_system` boolean default=False
- `temp_deleted` boolean default=False
- `is_archived` boolean default=False
- `contexts` array<string> default=list

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['name'], condition=models.Q(deleted=False), name='unique_name_if_not_deleted')]"
}
```
