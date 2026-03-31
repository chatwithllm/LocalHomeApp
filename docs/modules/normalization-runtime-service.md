# Module: normalization_runtime_service.py

## Purpose
Orchestrate merchant normalization, item cleanup, item normalization, and quality scoring.

## Inputs
Raw merchant name, raw item name, and line total.

## Outputs
Normalized merchant/item values and quality label.

## Dependencies
- dataclasses
- merchant_normalizer
- line_item_cleaner
- item_normalizer
- quality_scoring

## Execution Context
Used between parsing/storage/signal layers.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- unknown inputs remain only lightly normalized

## Related Tests
- tests/unit/test_normalization_runtime_service.py

## Related Docs
- docs/phases/data-quality-and-normalization.md
