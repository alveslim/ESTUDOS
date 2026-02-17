"""Lendo n linhas de um arquivo

Escreva um programa Python para ler as 
primeiras n linhas de um arquivo.

O nome do arquivo e a quantidade de 
linhas devem ser passadas via parâmetro 
na função."""

def file_read_from_line(fname, nlines): #fname = nome do arquivo, nlines = quantidade de linhas a ler
    from itertools import islice # importa a função islice do módulo itertools, que permite iterar sobre um arquivo a partir de uma linha específica
    with open(fname, "r", encoding="utf-8") as file:
        for line in islice(file, nlines): # para cada linha do arquivo, a partir da linha nlines, imprima a linha sem o caractere de nova linha
            print(f"---{line.rstrip()}---")

file_read_from_line("4-Manipulando_arquivos/2-names.txt", 6)


