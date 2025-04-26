from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.blog.api.v1.views.clap_view import ClapViewSet
from apps.blog.api.v1.views.bookmark_view import BookMarkViewSet 
from apps.blog.api.v1.views.rating_view import RatingExploreViewSet
from apps.blog.api.v1.views.post_view import PostExploreViewSet, PostViewSet

router = SimpleRouter()

router.register("post", PostViewSet, basename="post")
router.register("clap", ClapViewSet, basename="clap")
router.register("bookmark", BookMarkViewSet, basename="bookmark")
router.register("post-explore", PostExploreViewSet, basename="post-explore")
router.register("rating-explore", RatingExploreViewSet, basename="rating-explore")

urlpatterns = [

] + router.urls
