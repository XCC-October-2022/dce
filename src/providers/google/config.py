import os

CONTROL_PLANE_HOSTNAME = os.environ.get('CP_HOSTNAME') if os.environ.get('CP_HOSTNAME') else 'localhost'
BACKEND_HOSTNAME = os.environ.get('BE_HOSTNAME') if os.environ.get('BE_HOSTNAME') else 'localhost'