import os

from dotenv import load_dotenv

from core.settings.common import *

# Loading environment variable"s
load_dotenv()

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")

# REST-FRAMEWORK SERVER MODE
# ------------------------------------------------------------------------------
if not DEBUG:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
        "rest_framework.renderers.JSONRenderer",
    )

# HOST
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS] + [f"http://{host}" for host in ALLOWED_HOSTS]

# DATABASE
# ------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_DB", "roino"),
        "USER": os.environ.get("POSTGRES_USER", "root"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "root"),
        "HOST": os.environ.get("POSTGRES_HOST", "127.0.0.1"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# CORS
# ------------------------------------------------------------------------------
# TODO - change it when production ready!!!
CORS_ORIGIN_ALLOW_ALL = True
