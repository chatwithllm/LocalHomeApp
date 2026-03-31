# Module: merchant_normalizer.py

## Purpose
Normalize merchant name variants into a consistent canonical form.

## Inputs
Raw merchant name text.

## Outputs
Canonical merchant name.

## Dependencies
Standard library only.

## Execution Context
Used after parsing and before downstream storage/signal use.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- unknown merchant names remain unnormalized

## Related Tests
- tests/unit/test_merchant_normalizer.py

## Related Docs
- docs/phases/data-quality-and-normalization.md
