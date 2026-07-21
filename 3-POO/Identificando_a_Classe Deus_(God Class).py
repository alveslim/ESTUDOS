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
    