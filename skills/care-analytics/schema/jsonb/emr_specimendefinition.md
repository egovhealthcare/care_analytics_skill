# emr_specimendefinition JSONB schemas

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
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.BaseSpecimenDefinitionSpec"
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
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionReadSpec"
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
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionWriteSpec"
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

## type_collected

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.BaseSpecimenDefinitionSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionWriteSpec"
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

## patient_preparation

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.BaseSpecimenDefinitionSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionReadSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[PREPARE_PATIENT_PRIOR_SPECIMEN_CODE_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionWriteSpec"
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

## collection

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_COLLECTION_CODE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[SPECIMEN_COLLECTION_CODE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.BaseSpecimenDefinitionSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_COLLECTION_CODE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[SPECIMEN_COLLECTION_CODE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_COLLECTION_CODE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[SPECIMEN_COLLECTION_CODE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionWriteSpec"
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

## type_tested

```json
{
 "candidate_schemas": [
  {
   "annotation": "TypeTestedSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TypeTestedSpec | None",
    "ref": "TypeTestedSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.BaseSpecimenDefinitionSpec"
  },
  {
   "annotation": "TypeTestedSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TypeTestedSpec | None",
    "ref": "TypeTestedSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionReadSpec"
  },
  {
   "annotation": "TypeTestedSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TypeTestedSpec | None",
    "ref": "TypeTestedSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.SpecimenDefinitionWriteSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "bool",
     "name": "is_derived",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "PreferenceOptions",
     "name": "preference",
     "required": true,
     "schema": {
      "raw": "PreferenceOptions",
      "ref": "PreferenceOptions",
      "type": "ref"
     }
    },
    {
     "annotation": "ContainerSpec | None",
     "name": "container",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ContainerSpec | None",
      "ref": "ContainerSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "requirement",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "DurationSpec | None",
     "name": "retention_time",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DurationSpec | None",
      "ref": "DurationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "bool | None",
     "name": "single_use",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "HandlingSpec | None",
     "name": "handling",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "HandlingSpec | None",
      "ref": "HandlingSpec",
      "type": "ref"
     }
    }
   ],
   "name": "TypeTestedSpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.TypeTestedSpec"
  },
  {
   "fields": [
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
     "annotation": "QuantitySpec | None",
     "name": "capacity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "QuantitySpec | None",
      "ref": "QuantitySpec",
      "type": "ref"
     }
    },
    {
     "annotation": "MinimumVolumeSpec | None",
     "name": "minimum_volume",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "MinimumVolumeSpec | None",
      "ref": "MinimumVolumeSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CONTAINER_CAP_VALUESET.slug] | None",
     "name": "cap",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CONTAINER_CAP_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "str | None",
     "name": "preparation",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ContainerSpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.ContainerSpec"
  },
  {
   "fields": [
    {
     "annotation": "Decimal",
     "name": "value",
     "required": false,
     "schema": {
      "raw": "Decimal",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Coding",
     "name": "unit",
     "required": true,
     "schema": {
      "raw": "Coding",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "DurationSpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.DurationSpec"
  },
  {
   "fields": [
    {
     "annotation": "HandlingConditionOptions | None",
     "name": "temperature_qualifier",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "HandlingConditionOptions | None",
      "ref": "HandlingConditionOptions",
      "type": "ref"
     }
    },
    {
     "annotation": "RangeSpec | None",
     "name": "temperature_range",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "RangeSpec | None",
      "ref": "RangeSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "DurationSpec | None",
     "name": "max_duration",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DurationSpec | None",
      "ref": "DurationSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "instruction",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "HandlingSpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.HandlingSpec"
  },
  {
   "fields": [
    {
     "annotation": "Decimal",
     "name": "value",
     "required": false,
     "schema": {
      "raw": "Decimal",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Coding",
     "name": "unit",
     "required": true,
     "schema": {
      "raw": "Coding",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "QuantitySpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.QuantitySpec"
  },
  {
   "fields": [
    {
     "annotation": "QuantitySpec | None",
     "name": "quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "QuantitySpec | None",
      "ref": "QuantitySpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "MinimumVolumeSpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.MinimumVolumeSpec"
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
  },
  {
   "fields": [
    {
     "annotation": "QuantitySpec | None",
     "name": "low",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "QuantitySpec | None",
      "ref": "QuantitySpec",
      "type": "ref"
     }
    },
    {
     "annotation": "QuantitySpec | None",
     "name": "high",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "QuantitySpec | None",
      "ref": "QuantitySpec",
      "type": "ref"
     }
    }
   ],
   "name": "RangeSpec",
   "source_file": "care/emr/resources/specimen_definition/spec.py",
   "spec": "care.emr.resources.specimen_definition.spec.RangeSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "Decimal",
  "HandlingConditionOptions",
  "PreferenceOptions"
 ]
}
```
