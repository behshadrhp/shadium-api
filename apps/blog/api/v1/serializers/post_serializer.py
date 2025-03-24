from rest_framework import serializers

from apps.blog.models.post_model import Post

from taggit.serializers import TagListSerializerField


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SerializerMethodField()
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = [
            "id", "author", "cover", "title", "slug", "body", 
            "status","tags", "created_at", "updated_at"
        ]

    def get_author(self, post: Post):
        return post.author.email
