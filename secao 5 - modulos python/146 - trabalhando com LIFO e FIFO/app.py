

livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

print(livros)

livro_removido = livros.pop()
print(livros, livro_removido)

livro_removido = livros.pop()
print(livros, livro_removido)

livro_removido = livros.pop()
print(livros, livro_removido)

livro_removido = livros.pop()
print(livros, livro_removido)

livro_removido = livros.pop()
print(livros, livro_removido)

from collections import deque

fila = deque()
fila.append('a')
fila.append('b')
fila.append('c')
fila.append('d')
fila.append('e')
print(fila)
print(f'saiu: {fila.popleft()}')
print(f'saiu: {fila.popleft()}')
print(f'saiu: {fila.popleft()}')