from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.account.api.v1.views.user_register_view import RegisterUserView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh-token"),
]
