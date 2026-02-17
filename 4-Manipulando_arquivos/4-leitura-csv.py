with open("4-Manipulando_arquivos/4-courses.csv", "r", encoding="utf-8") as file:
    for line in file: 
        #row = line.rstrip().split(",") #remove o \n e separa por vírgula e guarda em uma lista(linha
        #print(f"Curso: {row[0]} - Aplicabilidade: {row[1]}")
        
        lang, category = line.rstrip().split(",")
        print(f"Curso: {lang} - Aplicabilidade: {category}")