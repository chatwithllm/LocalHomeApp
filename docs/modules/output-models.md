# Module: output_models.py

## Purpose
Represent structured output payloads for reports, summaries, and exports.

## Inputs
Parsed receipts, purchase history, and signal summaries.

## Outputs
Structured output records.

## Dependencies
- dataclasses
- typing

## Execution Context
Used by report builders, formatters, and output runtime services.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- missing required summary metadata

## Related Tests
- tests/unit/test_output_models.py

## Related Docs
- docs/phases/phase-06-output-integration.md
