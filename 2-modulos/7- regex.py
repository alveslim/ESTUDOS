import re
#expressao regular
# - indice inicial e final de palavras
text = "OneBitCode: Transformamos pessoas em programadores sem limites"
# - O r significa que estamos trabalhando com uma string bruta (raw string)
match = re.search(r'OneBitCode', text)
print('Indice inicial ', match.start())
print('Indice final ', match.end())

# - buscando o indice que possui o ponto

site = 'google.com'
# Sem usar a \\
match = re.search(r'\.', site)
print(match)

# - buscando uma lista de caracteres dentro de uma frase
pattern = "[A-Z]"
result = re.findall(pattern, text)
print(text)
print(result)

# - verificando o inicio de uma string
rule = r'^A'
phrases =  ['A casa esta suja', 'O homem ama', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Nãp corresponde: {f}")
        
# - verificando o final de uma string
rule_end = r'!$'
phrases2 = 'Corre!'
match = re.search(rule_end, phrases2)
if match:
    print("Matching")
else:
    print("No match")