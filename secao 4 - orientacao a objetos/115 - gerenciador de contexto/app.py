
#  sem gerenciador de comtexto
arquivo = open('abc.txt', 'w')
arquivo.write("texto")
arquivo.close()

#  com gerenciador de comtexto
with open('abc.txt', 'w') as arquivo :
    arquivo.write('texto')
