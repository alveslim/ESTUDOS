# ---- Cálculo da Distância
print("\n---- Cálculo da Distância ----\n")
print("Informe os quilometros percorridos: ")
Km = float(input(">"))

if Km <= 200 :
    precoPass = Km * 0.50
    print(f"O valor da passagem dos {Km}km percorrido ficou: R${precoPass:.2f}")
else: 
    precoPass = Km * 0.35
    print(f"O valor da passagem dos {Km}km percorrido ficou: R${precoPass:.2f}")
    
# ---- Aumento salário funcionário
