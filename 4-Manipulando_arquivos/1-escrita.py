name =  input("Digite seu nome: \n")

"""
1 - opcao "w" - escrita
2 - opcao "a" - escrita, mas sem apagar o que já existe(append)
3 - opcao "r" - leitura
"""

#alternativa 1

#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

#alternativa 2
with open("4-Manipulando_arquivos/2-names.txt", "a") as file:
# TENTE abrir o arquivo "names.txt" para escrita (append) APELIDO "file"
    file.write(f"{name}\n")