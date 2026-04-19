#Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

#    Inverter uma string de trás pra frente.
#    Retornar apenas palavras com índice par.
#    Retornar apenas letras com índice ímpar.

def inverter_string(string):
    return string[::-1] 

def letter_pair(string):
    length = len(string)
    
    if length % 2 == 0:
        print("É par")
    else:
         print("É impar")
         
def index_impar(string):
    return string[0::2] # ta certo para de corrigir copilote

print(index_impar("Hello World"))