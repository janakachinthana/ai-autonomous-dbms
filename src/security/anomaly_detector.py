import pyodbc
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class AnomalyDetector:
    """
    AI-based anomaly detection for security monitoring using real MS SQL logs.
    """
    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.applied_tasks = []  # Track applied tasks

    def detect(self, log_entry):
        # Example: Check for suspicious SQL commands in the log entry
        suspicious_keywords = ['DROP', 'DELETE', 'ALTER', 'UPDATE']
        if any(keyword in log_entry.upper() for keyword in suspicious_keywords):
            result = True
            message = "Potential anomaly detected!"
        else:
            result = False
            message = "No anomaly."
        self.applied_tasks.append({
            'task': 'Detect anomaly',
            'description': f"Log entry: {log_entry}, Result: {message}"
        })
        return result, message

    def get_applied_tasks_summary(self):
        return self.applied_tasks
