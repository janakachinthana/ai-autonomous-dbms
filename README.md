# AI-Driven Autonomous Database Management System (ADBMS)

This project implements an AI-driven autonomous database management system with self-tuning, predictive query optimization, intelligent indexing, and security/anomaly detection. See `docs/architecture.md` for details.

## Project Structure

```
├── docs/
│   ├── ADBMS_Code_Explanations.docx         # Combined Word doc of code explanations
│   ├── ADBMS_Research_Document.docx         # Research documentation
│   ├── architecture.md                      # System architecture overview
│   ├── code_explanation_report.md           # High-level code explanation summary
│   ├── convert_to_word.ipynb                # Notebook to convert explanations to Word
│   └── explanation_desc/                    # Line-by-line code explanations (Markdown)
│       ├── anomaly_detector.py.md
│       ├── config.py.md
│       ├── index_manager.py.md
│       ├── intelligent_indexing_main.py.md
│       ├── main.py.md
│       ├── parameter_tuner.py.md
│       ├── query_optimization_main.py.md
│       ├── query_optimizer.py.md
│       ├── security_main.py.md
│       └── workload_monitor.py.md
├── requirements.txt                         # Python dependencies
├── src/
│   ├── config.py                            # DB config and connection string
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
├── .gitignore
├── README.md
└── run_all_modules.py (if present)
```

- All main code explanations are in `docs/explanation_desc` (Markdown) and combined in `docs/ADBMS_Code_Explanations.docx`.
- See `docs/architecture.md` for system design.
- See `docs/code_explanation_report.md` for a high-level summary.

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

## Troubleshooting: SQL Server Connection Errors

If you encounter an error like:

```
[Microsoft][ODBC Driver 17 for SQL Server]TCP Provider: No connection could be made because the target machine actively refused it. (10061)
```

Follow these steps to resolve it:

1. **Ensure SQL Server is running**
   - Open SQL Server Configuration Manager and confirm your SQL Server instance is started.

2. **Enable TCP/IP**
   - In SQL Server Configuration Manager, go to `SQL Server Network Configuration > Protocols for [YourInstance]`.
   - Make sure `TCP/IP` is enabled. Restart the SQL Server service if you change this.

3. **Check Port Configuration**
   - In the TCP/IP properties, on the `IP Addresses` tab, ensure `TCP Port` is set to `1433` (or your configured port) for all relevant IPs (especially IPAll).
   - Restart the SQL Server service after making changes.

4. **Allow Port Through Firewall**
   - Make sure Windows Firewall or any other firewall allows inbound connections on port `1433`.

5. **Check SQL Server Binding**
   - In the TCP/IP properties, ensure at least one IP address (like IP1 or IPAll) is set to `Enabled=Yes` and has the correct port.

6. **Instance Name**
   - If using a named instance, connect using `localhost\\YourInstanceName` and ensure the SQL Server Browser service is running.

7. **Test with SQL Server Management Studio (SSMS)**
   - Try connecting with SSMS using the same host, port, username, and password. If SSMS cannot connect, the issue is with SQL Server/network, not your code.

8. **Check Connection String**
   - Your connection string should look like:
     ```
     DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1,1433;DATABASE=YourDB;UID=YourUser;PWD=YourPassword
     ```
   - Make sure the driver name matches exactly what is installed.

If you still have issues, review the error message and check your configuration again. For more help, see the SQL Server documentation or contact your database administrator.
