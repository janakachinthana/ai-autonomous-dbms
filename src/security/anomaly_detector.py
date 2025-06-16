import random

class AnomalyDetector:
    """
    Simulates AI-based anomaly detection for security monitoring.
    """
    def detect(self, log_entry):
        # Simulate anomaly detection with random chance
        if 'DROP' in log_entry or random.random() < 0.1:
            return True, "Potential anomaly detected!"
        return False, "No anomaly."
