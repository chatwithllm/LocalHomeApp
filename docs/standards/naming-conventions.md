# Naming Conventions

## Python Files
- Use lowercase snake_case.
- Use explicit names tied to responsibility.
- Avoid vague names such as `main.py`, `utils.py`, `helper.py`, or `temp.py`.

## Classes
- Use PascalCase.
- Use responsibility-driven names.

## Functions
- Use snake_case verbs describing behavior.

## Folders
- Use lowercase names grouped by bounded responsibility.

## Documentation Files
- Use lowercase kebab-case.
- Examples: `architecture-overview.md`, `phase-02-dual-local-ocr.md`.

## Branch Names
- `feature/phase-00-foundation`
- `feature/phase-01-telegram-intake`
- `feature/phase-02-dual-local-ocr`
- `docs/prd-refinement`
- `fix/receipt-line-item-parser`

## Background Service / Worker Names
- Use clear human-readable service names.
- Avoid generic process names where possible.
- Worker/service entry points should reveal function clearly, such as:
  - `localhomeapp-intake-worker`
  - `localhomeapp-ocr-worker`
  - `localhomeapp-alert-router`
