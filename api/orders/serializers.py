from django.db.models import F
from api.orders.services import service_order
from rest_framework import serializers
from api.products.models import Product
from api.orders.models import Order, OrderDetail


class OrderDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['cuantity', 'product']


class OrderModelSerializer(serializers.ModelSerializer):
    order_details = OrderDetailModelSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'date_time', 'order_details', 'total', 'total_usd']
    
    def validate(self, validated_data):
        if service_order.validate_products_in_zeros(validated_data) == False:
            raise serializers.ValidationError("No es posible si la cantiad es 0")
        if service_order.validate_products_duplicate(validated_data) == False:
            raise serializers.ValidationError("Existen productos duplicados")
        products = [i['product'] for i in validated_data['order_details']]
        if Product.objects.filter(pk__in=products, stock__gte=3).exists():
            raise serializers.ValidationError("No hay suficiente stock")
        return validated_data

    def create(self, validated_data):
        details_data = validated_data.pop('order_details')
        order = Order.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetail.objects.create(order=order, **detail_data)
            Product.objects.filter(pk=detail_data['product'].pk).update(stock=F('stock') - detail_data['cuantity'])
        return order
    
    def update(self, instance, validated_data):
        order_data = validated_data.pop('order_details')
        for data in order_data:
            detail = OrderDetail.objects.filter(order=instance, product=data['product'])
            if detail.exists():
                if detail[0].cuantity > data['cuantity']:
                    Product.objects.filter(pk=data['product'].pk).update(
                        stock=F('stock') + (detail[0].cuantity - data['cuantity'])
                    )
                elif detail[0].cuantity < data['cuantity']:
                    Product.objects.filter(pk=data['product'].pk).update(
                        stock=F('stock') - (data['cuantity'] - detail[0].cuantity)
                    )
                else:
                    pass
                detail.update(cuantity=data['cuantity'])
            else:
                product_id = data['product'].pk
                OrderDetail.objects.create(order=instance, product_id=product_id, cuantity=data['cuantity'])
                Product.objects.filter(id=product_id).update(stock=F('stock') - data['cuantity'])
        
        return instance
