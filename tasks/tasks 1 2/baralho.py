@ -9,4 +9,11 @@ for naipe in naipes:
    for valor in valores:
        baralho.append(f'{valor} de {naipe}')

print(baralho[0])
#print(baralho[0])

# Embaralhando as cartas
random.shuffle(baralho)

# Mostrando as 5 primeiras cartas
for carta in baralho[:5]:
    print(carta)