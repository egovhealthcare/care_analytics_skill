# emr_tokencategory JSONB schemas

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
   "source_file": "care/emr/resources/scheduling/token_category/spec.py",
   "spec": "care.emr.resources.scheduling.token_category.spec.TokenCategoryBaseSpec"
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
   "source_file": "care/emr/resources/scheduling/token_category/spec.py",
   "spec": "care.emr.resources.scheduling.token_category.spec.TokenCategoryReadSpec"
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
   "source_file": "care/emr/resources/scheduling/token_category/spec.py",
   "spec": "care.emr.resources.scheduling.token_category.spec.TokenCategoryRetrieveSpec"
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

## metadata

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
   "source_file": "care/emr/resources/scheduling/token_category/spec.py",
   "spec": "care.emr.resources.scheduling.token_category.spec.TokenCategoryBaseSpec"
  },
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
   "source_file": "care/emr/resources/scheduling/token_category/spec.py",
   "spec": "care.emr.resources.scheduling.token_category.spec.TokenCategoryReadSpec"
  },
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
   "source_file": "care/emr/resources/scheduling/token_category/spec.py",
   "spec": "care.emr.resources.scheduling.token_category.spec.TokenCategoryRetrieveSpec"
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
