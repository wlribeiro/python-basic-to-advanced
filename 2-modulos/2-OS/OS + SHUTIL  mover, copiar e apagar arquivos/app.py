import os
import shutil

def atual_path() -> str:
    caminho = os.path.realpath(__file__)
    caminho = caminho.split('\\')
    caminho.pop()
    return '\\'.join(caminho)


try:
    os.mkdir(f"{atual_path()}\\teste")
except FileExistsError:
    pass

try:
    os.mkdir(f"{atual_path()}\\teste\\output")
except FileExistsError:
    pass

with open(f"{atual_path()}\\teste\\a.txt", 'w') as f:
    pass

caminho_original = atual_path() + "\\teste"
caminho_novo = atual_path() + "\\teste\\output"

for root, dirs, files in os.walk(caminho_original):
    for file_ in files:
        old_file_path = os.path.join(root, file_)
        new_file_path = os.path.join(caminho_novo, file_)

        shutil.move(old_file_path, new_file_path)


shutil.copy(atual_path() + '\\app.py', caminho_novo + '\\codigo.py')


os.system('pause')

os.remove(caminho_novo + '\\codigo.py')
