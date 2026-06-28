from random import *

usr_password = input("Digite a senha: ")
crack = ""

password = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y',]

while crack != usr_password:
    crack = ""
    for i in range(len(usr_password)):
        crack_letter = password[randint(0, len(password) - 1)]
        crack += crack_letter
    print(crack)
    
print("Senha encontrada: ", crack)