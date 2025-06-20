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

    def detect(self, log_entry):
        # Simulate anomaly detection with random chance
        if 'DROP' in log_entry or random.random() < 0.1:
            result = True
            message = "Potential anomaly detected!"
        else:
            result = False
            message = "No anomaly."
        # Log the detection with timestamp
        log_record = {
            "task": "Detect anomaly",
            "description": f"Log entry: {log_entry}, Result: {message}",
            "timestamp": datetime.now().isoformat()
        }
        try:
            if os.path.exists(self.log_path):
                with open(self.log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []
        except Exception:
            data = []
        data.append(log_record)
        with open(self.log_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return result, message
