# Dependency Rationale

## Python dependencies currently in local development environment
- `pydantic`
- `pydantic-settings`
- `pytest`
- `ruff`
- `black`
- `mypy`

## Rationale
### pydantic / pydantic-settings
Used for typed configuration and structured runtime models.

### pytest
Used for unit and integration testing.

### ruff
Used for fast linting and code-quality enforcement.

### black
Used for deterministic code formatting.

### mypy
Used for static type checking.

## Privacy implications
These dependencies do not require cloud services for core local development and validation.

## Portability implications
These are standard Python tooling choices with strong portability across development environments.

## Ongoing rule
Any dependency added later must be documented with:
- why it is needed
- where it is used
- alternatives considered when significant
- privacy implications
- portability implications
