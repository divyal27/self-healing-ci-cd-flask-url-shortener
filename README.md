# Self-Healing CI/CD Pipeline – Flask URL Shortener

This project is a small DevOps lab where a sample Flask URL shortener app is wired to a **self-healing CI/CD pipeline** using GitHub Actions and Python.

The focus is not on complex business logic, but on:
- Reliable CI that runs on every push.
- Automatic log analysis when the pipeline fails.
- Clear hints for the developer on how to fix issues.

## Features

- GitHub Actions CI workflow triggered on every push to `main`.
- Installs Python dependencies from `requirements.txt`.
- Runs automated tests with `pytest`.
- On failure, runs a custom `analyze_failure.py` script to inspect logs and print human‑readable suggestions.
- Simple tests included (sample test + health placeholder) to keep the pipeline green and demonstrable.

## Tech Stack

- Python 3.12
- Pytest for testing
- GitHub Actions for CI
- Rule‑based self‑healing script in Python (`analyze_failure.py`)

## Repository structure

```text
self-healing-ci-cd-flask-url-shortener/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── tests/
│   ├── test_basic.py       # Simple sample test
│   └── test_app_health.py  # Placeholder health test
├── analyze_failure.py      # Self-healing analysis script
├── requirements.txt        # Python dependencies
└── README.md


Here is a complete, simple **README.md** you can copy‑paste and then adjust names/links. [perplexity](https://www.perplexity.ai/search/1d2e6de9-4aa6-4823-80b4-24a2955a632a)

```markdown
# Self-Healing CI/CD Pipeline – Flask URL Shortener

This project is a small DevOps lab where a sample Flask URL shortener app is wired to a **self-healing CI/CD pipeline** using GitHub Actions and Python.

The focus is not on complex business logic, but on:
- Reliable CI that runs on every push.
- Automatic log analysis when the pipeline fails.
- Clear hints for the developer on how to fix issues.

## Features

- GitHub Actions CI workflow triggered on every push to `main`.
- Installs Python dependencies from `requirements.txt`.
- Runs automated tests with `pytest`.
- On failure, runs a custom `analyze_failure.py` script to inspect logs and print human‑readable suggestions.
- Simple tests included (sample test + health placeholder) to keep the pipeline green and demonstrable.

## Tech Stack

- Python 3.12
- Pytest for testing
- GitHub Actions for CI
- Rule‑based self‑healing script in Python (`analyze_failure.py`)

## Repository structure

```text
self-healing-ci-cd-flask-url-shortener/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── tests/
│   ├── test_basic.py       # Simple sample test
│   └── test_app_health.py  # Placeholder health test
├── analyze_failure.py      # Self-healing analysis script
├── requirements.txt        # Python dependencies
└── README.md
```

## How the pipeline works

1. **Trigger**  
   - The workflow in `.github/workflows/ci.yml` runs on every push or pull request to the `main` branch.

2. **Build & Test steps**  
   - Checkout repository code.  
   - Set up Python 3.12 on the GitHub runner.  
   - Install dependencies with:  
     ```bash
     python -m pip install --upgrade pip
     pip install -r requirements.txt
     ```  
   - Run tests with:  
     ```bash
     python -m pytest
     ```

3. **Self-healing analysis**  
   - If the test step fails, a separate step runs:
     ```bash
     python -m pytest || true 2>&1 | python analyze_failure.py
     ```
   - `analyze_failure.py` reads the logs from standard input and looks for patterns such as:
     - `ModuleNotFoundError`
     - `AssertionError`
     - Missing `requirements.txt`
   - For each pattern it prints a clear hint (for example “Check requirements.txt and install the missing module with pip”).

## How to run tests locally

1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the test suite:
   ```bash
   python -m pytest
   ```

You should see all tests passing before pushing changes so that the CI pipeline also stays green.

## Ideas for future improvements

- Move the full Flask URL shortener application code into this repository and add real endpoint tests.
- Add more self‑healing rules (timeouts, database connection errors, etc.).
- Automatically open a GitHub issue if the same failure pattern appears multiple times.
- Integrate an LLM/AI service to generate smarter root‑cause analysis from the logs.

---

**Author:** Divyal Padalkar – Aspiring DevOps Engineer  
This project is part of a personal DevOps portfolio focused on CI/CD, reliability, and automation. [memory:1][memory:2]
```
