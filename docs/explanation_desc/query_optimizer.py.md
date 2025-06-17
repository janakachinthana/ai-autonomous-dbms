# query_optimizer.py - Line-by-line Explanation

1. `import pyodbc`
   - Imports the `pyodbc` module for database connectivity.
2. `import sys`
   - Imports the `sys` module for manipulating the Python path.
3. `import os`
   - Imports the `os` module for path operations.
4. `sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))`
   - Adds the parent directory to the Python path so `config` can be imported.
5. `from config import DB_CONNECTION_STRING`
   - Imports the database connection string from the config file.

7-60. `class QueryOptimizer:` ...
   - Defines the `QueryOptimizer` class for analyzing queries and predicting plans.

10-13. `def __init__(self): ...`
   - Initializes the class, connects to the database, and sets up a list to track actions.

15-44. `def analyze_query(self, query): ...`
   - Analyzes a SQL query, validates it, extracts features from the query plan, logs the action, and returns the features. Handles errors and logs them as well.

46-56. `def predict_plan(self, features): ...`
   - Predicts the optimal query plan based on extracted features, logs the prediction, and returns the plan type.

58-59. `def get_applied_tasks_summary(self): ...`
   - Returns the list of all actions performed (for auditing/reporting).
