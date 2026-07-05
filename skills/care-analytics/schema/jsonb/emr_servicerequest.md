# emr_servicerequest JSONB schemas

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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.BaseServiceRequestSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestCreateSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestReadSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestRetrieveSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestUpdateSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestWriteSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.BaseServiceRequestSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestCreateSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestReadSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestUpdateSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestWriteSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.BaseServiceRequestSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestCreateSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestReadSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestRetrieveSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestUpdateSpec"
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
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestWriteSpec"
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
