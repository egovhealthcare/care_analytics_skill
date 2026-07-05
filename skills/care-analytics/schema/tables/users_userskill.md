# users_userskill (UserSkill)

app: users | source: care/users/models.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `user` foreign_key -> users_user [col: user_id] NULL
- `skill` foreign_key -> users_skill [col: skill_id] NULL

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['skill', 'user'], condition=models.Q(deleted=False), name='unique_user_skill')]"
}
```
