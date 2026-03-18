    # Self-healing CI/CD pipeline – Flask URL shortener

Simple project to practice GitHub Actions and basic self-healing ideas in CI.

## What this pipeline does
- Runs on every push to `main`.
- Installs dependencies from `requirements.txt`.
- Runs `pytest` tests.
- If tests fail, runs `analyze_failure.py` to print helpful hints in the Actions log.

## Tech stack
- Python, pytest
- GitHub Actions (CI)
- Simple rule-based self-healing script (`analyze_failure.py`)

## Self-healing logic

The `analyze_failure.py` script:
- Reads the failed job logs from standard input.
- Looks for patterns like `ModuleNotFoundError`, `AssertionError`, or missing `requirements.txt`.
- Prints human-readable hints so the developer knows what to fix next.
