class MarketCar:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_products(self):
        for product in self.products:
            print(product.name, product.price)

    def total_sum(self):
        total = 0
        for product in self.products:
            total += product.price

        return total

class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price