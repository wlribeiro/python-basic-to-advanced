class Client:
    def __init__(self, name, idade):
        self.name = name
        self.idade = idade
        self.addresses = []


    def insert_address(self, city, state):
        self.addresses.append(Address(city, state))

    def list_address(self):
        for address in self.addresses:
            print(address.city, address.state)

class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state