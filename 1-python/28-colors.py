#O Código "Versão Final" (Menu, Funções, Limpeza e Cores)
"""Para fechar com chave de ouro, vamos adicionar as cores que mencionei. 
No terminal, usamos códigos chamados ANSI Escape Sequences. 
Eles parecem estranhos à primeira vista, mas funcionam como "etiquetas" 
que dizem ao terminal: "a partir daqui, pinte de vermelho"."""

import os
import time

# --- CORES ---
VERMELHO = '\033[31m'
VERDE    = '\033[32m'
AZUL     = '\033[34m'
CIANO    = '\033[36m'
RESET    = '\033[0m' # Importante: Volta para a cor padrão

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# --- FUNÇÕES ---

def calcular_soma():
    limpar_tela()
    print(f"{AZUL}=== MÓDULO DE SOMA ==={RESET}\n")
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"\n{VERDE}SOMA: {n1} + {n2} = {resultado}{RESET}")
    except ValueError:
        print(f"\n{VERMELHO}Erro: Digite apenas números!{RESET}")
    
    input(f"\n{CIANO}Pressione ENTER para voltar...{RESET}")

def menu_principal():
    while True:
        limpar_tela()
        print(f"{CIANO}==============================")
        print(f"      MEU SISTEMA PYTHON      ")
        print(f"=============================={RESET}")
        print(f"{VERDE}1.{RESET} Somar Números")
        print(f"{VERDE}2.{RESET} Ajuda")
        print(f"{VERMELHO}3. Sair{RESET}")
        
        opcao = input(f"\n{AZUL}>>> Escolha:{RESET} ")

        if opcao == "1":
            calcular_soma()
        elif opcao == "2":
            limpar_tela()
            print(f"{AZUL}--- AJUDA ---{RESET}")
            print("Sistema funcional com cores e limpeza de tela.")
            input(f"\n{CIANO}Pressione ENTER para voltar...{RESET}")
        elif opcao == "3":
            print(f"{VERMELHO}Encerrando...{RESET}")
            break
        else:
            print(f"{VERMELHO}Opção Inválida!{RESET}")
            time.sleep(1)

# --- O INTERRUPTOR ---
if __name__ == "__main__":
    menu_principal()
    
"""O que mudou?

    Variáveis de Cor: Criamos constantes como VERMELHO = '\033[31m'.

    O RESET: Sempre que você usa uma cor, precisa colocar o {RESET} no final da frase, 
    senão o terminal continuará pintando tudo o que vier depois daquela mesma cor 
    (até o seu nome de usuário no terminal ficará colorido!).

    Visual: O menu agora separa visualmente o que é instrução (Ciano/Azul), 
    4o que é sucesso (Verde) e o que é perigo/saída (Vermelho)."""