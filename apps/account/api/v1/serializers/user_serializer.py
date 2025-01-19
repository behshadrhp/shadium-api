from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        write_only=True,
        required=True,
        style={"input_type": "email", "placeholder": "Enter Your Email."}
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Enter Your Password."}
    )

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def save(self, request=None):
        email = self.validated_data['email']
        password = self.validated_data['password']

        user = User.objects.create_user(email=email, password=password)
        return user
