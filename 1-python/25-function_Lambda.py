#Pode ser vista como funções anônimas, ou seja, funções sem nome.
#receber qualquer numero de argumentos mas retornar apenas uma expressão.
#Sintaxe: lambda argumentos: expressão 

power = lambda num: num ** 2 # eleva ao quadrado
pair = lambda x: x % 2 == 0 # True se par, False se ímpar
divNum = lambda x, y: x/y # divide 
reverse = lambda s: s[:: -1] # inverte string

print(reverse("Python"))
print(divNum(10, 2))
print(pair(4))
print(power(5))
