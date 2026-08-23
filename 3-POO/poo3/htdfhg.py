rows = [['3','Ana','30'], ['1','Bruno','25'], ['2','Carlos','40']]

print(sorted(rows, key=lambda r: r[0]))
# -----------------------------------------------------------------------------
import csv

with open('seu_arquivo.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Construção que cria o dicionário mapeando 'id' -> linha inteira:
    dados_por_id = {row['id']: row for row in reader} 
    
# ==

{row['id']: row for row in csv.DictReader(open('seu_arquivo.csv'))} 

# -----------------------------------------------------------------------------

sorted(contatos.items(), key=lambda x: x[1], reverse=True)