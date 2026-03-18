import sqlite3
# 1 - Conectando no BD
connection = sqlite3.connect("tittle.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - lendo dados da tabela]

data = cursor.execute("""
        SELECT * FROM movies
                      """) 
# O comando SELECT é usado para selecionar dados de uma tabela. O "*" indica que queremos selecionar todas as colunas da tabela.
# ou SELECT name, year FROM movies; para selecionar apenas o nome e o ano dos filmes.

print(data.fetchall()) # O método fetchall() retorna todas as linhas do resultado da consulta como uma lista de tuplas.

# 4 - Iterando os dados

print("Iterando os dados:")
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}")

# 5 - ordenando os dados pelo score

print("Ordenando os dados pelo score:")
for row in cursor.execute("SELECT * FROM movies ORDER BY score DESC"):
    print(f"{row}")    

connection.commit() # Salva as alterações no banco de dados
connection.close()

