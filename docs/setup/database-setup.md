# Database Setup

## Purpose
Document the local database setup for LocalHomeApp.

## Initial decision
- database engine: SQLite
- database location: local sensitive storage root
- current target path: `/Users/assistant/LocalHomeAppSensitiveData/database/local_home_app.sqlite`

## Why SQLite
- local-first
- low operational complexity
- strong fit for single-household V1
- portable as a single-file database

## Rules
- database files must not be committed to Git
- migrations must be documented
- schema changes must remain traceable
- receipt provenance must be preserved from raw artifact to structured record

## Future work for later phases
- migration runner setup
- schema definition
- backup/export procedures
- integrity/constraint testing
