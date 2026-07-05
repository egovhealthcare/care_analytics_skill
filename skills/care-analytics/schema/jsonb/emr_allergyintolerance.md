# emr_allergyintolerance JSONB schemas

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
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceReadSpec"
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
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceUpdateSpec"
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
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceWriteSpec"
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
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.BaseAllergyIntoleranceSpec"
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
   "annotation": "Coding",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "Coding",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_ALLERGY_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_ALLERGY_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceWriteSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
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
 "status": "from_pydantic_spec"
}
```

## onset

```json
{
 "candidate_schemas": [
  {
   "annotation": "AllergyIntoleranceOnSetSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "AllergyIntoleranceOnSetSpec",
    "ref": "AllergyIntoleranceOnSetSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceReadSpec"
  },
  {
   "annotation": "AllergyIntoleranceOnSetSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "AllergyIntoleranceOnSetSpec",
    "ref": "AllergyIntoleranceOnSetSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceWriteSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "dict",
     "name": "meta",
     "required": false,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "datetime.datetime",
     "name": "onset_datetime",
     "required": false,
     "schema": {
      "raw": "datetime.datetime",
      "type": "datetime"
     }
    },
    {
     "annotation": "int",
     "name": "onset_age",
     "required": false,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "str",
     "name": "onset_string",
     "required": false,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "note",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "AllergyIntoleranceOnSetSpec",
   "source_file": "care/emr/resources/allergy_intolerance/spec.py",
   "spec": "care.emr.resources.allergy_intolerance.spec.AllergyIntoleranceOnSetSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
