from pathlib import Path
from multiprocessing import cpu_count
from os import environ


def max_workers():
    return (2 * cpu_count()) + 1


TIMEOUT = 90
bind = '0.0.0.0:' + environ.get('PORT', '8000')
max_requests = 1000
worker_class = 'gevent'
workers = max_workers()

env = {
    'DJANGO_SETTINGS_MODULE': 'config.settings'
}

reload = True
name = 'config'
