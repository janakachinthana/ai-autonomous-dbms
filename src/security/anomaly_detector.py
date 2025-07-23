import random
import json
import os
from datetime import datetime

class AnomalyDetector:
    """
    Simulates AI-based anomaly detection for security monitoring.
    """
    _log_dir = None

    def __init__(self):
        if AnomalyDetector._log_dir is None:
            now_str = datetime.now().strftime('%Y%m%d_%H%M%S')
            base_logs = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs'))
            log_dir = os.path.join(base_logs, now_str)
            os.makedirs(log_dir, exist_ok=True)
            AnomalyDetector._log_dir = log_dir
        self.log_path = os.path.join(AnomalyDetector._log_dir, 'anomaly_detector.json')
        self.applied_tasks = []

    def detect(self, log_entry, force_result=None):
        # Simulate anomaly detection with random chance, but always flag dangerous actions
        if force_result is not None:
            is_anomaly = force_result
        elif 'DROP' in log_entry.upper():
            is_anomaly = True
        else:
            import random
            is_anomaly = random.random() < 0.1  # 10% chance of anomaly
        message = "Potential anomaly detected!" if is_anomaly else "No anomaly."
        task = {
            'task': 'Detect anomaly',
            'description': f"Log entry: {log_entry}, Result: {message}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return is_anomaly, message

    def _log_task(self, task):
        import os, json, datetime
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
