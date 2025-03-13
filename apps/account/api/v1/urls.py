from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.account.api.v1.views.profile_view import ProfileViewSet, UserExploreViewSet

router = SimpleRouter()

router.register("profile", ProfileViewSet, basename="profile")
router.register("explore", UserExploreViewSet, basename="user-explore")

urlpatterns = [

] + router.urls
