import os

DATABASE_HOSTNAME = os.environ.get('DB_HOSTNAME') if os.environ.get('DB_HOSTNAME') else 'localhost'
