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
game["players"] = [2, 4]  # Também cria a chave se não existir ou atualiza se já existir

game = {"name": "Xadrez"}

# Adiciona ou atualiza múltiplas chaves de uma vez
game.update({"players": [2, 4], "status": "ativo", "year": 2026})

print(game)
# Saída: {'name': 'Xadrez', 'players': [2, 4], 'status': 'ativo', 'year': 2026}

game = {"name": "Xadrez"}

# Atualiza com novas chaves e valores
game |= {"players": [2, 4], "type": "board"}

print(game)
# Saída: {'name': 'Xadrez', 'players': [2, 4], 'type': 'board'}
