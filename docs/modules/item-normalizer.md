# Module: item_normalizer.py

## Purpose
Provide a clear boundary for item-name normalization beyond basic cleanup.

## Inputs
Cleaned item name text.

## Outputs
Normalized item identity text.

## Dependencies
Standard library only.

## Execution Context
Used before downstream signal generation and history aggregation.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- unknown item variants remain near-original

## Related Tests
- tests/unit/test_item_normalizer.py

## Related Docs
- docs/phases/data-quality-and-normalization.md
