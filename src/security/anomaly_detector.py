import pyodbc
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class AnomalyDetector:
    """
    AI-based anomaly detection for security monitoring using real MS SQL logs.
    """
    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.applied_tasks = []  # Track applied tasks

    def _log_task(self, task):
        log_path = os.path.join(os.path.dirname(__file__), '../../logs/anomaly_detector.json')
        log_path = os.path.abspath(log_path)
        try:
            if os.path.exists(log_path):
                with open(log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []
        except Exception:
            data = []
        data.append(task)
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def detect(self, log_entry):
        # Example: Check for suspicious SQL commands in the log entry
        suspicious_keywords = ['DROP', 'DELETE', 'ALTER', 'UPDATE']
        if any(keyword in log_entry.upper() for keyword in suspicious_keywords):
            result = True
            message = "Potential anomaly detected!"
        else:
            result = False
            message = "No anomaly."
        task = {
            'task': 'Detect anomaly',
            'description': f"Log entry: {log_entry}, Result: {message}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return result, message

    def get_applied_tasks_summary(self):
        return self.applied_tasks
