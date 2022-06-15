import os

class Encontrar:

    def __init__(self, caminho_de_busca = None, termo_de_busca= None):
        self.caminho_de_busca = caminho_de_busca
        self.termo_de_busca = termo_de_busca
        self.arquivos_encontrados = {}
        self.contador = 0

    def buscar(self):
        self.contador = 0
        for raiz, diretorio, arquivos in os.walk(self.caminho_de_busca):
            for arquivo in arquivos :
                if self.termo_de_busca in arquivo :
                    try:

                        self.contador += 1
                        caminho_completo = os.path.join(raiz, arquivo)
                        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                        tamanho = os.path.getsize(caminho_completo)

                        self.arquivos_encontrados[caminho_completo] = {
                                                                    "nome": nome_arquivo,
                                                                    "extensao": extensao_arquivo,
                                                                    "tamanho": self.formata_tamanho(tamanho),
                                                                    "Caminho": caminho_completo
                                                                        }

                    except PermissionError as e:
                        print('Sem pemissao')
                    except FileNotFoundError as e:
                        print('Arquivo nao encontrado')
                    except Exception as e:
                        print('Erro desconhecido: ', e)

    def encontraos(self):
        return f'{self.contador} arquivo(s) encontrado(s) com o termo: {self.termo_de_busca}'

    @staticmethod
    def formata_tamanho(tamanho):
        base = 1024
        kilo = base
        mega = base ** 2
        giga = base ** 3
        tera = base ** 4
        peta = base ** 5

        if tamanho < kilo :
            texto = 'B'
        
        elif tamanho < mega :
            tamanho /= kilo
            texto = 'KB'
        
        elif tamanho < giga :
            tamanho /= mega
            texto = 'MB'
        
        elif tamanho < tera :
            tamanho /= giga
            texto = 'GB'
        
        elif tamanho < peta :
            tamanho /= tera
            texto = "TB"
        
        else:
            tamanho /= peta
            texto = 'PB'

        tamanho = round(tamanho, 2)

        return f'{tamanho}{texto}'


if __name__ == "__main__" :
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    caminho = '\\'.join(caminho)


    encontrar = Encontrar()
    encontrar.caminho_de_busca = caminho
    encontrar.termo_de_busca = 'py'
    encontrar.buscar()
    response = encontrar.encontraos()
    print(response)

    for key, value in encontrar.arquivos_encontrados.items() :
        for k, val in value.items() :
            print(k, val, sep=" :: ")
        print("\n")