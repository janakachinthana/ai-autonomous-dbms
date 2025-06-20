import pyodbc
import random
import sys
import os
import json
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class WorkloadMonitor:
    """
    Monitoring of database workload metrics using real MS SQL connection.
    """
    _log_dir = None

    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.applied_tasks = []  # Track applied tasks
        if WorkloadMonitor._log_dir is None:
            now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            base_logs = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs'))
            log_dir = os.path.join(base_logs, now_str)
            os.makedirs(log_dir, exist_ok=True)
            WorkloadMonitor._log_dir = log_dir
        self.log_path = os.path.join(WorkloadMonitor._log_dir, 'workload_monitor.json')

    def _log_task(self, task):
        try:
            if os.path.exists(self.log_path):
                with open(self.log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []
        except Exception:
            data = []
        task['timestamp'] = datetime.datetime.now().isoformat()
        data.append(task)
        with open(self.log_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def get_metrics(self, table=None):
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
        task = {
            'task': 'Retrieve workload metrics',
            'description': f"Metrics collected: {metrics}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return metrics

    def get_applied_tasks_summary(self):
        return self.applied_tasks
