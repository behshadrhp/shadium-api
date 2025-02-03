from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ["email", "password", "password2"]
        
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError("Password is not match.", code=status.HTTP_400_BAD_REQUEST)
        return attrs

    def create(self, validated_data):        
        user = User.objects.create(
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
