# --- Contagem Regressiva
contagem = 10
sec = 5
print("--- Contagem Regressiva ---")
for num in range(contagem):
    if contagem >= 1:
        print(f"{contagem}")
        contagem = contagem - 1        
print(f"{contagem}") # para imprimir o 0 
while (sec != 0): # fazer o beep
    sec -= 1
    print("beep")
    
# --- Tabuada
print("--- Tabuada ---")
num = int(input("Digite um numero: "))
tabuada = 10
print("Escreva uma das aritméticas para resolução: \n" +
             "(+, -, x, /)")
while (tabuada != 0):
    result = num * tabuada
    print(f"{num} x {tabuada} = {result}")
    tabuada -= 1

# Resolução do professor: 
#lancamento
import winsound
x = 10
while x >= 0:
    print(x)
    x = x - 1
winsound.Beep(2500, 500) #o hz em beep frequencia

#tabuada 
number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin 
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1