gamesTuple = ("Soccer", "Basketball", "Tennis", "Baseball", "Hockey")
print(gamesTuple)
name = ("John")
list = ["John"]
print(type(name))
print(type(list))
print(type(gamesTuple))
# -  nao possibilita adicionar, remover ou alterar itens
# - permite acesso aos itens por indice e fatiamento
# - permite metodos de contagem e busca de indice
# Acessando itens da tupla
print(gamesTuple[:2])
print(gamesTuple[-1])
print(gamesTuple[3:])

# Metodos de tuplas
print(gamesTuple.index("Tennis")) 

"""Observe a classe abaixo. Ela viola o Princípio da Responsabilidade Única 
acumulando múltiplas funções:

class RelatorioFinanceiro:
    def gerar_dados((self):
        return {"saldo": 5000, "despesas": 1200}
    
    def formatar_pdf(self, dados):
        print("Formatando relatório em PDF...")
        
    def enviar_por_email(self, destinatario):
        print(f"Enviando relatório para {destinatario}...")

Sua tarefa: Refatore o código acima separando-o em 3 classes distintas, 
onde cada uma tenha apenas um motivo para mudar (Ex: uma para os dados, 
outra para formatação e outra para envio).
"""