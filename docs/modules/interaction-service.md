# Module: interaction_service.py

## Purpose
Provide simple query-oriented access to recent receipts and purchase history for user-facing responses.

## Inputs
- purchase history repository
- optional merchant/item filters

## Outputs
Concise structured summaries suitable for conversational delivery.

## Dependencies
- dataclasses
- typing
- purchase-history-repository

## Execution Context
Used by future messaging integrations and local query scripts.

## Required Permissions
Read access to the local database through the repository layer.

## Expected Errors / Failure Modes
- sparse stored data yields partial answers
- low-quality parsing limits response quality

## Related Tests
- tests/unit/test_interaction_service.py

## Related Docs
- docs/phases/phase-10-user-interaction-layer.md
