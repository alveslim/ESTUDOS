class Loja:
    taxa = 0.10

cliente1 = Loja()
cliente2 = Loja()

Loja.taxa = 0.15
cliente1.taxa = 0.20

print(cliente1.taxa)  # Linha A 20
print(cliente2.taxa)  # Linha B 15
print(Loja.taxa)      # Linha C 15 