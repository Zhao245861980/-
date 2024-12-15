_redis_url = 'redis://127.0.0.1:6379/0'

broker_url = _redis_url
broker_pool_limit = 1000

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'
result_expires = 3600

result_backend = _redis_url
result_serializer = 'pickle'
result_cache_max = 10000

worker_redirect_stdouts_level = 'INFO'
