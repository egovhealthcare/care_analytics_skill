# nhcx_insuranceplanplan JSONB schemas

## history

```json
{
 "candidate_schemas": [],
 "default_shape": {
  "type": "object"
 },
 "inferred_schema": {
  "type": "object"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "default_shape_only"
}
```

## meta

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.InsurancePlanPlanSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## identifiers

```json
{
 "candidate_schemas": [
  {
   "annotation": "list | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "list | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.InsurancePlanPlanSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## type

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "dict | None",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.InsurancePlanPlanSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
