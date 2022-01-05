

class MeuErroPersonalizado(Exception):
    pass


def testar():
    raise MeuErroPersonalizado('Erro')


try:
    testar()
except MeuErroPersonalizado as error:
    print(f'Erro: {error}')