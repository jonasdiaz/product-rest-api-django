import factory
from factory.faker import faker

from api.products.models import Product

FAKE = faker.Faker()


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product
    
    name = FAKE.name()
    price = FAKE.pydecimal(left_digits=5, right_digits=2,positive=True, max_value=10000)
    stock = FAKE.pyint(min_value=0)