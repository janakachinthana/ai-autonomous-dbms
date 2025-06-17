# AI-Driven Autonomous Database Management System (ADBMS)

This project implements an AI-driven autonomous database management system with self-tuning, predictive query optimization, intelligent indexing, and security/anomaly detection. See `docs/architecture.md` for details.

## Project Structure

```
├── docs/
│   ├── ADBMS_Research_Document.docx
│   ├── architecture.md
│   ├── generate_adbms_doc.py
│   └── jira_tasks_action_auditing.md
├── requirements.txt
├── src/
│   ├── config.py
│   ├── intelligent_indexing/
│   │   ├── index_manager.py
│   │   └── main.py
│   ├── query_optimization/
│   │   ├── main.py
│   │   └── query_optimizer.py
│   ├── security/
│   │   ├── anomaly_detector.py
│   │   └── main.py
│   └── self_tuning/
│       ├── main.py
│       ├── parameter_tuner.py
│       └── workload_monitor.py
├── tests/
│   └── integration/
│       ├── test_intelligent_indexing.py
│       ├── test_placeholder.py
│       ├── test_query_optimization.py
│       ├── test_security.py
│       └── test_self_tuning.py
└── README.md
```

## Project Setup

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/janakachinthana/ai-autonomous-dbms.git
   cd ai-autonomous-dbms
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

## Database Configuration

Update `src/config.py` with your database details or use environment variables:
```python
DB_TYPE = "mssql"  # Options: postgresql, mysql, mongodb, mssql
DB_HOST = "localhost"
DB_PORT = 1433  # Default port for MSSQL
DB_USER = "sa"
DB_PASSWORD = "your_password"
DB_NAME = "your_db_name"
DB_DRIVER = "ODBC Driver 17 for SQL Server"
```

## How to Run Each Module

Run the following commands in sequence from the project root directory:

1. **Intelligent Indexing Module**
   ```powershell
   python src/intelligent_indexing/main.py
   ```
2. **Predictive Query Optimizer**
   ```powershell
   python src/query_optimization/main.py
   ```
3. **Security & Compliance Layer**
   ```powershell
   python src/security/main.py
   ```
4. **Self-Tuning Engine**
   ```powershell
   python src/self_tuning/main.py
   ```

## Feature: Database Action Auditing and Reporting

All main modules now track and summarize actions performed on the database. After running each module, you can call the `get_applied_tasks_summary()` method to get a list of tasks and descriptions of what was done.

### Example Usage

After running a module, print the summary:

```python
# For IndexManager
manager = IndexManager()
# ... run actions ...
print(manager.get_applied_tasks_summary())

# For QueryOptimizer
optimizer = QueryOptimizer()
# ... run actions ...
print(optimizer.get_applied_tasks_summary())

# For AnomalyDetector
anomaly = AnomalyDetector()
# ... run actions ...
print(anomaly.get_applied_tasks_summary())

# For WorkloadMonitor
monitor = WorkloadMonitor()
# ... run actions ...
print(monitor.get_applied_tasks_summary())

# For ParameterTuner
param_tuner = ParameterTuner()
# ... run actions ...
print(param_tuner.get_applied_tasks_summary())
```

Each summary will show a list of tasks and their descriptions, providing a clear audit trail of what was applied to the database during execution.

## Jira Integration

Jira tasks have been created and linked for all new features related to action tracking and reporting. Reference the relevant ticket in your commit messages for traceability.

test