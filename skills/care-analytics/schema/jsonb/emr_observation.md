# emr_observation JSONB schemas

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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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

## category

```json
{
 "candidate_schemas": [
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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

## main_code

```json
{
 "candidate_schemas": [
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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

## alternate_coding

```json
{
 "candidate_schemas": [
  {
   "annotation": "CodeableConcept | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CodeableConcept | None",
    "ref": "CodeableConcept",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "CodeableConcept | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CodeableConcept | None",
    "ref": "CodeableConcept",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "CodeableConcept | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CodeableConcept | None",
    "ref": "CodeableConcept",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "CodeableConcept | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CodeableConcept | None",
    "ref": "CodeableConcept",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "CodeableConcept | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CodeableConcept | None",
    "ref": "CodeableConcept",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "id",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[Coding] | None",
     "name": "coding",
     "required": false,
     "schema": {
      "items": {
       "raw": "Coding",
       "ref": "Coding",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[Coding] | None",
      "type": "array"
     }
    },
    {
     "annotation": "str | None",
     "name": "text",
     "required": true,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "CodeableConcept",
   "source_file": "care/emr/resources/common/codable_concept.py",
   "spec": "care.emr.resources.common.codable_concept.CodeableConcept"
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
 "status": "from_pydantic_spec"
}
```

## performer

```json
{
 "candidate_schemas": [
  {
   "annotation": "Performer | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Performer | None",
    "ref": "Performer",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "Performer | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Performer | None",
    "ref": "Performer",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "Performer | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Performer | None",
    "ref": "Performer",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "Performer | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Performer | None",
    "ref": "Performer",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "Performer | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Performer | None",
    "ref": "Performer",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "PerformerType",
     "name": "type",
     "required": true,
     "schema": {
      "raw": "PerformerType",
      "ref": "PerformerType",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "id",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "Performer",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.Performer"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "PerformerType"
 ]
}
```

## value

```json
{
 "candidate_schemas": [
  {
   "annotation": "QuestionnaireSubmitResultValue",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "QuestionnaireSubmitResultValue",
    "ref": "QuestionnaireSubmitResultValue",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "QuestionnaireSubmitResultValue",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "QuestionnaireSubmitResultValue",
    "ref": "QuestionnaireSubmitResultValue",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "QuestionnaireSubmitResultValue",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "QuestionnaireSubmitResultValue",
    "ref": "QuestionnaireSubmitResultValue",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "QuestionnaireSubmitResultValue",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "QuestionnaireSubmitResultValue",
    "ref": "QuestionnaireSubmitResultValue",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "QuestionnaireSubmitResultValue | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "QuestionnaireSubmitResultValue | None",
    "ref": "QuestionnaireSubmitResultValue",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
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
     "annotation": "Coding | None",
     "name": "coding",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Coding | None",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "QuestionnaireSubmitResultValue",
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.QuestionnaireSubmitResultValue"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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

## method

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_COLLECTION_METHOD.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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

## reference_range

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ReferenceRange]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ReferenceRange",
     "ref": "ReferenceRange",
     "type": "ref"
    },
    "raw": "list[ReferenceRange]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "list[ReferenceRange]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ReferenceRange",
     "ref": "ReferenceRange",
     "type": "ref"
    },
    "raw": "list[ReferenceRange]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "list[ReferenceRange]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ReferenceRange",
     "ref": "ReferenceRange",
     "type": "ref"
    },
    "raw": "list[ReferenceRange]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "list[ReferenceRange]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ReferenceRange",
     "ref": "ReferenceRange",
     "type": "ref"
    },
    "raw": "list[ReferenceRange]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "list[ReferenceRange]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ReferenceRange",
     "ref": "ReferenceRange",
     "type": "ref"
    },
    "raw": "list[ReferenceRange]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "float | None",
     "name": "min",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "float | None",
     "name": "max",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "str | None",
     "name": "unit",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "interpretation",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ReferenceRange",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ReferenceRange"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## interpretation

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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
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
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
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

## component

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[Component]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "Component",
     "ref": "Component",
     "type": "ref"
    },
    "raw": "list[Component]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.BaseObservationSpec"
  },
  {
   "annotation": "list[Component]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "Component",
     "ref": "Component",
     "type": "ref"
    },
    "raw": "list[Component]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationReadSpec"
  },
  {
   "annotation": "list[Component]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "Component",
     "ref": "Component",
     "type": "ref"
    },
    "raw": "list[Component]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationRetrieveSpec"
  },
  {
   "annotation": "list[Component]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "Component",
     "ref": "Component",
     "type": "ref"
    },
    "raw": "list[Component]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationSpec"
  },
  {
   "annotation": "list[Component]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "Component",
     "ref": "Component",
     "type": "ref"
    },
    "raw": "list[Component]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ObservationUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "QuestionnaireSubmitResultValue",
     "name": "value",
     "required": true,
     "schema": {
      "raw": "QuestionnaireSubmitResultValue",
      "ref": "QuestionnaireSubmitResultValue",
      "type": "ref"
     }
    },
    {
     "annotation": "str | dict",
     "name": "interpretation",
     "required": false,
     "schema": {
      "any_of": [
       {
        "raw": "str",
        "type": "string"
       },
       {
        "raw": "dict",
        "type": "object"
       }
      ],
      "raw": "str | dict",
      "type": "union"
     }
    },
    {
     "annotation": "list[ReferenceRange]",
     "name": "reference_range",
     "required": false,
     "schema": {
      "items": {
       "raw": "ReferenceRange",
       "ref": "ReferenceRange",
       "type": "ref"
      },
      "raw": "list[ReferenceRange]",
      "type": "array"
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
    },
    {
     "annotation": "str",
     "name": "note",
     "required": false,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "Component",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.Component"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
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
     "annotation": "Coding | None",
     "name": "coding",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Coding | None",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "QuestionnaireSubmitResultValue",
   "source_file": "care/emr/resources/questionnaire_response/spec.py",
   "spec": "care.emr.resources.questionnaire_response.spec.QuestionnaireSubmitResultValue"
  },
  {
   "fields": [
    {
     "annotation": "float | None",
     "name": "min",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "float | None",
     "name": "max",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "str | None",
     "name": "unit",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "interpretation",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ReferenceRange",
   "source_file": "care/emr/resources/observation/spec.py",
   "spec": "care.emr.resources.observation.spec.ReferenceRange"
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
 "status": "from_pydantic_spec"
}
```
