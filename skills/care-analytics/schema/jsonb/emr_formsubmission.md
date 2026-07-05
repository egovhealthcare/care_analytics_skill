# emr_formsubmission JSONB schemas

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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.BaseFormSubmissionSpec"
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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.FormSubmissionReadSpec"
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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.FormSubmissionUpdateSpec"
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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.FormSubmissionWriteSpec"
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

## response_dump

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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.FormSubmissionReadSpec"
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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.FormSubmissionUpdateSpec"
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
   "source_file": "care/emr/resources/form_submission/spec.py",
   "spec": "care.emr.resources.form_submission.spec.FormSubmissionWriteSpec"
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
