import os
from datetime import timedelta
from pathlib import Path

from django.contrib import messages
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# APPS
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    "jazzmin",
    # Admin Panel
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "axes",
    "taggit",
    "storages",
    "drf_yasg",
    "csvexport",
    "markdownx",
    "corsheaders",
    "import_export",
    "rest_framework",
    "django_filters",
    "djcelery_email",
    "admin_honeypot",
    "multiselectfield",
    "django_extensions",
    "phonenumber_field",
    "django_celery_beat",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
]

LOCAL_APPS = [
    "apps.account.apps.AccountConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARES
# ------------------------------------------------------------------------------
BASE_MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Third-Party Middleware
    "axes.middleware.AxesMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_session_timeout.middleware.SessionTimeoutMiddleware",
]

def insert_middleware(middleware_list, middleware_to_add, position):
    middleware_list.insert(position, middleware_to_add)
    return middleware_list

MIDDLEWARE = BASE_MIDDLEWARE.copy()

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# PASSWORD HASHES
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# ACCOUNT CONFIGURATIONS
# ------------------------------------------------------------------------------
AUTH_USER_MODEL = "custom_account.User"
SITE_ID = 1

# REDIS CONFIGURATIONS
# ------------------------------------------------------------------------------
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_URL_BROKER = os.environ.get("REDIS_DB", "0")
REDIS_RESULT_BACKEND = os.environ.get("REDIS_DB", "1")

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_URL_BROKER}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# SESSION CONFIGURATIONS
# ------------------------------------------------------------------------------
SESSION_EXPIRE_SECONDS = 3600  # 1 hour
SESSION_COOKIE_AGE = 3600 # 1 hour
SESSION_TIMEOUT_REDIRECT = "/"
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_SECONDS = 604800  # 1 week -> Expire

# DATABASES
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    # Authentication With JWT
    "allauth.account.auth_backends.AuthenticationBackend",

    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesStandaloneBackend",

    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_NO_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

# GENERAL
# ------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True
LOCALE_PATH = [BASE_DIR / "locale"]
LANGUAGES = (
    ("en", _("English")),
    ("fa", _("Persian")),
)

# STATIC
# ------------------------------------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# REST-FRAMEWORK CONFIGURATIONS
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # Enable Authentication by JWT
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": {
        "rest_framework.permission.IsAuthenticated"
    },
    "DEFAULT_THROTTLE_RATES": {
        "anon": "5/day",
        "user": "5/day"
    },
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# SIMPLE JWT CONFIGURATIONS
# ------------------------------------------------------------------------------
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    # token expiry date --> for example after 2 hour
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": True,
    "SIGNING_KEY": os.environ.get("SIGNING_KEY"),
    "ALGORITHM": "HS512", # TODO Use Asymmetric key
    "VERIFYING_KEY": None,
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": (
        "rest_framework_simplejwt.tokens.AccessToken",
    ),
    "TOKEN_TYPE_CLAIM": "token_type",
}

# REST_AUTH CONFIGURATIONS
# ------------------------------------------------------------------------------
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_TOKEN": "authors-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "authors-refresh-token",
    "REGISTER_SERIALIZER": "apps.account.api.v1.serializers.user_serializer.UserSerializer",
}

# CSV EXPORT CONFIGURATIONS
# ------------------------------------------------------------------------------
CSV_EXPORT_SETTINGS = {
    "encoding": "utf-8",
    "delimiter": ",",
    "quotechar": "'",
    "quoting": True,
}

# AXES CONFIGURATIONS
# ------------------------------------------------------------------------------
AXES_FAILURE_LIMIT = 5
AXES_RESET_ON_SUCCESS = True
AXES_COOLOFF_TIME = timedelta(seconds=10)
AXES_LOCKOUT_TEMPLATE = "account/locked.html"

# PROJECT ADMIN EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_VERIFICATION_URL_TIMEOUT = 60 * 3  # seconds
EMAIL_USE_SSL = True
SITE_NAME = "medium-api"

# MESSAGE TAGS
# ------------------------------------------------------------------------------
MESSAGE_TAGS = {
    messages.DEBUG: "debug",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "danger",
}

# LOGS MANAGEMENT
# ------------------------------------------------------------------------------
LOG_DIR = os.path.join(BASE_DIR, "tmp", "logs")

# Check if the log directory exists, and create it if not
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file_debug": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "debug.log"),
        },
        "file_info": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "info.log"),
        },
        "file_warning": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "warning.log"),
        },
        "file_error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "error.log"),
        },
        "file_critical": {
            "level": "CRITICAL",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "critical.log"),
        },
    },
    "loggers": {
        "": {
            "handlers": ["file_debug", "file_info", "file_warning", "file_error", "file_critical"],
            "level": "INFO",
            "propagate": True,
        },
    },
}


# JAZZMIN CONFIGURATIONS
# ------------------------------------------------------------------------------
JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": None,

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Roino",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Roino",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-square",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Hi There, Welcome Back",

    # Copyright on the footer
    "copyright": "Roino",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string 
    "search_model": ["auth.User", "auth.Group"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "managment",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "support", "url": "", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "support", "url": "", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "style/main_admin.css",
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-teal",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "simplex",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-dark",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}
