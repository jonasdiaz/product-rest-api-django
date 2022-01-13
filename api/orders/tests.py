import json
from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.products.factories import ProductFactory


class TestOrder(TestCase):

    def setUp(self):
        product = ProductFactory()
        self.payload = {
            "order_details": [
                {
                    "cuantity": 1,
                    "product": product.pk
                }
            ]
        }
        User.objects.create_user(
            username = 'admin',
            password = '1234',
            is_active = True,
            is_superuser = True
        )
        self.sender = Client()
        self.auth = self.sender.post(
            '/auth/',
            {
                'username':'admin',
                'password':'1234'
            }
        )
        self.request = self.sender.post(
            '/api/v1/orders/',
            json.dumps(self.payload),
            HTTP_AUTHORIZATION = f"Bearer {self.auth.data['access']}",
            content_type='application/json'
        )
    
    def test_create_order(self):
        self.assertEqual(self.request.status_code, 201)
    
    def test_update_order(self):
        pk = self.request.data['id']
        self.payload['order_details'][0]['cuantity'] = 5
        self.request = self.sender.patch(
            f'/api/v1/orders/{pk}/', 
            self.payload,
            HTTP_AUTHORIZATION = f"Bearer {self.auth.data['access']}",
            content_type='application/json')
        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.request.data['id'], pk)
    
    def test_delete_order(self):
        pk = self.request.data['id']
        self.request = self.sender.delete(
            f'/api/v1/orders/{pk}/',
            HTTP_AUTHORIZATION = f"Bearer {self.auth.data['access']}"
        )
        self.assertEqual(self.request.status_code, 204)