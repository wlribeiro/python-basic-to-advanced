from contextlib import contextmanager


@contextmanager
def abrir (arquivo, modo):
    try:
        arquivo = open(arquivo, modo)
        yield arquivo

    finally:
        arquivo.close()


with abrir('abc.txt', 'w') as f:
    f.write('texto')