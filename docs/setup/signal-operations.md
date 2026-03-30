# Signal Operations

## Purpose
Describe how LocalHomeApp currently validates and inspects inventory and price signals.

## Current signal flow
1. purchase history rows are queried from SQLite
2. noisy rows are filtered and skip reasons are counted
3. purchase patterns are analyzed on the usable subset
4. price expectations are derived on the usable subset
5. inventory-style signals are generated
6. signals are formatted into simple recommendation lines

## Current local demo command
```bash
. .venv/bin/activate
python scripts/run_inventory_signal_demo.py
```

## Current known limitation
Signal quality is currently constrained by parse quality. Noisy or weak line-item extraction will directly affect signal usefulness.

The current signal demo now reports how many rows were skipped and why, so signal weakness can be traced back to input quality instead of being mistaken for a signal-engine failure.
