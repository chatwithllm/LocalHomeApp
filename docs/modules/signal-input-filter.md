# Module: signal_input_filter.py

## Purpose
Filter noisy purchase-history rows before signal generation and explain what was skipped.

## Inputs
Purchase history rows.

## Outputs
Usable rows and skip-reason counts.

## Dependencies
- collections
- typing

## Execution Context
Used before pattern and price signal generation.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- malformed row shapes

## Related Tests
- tests/unit/test_signal_input_filter.py

## Related Docs
- docs/phases/phase-05-inventory-signals.md
