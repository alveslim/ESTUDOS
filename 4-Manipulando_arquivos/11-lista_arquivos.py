import os, glob, zipfile
# Listar arquivos de um diretório # modulo de s.o # e compactar arq

# 1 -  diretório atual

os.getcwd()

# 2 - Listar arquivos txt & csv

for file in glob.glob("4-Manipulando_arquivos/*.txt"):
    print(file)
    
for file in glob.glob("4-Manipulando_arquivos/*.csv"):
    print(file)
    
# 3 - Compactar arquivos txt & csv

with zipfile.ZipFile("dados.zip", "w") as zip:
    for file in glob.glob("4-Manipulando_arquivos/*.txt"):
        zip.write(file)
    for file in glob.glob("4-Manipulando_arquivos/*.csv"):
        zip.write(file)
        
        
"////////////////////////////////////////////////////////////////"    
# 4 - Listar arquivos do zip
with zipfile.ZipFile("dados.zip", "r") as zip:
    print(zip.namelist())   
# 5 - Extrair arquivos do zip
with zipfile.ZipFile("dados.zip", "r") as zip:
    zip.extractall("dados")    
# 6 - Listar arquivos do diretório dados
for file in glob.glob("dados/*"):   
    print(file) 
# 7 - Excluir arquivos do diretório dados
for file in glob.glob("dados/*"):
    os.remove(file)
"////////////////////////////////////////////////////////////////"

# 8 - compactar todos arquivos 
       
with zipfile.ZipFile("todos_dados.zip", "w") as zip:
    for file in glob.glob("4-Manipulando_arquivos/*"):
        zip.write(file) # ou so ("*") para pegar tudo do diretório