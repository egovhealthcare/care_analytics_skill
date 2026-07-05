# emr_questionnaireresponsetemplate JSONB schemas

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
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateBaseSpec"
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
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateCreateSpec"
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
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateReadSpec"
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
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateRetrieveSpec"
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
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateUpdateSpec"
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

## template_data

```json
{
 "candidate_schemas": [
  {
   "annotation": "TemplateData",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "TemplateData",
    "ref": "TemplateData",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateBaseSpec"
  },
  {
   "annotation": "TemplateData",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "TemplateData",
    "ref": "TemplateData",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateCreateSpec"
  },
  {
   "annotation": "TemplateData",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "TemplateData",
    "ref": "TemplateData",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateReadSpec"
  },
  {
   "annotation": "TemplateData",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "TemplateData",
    "ref": "TemplateData",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateRetrieveSpec"
  },
  {
   "annotation": "TemplateData",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "TemplateData",
    "ref": "TemplateData",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireResponseTemplateUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "list[MedicationRequestTemplateSpec] | None",
     "name": "medication_request",
     "required": false,
     "schema": {
      "items": {
       "raw": "MedicationRequestTemplateSpec",
       "ref": "MedicationRequestTemplateSpec",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[MedicationRequestTemplateSpec] | None",
      "type": "array"
     }
    },
    {
     "annotation": "list[QuestionnaireAnswer] | None",
     "name": "questionnaire",
     "required": false,
     "schema": {
      "items": {
       "raw": "QuestionnaireAnswer",
       "ref": "QuestionnaireAnswer",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[QuestionnaireAnswer] | None",
      "type": "array"
     }
    },
    {
     "annotation": "list[ActivityDefinitionTemplateSpec] | None",
     "name": "activity_definition",
     "required": false,
     "schema": {
      "items": {
       "raw": "ActivityDefinitionTemplateSpec",
       "ref": "ActivityDefinitionTemplateSpec",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[ActivityDefinitionTemplateSpec] | None",
      "type": "array"
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
    }
   ],
   "name": "TemplateData",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.TemplateData"
  },
  {
   "fields": [
    {
     "annotation": "MedicationRequestStatus",
     "name": "status",
     "required": true,
     "schema": {
      "raw": "MedicationRequestStatus",
      "ref": "MedicationRequestStatus",
      "type": "ref"
     }
    },
    {
     "annotation": "StatusReason | None",
     "name": "status_reason",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "StatusReason | None",
      "ref": "StatusReason",
      "type": "ref"
     }
    },
    {
     "annotation": "MedicationRequestIntent",
     "name": "intent",
     "required": true,
     "schema": {
      "raw": "MedicationRequestIntent",
      "ref": "MedicationRequestIntent",
      "type": "ref"
     }
    },
    {
     "annotation": "MedicationRequestCategory",
     "name": "category",
     "required": true,
     "schema": {
      "raw": "MedicationRequestCategory",
      "ref": "MedicationRequestCategory",
      "type": "ref"
     }
    },
    {
     "annotation": "MedicationRequestPriority",
     "name": "priority",
     "required": true,
     "schema": {
      "raw": "MedicationRequestPriority",
      "ref": "MedicationRequestPriority",
      "type": "ref"
     }
    },
    {
     "annotation": "bool",
     "name": "do_not_perform",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
     "name": "medication",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_MEDICATION_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "list[DosageInstruction]",
     "name": "dosage_instruction",
     "required": true,
     "schema": {
      "items": {
       "raw": "DosageInstruction",
       "ref": "DosageInstruction",
       "type": "ref"
      },
      "raw": "list[DosageInstruction]",
      "type": "array"
     }
    },
    {
     "annotation": "datetime",
     "name": "authored_on",
     "required": true,
     "schema": {
      "raw": "datetime",
      "type": "datetime"
     }
    },
    {
     "annotation": "str | None",
     "name": "note",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "MedicationRequestDispenseStatus | None",
     "name": "dispense_status",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "MedicationRequestDispenseStatus | None",
      "ref": "MedicationRequestDispenseStatus",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "requested_product",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "MedicationRequestTemplateSpec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.MedicationRequestTemplateSpec"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "question_id",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "dict",
     "name": "answer",
     "required": true,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "dict",
     "name": "meta",
     "required": true,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    }
   ],
   "name": "QuestionnaireAnswer",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.QuestionnaireAnswer"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "slug",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "ServiceRequestUpdateSpec",
     "name": "service_request",
     "required": true,
     "schema": {
      "raw": "ServiceRequestUpdateSpec",
      "ref": "ServiceRequestUpdateSpec",
      "type": "ref"
     }
    }
   ],
   "name": "ActivityDefinitionTemplateSpec",
   "source_file": "care/emr/resources/questionnaire_response_template/spec.py",
   "spec": "care.emr.resources.questionnaire_response_template.spec.ActivityDefinitionTemplateSpec"
  },
  {
   "fields": [
    {
     "annotation": "int | None",
     "name": "sequence",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "int | None",
      "type": "integer"
     }
    },
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
     "annotation": "list[ValueSetBoundCoding[CARE_ADDITIONAL_INSTRUCTION_VALUESET.slug]] | None",
     "name": "additional_instruction",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetBoundCoding[CARE_ADDITIONAL_INSTRUCTION_VALUESET.slug]",
       "type": "valueset_coding"
      },
      "nullable": true,
      "raw": "list[ValueSetBoundCoding[CARE_ADDITIONAL_INSTRUCTION_VALUESET.slug]] | None",
      "type": "array"
     }
    },
    {
     "annotation": "str | None",
     "name": "patient_instruction",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "Timing | None",
     "name": "timing",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Timing | None",
      "ref": "Timing",
      "type": "ref"
     }
    },
    {
     "annotation": "bool",
     "name": "as_needed_boolean",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_AS_NEEDED_REASON_VALUESET.slug] | None",
     "name": "as_needed_for",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_AS_NEEDED_REASON_VALUESET.slug] | None",
      "type": "valueset_coding"
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
     "annotation": "DoseAndRate | None",
     "name": "dose_and_rate",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DoseAndRate | None",
      "ref": "DoseAndRate",
      "type": "ref"
     }
    },
    {
     "annotation": "DoseRange | None",
     "name": "max_dose_per_period",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DoseRange | None",
      "ref": "DoseRange",
      "type": "ref"
     }
    }
   ],
   "name": "DosageInstruction",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DosageInstruction"
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
     "annotation": "ServiceRequestStatusChoices | None",
     "name": "status",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ServiceRequestStatusChoices | None",
      "ref": "ServiceRequestStatusChoices",
      "type": "ref"
     }
    },
    {
     "annotation": "ServiceRequestIntentChoices | None",
     "name": "intent",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ServiceRequestIntentChoices | None",
      "ref": "ServiceRequestIntentChoices",
      "type": "ref"
     }
    },
    {
     "annotation": "ServiceRequestPriorityChoices | None",
     "name": "priority",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ServiceRequestPriorityChoices | None",
      "ref": "ServiceRequestPriorityChoices",
      "type": "ref"
     }
    },
    {
     "annotation": "ActivityDefinitionCategoryOptions | None",
     "name": "category",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ActivityDefinitionCategoryOptions | None",
      "ref": "ActivityDefinitionCategoryOptions",
      "type": "ref"
     }
    },
    {
     "annotation": "bool | None",
     "name": "do_not_perform",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "str | None",
     "name": "note",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
     "name": "body_site",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug] | None",
     "name": "code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[ACTIVITY_DEFINITION_PROCEDURE_CODE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "datetime.datetime | None",
     "name": "occurance",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "str | None",
     "name": "patient_instruction",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "healthcare_service",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "list[UUID4]",
     "name": "locations",
     "required": false,
     "schema": {
      "items": {
       "raw": "UUID4",
       "type": "uuid"
      },
      "raw": "list[UUID4]",
      "type": "array"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "requester",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    }
   ],
   "name": "ServiceRequestUpdateSpec",
   "source_file": "care/emr/resources/service_request/spec.py",
   "spec": "care.emr.resources.service_request.spec.ServiceRequestUpdateSpec"
  },
  {
   "fields": [
    {
     "annotation": "TimingRepeat",
     "name": "repeat",
     "required": true,
     "schema": {
      "raw": "TimingRepeat",
      "ref": "TimingRepeat",
      "type": "ref"
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
   "name": "Timing",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.Timing"
  },
  {
   "fields": [
    {
     "annotation": "DoseType",
     "name": "type",
     "required": true,
     "schema": {
      "raw": "DoseType",
      "ref": "DoseType",
      "type": "ref"
     }
    },
    {
     "annotation": "DoseRange | None",
     "name": "dose_range",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DoseRange | None",
      "ref": "DoseRange",
      "type": "ref"
     }
    },
    {
     "annotation": "DosageQuantity | None",
     "name": "dose_quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DosageQuantity | None",
      "ref": "DosageQuantity",
      "type": "ref"
     }
    }
   ],
   "name": "DoseAndRate",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DoseAndRate"
  },
  {
   "fields": [
    {
     "annotation": "DosageQuantity",
     "name": "low",
     "required": true,
     "schema": {
      "raw": "DosageQuantity",
      "ref": "DosageQuantity",
      "type": "ref"
     }
    },
    {
     "annotation": "DosageQuantity",
     "name": "high",
     "required": true,
     "schema": {
      "raw": "DosageQuantity",
      "ref": "DosageQuantity",
      "type": "ref"
     }
    }
   ],
   "name": "DoseRange",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DoseRange"
  },
  {
   "fields": [
    {
     "annotation": "int",
     "name": "frequency",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "Decimal",
     "name": "period",
     "required": false,
     "schema": {
      "raw": "Decimal",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingUnit",
     "name": "period_unit",
     "required": true,
     "schema": {
      "raw": "TimingUnit",
      "ref": "TimingUnit",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingQuantity | None",
     "name": "bounds_duration",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "TimingQuantity | None",
      "ref": "TimingQuantity",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingRange | None",
     "name": "bounds_range",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "TimingRange | None",
      "ref": "TimingRange",
      "type": "ref"
     }
    },
    {
     "annotation": "PeriodSpec | None",
     "name": "bounds_period",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PeriodSpec | None",
      "ref": "PeriodSpec",
      "type": "ref"
     }
    }
   ],
   "name": "TimingRepeat",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.TimingRepeat"
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
   "name": "DosageQuantity",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DosageQuantity"
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
     "annotation": "TimingUnit",
     "name": "unit",
     "required": true,
     "schema": {
      "raw": "TimingUnit",
      "ref": "TimingUnit",
      "type": "ref"
     }
    }
   ],
   "name": "TimingQuantity",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.TimingQuantity"
  },
  {
   "fields": [
    {
     "annotation": "TimingQuantity",
     "name": "low",
     "required": true,
     "schema": {
      "raw": "TimingQuantity",
      "ref": "TimingQuantity",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingQuantity",
     "name": "high",
     "required": true,
     "schema": {
      "raw": "TimingQuantity",
      "ref": "TimingQuantity",
      "type": "ref"
     }
    }
   ],
   "name": "TimingRange",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.TimingRange"
  },
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
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "ActivityDefinitionCategoryOptions",
  "Decimal",
  "DoseType",
  "MedicationRequestCategory",
  "MedicationRequestDispenseStatus",
  "MedicationRequestIntent",
  "MedicationRequestPriority",
  "MedicationRequestStatus",
  "ServiceRequestIntentChoices",
  "ServiceRequestPriorityChoices",
  "ServiceRequestStatusChoices",
  "StatusReason",
  "TimingUnit"
 ]
}
```
