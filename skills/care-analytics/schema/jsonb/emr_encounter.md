# emr_encounter JSONB schemas

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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterCreateSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterListSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterSpecBase"
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

## status_history

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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterListSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
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

## encounter_class_history

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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterListSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
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

## period

```json
{
 "candidate_schemas": [
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterCreateSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterListSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterSpecBase"
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

## hospitalization

```json
{
 "candidate_schemas": [
  {
   "annotation": "HospitalizationSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "HospitalizationSpec | None",
    "ref": "HospitalizationSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterCreateSpec"
  },
  {
   "annotation": "HospitalizationSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "HospitalizationSpec | None",
    "ref": "HospitalizationSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterListSpec"
  },
  {
   "annotation": "HospitalizationSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "HospitalizationSpec | None",
    "ref": "HospitalizationSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
  },
  {
   "annotation": "HospitalizationSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "HospitalizationSpec | None",
    "ref": "HospitalizationSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterSpecBase"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "bool | None",
     "name": "re_admission",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "AdmitSourcesChoices | None",
     "name": "admit_source",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "AdmitSourcesChoices | None",
      "ref": "AdmitSourcesChoices",
      "type": "ref"
     }
    },
    {
     "annotation": "DischargeDispositionChoices | None",
     "name": "discharge_disposition",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DischargeDispositionChoices | None",
      "ref": "DischargeDispositionChoices",
      "type": "ref"
     }
    },
    {
     "annotation": "DietPreferenceChoices | None",
     "name": "diet_preference",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DietPreferenceChoices | None",
      "ref": "DietPreferenceChoices",
      "type": "ref"
     }
    }
   ],
   "name": "HospitalizationSpec",
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.HospitalizationSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "AdmitSourcesChoices",
  "DietPreferenceChoices",
  "DischargeDispositionChoices"
 ]
}
```

## care_team

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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterListSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
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
   "source_file": "care/emr/resources/encounter/spec.py",
   "spec": "care.emr.resources.encounter.spec.EncounterRetrieveSpec"
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
