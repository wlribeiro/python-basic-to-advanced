class Arquivo:

    def __init(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)
    
    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('texto')
