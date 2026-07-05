# facility_facilityflag (FacilityFlag)

app: facility | source: care/facility/models/facility_flag.py
bases: BaseFlag (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['facility', 'flag'], condition=models.Q(deleted=False), name='unique_facility_flag')]",
 "verbose_name": "Facility Flag"
}
```
