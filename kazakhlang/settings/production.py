from .base import *

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
