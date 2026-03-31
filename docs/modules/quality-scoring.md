# Module: quality_scoring.py

## Purpose
Score parsed structured data for downstream usability.

## Inputs
Merchant name, item name, and line total.

## Outputs
Quality label.

## Dependencies
Standard library only.

## Execution Context
Used before signals and reports consume parsed data.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- simplistic scoring during early iterations

## Related Tests
- tests/unit/test_quality_scoring.py

## Related Docs
- docs/phases/data-quality-and-normalization.md
