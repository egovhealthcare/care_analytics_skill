# nhcx_claimconsent (ClaimConsent)

app: nhcx | source: app/care_nhcx/nhcx/models/claim_consent.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `stage` string(20) choices=[preauthorization|claim] default=ClaimConsentStage.PREAUTHORIZATION
- `payer_id` string(100)
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `token` string
- `expires_in` integer
- `refresh_token` string
- `refresh_expires_in` integer
- `accounts` jsonb default=list

JSONB shapes (`history`, `meta`, `accounts`): `jsonb/nhcx_claimconsent.md`

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['encounter', 'payer_id', 'stage'], name='uniq_claim_consent_encounter_payer_stage')]"
}
```
