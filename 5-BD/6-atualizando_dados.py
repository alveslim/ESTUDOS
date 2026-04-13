import sqlite3
# 1 - Conectando no BD
connection = sqlite3.connect("tittle.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Solicitando a atualização de dados

id = int(input("Digite o id do filme que deseja atualizar:\n "))

# 4 - Atualizando os dados

cursor.execute("""
               UPDATE movies set name = ?, year = ? 
               WHERE id = ?""", (name, year, id))
connection.commit() # Salva as alterações no banco de dados
print("Dados atualizados com sucesso.")

connection.close()