from django.db import models

from api.products.models import Product
from api.products.services import service_product


class Order(models.Model):
    date_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'{self.date_time}'
    
    @property
    def total(self):
        total_sum = OrderDetail.objects.filter(order=self)
        return sum([i.cuantity * i.product.price for i in total_sum])
    
    @property
    def total_usd(self):
        total_sum = OrderDetail.objects.filter(order=self)
        return (sum([i.cuantity * i.product.price for i in total_sum]) / service_product.get_usd())


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    cuantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'
    
    def __str__(self):
        return f'{self.order} - {self.cuantity} - {self.product}'