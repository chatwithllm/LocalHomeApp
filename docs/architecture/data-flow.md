# Data Flow

## V1 end-to-end flow
1. User sends receipt to `@OC4340_bot` via Main chat.
2. OpenClaw receives the Telegram update as the ingress owner.
3. OpenClaw hands the receipt input to LocalHomeApp's local intake processing boundary.
4. LocalHomeApp stores the raw receipt artifact to local sensitive storage.
5. Intake metadata is recorded with source channel provenance.
6. Workers chat receives operational progress events when appropriate.
7. OCR runs locally using configured engine selection.
8. OCR text is stored locally in sensitive storage.
9. Parsing transforms OCR text into structured grocery purchase records.
10. Structured purchase data is persisted locally.
11. Derived signals are generated from local purchase history.
12. Alerts chat receives failures/manual-review notices; Main receives user-facing summaries.

## Channel boundaries
- Main: user-facing interaction and approvals.
- Workers: operational context.
- Alerts: failures and manual review.

## Sensitive boundary
Raw receipts, OCR outputs, and household purchase history remain in local sensitive storage.
