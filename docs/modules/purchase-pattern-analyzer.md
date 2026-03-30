# Module: purchase_pattern_analyzer.py

## Purpose
Analyze item purchase history to derive repeat-purchase observations.

## Inputs
Purchase history rows.

## Outputs
Purchase pattern signals.

## Dependencies
- datetime
- collections
- signal_models

## Execution Context
Used by inventory and price signal generation.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- malformed date values
- sparse history for interval analysis

## Related Tests
- tests/unit/test_purchase_pattern_analyzer.py

## Related Docs
- docs/phases/phase-05-inventory-signals.md
