# Predictive Query Optimizer Entry Point
from query_optimizer import QueryOptimizer

def main():
    print("Starting Predictive Query Optimizer...")
    optimizer = QueryOptimizer()
    sample_queries = [
        "SELECT * FROM users WHERE age > 30;",
        "SELECT orders.id, users.name FROM orders JOIN users ON orders.user_id = users.id;",
        "SELECT COUNT(*) FROM logs;"
    ]
    for query in sample_queries:
        features = optimizer.analyze_query(query)
        plan = optimizer.predict_plan(features)
        print(f"Query: {query}\nFeatures: {features}\nPredicted Plan: {plan}\n")

if __name__ == "__main__":
    main()
