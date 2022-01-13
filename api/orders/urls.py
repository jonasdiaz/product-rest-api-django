from django.urls import path
from rest_framework.routers import DefaultRouter

from api.orders.views import *

router = DefaultRouter()
router.register(r'orders', OrderModelViewSet, basename='orders')

urlpatterns = router.urls
