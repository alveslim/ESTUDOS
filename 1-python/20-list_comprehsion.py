listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Chess", "Monopoly", "Fifa", "Fortnite", "Gta"]

# Jogos q tenham a letra "A"
newList = [game for game in  gamesList if "a" in game]
print(newList)

#Games win
gamesWin = [game for game in gamesList if game != "Fifa" and game != "Fortnite"]
print(gamesWin)

estoque = [
    {"nome": "B450M", "soquete": "AM4"},
    {"nome": "X670E", "soquete": "AM5"},
    {"nome": "B650M", "soquete": "AM5"}
]

# Quero apenas uma lista com os nomes das placas que são compatíveis com AM5
placas_am5 = [placa["nome"] for placa in estoque if placa["soquete"] == "AM5"]
# Retorna: ['X670E', 'B650M']

# Extrai o nome e o tipo apenas das peças AM4
pecas_am4 = [(item["nome"], item["tipo"]) for item in estoque if item["soquete"] == "AM4"]

# Retorna: [('B450M', 'Placa-Mãe'), ('Ryzen 5 5600', 'Processador')]

pecas_am4 = [{"produto": item["nome"], "categoria": item["tipo"]} for item in estoque if item["soquete"] == "AM4"]

# Retorna: [{'produto': 'B450M', 'categoria': 'Placa-Mãe'}, {'produto': 'Ryzen 5 5600', 'categoria': 'Processador'}]

pecas_am4 = [f'{item["nome"]} é do tipo {item["tipo"]}.' for item in estoque if item["soquete"] == "AM4"]

# Retorna: ['B450M é do tipo Placa-Mãe.', 'Ryzen 5 5600 é do tipo Processador.']