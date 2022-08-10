from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Djoser And Simple JWT User Auth App",
      default_version='v1',
      description="API to demonstratre how to use djoser and simple jwt for user registration and authentication",
      contact=openapi.Contact(email="henrychizobaudeh@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),

    # Schema Documentation
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
