import sqlite3
# 1 - Conectando no BD
connection = sqlite3.connect("tittle.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - solicitando dados do usuário

name = input("Digite o nome do filme: \n")
year = int(input("Digite o ano do filme: \n"))
score = float(input("Digite a nota do filme: \n"))

# 4 - Inserindo os dados na tabela
cursor.execute("""
    INSERT INTO movies (name, year, score)
        VALUES (?, ?, ?)
               """, (name, year, score)) # O "?" é um placeholder para os valores que serão inseridos, e os valores são passados como uma tupla no segundo argumento do método execute.

connection.commit() # Salva as alterações no banco de dados
connection.close()