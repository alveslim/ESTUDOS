import time
import os

def limpar_tela():
    # 'nt' significa Windows (New Technology)
    if os.name == 'nt':
        os.system('cls')
    else:
        # Para Mac e Linux (posix)
        os.system('clear')

# --- BLOCO DOS "ESPECIALISTAS" (FUNÇÕES) ---

def calcular_soma():
    print("\n--- INICIANDO SOMA ---")
    # Aqui usamos try/except para evitar erro se digitar letra
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"RESULTADO: {n1} + {n2} = {n1 + n2}")
    except ValueError:
        print("Erro: Você precisa digitar números!")
    
    input("\nPressione ENTER para voltar...") # Pausa para ler


def mostrar_ajuda():
    print("\n--- AJUDA DO SISTEMA ---")
    print("Este programa serve para demonstrar funções.")
    print("Versão 1.0 - Desenvolvido em Python.")
    print("Contate o suporte: admin@exemplo.com")
    
    input("\nPressione ENTER para voltar...")


def configurar_sistema():
    print("\n--- CONFIGURAÇÕES ---")
    print("Carregando preferências...")
    time.sleep(1.5) # Finge que está processando
    print("Sistema configurado com sucesso!")
    
    input("\nPressione ENTER para voltar...")


# --- BLOCO DO "GERENTE" (MENU PRINCIPAL) ---

def menu_principal():
    while True:
        limpar_tela() # <--- O SEGREDO ESTÁ AQUI
        # A tela é limpa antes de desenhar o menu novamente
        
        print("=== SISTEMA MODULAR ===")
        print("1. Calcular Soma")
        print("2. Ajuda")
        print("3. Configurações")
        print("4. Sair")
        
        opcao = input(">>> Escolha uma opção: ")

        if opcao == "1":
            calcular_soma() # O código "pula" para a linha 5
            
        elif opcao == "2":
            mostrar_ajuda() # O código "pula" para a linha 18
            
        elif opcao == "3":
            configurar_sistema() # O código "pula" para a linha 27
            
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break # Quebra o loop e encerra
            
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(1) # Dá tempo de ler o erro antes de limpar

# --- INÍCIO DO PROGRAMA ---
# É aqui que tudo começa. Chamamos apenas o gerente.
if __name__ == "__main__":
    menu_principal()