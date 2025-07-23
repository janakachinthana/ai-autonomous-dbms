from src.security.anomaly_detector import AnomalyDetector

def test_detect_anomaly():
    detector = AnomalyDetector()
    log = "User guest attempted DROP TABLE users;"
    is_anomaly, message = detector.detect(log)
    assert is_anomaly
    assert "anomaly" in message.lower()

def test_no_anomaly():
    detector = AnomalyDetector()
    log = "User admin logged in."
    is_anomaly, message = detector.detect(log, force_result=False)
    assert not is_anomaly
    assert "no anomaly" in message.lower()
