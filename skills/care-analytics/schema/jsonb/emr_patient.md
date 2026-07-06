# emr_patient JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — PatientOTPBaseSpec, PatientOTPReadSpec, PatientOTPWriteSpec, PatientBaseSpec +5
- stores (when `__store_metadata__`): {age: int?, identifiers: list[PatientIdentifierConfigRequest], tags: list[uuid]}

## instance_identifiers

- list[PatientIdentifierResponse], optional — PatientRetrieveSpec

## facility_identifiers

- list[PatientIdentifierResponse], optional — PatientRetrieveSpec

## facility_tags

- list[dict], optional — PatientListSpec, PatientRetrieveSpec

## extensions

- dict, required — PatientOTPReadSpec, PatientRetrieveSpec

## definitions

- `IdentifierConfig`: {use: PatientIdentifierUse, description: str, system: str, required: bool, unique: bool, regex: str, display: str, retrieve_config: PatientIdentifierRetrieveConfig, default_value: str?, auto_maintained: bool}
- `PatientIdentifierConfigRequest`: {config: uuid, value: str}
- `PatientIdentifierListSpec`: {meta: dict, id: uuid?, config: IdentifierConfig, status: PatientIdentifierStatus}
- `PatientIdentifierResponse`: {config: PatientIdentifierListSpec, value: str}
- `PatientIdentifierRetrieveConfig`: {retrieve_with_dob: bool, retrieve_with_year_of_birth: bool, retrieve_with_otp: bool, retrieve_partial_search: bool}
- `PatientIdentifierStatus`: 'draft' | 'active' | 'inactive'
- `PatientIdentifierUse`: 'usual' | 'official' | 'temp' | 'secondary' | 'old'
