from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Roino API",
      default_version="v1",
      description="Social network APIs like Medium",
      terms_of_service="https://roino.ir",
      contact=openapi.Contact(email="info@roino.ir"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)
