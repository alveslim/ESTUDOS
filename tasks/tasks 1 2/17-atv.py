"""
Desafio 5: Limpeza de Dados de Formulário
Foco: 15-dict_aninhados.py, 25-function_Lambda.py, 5-operators_Strings.py
Problema: Você recebeu um payload JSON (simulado como um dicionário aninhado) de um formulário de feedback de alunos, mas os dados estão sujos antes de irem para uma planilha.

Escreva um loop que passe por cada chave do dicionário principal. Use métodos de string para formatar o nome do aluno corretamente (iniciais em maiúsculo) e converta a string da nota para um número inteiro puro (removendo espaços). Atualize o próprio dicionário com os valores limpos.
"""

feedbacks = {
    101: {"aluno": "jOãO sIlva", "nota_seguranca": " 95 "},
    102: {"aluno": "MARIA souza", "nota_seguranca": "88"},
}