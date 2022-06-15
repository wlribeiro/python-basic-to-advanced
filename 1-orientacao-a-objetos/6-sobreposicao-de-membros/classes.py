class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def talk(self):
        print("Pessoa falando...")


class Client(Pessoa):
    def buy(self):
        print("Client comprando...")


class ClientVip(Client):
    def __init__(self, name, idade, lastname):
        super().__init__(name, idade)
        self.lastname = lastname
        
    def buy(self):
        super().buy()
        print("VIP comprando...")
