# emr_metaartifact (MetaArtifact)

app: emr | source: care/emr/models/meta_artifact.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `associating_type` string(255)
- `associating_external_id` uuid
- `name` string(255)
- `object_type` string(255)
- `object_value` jsonb
- `note` string NULL

JSONB shapes (`history`, `meta`, `object_value`): `jsonb/emr_metaartifact.md`

## Model meta

```json
{
 "indexes": "[models.Index(fields=['associating_type', 'associating_external_id'])]"
}
```
