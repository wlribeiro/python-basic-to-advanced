from classes import MarketCar, Product



car = MarketCar()

product1 = Product('camisa', 50)
product2 = Product('iPhone', 5090)
product3 = Product('xiara', 5)


car.insert_product(product1)
car.insert_product(product2)
car.insert_product(product3)

car.insert_product(product1)
car.insert_product(product2)
car.insert_product(product3)

car.insert_product(product1)
car.insert_product(product2)
car.insert_product(product3)

car.list_products()
print(car.total_sum())
