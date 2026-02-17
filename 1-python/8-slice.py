gameName = "Fifa 23"
gameDescription = """
In this game, you will practice using string operators in Python.  """

# string[inicio:fim] - indice comeca na posicao 0 | indice final -1
# busque toda string a partir da primeira posicao
print(gameName[0:])

# busque toda string a partir da segunda posicao
print(gameName[:7])

"""
string[inicio:fim:passo] - indice comeca na posicao 0 
| indice final -1 |
passo pula caracteres
"""
print(gameName[::2])  # pula de 2 em 2 caracteres
print(gameName[1::2]) 
print(gameName[::-1])