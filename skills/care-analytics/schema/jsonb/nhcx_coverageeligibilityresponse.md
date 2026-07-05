# nhcx_coverageeligibilityresponse JSONB schemas

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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityResponseRetrieveSpec"
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

## insurance

```json
{
 "candidate_schemas": [],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "inferred_schema": {
  "nullable": true,
  "type": "unknown"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "default_shape_only"
}
```

## error

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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityResponseRetrieveSpec"
  }
 ],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
