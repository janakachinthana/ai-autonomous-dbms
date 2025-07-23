import pyodbc
from src.intelligent_indexing.index_manager import IndexManager
from src.query_optimization.query_optimizer import QueryOptimizer
from src.security.anomaly_detector import AnomalyDetector
from src.self_tuning.workload_monitor import WorkloadMonitor
from src.self_tuning.parameter_tuner import ParameterTuner
from src.config import DB_CONNECTION_STRING
import subprocess
import os
import glob
import numpy as np

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

# Improved: Recommend indexes based on real query usage stats
# Only recommend/apply indexes for columns used in WHERE/JOIN/ORDER BY in recent queries

def get_frequently_used_columns(conn, min_usage=5):
    cursor = conn.cursor()
    # Improved: Only consider user-created tables in dbo schema
    cursor.execute("""
        SELECT t.name AS table_name, c.name AS column_name, COUNT(*) AS usage_count
        FROM sys.dm_exec_query_stats qs
        CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
        JOIN sys.tables t ON st.text LIKE '%' + t.name + '%'
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        JOIN sys.columns c ON st.text LIKE '%' + c.name + '%'
        WHERE s.name = 'dbo' AND t.is_ms_shipped = 0 AND t.type = 'U'
        GROUP BY t.name, c.name
        HAVING COUNT(*) >= ?
        ORDER BY usage_count DESC
    """, min_usage)
    return [(row[0], row[1]) for row in cursor.fetchall()]

# Auto-apply indexes for frequently used columns based on query stats
if __name__ == "__main__":
    def auto_apply_frequent_indexes():
        print("\n=== Auto-applying indexes for frequently used columns in user tables ===")
        print("\n=== Processing... ===")
        print("[DEBUG] Fetching frequently used columns...")
        used_columns = get_frequently_used_columns(conn, min_usage=1)  # Lower threshold for debug
        print(f"[DEBUG] Number of frequently used columns found: {len(used_columns)}")
        if not used_columns:
            print("[DEBUG] No frequently used columns found. Check your query stats or database activity.")
        for table, col in used_columns:
            print(f"[DEBUG] Processing: {table}.{col}")
            full_col = f"{table}.{col}"
            rec = index_manager.recommend_index(full_col)
            print(f"[Auto-Indexing] {full_col}: {rec}")
            if 'CREATE INDEX' in rec:
                result = index_manager.apply_index(full_col)
                print(f"[Auto-Indexing] {result}")
        print("=== Auto-indexing (frequent columns) complete ===\n")
    auto_apply_frequent_indexes()

# Gather all access counts for all columns
all_access_counts = []
per_table_access = {}
for schema, table in tables:
    cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=? AND TABLE_NAME=?", (schema, table))
    columns = [(row[0], row[1]) for row in cursor.fetchall()]
    per_table_access[table] = {}
    for col, data_type in columns:
        # Simulate or fetch real access count; here we use the access_count from IndexManager if available
        col_key = f"{table}.{col}"
        access_count = getattr(index_manager, 'access_count', {}).get(col_key, 0)
        per_table_access[table][col] = access_count
        all_access_counts.append(access_count)

# Compute 90th percentile threshold
if all_access_counts:
    percentile_90 = np.percentile(all_access_counts, 90)
else:
    percentile_90 = 0

for schema, table in tables:
    full_table = f"{schema}.{table}"
    print(f"\n=== Processing table: {full_table} ===")
    try:
        cursor.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA=? AND TABLE_NAME=?", (schema, table))
        columns = [(row[0], row[1]) for row in cursor.fetchall()]
        # Sort columns by access count descending
        table_access = per_table_access.get(table, {})
        sorted_columns = sorted(columns, key=lambda x: table_access.get(x[0], 0), reverse=True)
        # Get top 2 columns for this table
        top_n = set([col for col, _ in sorted_columns[:2]])
        for col, data_type in columns:
            access_count = table_access.get(col, 0)
            col_key = f"{table}.{col}"
            if not index_manager._is_suitable_type(data_type):
                print(f"[Indexing] Skipping column: {col} (unsuitable type: {data_type})")
                continue
            if index_manager._is_column_indexed(table, col):
                print(f"[Indexing] Skipping column: {col} (already indexed)")
                continue
            # Recommend if in top 10% globally or in top 2 for this table
            if access_count >= percentile_90 or col in top_n:
                print(f"[Indexing] Checking column: {col} (access_count={access_count})")
                rec = index_manager.recommend_index(f"{table}.{col}")
                print(f"[Indexing] Recommendation: {rec}")
                if 'CREATE INDEX' in rec:
                    result = index_manager.apply_index(f"{table}.{col}")
                    print(f"[Indexing] {result}")
            else:
                print(f"[Indexing] Skipping column: {col} (access_count={access_count} below threshold {percentile_90})")
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

