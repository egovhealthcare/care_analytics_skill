# emr_medicationstatement JSONB schemas

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
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.BaseMedicationStatementSpec"
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
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.MedicationStatementReadSpec"
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
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.MedicationStatementUpdateSpec"
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

## medication

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.BaseMedicationStatementSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.MedicationStatementReadSpec"
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

## effective_period

```json
{
 "candidate_schemas": [
  {
   "annotation": "PeriodSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "PeriodSpec | None",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.BaseMedicationStatementSpec"
  },
  {
   "annotation": "PeriodSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "PeriodSpec | None",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.MedicationStatementReadSpec"
  },
  {
   "annotation": "PeriodSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "PeriodSpec | None",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/statement/spec.py",
   "spec": "care.emr.resources.medication.statement.spec.MedicationStatementUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "datetime.datetime | None",
     "name": "start",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "datetime.datetime | None",
     "name": "end",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    }
   ],
   "name": "PeriodSpec",
   "source_file": "care/emr/resources/base.py",
   "spec": "care.emr.resources.base.PeriodSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
