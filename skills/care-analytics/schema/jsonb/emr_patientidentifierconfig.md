# emr_patientidentifierconfig JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BasePatientIdentifierSpec, PatientIdentifierCreateSpec, PatientIdentifierListSpec

## config

- IdentifierConfig, required — BasePatientIdentifierSpec, PatientIdentifierCreateSpec, PatientIdentifierListSpec

## definitions

- `IdentifierConfig`: {use: PatientIdentifierUse, description: str, system: str, required: bool, unique: bool, regex: str, display: str, retrieve_config: PatientIdentifierRetrieveConfig, default_value: str?, auto_maintained: bool}
- `PatientIdentifierRetrieveConfig`: {retrieve_with_dob: bool, retrieve_with_year_of_birth: bool, retrieve_with_otp: bool, retrieve_partial_search: bool}
- `PatientIdentifierUse`: 'usual' | 'official' | 'temp' | 'secondary' | 'old'
