names = [] #nossa lista de nomes, inicialmente vazia

with open("4-Manipulando_arquivos/2-names.txt", "r", encoding="utf-8") as file_APELIDO: 
    # TENTE abrir o arquivo "names.txt" para leitura APELIDO "file"
    for line in file_APELIDO: # para cada linha do arquivo(APELIDO)
        names.append(line.rstrip()) # ADD na nossa lista
        
#print(names)
for name in sorted(names): #ordena a lista de nomes em ordem alfabética
    print(f"---{name}---")