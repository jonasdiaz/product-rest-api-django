from django.db.models import F
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.products.models import Product
from api.orders.models import Order, OrderDetail
from api.orders.serializers import OrderModelSerializer, OrderDetailModelSerializer


class OrderModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderModelSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        detail = OrderDetail.objects.filter(order=instance)
        for d in detail:
            Product.objects.filter(pk=d.product.pk).update(
                stock=F('stock') + d.cuantity
            )
        instance.delete()


class OrderDetailModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailModelSerializer
    queryset = OrderDetail.objects.all()
    permission_classes = [IsAuthenticated]