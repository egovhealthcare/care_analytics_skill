# facility_facility JSONB schemas

## print_templates

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[PrintTemplate]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "PrintTemplate",
     "ref": "PrintTemplate",
     "type": "ref"
    },
    "raw": "list[PrintTemplate]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.FacilityCreateSpec"
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
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.FacilityRetrieveSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
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
     "annotation": "PageConfig | None",
     "name": "page",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PageConfig | None",
      "ref": "PageConfig",
      "type": "ref"
     }
    },
    {
     "annotation": "PrintSetupConfig | None",
     "name": "print_setup",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PrintSetupConfig | None",
      "ref": "PrintSetupConfig",
      "type": "ref"
     }
    },
    {
     "annotation": "BrandingConfig | None",
     "name": "branding",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "BrandingConfig | None",
      "ref": "BrandingConfig",
      "type": "ref"
     }
    },
    {
     "annotation": "WatermarkConfig | None",
     "name": "watermark",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "WatermarkConfig | None",
      "ref": "WatermarkConfig",
      "type": "ref"
     }
    }
   ],
   "name": "PrintTemplate",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.PrintTemplate"
  },
  {
   "fields": [
    {
     "annotation": "Literal['A4', 'A5', 'Letter', 'Legal'] | None",
     "name": "size",
     "required": false,
     "schema": {
      "enum": [
       "A4",
       "A5",
       "Letter",
       "Legal"
      ],
      "nullable": true,
      "raw": "Literal['A4', 'A5', 'Letter', 'Legal'] | None",
      "type": "literal"
     }
    },
    {
     "annotation": "Literal['portrait', 'landscape'] | None",
     "name": "orientation",
     "required": false,
     "schema": {
      "enum": [
       "portrait",
       "landscape"
      ],
      "nullable": true,
      "raw": "Literal['portrait', 'landscape'] | None",
      "type": "literal"
     }
    },
    {
     "annotation": "PageMargin | None",
     "name": "margin",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PageMargin | None",
      "ref": "PageMargin",
      "type": "ref"
     }
    }
   ],
   "name": "PageConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.PageConfig"
  },
  {
   "fields": [
    {
     "annotation": "bool | None",
     "name": "auto_print",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
     }
    }
   ],
   "name": "PrintSetupConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.PrintSetupConfig"
  },
  {
   "fields": [
    {
     "annotation": "LogoConfig | None",
     "name": "logo",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "LogoConfig | None",
      "ref": "LogoConfig",
      "type": "ref"
     }
    },
    {
     "annotation": "HeaderImageConfig | None",
     "name": "header_image",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "HeaderImageConfig | None",
      "ref": "HeaderImageConfig",
      "type": "ref"
     }
    },
    {
     "annotation": "FooterImageConfig | None",
     "name": "footer_image",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "FooterImageConfig | None",
      "ref": "FooterImageConfig",
      "type": "ref"
     }
    }
   ],
   "name": "BrandingConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.BrandingConfig"
  },
  {
   "fields": [
    {
     "annotation": "bool | None",
     "name": "enabled",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "bool | None",
      "type": "boolean"
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
     "annotation": "float | None",
     "name": "opacity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "float | None",
     "name": "rotation",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    }
   ],
   "name": "WatermarkConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.WatermarkConfig"
  },
  {
   "fields": [
    {
     "annotation": "float",
     "name": "top",
     "required": false,
     "schema": {
      "raw": "float",
      "type": "number"
     }
    },
    {
     "annotation": "float",
     "name": "bottom",
     "required": false,
     "schema": {
      "raw": "float",
      "type": "number"
     }
    },
    {
     "annotation": "float",
     "name": "left",
     "required": false,
     "schema": {
      "raw": "float",
      "type": "number"
     }
    },
    {
     "annotation": "float",
     "name": "right",
     "required": false,
     "schema": {
      "raw": "float",
      "type": "number"
     }
    }
   ],
   "name": "PageMargin",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.PageMargin"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "url",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "float | None",
     "name": "width",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "float | None",
     "name": "height",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "Literal['left', 'center', 'right']",
     "name": "alignment",
     "required": true,
     "schema": {
      "enum": [
       "left",
       "center",
       "right"
      ],
      "raw": "Literal['left', 'center', 'right']",
      "type": "literal"
     }
    }
   ],
   "name": "LogoConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.LogoConfig"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "url",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "float | None",
     "name": "height",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    }
   ],
   "name": "HeaderImageConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.HeaderImageConfig"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "url",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "float | None",
     "name": "height",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    }
   ],
   "name": "FooterImageConfig",
   "source_file": "care/emr/resources/facility/spec.py",
   "spec": "care.emr.resources.facility.spec.FooterImageConfig"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
