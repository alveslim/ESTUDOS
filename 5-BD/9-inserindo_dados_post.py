from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ("The Legend of Zelda: Breath of the Wild", 2017, 9.0),
    ("Farcry 4", 2014, 8.5)
]

for game in games:
    cursor_obj.execute("""
                       INSERT into game(name, year, score)
                       from conexao_post import conn
# lendo dados do pgadmin

cursor_obj = conn.cursor()
# print(cursor_obj)
                       """, game)
    
conn.commit()
conn.close()
print("Dados inseridos com sucesso!")