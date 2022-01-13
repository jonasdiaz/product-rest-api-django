from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
   TokenObtainPairView,
   TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="Api Market V1",
      contact=openapi.Contact(email="jonas.diaz0@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Django ADMIN
    url(r'^admin/', admin.site.urls),

    # Products
    url(r'api/v1/', include('api.products.urls')),

    # Orders
    url(r'api/v1/', include('api.orders.urls')),

    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
   urlpatterns += [
      # Swagger
      url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
      url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
      # Redoc
      url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]