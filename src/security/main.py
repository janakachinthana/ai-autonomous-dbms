# Security & Compliance Layer Entry Point
from anomaly_detector import AnomalyDetector

def main():
    print("Starting Security & Compliance Layer...")
    detector = AnomalyDetector()
    logs = [
        "User admin logged in.",
        "User guest attempted DROP TABLE users;",
        "User analyst ran SELECT * FROM sales;"
    ]
    for log in logs:
        is_anomaly, message = detector.detect(log)
        print(f"Log: {log}\nResult: {message}\n")

if __name__ == "__main__":
    main()
