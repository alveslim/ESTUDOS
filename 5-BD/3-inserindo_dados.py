import sqlite3
# - Conectando no BD
connection = sqlite3.connect("tittle.db")

# - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# ///// INSERINDO DADOS ///// #

cursor.execute("""
    INSERT INTO movies (name, year, score)
        VALUES ('The Shawshank Redemption', 1994, 9.3),
               ('Super Mario Bros', 1985, 8.5),
               ('Velozes e Furiosos', 2001, 6.8);
               """)

connection.commit() # Salva as alterações no banco de dados
connection.close()