from conexao_post import conn
# lendo dados do pgadmin

cursor_obj = conn.cursor()
# print(cursor_obj)

cursor_obj.execute("SELECT * FROM game")
result = cursor_obj.fetchall()
print(result)