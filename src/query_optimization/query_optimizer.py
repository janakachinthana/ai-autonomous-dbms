import pyodbc
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_DRIVER

class QueryOptimizer:
    """
    Predictive query optimization using real MS SQL connection.
    """
    def __init__(self):
        self.conn = pyodbc.connect(
            f"DRIVER={{{DB_DRIVER}}};SERVER={DB_HOST},{DB_PORT};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}")
        self.applied_tasks = []  # Track applied tasks

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
            self.applied_tasks.append({
                'task': 'Analyze query',
                'description': f"Query: {query}, Features: {features}"
            })
            return features
        except Exception as e:
            self.applied_tasks.append({
                'task': 'Analyze query',
                'description': f"Query: {query}, Error: {e}"
            })
            return {'complexity': 0, 'estimated_rows': 0, 'has_join': False, 'error': str(e)}

    def predict_plan(self, features):
        # Simulate ML-based plan selection
        if features.get('complexity', 0) > 7 or features.get('has_join', False):
            plan = 'Hash Join Plan'
        elif features.get('estimated_rows', 0) > 5000:
            plan = 'Index Scan Plan'
        else:
            plan = 'Sequential Scan Plan'
        self.applied_tasks.append({
            'task': 'Predict plan',
            'description': f"Features: {features}, Predicted Plan: {plan}"
        })
        return plan

    def get_applied_tasks_summary(self):
        return self.applied_tasks
