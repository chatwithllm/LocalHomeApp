# Python Tooling Setup

## Purpose
Document the required local Python development tooling for LocalHomeApp so a restart-from-scratch setup does not miss test and quality dependencies.

## Required initial tooling
- `pytest`
- `ruff`
- `black`
- `mypy`

## Why this matters
Phase 0 requires not only repository scaffolding but also a functioning local validation baseline. If the Python toolchain is missing, foundational tests cannot be executed and the phase cannot be considered complete.

## Current status note
During initial Phase 0 execution, running `python3 -m pytest tests/unit -q` failed because `pytest` was not installed in the local environment.

## Current install command used
```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pytest ruff black mypy pydantic pydantic-settings
```

## Current validation note
The first baseline pytest run exposed a src-layout import-path issue (`ModuleNotFoundError: local_home_app`). That packaging/test-path fix is part of Phase 0 and must be completed before this phase is marked stable.

The next baseline run exposed a Python-version alignment issue: the local virtual environment is currently Python 3.9, so code and project configuration must either remain compatible with that interpreter or the local environment must be upgraded to the target project version. This must be documented and resolved explicitly during Phase 0.

## Next setup tasks
- create or activate a local virtual environment
- install development dependencies
- rerun baseline unit tests
- document exact install command(s) used
- keep test-path/package-layout configuration aligned with the src-based repository structure
