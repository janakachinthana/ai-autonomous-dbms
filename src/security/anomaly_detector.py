import random
import json
import os
from datetime import datetime

class AnomalyDetector:
    """
    Simulates AI-based anomaly detection for security monitoring.
    """
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
        log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs/anomaly_detector.json'))
        try:
            if os.path.exists(log_path):
                with open(log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []
        except Exception:
            data = []
        data.append(log_record)
        with open(log_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        return result, message
