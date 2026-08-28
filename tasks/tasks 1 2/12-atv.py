"""
Desafio 1: Monitoramento de Carga Fluvial (BotoBot)
Foco: 19-while.py, 10-listas.py, 16-if_else.py, 3-input.py
Você precisa programar a lógica principal de controle de peso de um robô coletor de resíduos em rios.
Problema: Crie um loop infinito que simule a navegação. A cada iteração, peça ao usuário para inserir o peso (em kg) 
de um novo item de lixo coletado. Adicione esse valor a uma lista. Calcule a soma total a cada nova inserção. Se a soma 
atingir ou ultrapassar 50kg, interrompa o loop (usando break), imprima a lista de todos os pesos coletados e exiba a mensagem: 
"Capacidade máxima atingida. Retornando à base para descarregar."
"""
cacamba_peso = []
cacamba_peso = []
peso_total = 0

while peso_total < 50:
    lixo = int(input("Insira o peso do resíduo (ou -1 para abortar): "))
    
    # Verifica a condição de parada ANTES de mexer nos dados
    if lixo == -1:
        print("Operação abortada pelo usuário.")
        break 
        
    cacamba_peso.append(lixo)
    
    # Forma mais eficiente de somar: pega o peso atual e soma com o novo lixo
    peso_total += lixo 
    
    # A verificação de status acontece apenas uma vez por inserção
    if peso_total < 50:
        print(f"Navegando... Carga atual: {peso_total}kg. Itens coletados: {len(cacamba_peso)}\n")
    elif peso_total == 50:
        print("Atingiu o peso limite exato de 50kg!")
    else:
        print(f"Alerta: Ultrapassou o peso limite! Carga final: {peso_total}kg")
    
print("voltando para o porto...")
print(cacamba_peso)
