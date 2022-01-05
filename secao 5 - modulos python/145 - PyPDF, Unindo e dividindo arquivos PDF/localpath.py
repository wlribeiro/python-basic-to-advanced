import os


def localpath() -> str:
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    return '\\'.join(caminho)