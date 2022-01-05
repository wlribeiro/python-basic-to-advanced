#!/usr/bin/env python
import os
import sys


def show_menssage() -> None:
    print('-a', 'Para listar todo os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretorios nesta pasta', sep='\t')

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1 :
    print('Falta argumentos')
    show_menssage()
    sys.exit()

if '-h' in argumentos :
    print('Comandos')
    show_menssage()
    sys.exit()

so_arquivos= False
if '-a' in argumentos:
    so_arquivos = True


so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.') :
    if so_arquivos:
        if os.path.isfile(arquivo) :
            print(arquivo)

    if so_diretorios :
        if os.path.isdir(arquivo) :
            print(arquivo)