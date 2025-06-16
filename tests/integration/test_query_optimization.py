from src.query_optimization.query_optimizer import QueryOptimizer

def test_predict_plan_hash_join():
    optimizer = QueryOptimizer()
    features = {'complexity': 9, 'estimated_rows': 1000, 'has_join': True}
    plan = optimizer.predict_plan(features)
    assert plan == 'Hash Join Plan'

def test_predict_plan_index_scan():
    optimizer = QueryOptimizer()
    features = {'complexity': 3, 'estimated_rows': 9000, 'has_join': False}
    plan = optimizer.predict_plan(features)
    assert plan == 'Index Scan Plan'
