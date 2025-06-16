from src.intelligent_indexing.index_manager import IndexManager

def test_apply_index():
    manager = IndexManager()
    col = 'users.age'
    rec = manager.recommend_index(col)
    assert 'CREATE INDEX' in rec
    result = manager.apply_index(col)
    assert 'applied' in result
    rec2 = manager.recommend_index(col)
    assert 'already exists' in rec2
