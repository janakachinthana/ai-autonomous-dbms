import random
import pyodbc
import sys
import os
import json
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class IndexManager:
    """
    Intelligent index management using real MS SQL connection.
    """
    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.indexes = self._fetch_existing_indexes()
        self.applied_tasks = []  # Track applied tasks

    def _fetch_existing_indexes(self):
        indexes = set()
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sys.indexes WHERE object_id > 100")
        for row in cursor.fetchall():
            indexes.add(row[0])
        return indexes

    def _log_task(self, task):
        log_path = os.path.join(os.path.dirname(__file__), '../../logs/index_manager.json')
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

    def monitor_access(self):
        # Example: randomly select a column from real tables (customize as needed)
        columns = ['users.age', 'orders.date', 'logs.timestamp']
        column = random.choice(columns)
        task = {
            'task': 'Monitor access',
            'description': f"Monitored column: {column}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return column

    def recommend_index(self, column):
        # Recommend index if not exists (simulate ML logic)
        index_name = f"idx_{column.replace('.', '_')}"
        if index_name not in self.indexes:
            recommendation = f"CREATE INDEX {index_name} ON {column.split('.')[0]}({column.split('.')[1]})"
        else:
            recommendation = f"Index on {column} already exists"
        task = {
            'task': 'Recommend index',
            'description': f"Column: {column}, Recommendation: {recommendation}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return recommendation

    def apply_index(self, column):
        index_name = f"idx_{column.replace('.', '_')}"
        table, col = column.split('.')
        cursor = self.conn.cursor()
        try:
            cursor.execute(f"CREATE INDEX {index_name} ON {table}({col})")
            self.conn.commit()
            self.indexes.add(index_name)
            result = f"Index on {column} applied"
        except Exception as e:
            result = f"Failed to apply index: {e}"
        task = {
            'task': 'Apply index',
            'description': f"Column: {column}, Result: {result}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return result

    def get_applied_tasks_summary(self):
        return self.applied_tasks
