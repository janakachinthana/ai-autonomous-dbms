# Line-by-Line Code Explanation: src/self_tuning/workload_monitor.py

---

```python
import pyodbc
import random
import sys
import os
```
- Imports the `pyodbc` library for connecting to SQL Server databases.
- Imports the `random` module for generating random numbers (used for simulating metrics).
- Imports the `sys` and `os` modules for manipulating the Python path and working with the file system.

```python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```
- Modifies the Python module search path to include the parent directory of the current file, allowing imports from the parent directory (e.g., `config`).

```python
from config import DB_CONNECTION_STRING
```
- Imports the `DB_CONNECTION_STRING` variable from the `config.py` file in the parent directory, which contains the database connection string.

```python
class WorkloadMonitor:
    """
    Monitoring of database workload metrics using real MS SQL connection.
    """
```
- Defines the `WorkloadMonitor` class, which is responsible for monitoring database workload metrics.
- The docstring describes the purpose of the class.

```python
    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.applied_tasks = []  # Track applied tasks
```
- The constructor (`__init__`) establishes a connection to the database using the connection string.
- Initializes an empty list `applied_tasks` to keep track of monitoring tasks performed.

```python
    def get_metrics(self):
        # Example: Query sys.dm_os_performance_counters or similar for real metrics
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT cntr_value FROM sys.dm_os_performance_counters WHERE counter_name = 'Buffer cache hit ratio'")
            cache_hit_ratio = cursor.fetchone()[0] / 100.0
        except Exception:
            cache_hit_ratio = random.uniform(0.7, 1.0)
        # Simulate other metrics (customize as needed)
        metrics = {
            'cpu_usage': random.uniform(10, 90),
            'memory_usage': random.uniform(1000, 8000),
            'cache_hit_ratio': cache_hit_ratio,
            'query_throughput': random.randint(100, 1000)
        }
        # Log the metrics retrieval as a task
        self.applied_tasks.append({
            'task': 'Retrieve workload metrics',
            'description': f"Metrics collected: {metrics}"
        })
        return metrics
```
- Defines the `get_metrics` method, which retrieves or simulates workload metrics.
- Creates a database cursor.
- Tries to execute a SQL query to get the buffer cache hit ratio from SQL Server performance counters.
- If the query fails, simulates the cache hit ratio with a random value between 0.7 and 1.0.
- Simulates other metrics: CPU usage, memory usage, and query throughput with random values.
- Logs the metrics retrieval as a task in `applied_tasks`.
- Returns the metrics as a dictionary.

```python
    def get_applied_tasks_summary(self):
        return self.applied_tasks
```
- Defines a method to return the list of applied tasks (i.e., a summary of all monitoring actions performed).
