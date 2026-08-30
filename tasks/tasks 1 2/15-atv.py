"""
Contexto: Um robô fluvial de coleta de resíduos envia pacotes de telemetria contendo três 
sensores por segundo. O controlador precisa ler esses dados e disparar ações imediatas 
baseadas em uma árvore de prioridade.
Problema: Dada a lista de leituras abaixo, crie uma list comprehension que gere uma nova 
lista de "Comandos".
A regra de decisão segue esta prioridade estrita (se a condição 1 for verdadeira, 
ignore as outras; se for falsa, teste a 2, etc.):

    Se a bateria for menor ou igual a 15, o comando é "Retornar à base".

    Se a distância do sensor_frontal for menor que 20 cm, o comando é "Desviar obstáculo".

    Se a carga (peso_kg) for maior ou igual a 50, o comando é "Descarregar caçamba".

    Se nenhum alerta for acionado, o comando é "Avançar"
"""
telemetria = [
    {"bateria": 80, "peso_kg": 20, "sensor_frontal": 150},
    {"bateria": 50, "peso_kg": 40, "sensor_frontal": 15},
    {"bateria": 45, "peso_kg": 55, "sensor_frontal": 100},
    {"bateria": 10, "peso_kg": 60, "sensor_frontal": 10}
]

# Filtra apenas os dispositivos que possuem algum alerta
rule = [
    item for item in telemetria 
    if item["bateria"] <= 15 or item["peso_kg"] >= 50 or item["sensor_frontal"] <= 20
]

print("--- ALERTAS ---")
for item in rule:
    # Usando 'if' separado para exibir múltiplos alertas no mesmo dispositivo
    if item["bateria"] <= 15:
        print(f"Bateria: {item['bateria']}% - voltar para o porto")
    if item["peso_kg"] >= 50:
        print(f"Peso em {item['peso_kg']}kg: excesso de carga")      
    if item["sensor_frontal"] <= 20:
        print(f"Sensor em {item['sensor_frontal']}: obstáculo próximo")

print("\n--- STATUS GERAL ---")
for item in telemetria:
    # Condição segura para operar
    if item["bateria"] > 15 and item["peso_kg"] < 50 and item["sensor_frontal"] > 20:
        print(f"Dispositivo OK ({item}): Avançar")