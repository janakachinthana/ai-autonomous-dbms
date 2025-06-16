from src.self_tuning.parameter_tuner import ParameterTuner

def test_tuner_increases_buffer():
    tuner = ParameterTuner()
    metrics = {'cpu_usage': 20, 'memory_usage': 2000, 'cache_hit_ratio': 0.9, 'query_throughput': 500}
    old_size = tuner.parameters['buffer_size']
    new_params = tuner.tune(metrics)
    assert new_params['buffer_size'] > old_size

def test_tuner_decreases_buffer():
    tuner = ParameterTuner()
    metrics = {'cpu_usage': 90, 'memory_usage': 7500, 'cache_hit_ratio': 0.9, 'query_throughput': 500}
    old_size = tuner.parameters['buffer_size']
    new_params = tuner.tune(metrics)
    assert new_params['buffer_size'] < old_size
