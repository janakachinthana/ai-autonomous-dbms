from datetime import datetime
from src.intelligent_indexing.index_manager import IndexManager
from src.query_optimization.query_optimizer import QueryOptimizer
from src.security.anomaly_detector import AnomalyDetector
from src.self_tuning.workload_monitor import WorkloadMonitor
from src.self_tuning.parameter_tuner import ParameterTuner

summary_lines = []
summary_lines.append(f"ADBMS Module Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
summary_lines.append("")

# IndexManager
manager = IndexManager()
summary_lines.append("[Intelligent Indexing Module]")
summary_lines.append(str(manager.get_applied_tasks_summary()))
summary_lines.append("")

# QueryOptimizer
optimizer = QueryOptimizer()
summary_lines.append("[Predictive Query Optimizer]")
summary_lines.append(str(optimizer.get_applied_tasks_summary()))
summary_lines.append("")

# AnomalyDetector
anomaly = AnomalyDetector()
summary_lines.append("[Security & Compliance Layer]")
summary_lines.append(str(anomaly.get_applied_tasks_summary()))
summary_lines.append("")

# WorkloadMonitor
monitor = WorkloadMonitor()
summary_lines.append("[Workload Monitor]")
summary_lines.append(str(monitor.get_applied_tasks_summary()))
summary_lines.append("")

# ParameterTuner
param_tuner = ParameterTuner()
summary_lines.append("[Parameter Tuner]")
summary_lines.append(str(param_tuner.get_applied_tasks_summary()))
summary_lines.append("")

filename = datetime.now().strftime('%Y%m%d_%H%M%S') + '.txt'
filepath = f'docs/summary/{filename}'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write('\n'.join(summary_lines))

print(f"Summary written to {filepath}")
