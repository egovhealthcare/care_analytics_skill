# emr_questionnaire JSONB schemas

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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.AnswerOption"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.EnableWhen"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.Performer"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.Question"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireBaseSpec"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireReadSpec"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireSpec"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireWriteSpec"
  },
  {
   "annotation": "dict | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "dict | None",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.TemplateConfig"
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

## styling_metadata

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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.Question"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireReadSpec"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireSpec"
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
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireWriteSpec"
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

## questions

```json
{
 "candidate_schemas": [
  {
   "annotation": "list['Question']",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "'Question'",
     "type": "unknown"
    },
    "raw": "list['Question']",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.Question"
  },
  {
   "annotation": "list",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "list",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireReadSpec"
  },
  {
   "annotation": "list[Question]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "Question",
     "ref": "Question",
     "type": "ref"
    },
    "raw": "list[Question]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireSpec"
  },
  {
   "annotation": "list[Question]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "Question",
     "ref": "Question",
     "type": "ref"
    },
    "raw": "list[Question]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.QuestionnaireWriteSpec"
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
     "annotation": "str",
     "name": "link_id",
     "required": false,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "UUID4 | UUID5",
     "name": "id",
     "required": false,
     "schema": {
      "any_of": [
       {
        "raw": "UUID4",
        "type": "uuid"
       },
       {
        "raw": "UUID5",
        "ref": "UUID5",
        "type": "ref"
       }
      ],
      "raw": "UUID4 | UUID5",
      "type": "union"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
     "name": "code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "bool",
     "name": "collect_time",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool",
     "name": "collect_performer",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "str",
     "name": "text",
     "required": false,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "description",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "QuestionType",
     "name": "type",
     "required": true,
     "schema": {
      "raw": "QuestionType",
      "ref": "QuestionType",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "structured_type",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[EnableWhen] | None",
     "name": "enable_when",
     "required": false,
     "schema": {
      "items": {
       "raw": "EnableWhen",
       "ref": "EnableWhen",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[EnableWhen] | None",
      "type": "array"
     }
    },
    {
     "annotation": "EnableBehavior | None",
     "name": "enable_behavior",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "EnableBehavior | None",
      "ref": "EnableBehavior",
      "type": "ref"
     }
    },
    {
     "annotation": "DisabledDisplay | None",
     "name": "disabled_display",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DisabledDisplay | None",
      "ref": "DisabledDisplay",
      "type": "ref"
     }
    },
    {
     "annotation": "bool | None",
     "name": "collect_body_site",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool | None",
     "name": "collect_method",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool | None",
     "name": "required",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool | None",
     "name": "repeats",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "bool | None",
     "name": "read_only",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "int | None",
     "name": "max_length",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "int | None",
      "type": "integer"
     }
    },
    {
     "annotation": "AnswerConstraint | None",
     "name": "answer_constraint",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "AnswerConstraint | None",
      "ref": "AnswerConstraint",
      "type": "ref"
     }
    },
    {
     "annotation": "list[AnswerOption] | None",
     "name": "answer_option",
     "required": false,
     "schema": {
      "items": {
       "raw": "AnswerOption",
       "ref": "AnswerOption",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[AnswerOption] | None",
      "type": "array"
     }
    },
    {
     "annotation": "str | None",
     "name": "answer_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "bool | None",
     "name": "is_observation",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
     "name": "unit",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "list['Question']",
     "name": "questions",
     "required": false,
     "schema": {
      "items": {
       "raw": "'Question'",
       "type": "unknown"
      },
      "raw": "list['Question']",
      "type": "array"
     }
    },
    {
     "annotation": "str | None",
     "name": "formula",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "dict",
     "name": "styling_metadata",
     "required": false,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "list[TemplateConfig]",
     "name": "templates",
     "required": false,
     "schema": {
      "items": {
       "raw": "TemplateConfig",
       "ref": "TemplateConfig",
       "type": "ref"
      },
      "raw": "list[TemplateConfig]",
      "type": "array"
     }
    },
    {
     "annotation": "bool",
     "name": "is_component",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    }
   ],
   "name": "Question",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.Question"
  },
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
     "annotation": "str",
     "name": "question",
     "required": false,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "EnableOperator",
     "name": "operator",
     "required": true,
     "schema": {
      "raw": "EnableOperator",
      "ref": "EnableOperator",
      "type": "ref"
     }
    },
    {
     "annotation": "Any",
     "name": "answer",
     "required": false,
     "schema": {
      "raw": "Any",
      "type": "any"
     }
    }
   ],
   "name": "EnableWhen",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.EnableWhen"
  },
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
     "annotation": "Any",
     "name": "value",
     "required": false,
     "schema": {
      "raw": "Any",
      "type": "any"
     }
    },
    {
     "annotation": "bool",
     "name": "initial_selected",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    }
   ],
   "name": "AnswerOption",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.AnswerOption"
  },
  {
   "fields": [
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
     "annotation": "str",
     "name": "name",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "content",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "dict | None",
     "name": "structured_content",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    }
   ],
   "name": "TemplateConfig",
   "source_file": "care/emr/resources/questionnaire/spec.py",
   "spec": "care.emr.resources.questionnaire.spec.TemplateConfig"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "AnswerConstraint",
  "DisabledDisplay",
  "EnableBehavior",
  "EnableOperator",
  "QuestionType",
  "UUID5"
 ]
}
```
