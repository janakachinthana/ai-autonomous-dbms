import pyodbc
import sys
import os
import json
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class ParameterTuner:
    """
    Dynamic adjustment of database parameters based on metrics, using real MS SQL connection.
    """
    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.parameters = {
            'buffer_size': 1024,  # MB
            'cache_policy': 'LRU',
        }
        self.applied_tasks = []  # Track applied tasks

    def _log_task(self, task):
        log_path = os.path.join(os.path.dirname(__file__), '../../logs/parameter_tuner.json')
        log_path = os.path.abspath(log_path)
        try:
            if os.path.exists(log_path):
                with open(log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []
        except Exception:
            data = []
        task['timestamp'] = datetime.datetime.now().isoformat()
        data.append(task)
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def tune(self, metrics):
        # Example: Adjust buffer size based on CPU and memory usage
        old_params = self.parameters.copy()
        if metrics['cpu_usage'] > 80 or metrics['memory_usage'] > 7000:
            self.parameters['buffer_size'] = max(512, self.parameters['buffer_size'] - 128)
        elif metrics['cpu_usage'] < 30 and metrics['memory_usage'] < 4000:
            self.parameters['buffer_size'] = min(4096, self.parameters['buffer_size'] + 128)
        # Example: Change cache policy if cache hit ratio is low
        if metrics['cache_hit_ratio'] < 0.8:
            self.parameters['cache_policy'] = 'LFU'
        else:
            self.parameters['cache_policy'] = 'LRU'
        # Optionally, apply tuning to the real database (customize as needed)
        # cursor = self.conn.cursor()
        # cursor.execute("ALTER DATABASE CURRENT SET ...")
        # self.conn.commit()
        # Log the tuning as a task
        task = {
            'task': 'Tune database parameters',
            'description': f"Old: {old_params}, New: {self.parameters}, Metrics: {metrics}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return self.parameters

    def get_applied_tasks_summary(self):
        return self.applied_tasks
