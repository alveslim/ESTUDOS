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
        
class GerarDados:
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

class FormatarPDF:
    
    pdf = {} # EXISTE U  PROBLEMA DE SALVAR TODOS OS DADOS JUNTOS
    
    def __init__(self):
        # Inicializa as variáveis de instância como vazias ou None
        self.nome = None
        self.saldo = None
        self.despesas = None
        
    @property
    def dados(self) -> None:
        return dict
        dadosdict = {}
    @dados.setter
    def dados(self, tupla) -> dict:
        self.nome, self.saldo, self.despesas = tupla # desempacota da tupla
        FormatarPDF.pdf.update(
            {f"{self.nome}": {
                "Saldo": self.saldo,
                "Despesa": self.despesas
            }}) # transforma em dict
    
# teste formartar pdf  FormatarPDF  
pdfCarla = FormatarPDF()
pdfCarla.dados = ("carla", 10000.00, 2000.00)
#print(pdfJorge.pdf) # print o dict
#print(pdfCarla.pdf) # esta printando todos
print("email sendo enviado...")
print(FormatarPDF.pdf["carla"]) # nao ta printando o nome...
print("email enviado")

class EnviarEmail:
    def __init__(self):
        pass

    def __str__(self):
        pass

    
# teste gerar dados    
dadoJorge = GerarDados()
dadoJorge.saldo = 12.00
dadoJorge.despesas = 14.00
pdfJorge = FormatarPDF()
pdfJorge.dados = ("jorge", dadoJorge.saldo, dadoJorge.despesas) # tupla
print("email sendo enviado...")
print(FormatarPDF.pdf["jorge"]) # nao ta printando o nome...
print("email enviado")