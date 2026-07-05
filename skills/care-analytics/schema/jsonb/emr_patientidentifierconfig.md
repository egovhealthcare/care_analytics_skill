# emr_patientidentifierconfig JSONB schemas

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
   "source_file": "care/emr/resources/patient_identifier/spec.py",
   "spec": "care.emr.resources.patient_identifier.spec.BasePatientIdentifierSpec"
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
   "source_file": "care/emr/resources/patient_identifier/spec.py",
   "spec": "care.emr.resources.patient_identifier.spec.PatientIdentifierCreateSpec"
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

## config

```json
{
 "candidate_schemas": [
  {
   "annotation": "IdentifierConfig",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "IdentifierConfig",
    "ref": "IdentifierConfig",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient_identifier/spec.py",
   "spec": "care.emr.resources.patient_identifier.spec.BasePatientIdentifierSpec"
  },
  {
   "annotation": "IdentifierConfig",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "IdentifierConfig",
    "ref": "IdentifierConfig",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/patient_identifier/spec.py",
   "spec": "care.emr.resources.patient_identifier.spec.PatientIdentifierCreateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "PatientIdentifierUse",
     "name": "use",
     "required": true,
     "schema": {
      "raw": "PatientIdentifierUse",
      "ref": "PatientIdentifierUse",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "description",
     "required": false,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "system",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "bool",
     "name": "required",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool",
     "name": "unique",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "str",
     "name": "regex",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "display",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "PatientIdentifierRetrieveConfig",
     "name": "retrieve_config",
     "required": false,
     "schema": {
      "raw": "PatientIdentifierRetrieveConfig",
      "ref": "PatientIdentifierRetrieveConfig",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "default_value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "bool",
     "name": "auto_maintained",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    }
   ],
   "name": "IdentifierConfig",
   "source_file": "care/emr/resources/patient_identifier/spec.py",
   "spec": "care.emr.resources.patient_identifier.spec.IdentifierConfig"
  },
  {
   "fields": [
    {
     "annotation": "bool",
     "name": "retrieve_with_dob",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool",
     "name": "retrieve_with_year_of_birth",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool",
     "name": "retrieve_with_otp",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool",
     "name": "retrieve_partial_search",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    }
   ],
   "name": "PatientIdentifierRetrieveConfig",
   "source_file": "care/emr/resources/patient_identifier/spec.py",
   "spec": "care.emr.resources.patient_identifier.spec.PatientIdentifierRetrieveConfig"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "PatientIdentifierUse"
 ]
}
```
