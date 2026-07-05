# abdm_healthfacility (HealthFacility)

app: abdm | source: app/care_abdm/abdm/models/health_facility.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `hf_id` string(50) UNIQUE
- `registered` boolean default=False
- `facility` one_to_one -> facility_facility.external_id [col: facility_id]
