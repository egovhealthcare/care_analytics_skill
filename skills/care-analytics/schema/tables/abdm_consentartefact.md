# abdm_consentartefact (ConsentArtefact)

app: abdm | source: app/care_abdm/abdm/models/consent.py
bases: Consent (inherited columns: `_base_models.md`)

## Columns

- `consent_request` foreign_key -> abdm_consentrequest.consent_id [col: consent_request_id] NULL
- `cm` string(50) NULL
- `key_material_algorithm` string(20) NULL default=ECDH
- `key_material_curve` string(20) NULL default=Curve25519
- `key_material_public_key` string(100) NULL
- `key_material_private_key` string(200) NULL
- `key_material_nonce` string(100) NULL
- `signature` string NULL

JSONB shapes (`care_contexts`): `jsonb/abdm_consentartefact.md`
