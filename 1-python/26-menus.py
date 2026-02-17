print("=== MENU PRINCIPAL ===")
print("1. Calcular Soma")
print("2. Ver Data Atual")
print("3. Sair")

# Captura a opção como texto (string) para evitar erros se o usuário digitar letras
opcao = input("Qual opção deseja escolher? (1, 2 ou 3): ")

# Bloco de decisão
if opcao == "1":
    print("\n--- Você escolheu a Opção 1 ---")
    # Aqui iria o seu código de soma
    print("Executando bloco de soma...")

elif opcao == "2":
    print("\n--- Você escolheu a Opção 2 ---")
    # Aqui iria o seu código de data
    print("Mostrando a data...")

elif opcao == "3":
    print("\nSaindo do programa...")

else:
    print("\nOpção inválida! Por favor, digite 1, 2 ou 3.")
    
#Metodo moderno case

print("1. Iniciar Jogo")
print("2. Carregar Jogo")
print("3. Configurações")

opcao = input("Escolha uma opção: ")

match opcao:
    case "1":
        print("Iniciando o jogo...")
        # Código do bloco 1 aqui
    case "2":
        print("Carregando save...")
        # Código do bloco 2 aqui
    case "3":
        print("Abrindo configurações...")
        # Código do bloco 3 aqui
    case _:
        # O "case _" funciona como o "else" (padrão)
        print("Opção não reconhecida.")
        
# Dica Profissional: O Menu "Infinito" (while True)        

import time # Apenas para dar um efeito de espera

while True:
    print("\n--- MENU DO SISTEMA ---")
    print("1. Falar Oi")
    print("2. Falar Tchau")
    print("3. Encerrar Programa")
    
    escolha = input(">>> ")

    if escolha == "1":
        print("Olá, usuário!")
        time.sleep(1) # Espera 1 segundo antes de voltar ao menu
        
    elif escolha == "2":
        print("Até logo!")
        time.sleep(1)
        
    elif escolha == "3":
        print("Encerrando...")
        break # O comando 'break' quebra o loop e fecha o programa
        
    else:
        print("Opção inválida, tente novamente.")