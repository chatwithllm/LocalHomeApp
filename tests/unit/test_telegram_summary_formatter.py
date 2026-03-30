from local_home_app.output.output_models import ReceiptSummaryOutput, SignalSummaryOutput
from local_home_app.output.telegram_summary_formatter import format_telegram_summary


def test_format_telegram_summary() -> None:
    text = format_telegram_summary(
        receipt_summary=ReceiptSummaryOutput('Kroger', '03/15/26', 39.04, 'completed'),
        signal_summary=SignalSummaryOutput(['MILK: Observed 3 purchases']),
    )
    assert 'Receipt: Kroger' in text
    assert 'Signals:' in text
