import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
timeout = 120
bind = "0.0.0.0:10000"
worker_class = "sync"
worker_connections = 1000
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Reduce memory usage
max_requests = 1000
max_requests_jitter = 50 