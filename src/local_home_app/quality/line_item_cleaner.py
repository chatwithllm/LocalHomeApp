"""Line-item cleaning for LocalHomeApp.

Purpose:
- Clean noisy parsed line-item names into more usable item text while preserving simple rule-based explainability.

Inputs:
- raw parsed item name text

Outputs:
- cleaned item name text

Dependencies:
- re

Execution context:
- used before downstream history/signals consume parsed items.

Required permissions:
- none directly.

Expected errors/failure modes:
- some noisy item names remain imperfect

Related tests:
- tests/unit/test_line_item_cleaner.py

Related docs:
- docs/modules/line-item-cleaner.md
- docs/phases/data-quality-and-normalization.md
"""

from __future__ import annotations

import re


LEADING_JUNK_PATTERN = re.compile(r'^[^A-Za-z0-9]+')
MULTISPACE_PATTERN = re.compile(r'\s+')
TRAILING_LONG_CODE_PATTERN = re.compile(r'\s+[A-Z0-9]{6,}(?:\s+[A-Z])?$')
TRAILING_SHORT_FLAG_PATTERN = re.compile(r'\s+[A-Z]$')


def clean_line_item_name(raw_item_name: str | None) -> str | None:
    if raw_item_name is None:
        return None
    text = raw_item_name.strip()
    if not text:
        return None
    text = LEADING_JUNK_PATTERN.sub('', text)
    text = TRAILING_LONG_CODE_PATTERN.sub('', text)
    text = TRAILING_SHORT_FLAG_PATTERN.sub('', text)
    text = MULTISPACE_PATTERN.sub(' ', text).strip()
    return text or None
