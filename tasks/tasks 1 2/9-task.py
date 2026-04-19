#Advinhe o Número

#Escreva um programa em Python que gera um número aleatório para que o usuário 
#tente acertar o número. Algumas sugestões para o programa:

    #Utilizar um laço de repetição para que o programa execute até que o usuário 
    #informe um número referente a opção para sair do programa.
    
    #Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. 
    #Ex: 1 a 10.
    
    #Lê o número que o usuário digitar via input e comparar se é o mesmo número que 
    #o programa sorteou.
    
import random

random_number = random.randint(0, 10)

while True:
    user_number = int(input("Type a number between 0 and 10 (or -1 to exit): "))
    if user_number == -1:
        print("Exiting the game. Gooodbye!")
        break
    elif user_number == random_number:
        print(f"Congratylations! You guerssed the number! {random_number} was the correct answer.")
    elif user_number < random_number:
        print("Too low! Try again.")
    else:        
        print("Too high! Try again.")
    if user_number != random_number:
        print("Wrong guess! Try again.")


