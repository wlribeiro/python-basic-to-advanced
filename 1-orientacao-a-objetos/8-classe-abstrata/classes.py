from abc import ABC, abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser  numerico")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Deposito precisa ser  numerico")

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'saldo: {self.saldo}', end=' ')

    @abstractmethod
    def sacar(self, valor):
        pass



class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        if self.saldo < valor :
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if(self.saldo + self._limite) < valor :
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()