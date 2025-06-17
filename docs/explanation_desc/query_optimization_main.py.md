# main.py (query_optimization) - Line-by-line Explanation

1. `# Predictive Query Optimizer Entry Point`
   - A comment describing the file as the entry point for the query optimization module.
2. `from query_optimizer import QueryOptimizer`
   - Imports the `QueryOptimizer` class from the local `query_optimizer.py` file.

4-17. `def main(): ...`
   - Defines the main function that runs the predictive query optimizer workflow.
5. `print("Starting Predictive Query Optimizer...")`
   - Prints a message indicating the module is starting.
6. `optimizer = QueryOptimizer()`
   - Instantiates the `QueryOptimizer` class.
7-10. `sample_queries = [...]`
   - Defines a list of sample SQL queries to be analyzed and optimized.
11-15. `for query in sample_queries: ...`
   - Loops through each sample query.
12. `features = optimizer.analyze_query(query)`
   - Analyzes the query and extracts features using the optimizer.
13. `plan = optimizer.predict_plan(features)`
   - Predicts the optimal execution plan for the query.
14. `print(f"Query: {query}\nFeatures: {features}\nPredicted Plan: {plan}\n")`
   - Prints the query, its features, and the predicted plan.

17-18. `if __name__ == "__main__": ...`
   - If the script is run directly, calls the `main()` function to start the workflow.
