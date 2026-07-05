# encounter_identifiers_facilityencounteridentifierconfig JSONB schemas

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
   "source_file": "app/care_state_hmis/encounter_identifiers/spec.py",
   "spec": "encounter_identifiers.spec.FacilityEncounterIdentifierConfigReadSpec"
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
   "source_file": "app/care_state_hmis/encounter_identifiers/spec.py",
   "spec": "encounter_identifiers.spec.FacilityEncounterIdentifierConfigWriteSpec"
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

## enabled_encounter_classes

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ClassChoices]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClassChoices",
     "ref": "ClassChoices",
     "type": "ref"
    },
    "raw": "list[ClassChoices]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_state_hmis/encounter_identifiers/spec.py",
   "spec": "encounter_identifiers.spec.FacilityEncounterIdentifierConfigReadSpec"
  },
  {
   "annotation": "list[ClassChoices]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ClassChoices",
     "ref": "ClassChoices",
     "type": "ref"
    },
    "raw": "list[ClassChoices]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_state_hmis/encounter_identifiers/spec.py",
   "spec": "encounter_identifiers.spec.FacilityEncounterIdentifierConfigWriteSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "ClassChoices"
 ]
}
```
