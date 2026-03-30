from local_home_app.output.local_report_builder import build_local_report
from local_home_app.output.output_models import PurchaseHistorySummaryOutput, ReceiptSummaryOutput, SignalSummaryOutput


def test_build_local_report() -> None:
    report = build_local_report(
        receipt_summary=ReceiptSummaryOutput('Kroger', '03/15/26', 39.04, 'completed'),
        purchase_history_summary=PurchaseHistorySummaryOutput(2, ['Kroger']),
        signal_summary=SignalSummaryOutput(['MILK: Observed 3 purchases']),
    )
    assert 'Merchant: Kroger' in report
    assert 'Signals:' in report
