# AI-Autonomous-DBMS Codebase Overview

This document provides a high-level explanation of each code file and directory in the project, helping you understand the purpose and logic of every component.

---

## Project Root

- **README.md**: Project documentation, setup, usage, and references.
- **requirements.txt**: Lists Python dependencies.
- **Setup.bat**: Batch script for environment setup (e.g., installing dependencies, setting environment variables).
- **import sys.txt**: Likely a placeholder or note (not code).
- **auto_run_all_tables.py**: Main automation script to run processes for all tables in the database. Likely orchestrates the execution of various modules.

---

## docs/
- Contains documentation, architecture diagrams, research documents, and Jupyter notebooks for research and code explanations.
- **CODEBASE_OVERVIEW.md**: This file. High-level explanation of the codebase.

---

## logs/
- Stores output logs and JSON files for each module (anomaly detection, index management, etc.) for different runs.

---

## src/
Main source code directory, organized by feature/module.

- **config.py**: Handles database connection configuration using environment variables. Supports multiple DB types (MSSQL, PostgreSQL, MySQL, MongoDB). Constructs a connection string for MSSQL by default.

- **intelligent_indexing/**
  - **index_manager.py**: Manages database indexes, automating their creation, adaptation, and removal based on workload or AI recommendations.
  - **main.py**: Entry point for the intelligent indexing module; orchestrates index analysis and management.

- **query_optimization/**
  - **main.py**: Entry point for the query optimization module; runs the optimizer logic.
  - **query_optimizer.py**: Implements the logic for optimizing SQL queries, possibly using machine learning to predict better execution plans.

- **security/**
  - **anomaly_detector.py**: Implements anomaly detection for database activity, using AI/ML to spot suspicious or non-compliant behavior.
  - **main.py**: Entry point for the security module; coordinates anomaly detection and other security checks.

- **self_tuning/**
  - **main.py**: Entry point for the self-tuning engine; manages the overall tuning process.
  - **parameter_tuner.py**: Adjusts database/system parameters dynamically based on workload and performance metrics.
  - **workload_monitor.py**: Monitors database workload, collects metrics, and possibly triggers tuning or indexing actions.

---

## tests/integration/
- Contains integration tests for each major module:
  - **test_intelligent_indexing.py**: Tests for the intelligent indexing module.
  - **test_query_optimization.py**: Tests for the query optimization module.
  - **test_security.py**: Tests for the security/anomaly detection module.
  - **test_self_tuning.py**: Tests for the self-tuning module.
  - **test_placeholder.py**: Likely a template or placeholder for future tests.

---

## How the Project Works Together

- Each module in `src/` is responsible for a core aspect of autonomous database management:
  - *Self-tuning* monitors and adjusts system parameters.
  - *Query optimization* improves SQL performance using AI.
  - *Intelligent indexing* automates index management.
  - *Security* uses anomaly detection to protect the database.
- The main scripts in each module (`main.py`) act as entry points, orchestrating the logic in their respective submodules.
- Configuration is centralized in `config.py`, making it easy to adapt the system to different environments.
- Integration tests ensure that each module works correctly with the others.

---

## Example: config.py Explanation

- Imports the `os` module to access environment variables.
- Sets up database configuration variables (`DB_TYPE`, `DB_HOST`, `DB_PORT`, etc.) with defaults, allowing overrides via environment variables.
- Constructs a connection string for MSSQL using the provided or default values.
- Supports easy adaptation to other database types by changing environment variables.

---

If you want a detailed, function-by-function explanation for a specific file, please specify the file and I can provide a deep dive!
