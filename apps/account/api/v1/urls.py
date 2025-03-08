from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.account.api.v1.views.profile_view import ProfileViewSet, AllProfileViewSet

router = SimpleRouter()

router.register("profile", ProfileViewSet, basename="profile")
router.register("all-profiles", AllProfileViewSet, basename="all-profiles")

urlpatterns = [

] + router.urls
