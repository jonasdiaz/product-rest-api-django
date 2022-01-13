from django.urls import path
from rest_framework.routers import DefaultRouter

from api.products.views import *

router = DefaultRouter()
router.register(r'products', ProductModelViewSet, basename='products')

urlpatterns = router.urls
