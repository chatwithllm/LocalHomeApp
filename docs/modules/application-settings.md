# Module: application_settings.py

## Purpose
Central typed configuration model for LocalHomeApp.

## Inputs
Environment variables and local runtime configuration.

## Outputs
Typed settings object for all runtime components.

## Dependencies
- pydantic-settings

## Execution Context
Loaded by CLI entry points and worker processes.

## Required Permissions
Read access to local environment/config values.

## Expected Errors / Failure Modes
- missing required settings
- invalid path values
- invalid OCR engine identifiers

## Related Tests
- tests/unit/test_application_settings.py

## Related Docs
- docs/setup/development-setup.md
- docs/architecture/portability-strategy.md
