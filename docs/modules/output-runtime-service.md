# Module: output_runtime_service.py

## Purpose
Assemble structured output summaries from receipt, history, and signal data.

## Inputs
Receipt summary, purchase history summary, and signal summary.

## Outputs
Local report text and Telegram summary text.

## Dependencies
- local_report_builder
- telegram_summary_formatter
- output_models

## Execution Context
Used by future output/integration workflows.

## Required Permissions
None directly.

## Expected Errors / Failure Modes
- incomplete upstream summary data

## Related Tests
- tests/unit/test_output_runtime_service.py

## Related Docs
- docs/phases/phase-06-output-integration.md
