import os
import csv


def atual_path() -> str:
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    return '\\'.join(caminho)


with open(atual_path() + '\\clientes.csv', 'r') as filecsv:
    dados = csv.reader(filecsv)
    dicionario = csv.DictReader(filecsv)

    # exportar para fora do gerador
    data = [x for x in csv.DictReader(filecsv)]

    # next(dados) para pul;ar uma linha

    for dado in dados:
        print(dado)

with open(atual_path() + '\\cliente2.csv', 'w') as filecsv:
    escreve = csv.writer(
        filecsv,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = data[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in data :
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
