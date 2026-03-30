# Coding Standards

## General
- prefer explicit names
- avoid vague utility dumping grounds
- keep modules single-responsibility where practical
- use typed models/configs where possible

## Errors
- raise domain-specific exceptions for expected operational failures
- separate configuration errors from runtime processing errors

## Logging
- log operationally useful events
- avoid leaking sensitive payloads into logs
- treat household data as privacy-sensitive

## Configuration
- keep machine-specific settings in config, not business logic
- keep secrets outside Git-tracked files
