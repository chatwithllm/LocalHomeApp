# Data Quality and Normalization

## Objective
Improve the quality, consistency, and downstream usability of LocalHomeApp structured data by normalizing merchants, cleaning line items, and explicitly scoring data quality.

## Scope
- merchant normalization
- line-item cleanup
- item normalization scaffolding
- quality scoring
- normalization runtime orchestration

## Out of Scope
- advanced ML classification
- external product catalogs
- cloud normalization services

## Deliverables
- merchant normalizer
- line-item cleaner
- item normalizer scaffold
- quality scoring module
- normalization runtime service
- initial docs and baseline tests

## Risks
- over-normalizing and losing useful provenance
- brittle normalization rules
- hidden coupling between normalization and downstream signal logic

## Dependencies
- completed receipt parsing and storage phases
- real receipt examples that exposed noisy merchant/item data

## Acceptance Criteria
- merchant aliases can be normalized consistently
- noisy line-item text can be cleaned predictably
- quality scoring can distinguish usable vs weak parsed data
- local tests pass

## Test Considerations
- merchant normalization tests
- line-item cleanup tests
- quality scoring tests
- runtime normalization flow tests

## Documentation Updates Required
- track doc
- module docs
- update downstream docs if normalization changes assumptions

## Current Status Notes
- Rule-based merchant normalization, line-item cleanup, item normalization scaffolding, quality scoring, and normalization runtime orchestration have now been implemented.
- Baseline unit tests now cover merchant normalization, line-item cleanup, quality scoring, and runtime normalization flow.
- This track is intended to improve downstream signal/report quality without introducing cloud dependencies or hiding original parsed provenance.
