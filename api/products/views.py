from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.products.serializers import ProductModelSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ProductModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        model = self.serializer_class.Meta.model
        queryset = model.objects.filter().order_by('-id')
        if self.action not in ['list', 'retrieve']:
            queryset = queryset.filter().order_by('-id')
        return queryset
