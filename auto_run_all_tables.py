import pyodbc
from src.intelligent_indexing.index_manager import IndexManager
from src.query_optimization.query_optimizer import QueryOptimizer
from src.security.anomaly_detector import AnomalyDetector
from src.self_tuning.workload_monitor import WorkloadMonitor
from src.self_tuning.parameter_tuner import ParameterTuner
from src.config import DB_CONNECTION_STRING

# Connect to the database and get all user tables
conn = pyodbc.connect(DB_CONNECTION_STRING)
cursor = conn.cursor()
cursor.execute("SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
tables = cursor.fetchall()

print(f"Found {len(tables)} tables in the database.")

# Initialize modules
index_manager = IndexManager()
query_optimizer = QueryOptimizer()
anomaly_detector = AnomalyDetector()
workload_monitor = WorkloadMonitor()
parameter_tuner = ParameterTuner()

for schema, table in tables:
    full_table = f"{schema}.{table}"
    print(f"\n=== Processing table: {full_table} ===")
    # Intelligent Indexing: Simulate monitoring and recommending/applying index for each column
    try:
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=? AND TABLE_NAME=?", (schema, table))
        columns = [row[0] for row in cursor.fetchall()]
        for col in columns:
            print(f"[Indexing] Checking column: {col}")
            rec = index_manager.recommend_index(f"{table}.{col}")
            print(f"[Indexing] Recommendation: {rec}")
            if 'CREATE INDEX' in rec:
                result = index_manager.apply_index(f"{table}.{col}")
                print(f"[Indexing] {result}")
    except Exception as e:
        print(f"[Indexing] Error: {e}")

    # Query Optimization: Analyze a simple query for the table
    try:
        query = f"SELECT * FROM {full_table}"
        features = query_optimizer.analyze_query(query)
        plan = query_optimizer.predict_plan(features)
        print(f"[Query Optimization] Features: {features}")
        print(f"[Query Optimization] Predicted Plan: {plan}")
    except Exception as e:
        print(f"[Query Optimization] Error: {e}")

    # Security/Anomaly Detection: Simulate a log entry for the table
    try:
        log_entry = f"User accessed table {full_table}"
        is_anomaly, message = anomaly_detector.detect(log_entry)
        print(f"[Security] Log: {log_entry}\n[Security] Result: {message}")
    except Exception as e:
        print(f"[Security] Error: {e}")

    # Self-Tuning: Monitor and tune for the table (simulate)
    try:
        metrics = workload_monitor.get_metrics()
        print(f"[Self-Tuning] Metrics: {metrics}")
        new_params = parameter_tuner.tune(metrics)
        print(f"[Self-Tuning] Tuned Parameters: {new_params}")
    except Exception as e:
        print(f"[Self-Tuning] Error: {e}")

print("\n=== All tables processed. ===")
