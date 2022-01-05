from dados import *

import json
import os

def atual_path() -> str:
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    return '\\'.join(caminho)

dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

dicionario = json.loads(clientes_json)
for chave, valor in dicionario.items() :
    print(chave)
    print(valor)

with open(atual_path() + '\\clientes.json', 'w') as fjs:
    json.dump(clientes_dicionario, fjs, indent=4)

with open(atual_path() + '\\clientes.json', 'r') as fjs:
    dados = json.load(fjs)

for chave, valor in dados.items() :
    print(chave)
    print(valor)
