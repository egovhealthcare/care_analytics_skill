# nhcx_insuranceplanbenefit JSONB schemas

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
   "spec": "nhcx.specs.insurance_plan.InsurancePlanBenefitDetailSpec"
  },
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
   "spec": "nhcx.specs.insurance_plan.InsurancePlanBenefitListSpec"
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

## coverage_benefit_fhir_ids

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[str]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "str",
     "type": "string"
    },
    "raw": "list[str]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.InsurancePlanBenefitDetailSpec"
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

## questionnaire_fhir_ids

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[str]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "str",
     "type": "string"
    },
    "raw": "list[str]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.InsurancePlanBenefitDetailSpec"
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
