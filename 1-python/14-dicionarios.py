game = {
    "name": "Chess",
    "yearLaunched": 1450,
    "gameSize": "2MB",
    "players": [2],
    "categories": ["Strategy", "Board Game"],
}
print(game)
print(len(game))  # tamanho do dicionario
print(game["name"])  # acessa valor pela chave
print(type(game))
print(game.keys())  # retorna as chaves do dicionario
print(game.values())  # retorna os valores do dicionario
print(game.items())  # retorna os itens (chave, valor) do dicionario

print(game['categories']) ## acessa valor pela chave
print(game.get('players')) ## acessa valor pela chave

game["version"] = 1.0  # adiciona novo par chave/valor
game.update({"players": [2, 4]})  # atualiza valor de uma chave existente
