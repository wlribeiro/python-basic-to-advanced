import sqlite3
from localpath import localpath 
conexao = sqlite3.connect( localpath() + '\\basededados.db')
cursor = conexao.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'nome TEXT,'
                'peso REAL'
                ')')


cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
conexao.commit()


cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    print(linha)


cursor.close()
conexao.close()