import random
import pyodbc
import sys
import os
import json
import datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import DB_CONNECTION_STRING

class IndexManager:
    """
    Intelligent index management using real MS SQL connection.
    """
    _log_dir = None

    def __init__(self):
        self.conn = pyodbc.connect(DB_CONNECTION_STRING)
        self.indexes = self._fetch_existing_indexes()
        self.applied_tasks = []  # Track applied tasks
        if IndexManager._log_dir is None:
            now_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            base_logs = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs'))
            log_dir = os.path.join(base_logs, now_str)
            os.makedirs(log_dir, exist_ok=True)
            IndexManager._log_dir = log_dir
        self.log_path = os.path.join(IndexManager._log_dir, 'index_manager.json')

    def _fetch_existing_indexes(self):
        indexes = set()
        cursor = self.conn.cursor()
        # Only fetch indexes for user tables in dbo schema (exclude system tables)
        cursor.execute("""
            SELECT i.name
            FROM sys.indexes i
            JOIN sys.tables t ON i.object_id = t.object_id
            JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE t.is_ms_shipped = 0 AND t.type = 'U' AND s.name = 'dbo'
        """)
        for row in cursor.fetchall():
            indexes.add(row[0])
        return indexes

    def _log_task(self, task):
        try:
            if os.path.exists(self.log_path):
                with open(self.log_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = []
        except Exception:
            data = []
        task['timestamp'] = datetime.datetime.now().isoformat()
        data.append(task)
        with open(self.log_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def get_user_tables(self):
        # Fetch only user-created tables in the dbo schema in the current database
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT t.name
            FROM sys.tables t
            JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE t.is_ms_shipped = 0 AND t.type = 'U' AND s.name = 'dbo'
        """)
        return [row[0] for row in cursor.fetchall()]

    def monitor_access(self):
        # Only monitor columns from user tables in dbo schema
        user_tables = self.get_user_tables()
        columns = []
        cursor = self.conn.cursor()
        for table in user_tables:
            cursor.execute("""
                SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = ? AND TABLE_SCHEMA = 'dbo'""", table)
            for row in cursor.fetchall():
                columns.append(f"{table}.{row[0]}")
        if not columns:
            return None
        column = random.choice(columns)
        task = {
            'task': 'Monitor access',
            'description': f"Monitored column: {column}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return column

    def _fetch_indexed_columns(self):
        # Returns a set of (table, column) tuples that are already indexed
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT t.name AS table_name, c.name AS column_name
            FROM sys.index_columns ic
            JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
            JOIN sys.tables t ON c.object_id = t.object_id
            JOIN sys.schemas s ON t.schema_id = s.schema_id
            WHERE t.is_ms_shipped = 0 AND t.type = 'U' AND s.name = 'dbo'
        ''')
        return set((row[0], row[1]) for row in cursor.fetchall())

    def _get_column_data_type(self, table, column):
        cursor = self.conn.cursor()
        print(f"[DEBUG] Querying data type for: table={table}, column={column}")
        cursor.execute('''
            SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = ? AND COLUMN_NAME = ?
        ''', (table, column))
        row = cursor.fetchone()
        print(f"[DEBUG] Data type result for {table}.{column}: {row[0] if row else None}")
        return row[0] if row else None

    def _is_column_indexed(self, table, column):
        if not hasattr(self, '_indexed_columns'):
            self._indexed_columns = self._fetch_indexed_columns()
        return (table, column) in self._indexed_columns

    def _is_suitable_type(self, data_type):
        # Exclude types that are not suitable for indexing
        unsuitable = {'text', 'ntext', 'image', 'xml', 'geography', 'geometry', 'hierarchyid', 'sql_variant'}
        return data_type is not None and data_type.lower() not in unsuitable

    def recommend_index(self, column):
        # Only recommend index if column is frequently accessed, not already indexed, and of suitable type
        if not hasattr(self, 'access_count'):
            self.access_count = {}
        self.access_count[column] = self.access_count.get(column, 0) + 1
        table, col = column.split('.')
        data_type = self._get_column_data_type(table, col)
        already_indexed = self._is_column_indexed(table, col)
        suitable_type = self._is_suitable_type(data_type)
        index_name = f"idx_{table}_{col}"
        if not suitable_type:
            recommendation = f"No index recommended for {column} (unsuitable data type: {data_type})"
        elif already_indexed:
            recommendation = f"Index on {column} already exists"
        elif self.access_count[column] > 3:
            recommendation = f"CREATE INDEX {index_name} ON {table}({col})"
        else:
            recommendation = f"No index recommended for {column} (insufficient access frequency)"
        task = {
            'task': 'Recommend index',
            'description': f"Column: {column}, Recommendation: {recommendation}"
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return recommendation

    def apply_index(self, column):
        index_name = f"idx_{column.replace('.', '_')}"
        table, col = column.split('.')
        cursor = self.conn.cursor()
        query = f"CREATE INDEX {index_name} ON {table}({col})"
        try:
            cursor.execute(query)
            self.conn.commit()
            self.indexes.add(index_name)
            result = f"Index on {column} applied"
        except Exception as e:
            result = f"Failed to apply index: {e}"
        task = {
            'task': 'Apply index',
            'description': f"Column: {column}, Result: {result}",
            'applied_query': query
        }
        self.applied_tasks.append(task)
        self._log_task(task)
        return result

    def get_applied_tasks_summary(self):
        return self.applied_tasks
