import sqlite3
# 1 - Conectando no BD
connection = sqlite3.connect("tittle.db")

# 2 - Criando um cursor
'''
Cursor é um interador que permite
navegar e manipular os do bd.
'''
cursor = connection.cursor()

# 3 - Criando a Tabela  
# Criando a tabela 'movies' com os tipos de dados apropriados:
# id: INTEGER, chave primária autoincrementada para identificar cada filme unicamente.
# name: TEXT, armazena o nome do filme.
# year: INTEGER, armazena o ano de lançamento do filme.
# score: REAL, armazena a nota do filme (pode ser decimal).
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
    );
""")

# 4 - Fechando conexão
print('Tabela criada com sucesso.')
# desconectando...
connection.close()