# index_manager.py - Line-by-line Explanation

1. `import random`
   - Imports the `random` module for random selection of columns.
2. `import pyodbc`
   - Imports the `pyodbc` module for connecting to SQL Server databases.
3. `import sys`
   - Imports the `sys` module for manipulating the Python path.
4. `import os`
   - Imports the `os` module for path operations.
5. `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`
   - Adds the parent directory to the Python path so `config` can be imported.
6. `from config import DB_CONNECTION_STRING`
   - Imports the database connection string from the config file.

8-67. `class IndexManager:` ...
   - Defines the `IndexManager` class for managing indexes in the database.

10-13. `def __init__(self): ...`
   - Initializes the class, connects to the database, fetches existing indexes, and sets up a list to track actions.

14-20. `def _fetch_existing_indexes(self): ...`
   - Fetches all existing index names from the database and returns them as a set.

22-30. `def monitor_access(self): ...`
   - Randomly selects a column to simulate access, logs the action, and returns the column name.

32-41. `def recommend_index(self, column): ...`
   - Recommends an index for a column if it doesn't already exist, logs the recommendation, and returns the recommendation string.

43-58. `def apply_index(self, column): ...`
   - Attempts to create an index on the specified column, logs the result, and returns a message indicating success or failure.

60-62. `def get_applied_tasks_summary(self): ...`
   - Returns the list of all actions performed (for auditing/reporting).
