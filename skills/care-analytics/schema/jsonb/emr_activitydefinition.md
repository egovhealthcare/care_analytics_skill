# emr_activitydefinition JSONB schemas

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
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionReadSpec"
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
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionRetrieveSpec"
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
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionWriteSpec"
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
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.BaseActivityDefinitionSpec"
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

## code

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionWriteSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.BaseActivityDefinitionSpec"
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

## body_site

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionWriteSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.BaseActivityDefinitionSpec"
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

## diagnostic_report_codes

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionReadSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionRetrieveSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.ActivityDefinitionWriteSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/activity_definition/spec.py",
   "spec": "care.emr.resources.activity_definition.spec.BaseActivityDefinitionSpec"
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
