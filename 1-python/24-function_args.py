"""*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""
#args -----------------------------
def sum(*num):
    total = 0
    for n in num:
        total += n
    print(f"The sum is : {total}")
sum(7, 9, 10, 20)

#kwargs ---------------------------
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("---curso---")
presentation(name="Python", category="Backend", level="Easy")
presentation(name="Javascript", category="Backend", level="Easy")
presentation(name="Java", category="Backend", level="Medium")