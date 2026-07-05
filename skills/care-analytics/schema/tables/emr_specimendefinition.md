# emr_specimendefinition (SpecimenDefinition)

app: emr | source: care/emr/models/specimen_definition.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `version` integer default=1
- `slug` string(255)
- `title` string(1024)
- `derived_from_uri` string NULL
- `status` string(255)
- `description` string
- `type_collected` jsonb NULL
- `patient_preparation` jsonb default=list
- `collection` jsonb NULL
- `type_tested` jsonb default=dict

JSONB shapes (`history`, `meta`, `type_collected`, `patient_preparation`, `collection`, `type_tested`): `jsonb/emr_specimendefinition.md`
