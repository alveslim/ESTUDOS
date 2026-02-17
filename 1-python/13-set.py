gamesSet = {"Chess", "Monopoly", "Scrabble", "Clue", "Risk", "Catan"}

# nao possibilita recuperar valores via fatiamento ou slice

print(len(gamesSet))
exampleSet = {0, False}
print(exampleSet)
gamesSet.update(exampleSet)
print(gamesSet)
gamesSet.remove("0" or "Chess")  # se o valor nao existir, gera erro
#gamesSet.discard("Monopoly")  # se o valor nao existir, nao gera erro
print(gamesSet)