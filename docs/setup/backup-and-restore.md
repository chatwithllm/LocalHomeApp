# Backup and Restore

## Purpose
Define the early backup/restore direction for LocalHomeApp local data.

## Current local assets to protect
- SQLite database
- local receipt artifacts
- OCR outputs
- structured parse outputs
- exports
- local secrets/config outside Git

## Early guidance
- back up the SQLite database file regularly
- back up the sensitive data root alongside the repository when preserving full local state
- keep Git as the source of truth for code/docs only

## Current known limitation
A fully automated backup flow is not yet implemented. Phase 7 begins documenting and validating operational expectations before deeper automation is added.
