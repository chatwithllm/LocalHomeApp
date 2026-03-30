# Portability Strategy

## Goals
Keep LocalHomeApp movable to another machine without redesigning the application.

## Rules
- use configuration-driven paths
- isolate machine-specific dependencies in setup docs
- keep OCR behind an interface
- avoid hardcoded absolute paths in business logic
- store sensitive runtime artifacts outside the Git repository

## Current machine-specific assumptions
- initial runtime host: local Mac mini
- Apple-oriented OCR path may depend on macOS-native capabilities
- local sensitive storage root currently targeted at `/Users/assistant/LocalHomeAppSensitiveData`

## Portable assets
- source code
- documentation
- test fixtures
- structured schemas
- migration rules

## Machine-specific assets
- bot token / secrets
- local runtime logs
- raw receipt archive
- local OCR binaries or platform OCR dependencies
- local database file

## Migration expectation
A future migration should move:
- repository
- environment/config templates
- sensitive data root contents as needed
- OCR/runtime dependencies per machine
