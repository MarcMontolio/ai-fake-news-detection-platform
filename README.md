# AI Fake News Detection Platform

A professional NLP and machine learning platform for misinformation risk analysis, explainable fake news classification, and credibility scoring.

## Overview

The **AI Fake News Detection Platform** is a backend and machine learning project designed to analyse news content and estimate misinformation risk using NLP, machine learning models, and transparent credibility signals.

The goal is not to determine whether a claim is absolutely true or false. Instead, the platform provides an explainable risk assessment based on textual patterns, model confidence, source metadata, and credibility-related indicators.

## Planned Features

* FastAPI backend
* PostgreSQL persistence
* NLP preprocessing pipeline
* Baseline scikit-learn classifier
* Explainable predictions
* Credibility scoring system
* Redis and Celery for asynchronous processing
* Dashboard for analysis and visualisation
* Docker-based local development
* CI with GitHub Actions

## Project Status

Initial project foundation in progress.

## Local Development

This project uses Python 3.12 and a local virtual environment for development.

### Create and activate the virtual environment

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install the project in development mode

Once the virtual environment is active, install the project with its development dependencies:

```powershell
python -m pip install -e '.[dev]'
```

This installs the project in editable mode, which means local code changes are available without reinstalling the package.

### Verify the environment

You can verify that Python is running from the virtual environment with:

```powershell
python --version
pip --version
```

### Run linting

```powershell
ruff check .
```

### Check formatting

```powershell
ruff format --check .
```

To automatically format the codebase:

```powershell
ruff format .
```

### Run tests

```powershell
pytest
```

### Deactivate the virtual environment

When you are done working on the project, deactivate the environment with:

```powershell
deactivate
```

### Run the API locally

Start the FastAPI development server with:

```powershell
python -m uvicorn apps.api.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Check the health endpoint with:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

The interactive API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

### Run with Docker Compose

Start the local development environment with:

```powershell
docker compose up --build
```

This starts the following services:

* FastAPI backend on `http://127.0.0.1:8000`
* PostgreSQL on port `5432`

Check the health endpoint with:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```

Stop the services with:

```powershell
docker compose down
```

## Database Configuration

The application reads PostgreSQL connection settings from environment variables.

By default, the database URL is built from the following variables:

* `POSTGRES_HOST`
* `POSTGRES_PORT`
* `POSTGRES_DB`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`

An explicit `DATABASE_URL` can also be provided. When set, it takes priority over the individual PostgreSQL settings.

Example SQLAlchemy URL format:

```text
postgresql+psycopg://fake_news_user:fake_news_password@localhost:5432/fake_news_platform
```

Application settings are defined in:

```text
packages/shared/config.py
```

Database engine and session configuration are defined in:

```text
packages/shared/database.py
```

Alembic migrations and database models are handled separately in later Milestone 2 issues.

## Roadmap

* Milestone 1 — Project Foundation
* Milestone 2 — Database and Domain Model
* Milestone 3 — Dataset Pipeline
* Milestone 4 — Baseline Machine Learning Model
* Milestone 5 — Inference API
* Milestone 6 — Explainability and Credibility Scoring
* Milestone 7 — Async Processing and Dashboard
* Milestone 8 — Advanced NLP and Portfolio Polish

## Disclaimer

This platform does not determine whether a claim is absolutely true or false. It estimates misinformation risk using machine learning models and credibility signals.

The results should be interpreted as decision-support outputs, not as final fact-checking conclusions.
