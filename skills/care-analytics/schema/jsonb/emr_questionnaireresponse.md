# emr_questionnaireresponse JSONB schemas

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
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.EMRQuestionnaireResponseBase"
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
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.QuestionnaireResponseReadSpec"
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
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.QuestionnaireResponseUpdate"
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

## responses

```json
{
 "candidate_schemas": [
  {
   "annotation": "list",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "list",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.QuestionnaireResponseReadSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## structured_responses

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
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.QuestionnaireResponseReadSpec"
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
