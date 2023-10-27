import os

REDIS_HOSTNAME = os.environ.get('REDIS_HOSTNAME') if os.environ.get('REDIS_HOSTNAME') else 'localhost'