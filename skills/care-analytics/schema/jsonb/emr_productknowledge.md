# emr_productknowledge JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseProductKnowledgeSpec, ProductKnowledgeReadSpec, ProductKnowledgeUpdateSpec, ProductKnowledgeWriteSpec

## code

- Coding?, optional — BaseProductKnowledgeSpec, ProductKnowledgeReadSpec, ProductKnowledgeUpdateSpec, ProductKnowledgeWriteSpec

## names

- list[ProductName]?, optional — BaseProductKnowledgeSpec, ProductKnowledgeReadSpec, ProductKnowledgeUpdateSpec, ProductKnowledgeWriteSpec

## storage_guidelines

- list[StorageGuideline]?, optional — BaseProductKnowledgeSpec, ProductKnowledgeReadSpec, ProductKnowledgeUpdateSpec, ProductKnowledgeWriteSpec

## definitional

- ProductDefinitionSpec?, optional — BaseProductKnowledgeSpec, ProductKnowledgeReadSpec, ProductKnowledgeUpdateSpec, ProductKnowledgeWriteSpec

## base_unit

- Coding (valueset-bound), required — BaseProductKnowledgeSpec, ProductKnowledgeReadSpec, ProductKnowledgeUpdateSpec, ProductKnowledgeWriteSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `DrugCharacteristic`: {code: DrugCharacteristicCode, value: str}
- `DurationSpec`: {value: int, unit: Coding}
- `ProductDefinitionSpec`: {dosage_form: Coding?, intended_routes: list[Coding], ingredients: list[ProductIngredient], nutrients: list[ProductNutrient], drug_characteristic: list[DrugCharacteristic]}
- `ProductIngredient`: {is_active: bool, substance: Coding, strength: ProductStrength}
- `ProductName`: {name_type: ProductNameTypes, name: str}
- `ProductNutrient`: {item: Coding, amount: ProductStrength}
- `ProductStrength`: {ratio: Ratio, quantity: Quantity}
- `Quantity`: {value: decimal?, unit: Coding?, meta: dict?, code: Coding?}
- `Ratio`: {numerator: Quantity, denominator: Quantity}
- `StorageGuideline`: {note: str, stability_duration: DurationSpec}
- `DrugCharacteristicCode`: 'imprint_code' | 'size' | 'shape' | 'color' | 'coating' | 'scoring' | 'logo' | 'image'
- `ProductNameTypes`: 'trade_name' | 'alias' | 'original_name' | 'preferred'
- unresolved refs: Coding
