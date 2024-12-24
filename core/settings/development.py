from core.settings.common import *


# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = "ll1*tq$z$%t7-$x@8*ow+*xn-av!swn!aux@)gs!c*jx=1&h64"

# DATABASES
# ------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# APPS
# ------------------------------------------------------------------------------
APPS = [
    "debug_toolbar"
]

INSTALLED_APPS += APPS

# MIDDLEWARE
# ------------------------------------------------------------------------------
insert_middleware(MIDDLEWARE, "debug_toolbar.middleware.DebugToolbarMiddleware", 2)

# DJANGO DEBUG
# ------------------------------------------------------------------------------
INTERNAL_IPS = [
    "127.0.0.1",
]
