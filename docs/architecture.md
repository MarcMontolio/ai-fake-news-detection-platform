# Architecture

## Overview

The **AI Fake News Detection Platform** is designed as a modular NLP and machine learning system for analysing misinformation risk, classifying potentially fake news, and generating credibility scores.

The project will start with a simple backend and a baseline machine learning pipeline. Over time, it will evolve into a more complete platform with API access, persistent storage, asynchronous processing, explainability features, credibility scoring, and a dashboard.

The purpose of the platform is not to decide what is absolutely true or false. Instead, it aims to provide an explainable risk assessment based on textual patterns, model confidence, source metadata, and other credibility-related indicators.

## Repository Structure

```text
apps/
  Main application entrypoints, such as the FastAPI backend, future async workers, and dashboard.

packages/
  Shared internal packages for configuration, NLP processing, machine learning, database access, explainability, and credibility scoring.

scripts/
  Utility scripts for dataset preparation, model training, evaluation, and maintenance tasks.

tests/
  Automated tests for application code, shared packages, and ML pipeline components.

docs/
  Technical documentation, architecture notes, API documentation, ML pipeline documentation, and model cards.

data/
  Dataset files used for development and experimentation.

data/raw/
  Raw datasets before any cleaning or transformation.

data/processed/
  Cleaned and processed datasets ready for training and evaluation.

models/
  Trained model artifacts and their related metadata.

reports/
  Evaluation reports, metrics, confusion matrices, and model comparison outputs.
```

## Planned Components

The platform is expected to grow through the following components:

* A FastAPI backend to expose the REST API
* A PostgreSQL database to store articles, analyses, explanations, and source metadata
* An NLP preprocessing pipeline for text cleaning and feature preparation
* A baseline machine learning model using TF-IDF and Logistic Regression
* An explainability layer based on model feature weights
* A credibility scoring service that combines model predictions with content and source signals
* Redis and Celery for asynchronous processing
* A dashboard to submit articles and visualise analysis results
* A future classifier based on HuggingFace Transformers
* Future experimental analysis for bias and subjectivity detection

## Design Principles

The project follows these engineering principles:

* Modular architecture
* Clear separation between API, machine learning, and persistence layers
* Reproducible data and model pipelines
* Explainable prediction outputs
* Testable components
* Docker-based local development
* Documentation-first project evolution
* Portfolio-ready engineering practices

## Current Scope

At this stage, the project defines the initial repository structure and documentation foundation.

Application logic, Python tooling, API implementation, Docker configuration, database integration, and machine learning functionality will be added in later milestones and issues.
