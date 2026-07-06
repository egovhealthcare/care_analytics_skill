# emr_encounter JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — EncounterCreateSpec, EncounterListSpec, EncounterRetrieveSpec, EncounterSpecBase

## status_history

- dict, required — EncounterListSpec, EncounterRetrieveSpec

## encounter_class_history

- dict, required — EncounterListSpec, EncounterRetrieveSpec

## period

- PeriodSpec, optional — EncounterCreateSpec, EncounterListSpec, EncounterRetrieveSpec, EncounterSpecBase

## hospitalization

- HospitalizationSpec?, optional — EncounterCreateSpec, EncounterListSpec, EncounterRetrieveSpec, EncounterSpecBase

## care_team

- list[dict], optional — EncounterListSpec, EncounterRetrieveSpec

## extensions

- dict, required — EncounterRetrieveSpec

## definitions

- `HospitalizationSpec`: {re_admission: bool?, admit_source: AdmitSourcesChoices?, discharge_disposition: DischargeDispositionChoices?, diet_preference: DietPreferenceChoices?}
- `PeriodSpec`: {start: datetime?, end: datetime?}
- `AdmitSourcesChoices`: 'hosp_trans' | 'emd' | 'outp' | 'born' | 'gp' | 'mp' | 'nursing' | 'psych' | 'rehab' | 'other'
- `DietPreferenceChoices`: 'vegetarian' | 'dairy_free' | 'nut_free' | 'gluten_free' | 'vegan' | 'halal' | 'kosher' | 'none'
- `DischargeDispositionChoices`: 'home' | 'alt_home' | 'other_hcf' | 'hosp' | 'long' | 'aadvice' | 'exp' | 'psy' | 'rehab' | 'snf' | 'oth'
