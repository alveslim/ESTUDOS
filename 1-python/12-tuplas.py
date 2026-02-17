gamesTuple = ("Soccer", "Basketball", "Tennis", "Baseball", "Hockey")
print(gamesTuple)
name = ("John")
list = ["John"]
print(type(name))
print(type(list))
print(type(gamesTuple))
# -  nao possibilita adicionar, remover ou alterar itens
# - permite acesso aos itens por indice e fatiamento
# - permite metodos de contagem e busca de indice
# Acessando itens da tupla
print(gamesTuple[:2])
print(gamesTuple[-1])
print(gamesTuple[3:])

# Metodos de tuplas
print(gamesTuple.index("Tennis")) 
