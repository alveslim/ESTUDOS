"""3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
#Factorial de um número usando recursão

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

number = int(input("Digite o número para fatorial:\n"))
print(f"O fatorial de {number} é: {factorial(number)}")

print("\n-----------------\n")
#$um fact

def total_sum(num):
    if num == 1:
        return 1
    else:
        return num + total_sum(num - 1)
    
number = int(input("Type a number to sum up to:\n"))
print(f"The total sum up to {number} is: {total_sum(number)}")