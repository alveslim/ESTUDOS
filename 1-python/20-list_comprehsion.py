listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Chess", "Monopoly", "Fifa", "Fortnite", "Gta"]

# Jogos q tenham a letra "A"
newList = [game for game in  gamesList if "a" in game]
print(newList)

#Games win
gamesWin = [game for game in gamesList if game != "Fifa" and game != "Fortnite"]
print(gamesWin)