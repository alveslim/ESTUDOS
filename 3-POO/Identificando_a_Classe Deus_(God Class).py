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

class RelatorioFinanceiro:
    def gerar_dados(self):
        return {"saldo": 5000, "despesas": 1200}
    
    def formatar_pdf(self, dados):
        print("Formatando relatório em PDF...")
        
    def enviar_por_email(self, destinatario):
        print(f"Enviando relatório para {destinatario}...")
        
class Gerar_dados:
    def __init__(self):
        pass
    
    @property
    def dados(self, dados) -> float:
        self.dados = dados
        return self.dados
        
    @dados.setter
    def dados(self, saldo, despesas) -> float:
        self.saldo = saldo
        self.despesas = despesas

class Formatar_PDF:
    
    pdf = {}
    
    def __init__(self):
        pass
    
    @property
    def dados(self, dados) -> dict:
        self.dados = dados
        return self.dados
        
    @dados.setter
    def dados(self, nome, idade) -> dict:
        self.nome = nome
        self.idade = idade
        Formatar_PDF.pdf["nome"] = self.nome
    
pdfJorge = Formatar_PDF()
pdfJorge.dados = "jorge", 22
print(pdfJorge.pdf)
    
    
"""dadoJorge = Gerar_dados()
dadoJorge.saldo = 12.00
dadoJorge.despesas = 14.00
print(dadoJorge.saldo)
print(dadoJorge.despesas)"""
