# nhcx_claim JSONB schemas

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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimBaseSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [
  {
   "annotation": "str | None",
   "name": "claim_flow_id",
   "schema": {
    "nullable": true,
    "raw": "str | None",
    "type": "string"
   },
   "source_specs": [
    "nhcx.specs.claim.ClaimBaseSpec",
    "nhcx.specs.claim.ClaimCreateSpec",
    "nhcx.specs.claim.ClaimListSpec"
   ],
   "spec": "nhcx.specs.claim.ClaimBaseSpec"
  },
  {
   "annotation": "UUID4",
   "name": "facility",
   "schema": {
    "raw": "UUID4",
    "type": "uuid"
   },
   "source_specs": [
    "nhcx.specs.claim.ClaimCreateSpec"
   ],
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "dict | None",
   "name": "latest_response",
   "schema": {
    "nullable": true,
    "raw": "dict | None",
    "type": "object"
   },
   "source_specs": [
    "nhcx.specs.claim.ClaimListSpec"
   ],
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "status": "from_pydantic_spec"
}
```

## type

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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
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

## insurer

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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
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

## billable_period

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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
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

## related

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimRelatedSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimRelatedSpec",
     "ref": "ClaimRelatedSpec",
     "type": "ref"
    },
    "raw": "list[ClaimRelatedSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "UUID4",
     "name": "claim",
     "required": true,
     "schema": {
      "raw": "UUID4",
      "type": "uuid"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[NHCX_CLAIM_RELATED_RELATIONSHIP_VALUESET.slug] | None",
     "name": "relationship",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[NHCX_CLAIM_RELATED_RELATIONSHIP_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "str | None",
     "name": "reference",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ClaimRelatedSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimRelatedSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## care_team

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimCareTeamSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimCareTeamSpec",
     "ref": "ClaimCareTeamSpec",
     "type": "ref"
    },
    "raw": "list[ClaimCareTeamSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "UUID4",
     "name": "provider",
     "required": true,
     "schema": {
      "raw": "UUID4",
      "type": "uuid"
     }
    },
    {
     "annotation": "bool | None",
     "name": "responsible",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[NHCX_CLAIM_CARE_TEAM_ROLE_VALUESET.slug] | None",
     "name": "role",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[NHCX_CLAIM_CARE_TEAM_ROLE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    }
   ],
   "name": "ClaimCareTeamSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCareTeamSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## supporting_info

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimSupportingInfoSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimSupportingInfoSpec",
     "ref": "ClaimSupportingInfoSpec",
     "type": "ref"
    },
    "raw": "list[ClaimSupportingInfoSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "dict",
     "name": "category",
     "required": true,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "dict",
     "name": "code",
     "required": true,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "PeriodSpec | None",
     "name": "timing",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PeriodSpec | None",
      "ref": "PeriodSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "value_attachment",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    }
   ],
   "name": "ClaimSupportingInfoSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimSupportingInfoSpec"
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
 "status": "from_pydantic_spec"
}
```

## procedure

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimProcedureSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimProcedureSpec",
     "ref": "ClaimProcedureSpec",
     "type": "ref"
    },
    "raw": "list[ClaimProcedureSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "list[ValueSetBoundCoding[NHCX_CLAIM_PROCEDURE_TYPE_VALUESET.slug]]",
     "name": "type",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetBoundCoding[NHCX_CLAIM_PROCEDURE_TYPE_VALUESET.slug]",
       "type": "valueset_coding"
      },
      "raw": "list[ValueSetBoundCoding[NHCX_CLAIM_PROCEDURE_TYPE_VALUESET.slug]]",
      "type": "array"
     }
    },
    {
     "annotation": "datetime | None",
     "name": "date",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "procedure_reference",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[NHCX_CLAIM_PROCEDURE_CODE_VALUESET.slug] | None",
     "name": "procedure_code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[NHCX_CLAIM_PROCEDURE_CODE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    }
   ],
   "name": "ClaimProcedureSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimProcedureSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## diagnosis

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimDiagnosisSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimDiagnosisSpec",
     "ref": "ClaimDiagnosisSpec",
     "type": "ref"
    },
    "raw": "list[ClaimDiagnosisSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "list[ValueSetBoundCoding[NHCX_CLAIM_DIAGNOSIS_TYPE_VALUESET.slug]]",
     "name": "type",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetBoundCoding[NHCX_CLAIM_DIAGNOSIS_TYPE_VALUESET.slug]",
       "type": "valueset_coding"
      },
      "raw": "list[ValueSetBoundCoding[NHCX_CLAIM_DIAGNOSIS_TYPE_VALUESET.slug]]",
      "type": "array"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "diagnosis_reference",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[NHCX_CLAIM_DIAGNOSIS_CODE_VALUESET.slug] | None",
     "name": "diagnosis_code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[NHCX_CLAIM_DIAGNOSIS_CODE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ClaimDiagnosisOnAdmissionChoices | None",
     "name": "on_admission",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ClaimDiagnosisOnAdmissionChoices | None",
      "ref": "ClaimDiagnosisOnAdmissionChoices",
      "type": "ref"
     }
    }
   ],
   "name": "ClaimDiagnosisSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimDiagnosisSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "ClaimDiagnosisOnAdmissionChoices"
 ]
}
```

## insurance

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimInsuranceSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimInsuranceSpec",
     "ref": "ClaimInsuranceSpec",
     "type": "ref"
    },
    "raw": "list[ClaimInsuranceSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "bool",
     "name": "focal",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "Policy",
     "name": "policy",
     "required": true,
     "schema": {
      "raw": "Policy",
      "ref": "Policy",
      "type": "ref"
     }
    }
   ],
   "name": "ClaimInsuranceSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimInsuranceSpec"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "sno",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "abhanumber",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "mobilenumber",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "memberid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "payerid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "productid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "productname",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "processingid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "PolicyPeriod | None",
     "name": "policy_period",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PolicyPeriod | None",
      "ref": "PolicyPeriod",
      "type": "ref"
     }
    }
   ],
   "name": "Policy",
   "source_file": "app/care_nhcx/nhcx/services/types/participant.py",
   "spec": "nhcx.services.types.participant.Policy"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "start",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "end",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "PolicyPeriod",
   "source_file": "app/care_nhcx/nhcx/services/types/participant.py",
   "spec": "nhcx.services.types.participant.PolicyPeriod"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## item

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimItemSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimItemSpec",
     "ref": "ClaimItemSpec",
     "type": "ref"
    },
    "raw": "list[ClaimItemSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "list[int]",
     "name": "care_team_sequence",
     "required": false,
     "schema": {
      "items": {
       "raw": "int",
       "type": "integer"
      },
      "raw": "list[int]",
      "type": "array"
     }
    },
    {
     "annotation": "list[int]",
     "name": "diagnosis_sequence",
     "required": false,
     "schema": {
      "items": {
       "raw": "int",
       "type": "integer"
      },
      "raw": "list[int]",
      "type": "array"
     }
    },
    {
     "annotation": "list[int]",
     "name": "procedure_sequence",
     "required": false,
     "schema": {
      "items": {
       "raw": "int",
       "type": "integer"
      },
      "raw": "list[int]",
      "type": "array"
     }
    },
    {
     "annotation": "list[int]",
     "name": "information_sequence",
     "required": false,
     "schema": {
      "items": {
       "raw": "int",
       "type": "integer"
      },
      "raw": "list[int]",
      "type": "array"
     }
    },
    {
     "annotation": "dict | None",
     "name": "category",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "dict | None",
     "name": "product_or_service",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "list[dict]",
     "name": "modifier",
     "required": false,
     "schema": {
      "items": {
       "raw": "dict",
       "type": "object"
      },
      "raw": "list[dict]",
      "type": "array"
     }
    },
    {
     "annotation": "list[UUID4]",
     "name": "charge_items",
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
     "annotation": "list[dict]",
     "name": "program_code",
     "required": false,
     "schema": {
      "items": {
       "raw": "dict",
       "type": "object"
      },
      "raw": "list[dict]",
      "type": "array"
     }
    },
    {
     "annotation": "PeriodSpec",
     "name": "serviced_period",
     "required": true,
     "schema": {
      "raw": "PeriodSpec",
      "ref": "PeriodSpec",
      "type": "ref"
     }
    },
    {
     "annotation": "Quantity | None",
     "name": "quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Quantity | None",
      "ref": "Quantity",
      "type": "ref"
     }
    },
    {
     "annotation": "float | None",
     "name": "unit_price",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "float | None",
     "name": "factor",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    }
   ],
   "name": "ClaimItemSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimItemSpec"
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
  },
  {
   "fields": [
    {
     "annotation": "Decimal | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
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
   "name": "Quantity",
   "source_file": "care/emr/resources/common/quantity.py",
   "spec": "care.emr.resources.common.quantity.Quantity"
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

## accident

```json
{
 "candidate_schemas": [
  {
   "annotation": "ClaimAccidentSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ClaimAccidentSpec | None",
    "ref": "ClaimAccidentSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
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
     "annotation": "datetime",
     "name": "date",
     "required": true,
     "schema": {
      "raw": "datetime",
      "type": "datetime"
     }
    },
    {
     "annotation": "dict | None",
     "name": "type",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "str | None",
     "name": "location",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ClaimAccidentSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimAccidentSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## payee

```json
{
 "candidate_schemas": [
  {
   "annotation": "ClaimPayeeSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ClaimPayeeSpec | None",
    "ref": "ClaimPayeeSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "definitions": [
  {
   "fields": [],
   "name": "ClaimPayeeSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimPayeeSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## questionnaire_responses

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClaimQuestionnaireResponseSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClaimQuestionnaireResponseSpec",
     "ref": "ClaimQuestionnaireResponseSpec",
     "type": "ref"
    },
    "raw": "list[ClaimQuestionnaireResponseSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
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
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "str",
     "name": "questionnaire",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "dict",
     "name": "category",
     "required": true,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "dict",
     "name": "code",
     "required": true,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "list[ClaimQuestionnaireResponseItemSpec]",
     "name": "item",
     "required": false,
     "schema": {
      "items": {
       "raw": "ClaimQuestionnaireResponseItemSpec",
       "ref": "ClaimQuestionnaireResponseItemSpec",
       "type": "ref"
      },
      "raw": "list[ClaimQuestionnaireResponseItemSpec]",
      "type": "array"
     }
    }
   ],
   "name": "ClaimQuestionnaireResponseSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimQuestionnaireResponseSpec"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "link_id",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
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
     "annotation": "list[ClaimQuestionnaireResponseAnswerSpec]",
     "name": "answer",
     "required": false,
     "schema": {
      "items": {
       "raw": "ClaimQuestionnaireResponseAnswerSpec",
       "ref": "ClaimQuestionnaireResponseAnswerSpec",
       "type": "ref"
      },
      "raw": "list[ClaimQuestionnaireResponseAnswerSpec]",
      "type": "array"
     }
    },
    {
     "annotation": "list['ClaimQuestionnaireResponseItemSpec']",
     "name": "item",
     "required": false,
     "schema": {
      "items": {
       "raw": "'ClaimQuestionnaireResponseItemSpec'",
       "type": "unknown"
      },
      "raw": "list['ClaimQuestionnaireResponseItemSpec']",
      "type": "array"
     }
    }
   ],
   "name": "ClaimQuestionnaireResponseItemSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimQuestionnaireResponseItemSpec"
  },
  {
   "fields": [
    {
     "annotation": "bool | None",
     "name": "value_boolean",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    },
    {
     "annotation": "float | None",
     "name": "value_decimal",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "int | None",
     "name": "value_integer",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "int | None",
      "type": "integer"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_date",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_date_time",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_time",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_uri",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "value_attachment",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "dict | None",
     "name": "value_coding",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "dict | None",
     "name": "value_quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    }
   ],
   "name": "ClaimQuestionnaireResponseAnswerSpec",
   "source_file": "app/care_nhcx/nhcx/specs/claim.py",
   "spec": "nhcx.specs.claim.ClaimQuestionnaireResponseAnswerSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
