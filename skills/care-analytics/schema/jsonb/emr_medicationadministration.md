# emr_medicationadministration JSONB schemas

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
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.BaseMedicationAdministrationSpec"
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
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationReadSpec"
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
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationSpec"
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
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationUpdateSpec"
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

## status_reason

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.BaseMedicationAdministrationSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationSpec"
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

## medication

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.BaseMedicationAdministrationSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationSpec"
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

## performer

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[MedicationAdministrationPerformer] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "MedicationAdministrationPerformer",
     "ref": "MedicationAdministrationPerformer",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[MedicationAdministrationPerformer] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.BaseMedicationAdministrationSpec"
  },
  {
   "annotation": "list[MedicationAdministrationPerformer] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "MedicationAdministrationPerformer",
     "ref": "MedicationAdministrationPerformer",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[MedicationAdministrationPerformer] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationReadSpec"
  },
  {
   "annotation": "list[MedicationAdministrationPerformer] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "MedicationAdministrationPerformer",
     "ref": "MedicationAdministrationPerformer",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[MedicationAdministrationPerformer] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "UUID4",
     "name": "actor",
     "required": false,
     "schema": {
      "raw": "UUID4",
      "type": "uuid"
     }
    },
    {
     "annotation": "MedicationAdministrationPerformerFunction | None",
     "name": "function",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "MedicationAdministrationPerformerFunction | None",
      "ref": "MedicationAdministrationPerformerFunction",
      "type": "ref"
     }
    }
   ],
   "name": "MedicationAdministrationPerformer",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationPerformer"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "MedicationAdministrationPerformerFunction"
 ]
}
```

## dosage

```json
{
 "candidate_schemas": [
  {
   "annotation": "Dosage | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Dosage | None",
    "ref": "Dosage",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.BaseMedicationAdministrationSpec"
  },
  {
   "annotation": "Dosage | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Dosage | None",
    "ref": "Dosage",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationReadSpec"
  },
  {
   "annotation": "Dosage | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Dosage | None",
    "ref": "Dosage",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.MedicationAdministrationSpec"
  }
 ],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "text",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
     "name": "site",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_ROUTE_VALUESET.slug] | None",
     "name": "route",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_ROUTE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_ADMINISTRATION_METHOD_VALUESET.slug] | None",
     "name": "method",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_ADMINISTRATION_METHOD_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "Quantity | None",
     "name": "dose",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Quantity | None",
      "ref": "Quantity",
      "type": "ref"
     }
    },
    {
     "annotation": "Quantity | None",
     "name": "rate",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Quantity | None",
      "ref": "Quantity",
      "type": "ref"
     }
    }
   ],
   "name": "Dosage",
   "source_file": "care/emr/resources/medication/administration/spec.py",
   "spec": "care.emr.resources.medication.administration.spec.Dosage"
  },
  {
   "fields": [
    {
     "annotation": "Decimal | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Coding | None",
     "name": "unit",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Coding | None",
      "ref": "Coding",
      "type": "ref"
     }
    },
    {
     "annotation": "dict | None",
     "name": "meta",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "Coding | None",
     "name": "code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Coding | None",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "Quantity",
   "source_file": "care/emr/resources/common/quantity.py",
   "spec": "care.emr.resources.common.quantity.Quantity"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "system",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "version",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "code",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "display",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "Coding",
   "source_file": "care/emr/resources/common/coding.py",
   "spec": "care.emr.resources.common.coding.Coding"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "Decimal"
 ]
}
```
