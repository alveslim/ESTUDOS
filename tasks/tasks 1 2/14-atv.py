"""
Desafio 3: Validador de Senha para Gincana Infantil
Foco: 9-metodos_string.py, 21-funcoes.py, 17-elif.py
Para uma atividade de segurança digital voltada para crianças, você precisa validar 
as senhas de forma simples, sem usar RegEx.
Problema: Escreva uma função que receba uma string. Ela deve iterar sobre a string ou 
usar métodos nativos e retornar True apenas se cumprir todas as regras abaixo, 
ou False caso falhe em qualquer uma:

    Ter pelo menos 6 caracteres.

    Não conter nenhum espaço em branco.

    Conter pelo menos um número.

    Conter pelo menos uma letra.
"""

def validar_senha(senha):
    
    total_digitos = len(senha)
    if total_digitos < 6:
        print("precisa ter ao menos 6 digitos!")
        return False
        
    if " " in senha:
        print('Nao pode conter espaco em branco')
        return False
        
    letters = 0
    numbers = 0
    # contador letras e numeros 
    for char in senha:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1            
    if letters <= 0:
        print("deve conter pelo menos uma letra")
        return False       
    if numbers <= 0:
        print("deve conter pelo menos um numero")
        return False
    return True 
        
while True:
    password = input("\nEscreva a senha: ")
    if validar_senha(password):
        print("Senha cadastrada com sucesso!")
        break