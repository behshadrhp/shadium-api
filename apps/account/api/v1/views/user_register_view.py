from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken

from apps.account.api.v1.serializers.user_serializer import UserSerializer


class RegisterUserView(APIView):
        
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        try:
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "error": False,
                        "message": "Register is Successful.",
                        "code": 1001,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }, status=status.HTTP_201_CREATED
                )
        
        except ValidationError as error:
            raise ValidationError(
                {
                    "error": True,
                    "message": "Check your fields and try again.",
                    "code": 2001
                }
            )
            
        except Exception as error:
            raise ValidationError(
                {
                    "error": True,
                    "message": "Registration failed. Please try again later.",
                    "code": 2002,
                }
            )
