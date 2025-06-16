import random

class IndexManager:
    """
    Simulates intelligent index management using mock ML logic.
    """
    def __init__(self):
        self.indexes = set()

    def monitor_access(self):
        # Simulate access patterns
        return random.choice(['users.age', 'orders.date', 'logs.timestamp'])

    def recommend_index(self, column):
        # Simulate ML-based recommendation
        if column not in self.indexes:
            return f"CREATE INDEX ON {column}"
        else:
            return f"Index on {column} already exists"

    def apply_index(self, column):
        self.indexes.add(column)
        return f"Index on {column} applied"
