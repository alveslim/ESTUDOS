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

id = int(input("Digite o id do filme que deseja remover:\n "))

# 4 - Atualizando os dados

cursor.execute("""
               DELETE FROM movies 
               WHERE id = ?
               """, (id,))
connection.commit() # Salva as alterações no banco de dados
print(f"Filme {id} removido com sucesso.")

connection.close()