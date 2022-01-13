
from django.db.models import F
from api.products.services import service_product
from rest_framework import serializers
from api.products.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
