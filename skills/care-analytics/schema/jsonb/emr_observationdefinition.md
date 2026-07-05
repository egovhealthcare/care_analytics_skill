# emr_observationdefinition JSONB schemas

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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
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
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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

## permitted_unit

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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

## component

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ObservationDefinitionComponentSpec] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ObservationDefinitionComponentSpec",
     "ref": "ObservationDefinitionComponentSpec",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ObservationDefinitionComponentSpec] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
  },
  {
   "annotation": "list[ObservationDefinitionComponentSpec] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ObservationDefinitionComponentSpec",
     "ref": "ObservationDefinitionComponentSpec",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ObservationDefinitionComponentSpec] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
  },
  {
   "annotation": "list[ObservationDefinitionComponentSpec] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ObservationDefinitionComponentSpec",
     "ref": "ObservationDefinitionComponentSpec",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ObservationDefinitionComponentSpec] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
  },
  {
   "annotation": "list[ObservationDefinitionComponentSpec] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ObservationDefinitionComponentSpec",
     "ref": "ObservationDefinitionComponentSpec",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ObservationDefinitionComponentSpec] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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
     "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
     "name": "code",
     "required": true,
     "schema": {
      "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug]",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "QuestionType",
     "name": "permitted_data_type",
     "required": true,
     "schema": {
      "raw": "QuestionType",
      "ref": "QuestionType",
      "type": "ref"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
     "name": "permitted_unit",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "list[QualifiedRangeSpec]",
     "name": "qualified_ranges",
     "required": true,
     "schema": {
      "items": {
       "raw": "QualifiedRangeSpec",
       "ref": "QualifiedRangeSpec",
       "type": "ref"
      },
      "raw": "list[QualifiedRangeSpec]",
      "type": "array"
     }
    }
   ],
   "name": "ObservationDefinitionComponentSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionComponentSpec"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "title",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[EvaluatorConditionSpec]",
     "name": "conditions",
     "required": false,
     "schema": {
      "items": {
       "raw": "EvaluatorConditionSpec",
       "ref": "EvaluatorConditionSpec",
       "type": "ref"
      },
      "raw": "list[EvaluatorConditionSpec]",
      "type": "array"
     }
    },
    {
     "annotation": "list[NumericRangeSpec]",
     "name": "ranges",
     "required": false,
     "schema": {
      "items": {
       "raw": "NumericRangeSpec",
       "ref": "NumericRangeSpec",
       "type": "ref"
      },
      "raw": "list[NumericRangeSpec]",
      "type": "array"
     }
    },
    {
     "annotation": "InterpretationSpec | None",
     "name": "default_interpretation",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "InterpretationSpec | None",
      "ref": "InterpretationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "normal_coded_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "critical_coded_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "abnormal_coded_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[ValueSetInterpretationSpec]",
     "name": "valueset_interpretation",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetInterpretationSpec",
       "ref": "ValueSetInterpretationSpec",
       "type": "ref"
      },
      "raw": "list[ValueSetInterpretationSpec]",
      "type": "array"
     }
    }
   ],
   "name": "QualifiedRangeSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.QualifiedRangeSpec"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "metric",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "operation",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "dict | str",
     "name": "value",
     "required": true,
     "schema": {
      "any_of": [
       {
        "raw": "dict",
        "type": "object"
       },
       {
        "raw": "str",
        "type": "string"
       }
      ],
      "raw": "dict | str",
      "type": "union"
     }
    }
   ],
   "name": "EvaluatorConditionSpec",
   "source_file": "care/emr/resources/common/condition_evaluator.py",
   "spec": "care.emr.resources.common.condition_evaluator.EvaluatorConditionSpec"
  },
  {
   "fields": [
    {
     "annotation": "InterpretationSpec",
     "name": "interpretation",
     "required": true,
     "schema": {
      "raw": "InterpretationSpec",
      "ref": "InterpretationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "min",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "max",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    }
   ],
   "name": "NumericRangeSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.NumericRangeSpec"
  },
  {
   "fields": [
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
     "annotation": "str | None",
     "name": "icon",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "color",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "bool | None",
     "name": "highlight",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
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
   "name": "InterpretationSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.InterpretationSpec"
  },
  {
   "fields": [
    {
     "annotation": "InterpretationSpec",
     "name": "interpretation",
     "required": true,
     "schema": {
      "raw": "InterpretationSpec",
      "ref": "InterpretationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "valuset",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "ValueSetInterpretationSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ValueSetInterpretationSpec"
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
  "Decimal",
  "QuestionType"
 ]
}
```

## qualified_ranges

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[QualifiedRangeSpec]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "QualifiedRangeSpec",
     "ref": "QualifiedRangeSpec",
     "type": "ref"
    },
    "raw": "list[QualifiedRangeSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.BaseObservationDefinitionSpec"
  },
  {
   "annotation": "list[QualifiedRangeSpec]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "QualifiedRangeSpec",
     "ref": "QualifiedRangeSpec",
     "type": "ref"
    },
    "raw": "list[QualifiedRangeSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionCreateSpec"
  },
  {
   "annotation": "list[QualifiedRangeSpec]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "QualifiedRangeSpec",
     "ref": "QualifiedRangeSpec",
     "type": "ref"
    },
    "raw": "list[QualifiedRangeSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionReadSpec"
  },
  {
   "annotation": "list[QualifiedRangeSpec]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "QualifiedRangeSpec",
     "ref": "QualifiedRangeSpec",
     "type": "ref"
    },
    "raw": "list[QualifiedRangeSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ObservationDefinitionUpdateSpec"
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
     "name": "title",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[EvaluatorConditionSpec]",
     "name": "conditions",
     "required": false,
     "schema": {
      "items": {
       "raw": "EvaluatorConditionSpec",
       "ref": "EvaluatorConditionSpec",
       "type": "ref"
      },
      "raw": "list[EvaluatorConditionSpec]",
      "type": "array"
     }
    },
    {
     "annotation": "list[NumericRangeSpec]",
     "name": "ranges",
     "required": false,
     "schema": {
      "items": {
       "raw": "NumericRangeSpec",
       "ref": "NumericRangeSpec",
       "type": "ref"
      },
      "raw": "list[NumericRangeSpec]",
      "type": "array"
     }
    },
    {
     "annotation": "InterpretationSpec | None",
     "name": "default_interpretation",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "InterpretationSpec | None",
      "ref": "InterpretationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "normal_coded_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "critical_coded_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "abnormal_coded_value_set",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[ValueSetInterpretationSpec]",
     "name": "valueset_interpretation",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetInterpretationSpec",
       "ref": "ValueSetInterpretationSpec",
       "type": "ref"
      },
      "raw": "list[ValueSetInterpretationSpec]",
      "type": "array"
     }
    }
   ],
   "name": "QualifiedRangeSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.QualifiedRangeSpec"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "metric",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "operation",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "dict | str",
     "name": "value",
     "required": true,
     "schema": {
      "any_of": [
       {
        "raw": "dict",
        "type": "object"
       },
       {
        "raw": "str",
        "type": "string"
       }
      ],
      "raw": "dict | str",
      "type": "union"
     }
    }
   ],
   "name": "EvaluatorConditionSpec",
   "source_file": "care/emr/resources/common/condition_evaluator.py",
   "spec": "care.emr.resources.common.condition_evaluator.EvaluatorConditionSpec"
  },
  {
   "fields": [
    {
     "annotation": "InterpretationSpec",
     "name": "interpretation",
     "required": true,
     "schema": {
      "raw": "InterpretationSpec",
      "ref": "InterpretationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "min",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "max",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    }
   ],
   "name": "NumericRangeSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.NumericRangeSpec"
  },
  {
   "fields": [
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
     "annotation": "str | None",
     "name": "icon",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "color",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "bool | None",
     "name": "highlight",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
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
   "name": "InterpretationSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.InterpretationSpec"
  },
  {
   "fields": [
    {
     "annotation": "InterpretationSpec",
     "name": "interpretation",
     "required": true,
     "schema": {
      "raw": "InterpretationSpec",
      "ref": "InterpretationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "valuset",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "ValueSetInterpretationSpec",
   "source_file": "care/emr/resources/observation_definition/spec.py",
   "spec": "care.emr.resources.observation_definition.spec.ValueSetInterpretationSpec"
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
