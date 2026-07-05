# abdm_consentartefact JSONB schemas

## care_contexts

```json
{
 "candidate_schemas": [],
 "default_shape": {
  "type": "array"
 },
 "json_schema_validators": [
  {
   "schema": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "content": [
     {
      "additionalProperties": false,
      "properties": {
       "careContextReference": {
        "type": "string"
       },
       "patientReference": {
        "type": "string"
       }
      },
      "required": [
       "patientReference",
       "careContextReference"
      ],
      "type": "object"
     }
    ],
    "type": "array"
   },
   "schema_source": "app/care_abdm/abdm/models/json_schema/consent.py",
   "symbol": "CARE_CONTEXTS"
  }
 ],
 "meta_stored_fields": [],
 "status": "from_json_schema_validator"
}
```
