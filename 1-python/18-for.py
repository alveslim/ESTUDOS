gameList = ["Chess", "Monopoly", "Fifa", "Fortnite"]

# iterando valores de uma lista
for game in gameList: 
    print(game)
    
# quando a condicao for atingida, o loop para

for game in gameList:
    if game == "Fifa":
        break
    print(game)

#quando a condicao for atingida, o loop pula para a proxima iteracao
for game in gameList:
    if game == "Fifa":
        continue
    print(game)
    
# iterando um range de numeros
gameName = input("Enter game name: \n")
gameRating = int(input("Enter game rating (1-10): \n"))
sum = 0

for i in range(gameRating):
    note = float(input("Enter rating note: \n"))
    sum += note
print(f"The average rating for the game {gameName} if {sum / gameRating:.2f}")