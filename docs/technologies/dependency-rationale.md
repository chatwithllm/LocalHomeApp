# Dependency Rationale

## Python dependencies currently in local development environment
- `pydantic`
- `pydantic-settings`
- `Pillow`
- `pytest`
- `ruff`
- `black`
- `mypy`

## Rationale
### pydantic / pydantic-settings
Used for typed configuration and structured runtime models.

### Pillow
Used for basic local image preprocessing prior to OCR. Helps produce grayscale and autocontrasted images for OCR engines.

### pytest
Used for unit and integration testing.

### ruff
Used for fast linting and code-quality enforcement.

### black
Used for deterministic code formatting.

### mypy
Used for static type checking.

## Non-Python runtime dependency
### Tesseract OCR
- used as the first real local OCR engine path
- installed locally on the current machine
- chosen because it is local-only, mature, and portable across future environments

## Apple-oriented OCR dependency note
The Apple OCR path currently depends on a future macOS-native bridge implementation because Apple framework bindings were not available in the current Python environment.

## Privacy implications
These dependencies support local-only OCR and local development workflows without requiring cloud OCR services.

## Portability implications
- Tesseract improves portability
- Pillow improves local preprocessing quality
- Apple-oriented OCR remains more environment-specific and is intentionally isolated behind a bridge/interface boundary

## Ongoing rule
Any dependency added later must be documented with:
- why it is needed
- where it is used
- alternatives considered when significant
- privacy implications
- portability implications
