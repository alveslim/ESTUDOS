with open("4-Manipulando_arquivos/2-names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"---{line.rstrip()}---")