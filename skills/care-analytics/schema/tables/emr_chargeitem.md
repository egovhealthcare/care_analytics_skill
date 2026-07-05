# emr_chargeitem (ChargeItem)

app: emr | source: care/emr/models/charge_item.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `title` string(255)
- `description` string NULL
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `charge_item_definition` foreign_key -> emr_chargeitemdefinition [col: charge_item_definition_id] NULL
- `account` foreign_key -> emr_account [col: account_id]
- `status` string(255)
- `code` jsonb NULL
- `quantity` decimal NULL
- `unit_price_components` jsonb NULL
- `total_price_components` jsonb NULL
- `total_price` decimal NULL
- `note` string NULL
- `override_reason` jsonb NULL
- `service_resource` string(255) NULL
- `service_resource_id` string(255) NULL
- `paid_invoice` foreign_key -> emr_invoice [col: paid_invoice_id] NULL
- `paid_on` datetime NULL
- `tags` array<integer> default=list
- `performer_actor` foreign_key -> users_user [col: performer_actor_id] NULL
- `discount_configuration` jsonb NULL

JSONB shapes (`history`, `meta`, `code`, `unit_price_components`, `total_price_components`, `override_reason`, `discount_configuration`): `jsonb/emr_chargeitem.md`
