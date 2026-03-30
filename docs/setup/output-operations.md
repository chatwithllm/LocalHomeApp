# Output Operations

## Purpose
Describe how LocalHomeApp currently validates local report generation, Telegram-style summaries, and structured exports.

## Current output flow
1. purchase history rows are queried from SQLite
2. rows are filtered for signal generation
3. signals are derived and formatted
4. output runtime builds local and Telegram-style summaries
5. purchase history rows can be exported as JSON

## Current local demo command
```bash
. .venv/bin/activate
python scripts/run_output_demo.py
```

## Current known limitation
Output usefulness is currently bounded by the quality of parsed purchase history and signals. The output layer is intentionally structured and privacy-safe, but it cannot improve upstream data quality on its own.
