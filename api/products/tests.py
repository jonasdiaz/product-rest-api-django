from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.products.models import Product


class TestProducts(TestCase):

    def setUp(self):
        self.payload ={
            "name": "Papel Higienico Mamadera",
            "price": 100.00,
            "stock": 100
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
            '/api/v1/products/',
            self.payload,
            HTTP_AUTHORIZATION = f"Bearer {self.auth.data['access']}",
        )
        dir(self.request)
    
    def test_create_product(self):
        self.assertEqual(self.request.status_code, 201)
    
    def test_update_product(self):
        pk = self.request.data['id']
        self.payload['stock'] = 50
        self.request = self.sender.patch(
            f'/api/v1/products/{pk}/', 
            self.payload,
            HTTP_AUTHORIZATION = f"Bearer {self.auth.data['access']}",
            content_type='application/json')
        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.request.data['id'], pk)
    
    def test_delete_product(self):
        pk = self.request.data['id']
        self.request = self.sender.delete(
            f'/api/v1/products/{pk}/',
            HTTP_AUTHORIZATION = f"Bearer {self.auth.data['access']}"
        )
        self.assertEqual(self.request.status_code, 204)