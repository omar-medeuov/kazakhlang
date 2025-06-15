import os

from django.conf.global_settings import SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE

from .base import *




DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS= os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")

CSRF_COOKIE_SECURE=True

SECURE_HSTS_SECONDS = 2592000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE=True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # ManifestStaticFilesStorage is recommended in production, to prevent
    # outdated JavaScript / CSS assets being served from cache
    # (e.g. after a Wagtail upgrade).
    # See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

try:
    from .local import *
except ImportError:
    pass
