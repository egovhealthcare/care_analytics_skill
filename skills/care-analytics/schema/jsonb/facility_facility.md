# facility_facility JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## print_templates

- list[PrintTemplate], optional — FacilityCreateSpec
- list[dict], optional — FacilityRetrieveSpec

## definitions

- `BrandingConfig`: {logo: LogoConfig?, header_image: HeaderImageConfig?, footer_image: FooterImageConfig?}
- `FooterImageConfig`: {url: str?, height: float?}
- `HeaderImageConfig`: {url: str, height: float?}
- `LogoConfig`: {url: str, width: float?, height: float?, alignment: 'left' | 'center' | 'right'}
- `PageConfig`: {size: 'A4' | 'A5' | 'Letter' | 'Legal'?, orientation: 'portrait' | 'landscape'?, margin: PageMargin?}
- `PageMargin`: {top: float, bottom: float, left: float, right: float}
- `PrintSetupConfig`: {auto_print: bool?}
- `PrintTemplate`: {slug: str, page: PageConfig?, print_setup: PrintSetupConfig?, branding: BrandingConfig?, watermark: WatermarkConfig?}
- `WatermarkConfig`: {enabled: bool?, text: str?, opacity: float?, rotation: float?}
