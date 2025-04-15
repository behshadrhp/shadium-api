from rest_framework import serializers

from apps.blog.models.rating_model import Rating
from apps.account.api.v1.serializers.user_serializer import UserSerializer
from apps.blog.api.v1.serializers.post_serializer import PostSerializer


class RatingSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ["id", "user", "created_at", "updated_at"]
    