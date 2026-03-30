from local_home_app.output.output_models import PurchaseHistorySummaryOutput, ReceiptSummaryOutput, SignalSummaryOutput
from local_home_app.output.output_runtime_service import build_outputs


def test_build_outputs() -> None:
    result = build_outputs(
        receipt_summary=ReceiptSummaryOutput('Kroger', '03/15/26', 39.04, 'completed'),
        purchase_history_summary=PurchaseHistorySummaryOutput(2, ['Kroger']),
        signal_summary=SignalSummaryOutput(['MILK: Observed 3 purchases']),
    )
    assert 'Merchant: Kroger' in result.local_report
    assert 'Receipt: Kroger' in result.telegram_summary
