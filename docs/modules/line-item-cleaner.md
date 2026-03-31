# Module: line_item_cleaner.py

## Purpose
Clean noisy parsed line-item names into more usable item text while preserving rule-based explainability.

## Inputs
Raw parsed item name text.

## Outputs
Cleaned item name text.

## Dependencies
- re

## Execution Context
Used before downstream history/signals consume parsed items.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- some noisy item names remain imperfect

## Related Tests
- tests/unit/test_line_item_cleaner.py

## Related Docs
- docs/phases/data-quality-and-normalization.md
