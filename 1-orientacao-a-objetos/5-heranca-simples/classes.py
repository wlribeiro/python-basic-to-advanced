class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def talk(self):
        print("Pessoa falando...")


class Cient(Pessoa):
    def buy(self):
        print("Client comprando...")


class Studant(Pessoa):
    def study(self):
        print("Aluno estudando...")