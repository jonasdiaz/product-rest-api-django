import requests
import json
from decimal import Decimal


class Service:

    def get_usd(self):
        response = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        precios_dolar = json.loads(response.text)
        dolar_blue = precios_dolar[1]
        return Decimal(dolar_blue['casa']['venta'].replace(',', '.'))

service_product = Service()
