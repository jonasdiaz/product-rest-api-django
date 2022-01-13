class Service:
    
    def validate_products_in_zeros(self, data):
        order = data['order_details']
        lista_zeros = [0 in i.values() for i in order if i['cuantity'] == 0]
        if len(lista_zeros) >= 1:
            return False
        return True
    
    def validate_products_duplicate(self, data):
        order = data['order_details']
        lista = [i['product'] for i in order]
        if len(set(lista)) < len(lista):
            return False
        return True

service_order = Service()