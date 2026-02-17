gameData = ["Fifa23", 2022, 90.50, 8.5] 

gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2",
             "God of War", "Minecraft", "Fortnite"]
print(gamesList)

# 1 - Busque os dois primeiros itens da lista
print(gamesList[0:2])

# 2 - Busque o último item da lista
print(gamesList[-1])

# 3 - Busca jogos até uma posição
print(gamesList[:2])

# 4 - Busca jogos de uma posição em diante
print(gamesList[2:])

# Metodos de listas 
print(len(gamesList)) # tamanho da lista
print(gamesList.index("Minecraft") ) # busca o indice do item especifico
gamesList.append("Cyberpunk 2077") # adiciona um item no final da lista
print(gamesList)
gamesList.sort() # ordena a lista em ordem alfabetica
gameReset = gamesList.copy()
gameReset.remoce("Star wars") # remove o item especifico da lista
gamesList.clear() # limpa toda a lista
