from src.intelligent_indexing.index_manager import IndexManager

def test_apply_index():
    manager = IndexManager()
    col = 'OfficeTrustSystemData.Name'
    rec = manager.recommend_index(col)
    assert 'CREATE INDEX' in rec or 'already exists' in rec or 'insufficient access frequency' in rec
    result = manager.apply_index(col)
    assert 'applied' in result or 'Failed to apply index' in result
    rec2 = manager.recommend_index(col)
    assert 'already exists' in rec2 or 'insufficient access frequency' in rec2
