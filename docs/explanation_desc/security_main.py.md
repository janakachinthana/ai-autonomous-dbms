# main.py (security) - Line-by-line Explanation

1. `# Security & Compliance Layer Entry Point`
   - A comment describing the file as the entry point for the security module.
2. `from anomaly_detector import AnomalyDetector`
   - Imports the `AnomalyDetector` class from the local `anomaly_detector.py` file.

4-16. `def main(): ...`
   - Defines the main function that runs the security and compliance workflow.
5. `print("Starting Security & Compliance Layer...")`
   - Prints a message indicating the module is starting.
6. `detector = AnomalyDetector()`
   - Instantiates the `AnomalyDetector` class.
7-10. `logs = [...]`
   - Defines a list of sample log entries to be checked for anomalies.
11-13. `for log in logs: ...`
   - Loops through each log entry.
12. `is_anomaly, message = detector.detect(log)`
   - Checks if the log entry is anomalous using the detector.
13. `print(f"Log: {log}\nResult: {message}\n")`
   - Prints the log entry and the result of the anomaly check.

15-16. `if __name__ == "__main__": ...`
   - If the script is run directly, calls the `main()` function to start the workflow.
