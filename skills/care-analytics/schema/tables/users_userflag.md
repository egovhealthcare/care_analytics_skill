# users_userflag (UserFlag)

app: users | source: care/users/models.py
bases: BaseFlag (inherited columns: `_base_models.md`)

## Columns

- `user` foreign_key -> users_user [col: user_id]

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['user', 'flag'], condition=models.Q(deleted=False), name='unique_user_flag')]",
 "verbose_name": "User Flag"
}
```
