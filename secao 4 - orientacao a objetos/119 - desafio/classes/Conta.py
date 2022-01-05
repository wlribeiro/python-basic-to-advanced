from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Deposito precisa ser  numerico")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'saldo: {self.saldo}', end=' ')
        print('\n')


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if self.saldo < valor :
            print("saldo insuficiente")
            return 

        else:
            self.saldo -= valor


class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor :
            print("saldo insuficiente")
            return 

        else:
            self.saldo -= valor