# Module: file_system_paths.py

## Purpose
Resolve and manage local sensitive storage paths.

## Inputs
Application settings.

## Outputs
Runtime path helpers.

## Dependencies
- pathlib
- application_settings

## Execution Context
All local-storage-related workflows.

## Required Permissions
Read/write access to local sensitive storage root.

## Expected Errors / Failure Modes
- invalid data root
- directory creation failures

## Related Tests
- tests/unit/test_file_system_paths.py

## Related Docs
- docs/architecture/privacy-boundaries.md
- docs/architecture/portability-strategy.md
