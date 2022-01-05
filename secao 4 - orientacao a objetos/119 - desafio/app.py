from classes.Conta import ContaCorrente
from classes.Conta import ContaPoupanca
from classes.Cliente import Cliente




cliente = {"nome": "Fabo",
            "idade": 30}

conta = {"agencia": 123332,
        "conta": 987612343,
        "saldo_poupanca": 230,
        "saldo_corrente": 100,
        "limite_corrente": 200}

conta_corrente = ContaCorrente(agencia=conta["agencia"], conta=conta["conta"], saldo=conta["saldo_corrente"], limite=conta["limite_corrente"])
conta_poupanca = ContaPoupanca(agencia=conta["agencia"], conta=conta["conta"], saldo=conta["saldo_poupanca"])
cliente = Cliente(nome=cliente["nome"], idade=cliente["idade"])


