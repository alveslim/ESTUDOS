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
    
    pdf = {} # EXISTE U  PROBLEMA DE SALVAR TODOS OS DADOS JUNTOS
    
    def __init__(self):
        # Inicializa as variáveis de instância como vazias ou None
        self.nome = None
        self.idade = None
        
    
    @property
    def dados(self) -> dict:
        return print("Formatando relatório em PDF...")
        
    @dados.setter
    def dados(self, tupla) -> dict:
        self.nome, self.idade = tupla # desempacota da tupla
        Formatar_PDF.pdf.update({"Nome": f"{self.nome}", "Idade": self.idade}) # transforma em dict

def enviar_por_email(self, destinatario):
        print(f"Enviando relatório para {destinatario}...")
        
class Enviar_Email_Destinatario:
    def __init__(self):
        pass


# teste formartar pdf    
"""pdfJorge = Formatar_PDF()
pdfJorge.dados = ("jorge", 22) # tupla
print(pdfJorge.pdf) # print o dict"""
    
# teste gerar dados    
"""dadoJorge = Gerar_dados()
dadoJorge.saldo = 12.00
dadoJorge.despesas = 14.00
print(dadoJorge.saldo)
print(dadoJorge.despesas)"""
