from string import Template
from datetime import datetime
import os


def atual_path() -> str:
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    return '\\'.join(caminho)

with open(atual_path() + '\\template.html') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='William Ribeiro', data=data_atual)


print(corpo_msg)