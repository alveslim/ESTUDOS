name = input("Type the game name:\n")
yearLaunch = int(input("Type the year of launch:\n"))
gamePrice = float(input("Type the game price:\n"))
planIncluded = bool(input("Is the plane included? (True/False):\n"))

print("### Game Information ###")
print("========================")
print(f"Nome do Jogo: {name} \\nAno Lançamento: {yearLaunch} \\nPreço do Jogo: {gamePrice} \\nEstá incluso no serviço? {planIncluded}")
#Why use the `{}` syntax?
#The `{}` syntax is used for f-strings (formatted string literals) in Python.
