# emr_patient JSONB schemas

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
   "source_file": "care/emr/resources/patient/otp_based_flow.py",
   "spec": "care.emr.resources.patient.otp_based_flow.PatientOTPBaseSpec"
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
   "source_file": "care/emr/resources/patient/otp_based_flow.py",
   "spec": "care.emr.resources.patient.otp_based_flow.PatientOTPReadSpec"
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
   "source_file": "care/emr/resources/patient/otp_based_flow.py",
   "spec": "care.emr.resources.patient.otp_based_flow.PatientOTPWriteSpec"
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
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientBaseSpec"
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
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientCreateSpec"
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
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientListSpec"
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
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientPartialSpec"
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
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientRetrieveSpec"
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
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "UUID4",
     "name": "config",
     "required": true,
     "schema": {
      "raw": "UUID4",
      "type": "uuid"
     }
    },
    {
     "annotation": "str",
     "name": "value",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "PatientIdentifierConfigRequest",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientIdentifierConfigRequest"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [
  {
   "annotation": "int | None",
   "name": "age",
   "schema": {
    "nullable": true,
    "raw": "int | None",
    "type": "integer"
   },
   "source_specs": [
    "care.emr.resources.patient.spec.PatientCreateSpec",
    "care.emr.resources.patient.spec.PatientUpdateSpec"
   ],
   "spec": "care.emr.resources.patient.spec.PatientCreateSpec"
  },
  {
   "annotation": "list[PatientIdentifierConfigRequest]",
   "name": "identifiers",
   "schema": {
    "items": {
     "raw": "PatientIdentifierConfigRequest",
     "ref": "PatientIdentifierConfigRequest",
     "type": "ref"
    },
    "raw": "list[PatientIdentifierConfigRequest]",
    "type": "array"
   },
   "source_specs": [
    "care.emr.resources.patient.spec.PatientCreateSpec",
    "care.emr.resources.patient.spec.PatientUpdateSpec"
   ],
   "spec": "care.emr.resources.patient.spec.PatientCreateSpec"
  },
  {
   "annotation": "list[UUID4]",
   "name": "tags",
   "schema": {
    "items": {
     "raw": "UUID4",
     "type": "uuid"
    },
    "raw": "list[UUID4]",
    "type": "array"
   },
   "source_specs": [
    "care.emr.resources.patient.spec.PatientCreateSpec"
   ],
   "spec": "care.emr.resources.patient.spec.PatientCreateSpec"
  }
 ],
 "status": "from_pydantic_spec"
}
```

## instance_identifiers

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[PatientIdentifierResponse]",
   "excluded_by_spec": true,
   "required": false,
   "schema": {
    "items": {
     "raw": "PatientIdentifierResponse",
     "ref": "PatientIdentifierResponse",
     "type": "ref"
    },
    "raw": "list[PatientIdentifierResponse]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientRetrieveSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "PatientIdentifierListSpec",
     "name": "config",
     "required": true,
     "schema": {
      "raw": "PatientIdentifierListSpec",
      "ref": "PatientIdentifierListSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "value",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "PatientIdentifierResponse",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientIdentifierResponse"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "PatientIdentifierListSpec"
 ]
}
```

## facility_identifiers

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[PatientIdentifierResponse]",
   "excluded_by_spec": true,
   "required": false,
   "schema": {
    "items": {
     "raw": "PatientIdentifierResponse",
     "ref": "PatientIdentifierResponse",
     "type": "ref"
    },
    "raw": "list[PatientIdentifierResponse]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientRetrieveSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "PatientIdentifierListSpec",
     "name": "config",
     "required": true,
     "schema": {
      "raw": "PatientIdentifierListSpec",
      "ref": "PatientIdentifierListSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "value",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "PatientIdentifierResponse",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientIdentifierResponse"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "PatientIdentifierListSpec"
 ]
}
```

## facility_tags

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[dict]",
   "excluded_by_spec": true,
   "required": false,
   "schema": {
    "items": {
     "raw": "dict",
     "type": "object"
    },
    "raw": "list[dict]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientListSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": true,
   "required": false,
   "schema": {
    "items": {
     "raw": "dict",
     "type": "object"
    },
    "raw": "list[dict]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientRetrieveSpec"
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

## extensions

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient/otp_based_flow.py",
   "spec": "care.emr.resources.patient.otp_based_flow.PatientOTPReadSpec"
  },
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient/spec.py",
   "spec": "care.emr.resources.patient.spec.PatientRetrieveSpec"
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
