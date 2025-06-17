import pyodbc
from src.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_DRIVER

class AnomalyDetector:
    """
    AI-based anomaly detection for security monitoring using real MS SQL logs.
    """
    def __init__(self):
        self.conn = pyodbc.connect(
            f"DRIVER={{{DB_DRIVER}}};SERVER={DB_HOST},{DB_PORT};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}")
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
