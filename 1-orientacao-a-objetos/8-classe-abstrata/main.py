from classes import ContaPoupanca
from classes import ContaCorrente


contaPoupanca = ContaPoupanca(1212, 2341, 0)

contaPoupanca.depositar(10)
contaPoupanca.sacar(5)
contaPoupanca.sacar(5)
contaPoupanca.sacar(1)

contaCorrente = ContaCorrente(agencia=1212, conta=4432, saldo=0, limite=500)

contaCorrente.depositar(100)
contaCorrente.sacar(250)
contaCorrente.sacar(500)
contaCorrente.depositar(1000)