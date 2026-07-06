# emr_medicationadministration JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseMedicationAdministrationSpec, MedicationAdministrationReadSpec, MedicationAdministrationSpec, MedicationAdministrationUpdateSpec

## status_reason

- Coding? (valueset-bound), optional — BaseMedicationAdministrationSpec, MedicationAdministrationReadSpec, MedicationAdministrationSpec

## medication

- Coding? (valueset-bound), optional — BaseMedicationAdministrationSpec, MedicationAdministrationReadSpec, MedicationAdministrationSpec

## performer

- list[MedicationAdministrationPerformer]?, optional — BaseMedicationAdministrationSpec, MedicationAdministrationReadSpec, MedicationAdministrationSpec

## dosage

- Dosage?, optional — BaseMedicationAdministrationSpec, MedicationAdministrationReadSpec, MedicationAdministrationSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `Dosage`: {text: str?, site: Coding?, route: Coding?, method: Coding?, dose: Quantity?, rate: Quantity?}
- `MedicationAdministrationPerformer`: {actor: uuid, function: MedicationAdministrationPerformerFunction?}
- `MedicationAdministrationPerformerFunction`: 'performer' | 'verifier' | 'witness'
- unresolved refs: Quantity
