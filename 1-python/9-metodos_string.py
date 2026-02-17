gameName = "fifa 23"
gameDescription = """
In this game, you will practice using string operators in Python.  """

print(gameName.upper()) # transforma todos os caracteres em maiusculo
print(gameName.lower()) # transforma todos os caracteres em minusculo
print(gameName.capitalize()) # transforma o primeiro caractere em maiusculo
print(gameName.title()) # transforma o primeiro caractere de cada palavra em maiusculo
print(gameName.center(10, "-")) # centraliza a string em um campo de tamanho especifico, preenchendo com o caractere especifico
print(gameName.find("f")) # busca a posicao inicial da substring especifica
print(gameDescription.count("f")) # conta quantas vezes a substring especifica aparece na string
#print(gameDescription.replace("Python", "Javascript")) # substitui uma parte da string por outra
#print(gameDescription.split(",")) 


"""
print(gameName.strip()) # remove espacos no inicio e no fim da string
print(gameName.replace("23", "24")) # substitui uma parte da string por outra
print(gameName.split(" ")) # divide a string em uma lista, usando o caractere especific
print(" ".join(["Welcome", "to", "Fifa", "23"])) # junta uma lista de strings em uma unica string, usando o caractere especifico
print(gameName.find("Fifa")) # busca a posicao inicial da substring especifica
print(gameName.count("a")) # conta quantas vezes a substring especifica aparece na string
print(gameName.startswith("Fifa")) # verifica se a string comeca com a substring especifica
print(gameName.endswith("23")) # verifica se a string termina com a substring especifica
"""