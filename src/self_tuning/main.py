# Self-Tuning Engine Entry Point
from workload_monitor import WorkloadMonitor
from parameter_tuner import ParameterTuner
import time

def main():
    print("Starting Self-Tuning Engine...")
    monitor = WorkloadMonitor()
    tuner = ParameterTuner()
    for _ in range(5):  # Simulate 5 monitoring cycles
        metrics = monitor.get_metrics()
        print(f"[Metrics] {metrics}")
        new_params = tuner.tune(metrics)
        print(f"[Tuned Parameters] {new_params}\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
