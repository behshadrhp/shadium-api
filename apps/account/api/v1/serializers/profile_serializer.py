from rest_framework import serializers

from apps.account.models.profile_model import Profile


class FollowingSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()

    class Meta:

        model = Profile
        fields = ["id", "user", "avatar", "first_name", "last_name", "biography"]

    def get_user(self, obj):
        return obj.user.email


class GetProfileSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    following = FollowingSerializer(many=True)

    class Meta:

        model = Profile
        fields = [
            "id", "user", "avatar", "following", "first_name", "last_name", "phone_number",
            "biography", "gender", "country", "city", "twitter", "created_at", "updated_at",
        ]

    def get_user(self, obj):
        return obj.user.email
    
    def get_country(self, obj):
        return obj.country.name
    

class PutProfileSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:

        model = Profile
        fields = [
            "id", "user", "avatar", "following", "first_name", "last_name", "phone_number",
            "biography", "gender", "country", "city", "twitter", "created_at", "updated_at",
        ]

    def get_user(self, obj):
        return obj.user.email
    
    def get_country(self, obj):
        return obj.country.name


class AllProfileSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["id", "user", "avatar", "first_name", "last_name", "biography", "gender", "country", "city", "twitter"]

    def get_user(self, obj):
        return obj.user.email
    
    def get_country(self, obj):
        return obj.country.name
