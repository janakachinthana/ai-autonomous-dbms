# anomaly_detector.py - Line-by-line Explanation

1. `import pyodbc`
   - Imports the `pyodbc` module for database connectivity.
2. `import sys`
   - Imports the `sys` module for manipulating the Python path.
3. `import os`
   - Imports the `os` module for path operations.
4. `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`
   - Adds the parent directory to the Python path so `config` can be imported.
5. `from config import DB_CONNECTION_STRING`
   - Imports the database connection string from the config file.

7-32. `class AnomalyDetector:` ...
   - Defines the `AnomalyDetector` class for detecting anomalies in log entries.

10-13. `def __init__(self): ...`
   - Initializes the class, connects to the database, and sets up a list to track actions.

15-28. `def detect(self, log_entry): ...`
   - Checks if the log entry contains suspicious SQL keywords, logs the result, and returns whether an anomaly was detected.

30-31. `def get_applied_tasks_summary(self): ...`
   - Returns the list of all actions performed (for auditing/reporting).
