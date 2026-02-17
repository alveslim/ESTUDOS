name = input("Enter name game: \n")
yearLaunch = int(input("Enter year launch game: \n"))
classification = float(input("Enter classification game: \n"))

if classification >= 8.0 or yearLaunch > 2015:
    print(f"The game {name} is classified as excellent.")
else:
    print(f"The game {name} is classified as good.")
    
#nao trabalha com () ou {} em blocos de codigos, só por indentação

