# Data Flow

## V1 end-to-end flow
1. User sends receipt to `@OC4340_bot` via Main chat.
2. Intake system downloads the raw receipt artifact to local sensitive storage.
3. Intake metadata is recorded with source channel provenance.
4. Workers chat receives operational progress events when appropriate.
5. OCR runs locally using configured engine selection.
6. OCR text is stored locally in sensitive storage.
7. Parsing transforms OCR text into structured grocery purchase records.
8. Structured purchase data is persisted locally.
9. Derived signals are generated from local purchase history.
10. Alerts chat receives failures/manual-review notices; Main receives user-facing summaries.

## Channel boundaries
- Main: user-facing interaction and approvals.
- Workers: operational context.
- Alerts: failures and manual review.

## Sensitive boundary
Raw receipts, OCR outputs, and household purchase history remain in local sensitive storage.
