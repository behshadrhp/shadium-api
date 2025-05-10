from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.blog.api.v1.views.clap_view import ClapViewSet
from apps.blog.api.v1.views.bookmark_view import BookMarkViewSet 
from apps.blog.api.v1.views.rating_view import RatingExploreViewSet
from apps.blog.api.v1.views.post_view import PostExploreViewSet, PostViewSet
from apps.blog.api.v1.views.post_elasticsearch_view import PostElasticSearchViewSet
from apps.blog.api.v1.views.comment_view import CommentViewSet, CommentExploreViewSet

router = SimpleRouter()

router.register("post", PostViewSet, basename="post")
router.register("clap", ClapViewSet, basename="clap")
router.register("comment", CommentViewSet, basename="comment")
router.register("bookmark", BookMarkViewSet, basename="bookmark")
router.register("post-explore", PostExploreViewSet, basename="post-explore")
router.register("post-search", PostElasticSearchViewSet, basename="post-search")
router.register("rating-explore", RatingExploreViewSet, basename="rating-explore")
router.register("comment-explore", CommentExploreViewSet, basename="comment-explore")

urlpatterns = [

] + router.urls
