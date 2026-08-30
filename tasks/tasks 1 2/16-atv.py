"""
Desafio 4: Distribuição de Tarefas no Grupo 2
Foco: 24-function_args.py, 12-tuplas.py, 11-method_list.py
Problema: Crie uma função chamada distribuir_tarefas. 
Ela deve aceitar o nome de um projeto como argumento posicional obrigatório e, 
em seguida, um número indefinido de tarefas usando *args.
A função deve possuir uma tupla interna com os nomes dos membros do seu grupo acadêmico 
(ex: membros = ("Alice", "Bruno", "Você")). Distribua cada tarefa recebida 
sequencialmente entre os membros (a primeira para a Alice, a segunda para o Bruno, 
a terceira para você, a quarta volta para a Alice, e assim por diante). 
Imprima o resultado na tela.
"""

def distribuir_tarefas(nome, *tarefas):
    membros = ("Alice", "Bruno", "Voce")
    total_membros = len(membros)
    print(f"nome do projeto: {nome}")
    
    for indice, tarefa in enumerate(tarefas):
        responsavel = membros[indice % total_membros]
        print(f"Integrante: {responsavel} ficará com a tarefa: {tarefa}")
        
distribuir_tarefas("Projeto Jardinagem", "Reguar", "Plantar", 
                   "Colher", "Adubar", "Podar")

"""
Como o operador % funciona nesse caso:
Tarefa 0: 0 % 3 = 0 -> membros[0] (Alice)
Tarefa 1: 1 % 3 = 1 -> membros[1] (Bruno)
Tarefa 2: 2 % 3 = 2 -> membros[2] (Você)
Tarefa 3: 3 % 3 = 0 -> membros[0] (Alice) — reinicia o ciclo
Tarefa 4: 4 % 3 = 1 -> membros[1] (Bruno)
"""