from local_home_app.output.output_models import PurchaseHistorySummaryOutput, ReceiptSummaryOutput, SignalSummaryOutput


def test_output_models_fields() -> None:
    receipt = ReceiptSummaryOutput('Kroger', '03/15/26', 39.04, 'completed')
    history = PurchaseHistorySummaryOutput(3, ['Kroger'])
    signals = SignalSummaryOutput(['MILK: Observed 3 purchases'])

    assert receipt.merchant_name == 'Kroger'
    assert history.receipt_count == 3
    assert signals.lines[0].startswith('MILK')
