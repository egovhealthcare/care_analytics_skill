# emr_schedule (Schedule)

app: emr | source: care/emr/models/scheduling/schedule.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `resource` foreign_key -> emr_schedulableresource [col: resource_id]
- `name` string(255)
- `valid_from` datetime
- `valid_to` datetime
- `charge_item_definition` foreign_key -> emr_chargeitemdefinition [col: charge_item_definition_id] NULL
- `revisit_allowed_days` integer NULL
- `revisit_charge_item_definition` foreign_key -> emr_chargeitemdefinition [col: revisit_charge_item_definition_id] NULL
- `is_public` boolean default=False

JSONB shapes (`history`, `meta`): `jsonb/emr_schedule.md`