# === Summary Report Generation ===
def print_summary_report(index_manager, query_optimizer, anomaly_detector, parameter_tuner, workload_monitor):
    import os
    import datetime
    import json
    # Create a new summary folder in logs with datetime prefix
    now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    summary_dir = os.path.join('logs', f'summary_{now_str}')
    os.makedirs(summary_dir, exist_ok=True)

    print("\n=== SUMMARY REPORT ===\n")
    # Collect all tasks from each component
    index_tasks = getattr(index_manager, 'applied_tasks', [])
    query_tasks = getattr(query_optimizer, 'applied_tasks', [])
    anomaly_tasks = getattr(anomaly_detector, 'applied_tasks', [])
    tuning_tasks = getattr(parameter_tuner, 'applied_tasks', [])
    workload_tasks = getattr(workload_monitor, 'applied_tasks', [])

    def extract_table_column(desc):
        import re
        match = re.search(r"([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)", desc)
        if match:
            return match.group(1), match.group(2)
        match = re.search(r"table ([A-Za-z0-9_]+)", desc)
        if match:
            return match.group(1), None
        return None, None

    def extract_applied_query(task):
        # Try to extract the actual query or action from the task description or add a new field if available
        desc = task.get('description', '')
        if 'CREATE INDEX' in desc:
            # Extract the CREATE INDEX statement
            import re
            match = re.search(r'(CREATE INDEX [^\n]+)', desc)
            if match:
                return match.group(1)
        # For other components, you can add logic to extract or include the query/action if available
        return task.get('applied_query', '')

    records = []
    for task in index_tasks:
        table, column = extract_table_column(task.get('description', ''))
        records.append({
            'component': 'Indexing',
            'table': table or '',
            'column': column or '',
            'issue': '',
            'recommendation': task.get('description', ''),
            'applied': task.get('task', ''),
            'applied_query': extract_applied_query(task)
        })
    for task in query_tasks:
        table, column = extract_table_column(task.get('description', ''))
        records.append({
            'component': 'Query Optimization',
            'table': table or '',
            'column': column or '',
            'issue': task.get('issue', ''),
            'recommendation': task.get('recommendation', task.get('description', '')),
            'applied': task.get('task', ''),
            'applied_query': extract_applied_query(task)
        })
    for task in anomaly_tasks:
        table, column = extract_table_column(task.get('description', ''))
        records.append({
            'component': 'Security/Anomaly',
            'table': table or '',
            'column': column or '',
            'issue': task.get('issue', ''),
            'recommendation': task.get('recommendation', task.get('description', '')),
            'applied': task.get('task', ''),
            'applied_query': extract_applied_query(task)
        })
    for task in tuning_tasks:
        table, column = extract_table_column(task.get('description', ''))
        records.append({
            'component': 'Self-Tuning',
            'table': table or '',
            'column': column or '',
            'issue': task.get('issue', ''),
            'recommendation': task.get('recommendation', task.get('description', '')),
            'applied': task.get('task', ''),
            'applied_query': extract_applied_query(task)
        })
    for task in workload_tasks:
        table, column = extract_table_column(task.get('description', ''))
        records.append({
            'component': 'Workload Monitor',
            'table': table or '',
            'column': column or '',
            'issue': task.get('issue', ''),
            'recommendation': task.get('recommendation', task.get('description', '')),
            'applied': task.get('task', ''),
            'applied_query': extract_applied_query(task)
        })
    records.sort(key=lambda r: (r['table'], r['component']))
    # Move records with a non-empty applied_query to the end
    non_applied = [rec for rec in records if not rec.get('applied_query')]
    applied = [rec for rec in records if rec.get('applied_query')]
    lines = []
    # Print non-applied records first
    for rec in non_applied:
        line = f"[Table: {rec['table']}] [Column: {rec['column']}] [Component: {rec['component']}]\n  Issue: {rec['issue']}\n  Recommendation: {rec['recommendation']}\n  Applied: {rec['applied']}\n  Applied Query: {rec['applied_query']}\n"
        print(line)
        lines.append(line)
    # Add section header for applied changes
    if applied:
        applied_header = "\n**********  APPLIED CHANGES  **********\n"
        print(applied_header)
        lines.append(applied_header)
        for rec in applied:
            line = f"[Table: {rec['table']}] [Column: {rec['column']}] [Component: {rec['component']}]\n  Issue: {rec['issue']}\n  Recommendation: {rec['recommendation']}\n  Applied: {rec['applied']}\n  Applied Query: {rec['applied_query']}\n"
            print(line)
            lines.append(line)
    print("=== END OF SUMMARY REPORT ===\n")
    lines.append("=== END OF SUMMARY REPORT ===\n")
    # Export to JSON
    with open(os.path.join(summary_dir, 'summary_report.json'), 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2)
    # Export to TXT
    with open(os.path.join(summary_dir, 'summary_report.txt'), 'w', encoding='utf-8') as f:
        f.writelines(lines)

# At the end, after running all main components and before running tests:
print_summary_report(index_manager, query_optimizer, anomaly_detector, parameter_tuner, workload_monitor)

# Run anomaly analysis at the end, placing report in the latest log folder
# run_anomaly_analysis()

# Run integration tests using pytest
print("\n=== Running integration tests with pytest ===")
try:
    import pytest
    import sys
    # Run pytest programmatically on the integration tests directory
    result = pytest.main(['tests/integration/'])
    if result == 0:
        print("All integration tests passed!\n")
    else:
        print(f"Some tests failed. pytest exit code: {result}\n")
except ImportError:
    print("pytest is not installed. Please install pytest to run integration tests automatically.\n")
except Exception as e:
    print(f"Error running integration tests: {e}\n")
