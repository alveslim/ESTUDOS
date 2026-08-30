"""
Desafio 2: Filtro de Compatibilidade de Hardware
Foco: 14-dicionarios.py, 20-list_comprehsion.py, 18-for.py
Problema: Dada a lista de dicionários abaixo, escreva uma lógica de apenas uma linha usando l
ist comprehension para gerar uma nova lista. Esta nova lista deve conter apenas os nomes das 
placas-mãe que possuam o soquete "AM5" para evitar problemas de compatibilidade em um setup novo.

Python:

"""

componentes = [
    {"nome": "B450M", "tipo": "Placa-Mãe", "soquete": "AM4"},
    {"nome": "Ryzen 5 5600", "tipo": "CPU", "soquete": "AM4"},
    {"nome": "B650M", "tipo": "Placa-Mãe", "soquete": "AM5"},
    {"nome": "X670E", "tipo": "Placa-Mãe", "soquete": "AM5"},
    {"nome": "RTX 4060", "tipo": "GPU", "soquete": "N/A"}
]

#am4 = [i for i in componentes if componentes[i]['soquete'] == 'AM4' in i]

placas_am4 = [{"Produto": item["nome"], "Soquete": item['soquete']} for item in componentes if item['soquete'] == 'AM5' and item['tipo'] == 'Placa-Mãe']
#print(placas_am4)
##for placa in placas_am4:
#    print(placa['Produto'])
#print(placas_am4[0]['Produto']) 


cpus_am4 = [{"Produto": item["nome"], "Soquete": item['soquete']} for item in componentes if item['soquete'] == 'AM4' and item['tipo'] == 'CPU']
#print(cpus_am4)

for placa in placas_am4:
    for cpu in cpus_am4:
        if placa['Soquete'] != cpu['Soquete']:
            print(f"Problema na compatibilidade da {placa['Produto']} com a {cpu['Produto']}")