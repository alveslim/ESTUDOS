import random

naipes = ['Ouros', 'Espadas', 'Copas', 'Paus']
valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Criando a lista de cartas
baralho = []
for naipe in naipes:
    for valor in valores:
        baralho.append(f'{valor} de {naipe}')

print(baralho[0])