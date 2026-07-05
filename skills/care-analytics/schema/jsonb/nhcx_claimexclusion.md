# nhcx_claimexclusion JSONB schemas

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
   "spec": "nhcx.specs.insurance_plan.ClaimExclusionSpec"
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

## category

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
   "spec": "nhcx.specs.insurance_plan.ClaimExclusionSpec"
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

## statements

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[str] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "str",
     "type": "string"
    },
    "nullable": true,
    "raw": "list[str] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.ClaimExclusionSpec"
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

## items

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
   "spec": "nhcx.specs.insurance_plan.ClaimExclusionSpec"
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

## items_codes

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[str] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "str",
     "type": "string"
    },
    "nullable": true,
    "raw": "list[str] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/insurance_plan.py",
   "spec": "nhcx.specs.insurance_plan.ClaimExclusionSpec"
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
