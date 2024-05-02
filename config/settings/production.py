from .base import *  # noqa

# TODO: as soon as the project goes to production fix allowed hosts
SERVER_IP = os.environ.get("SERVER_IP")
ALLOWED_HOSTS = ["*"]
DEBUG = True
