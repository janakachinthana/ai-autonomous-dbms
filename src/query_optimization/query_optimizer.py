import pyodbc
import sys
import os
import json
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class QueryOptimizer:
    """
    Predictive query optimization using real MS SQL connection.
    """
    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.applied_tasks = []  # Track applied tasks

    def _log_task(self, task):
        log_path = os.path.join(os.path.dirname(__file__), '../../logs/query_optimizer.json')
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

    def analyze_query(self, query):
        # Use SQL Server's query plan to extract features
        cursor = self.conn.cursor()
        try:
            # Basic validation: only allow SELECT queries and block dangerous keywords
            allowed = query.strip().upper().startswith("SELECT") and all(
                kw not in query.upper() for kw in [";--", "DROP", "DELETE", "INSERT", "UPDATE", "ALTER"]
            )
            if not allowed:
                raise ValueError("Only simple SELECT queries are allowed for analysis.")
            cursor.execute(f"SET SHOWPLAN_ALL ON; {query}; SET SHOWPLAN_ALL OFF;")
            plan = cursor.fetchall()
            # Example: extract some features from the plan (customize as needed)
            features = {
                'complexity': len(plan),
                'estimated_rows': sum(int(row[7]) for row in plan if row[7].isdigit()),
                'has_join': any('JOIN' in str(row) for row in plan)
            }
            task = {
                'task': 'Analyze query',
                'description': f"Query: {query}, Features: {features}"
            }
            self.applied_tasks.append(task)
            self._log_task(task)
            return features
        except Exception as e:
            task = {
                'task': 'Analyze query',
                'description': f"Query: {query}, Error: {e}"
            }
            self.applied_tasks.append(task)
            self._log_task(task)
            return {'complexity': 0, 'estimated_rows': 0, 'has_join': False, 'error': str(e)}

    def predict_plan(self, features):
        # Simulate ML-based plan selection
        if features.get('complexity', 0) > 7 or features.get('has_join', False):
            plan = 'Hash Join Plan'
        elif features.get('estimated_rows', 0) > 5000:
            plan = 'Index Scan Plan'
        else:
            plan = 'Sequential Scan Plan'
        task = {
            'task': 'Predict plan',
            'description': f"Features: {features}, Predicted Plan: {plan}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return plan

    def get_applied_tasks_summary(self):
        return self.applied_tasks
