# Phase Workflow Standard

## Rule
Every phase in LocalHomeApp must follow this sequence:
1. implement locally
2. test locally
3. update documentation
4. commit phase work on a dedicated branch
5. request approval before merging to `main`

## Required phase completion evidence
- local tests executed successfully
- phase document updated
- relevant module/setup/architecture docs updated
- branch name reflects the phase or scoped feature
- commit message states local testing status and documentation updates

## Merge rule
No phase should be merged to `main` until local testing has passed and approval has been explicitly given.

## Why this matters
This keeps LocalHomeApp disciplined, restart-safe, and traceable as a real production system instead of a sequence of unstructured edits.
