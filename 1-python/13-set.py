gamesSet = {"Chess", "Monopoly", "Scrabble", "Clue", "Risk", "Catan"}

# nao possibilita recuperar valores via fatiamento ou slice

print(len(gamesSet))
exampleSet = {0, False}
print(exampleSet)
gamesSet.update(exampleSet)
print(gamesSet)
# gamesSet.remove("0" or "Chess")  # se o valor nao existir, gera erro
#gamesSet.discard("Monopoly")  # se o valor nao existir, nao gera erro
print(gamesSet)

regras_firewall = {
    frozenset([80, 443]),        # Portas Web (HTTP/HTTPS)
    frozenset([21, 22])          # Portas de Arquivo/Terminal (FTP/SSH)
}
print(regras_firewall)