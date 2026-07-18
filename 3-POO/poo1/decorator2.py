#Criaando decorators em Python

# Exemplo de um decorator simples que adiciona comportamento antes e depois da execução de uma função

def my_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

# Exemplo de um decorator que transforma o 
# retorno de uma função em maiúsculas

def uppercase_decorator(function):
    def wrapper():
        func = function()             # 1. Executa a função original e guarda o texto
        make_uppercase = func.upper() # 2. Pega o texto e aplica o método .upper()
        return make_uppercase         # 3. Retorna o texto já transformado
    return wrapper

# Exemplo de um decorator que divide uma 
# string retornada por uma função em uma lista de palavras

def split_string(function):
    def wrapper():
        func = function()                # 1. Executa a função e recebe a string
        splitted_string = func.split()   # 2. Divide a string nos espaços em branco
        return splitted_string           # 3. Retorna uma Lista (ex: ["Olá", "Mundo"])
    return wrapper
