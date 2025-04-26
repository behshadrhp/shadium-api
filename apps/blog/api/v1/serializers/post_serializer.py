from rest_framework import serializers

from taggit.serializers import TagListSerializerField

from apps.blog.models.post_model import Post, Clap


class ClapSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Clap
        fields = ["id", "user", "created_at", "updated_at"]

    def get_user(self, clap: Clap):
        return clap.user.email


class PostSerializer(serializers.ModelSerializer):

    # initial fields
    author = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    # rating serializer
    rating = serializers.SerializerMethodField()

    # clap serializer
    claps = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id", "author", "cover", "title", "slug", "body", 
            "status","tags", "rating", "claps", "created_at", "updated_at"
        ]

    def get_author(self, post: Post):
        return post.author.email
    
    def get_rating(self, post: Post):
        from apps.blog.api.v1.serializers.rating_serializer import RatingSerializer
        rating = post.post_rating.select_related("user", "post").all()
        return RatingSerializer(rating, many=True).data

    def get_claps(self, post: Post):
        claps = post.post_clap.select_related("user", "post").filter(is_deleted=False)
        return ClapSerializer(claps, many=True).data
