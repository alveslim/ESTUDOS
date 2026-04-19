#Verificar conteúdo da String
#Escreva um programa em Python para verificar se uma string 
#contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

import re

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)
    
print(check_character("HelloWorld123")) # None, pois a string contém apenas os caracteres permitidos
print(check_character("Hello World!")) # <re.Match object; span=(5, 6), match=' '> , pois a string contém um espaço e um ponto de exclamação, que não são permitidos
