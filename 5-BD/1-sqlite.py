import sqlite3

# 1 -  CRIANDO O BANCO DE DADOS
connection =  sqlite3.connect("tittle.db")

# 2 - VERIFICANDO SE HOUVE ALTERACAOES NO BANCO DE DADOS
print(connection.total_changes)