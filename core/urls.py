import os

from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import re_path, path, include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import debug_toolbar
from dotenv import load_dotenv

from apps.account.api.v1.views.user_logout_view import LogoutView
from apps.account.api.v1.views.user_register_view import RegisterUserView

from utils.docs.api.yasg_doc import schema_view


# Loading environment variable"s
load_dotenv()

# information panel
admin.site.index_title = "Roino"
admin.site.site_title = "Admin Panel"
admin.site.site_header = "Roino Admin Panel"

if settings.DEBUG: 
    ADMIN_URL_PREFIX = os.environ.setdefault("ADMIN_URL_PREFIX", "real-admin")
else:
    ADMIN_URL_PREFIX = os.environ.get("ADMIN_URL_PREFIX")

api_v1_urls = [
    # docs
    path("docs/schema/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("docs/schema/swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("docs/schema/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),

    # authentication
    path("account/auth/token/login/", TokenObtainPairView.as_view(), name="login"),
    path("account/auth/token/register/", RegisterUserView.as_view(), name="register"),
    path("account/auth/token/refresh/", TokenRefreshView.as_view(), name="refresh-token"),

    # account app
    path("account/", include("apps.account.api.v1.urls")),

    # blog app
    path("blog/", include("apps.blog.api.v1.urls")),
]

urlpatterns = [
    # Admin paths
    path(f"{ADMIN_URL_PREFIX}/", admin.site.urls),
    path(f"{ADMIN_URL_PREFIX}/logout/", LogoutView.as_view(), name="logout-admin"),
    path("admin/", include("admin_honeypot.urls")),

    # Favicon
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("img/favicon.ico"))),

    # Tinymce Editor
    path("tinymce/", include("tinymce.urls")),
    
    # API v1 paths
    path("api/v1/", include((api_v1_urls, "api_v1"))),
]

# Static and Media
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  Media static
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

# Debug Toolbar
if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
