from zipfile import ZipFile
import os

# from ..helper import localpath
from localpath import localpath


try:
    os.mkdir(localpath() + "\\output")
except FileExistsError :
    pass

try:
    os.mkdir(localpath() + "\\pastateste")
except FileExistsError :
    pass


for i in range(10) :
    with open(f'{localpath()}\\pastateste\\{i}.txt', 'w') as fil :
        fil.write('oafihngjfhgbanfgrhabgajnfnanhabhahgiaeyfaihbgvh')

caminho = localpath() + '\\pastateste'
with ZipFile(localpath() + '\\output\\arquivo.zip', 'w') as zipfile :
    for arquivo in os.listdir(caminho) :
        caminho_completo = os.path.join(caminho, arquivo)
        zipfile.write(caminho_completo, arquivo)


with ZipFile(localpath() + '\\output\\arquivo.zip', 'r') as zipfile :
    for arquivo in zipfile.namelist() :
        print(arquivo)


with ZipFile(localpath() + '\\output\\arquivo.zip', 'r') as zipfile :
    zipfile.extractall(localpath() + '\\output\\descompactado')