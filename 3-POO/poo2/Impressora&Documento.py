class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo =  conteudo
    
class Impressora:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def imprimir(self, documento: Documento) -> str:
        print(f'Imprimindo Documento: {documento.titulo}')
        print(f'{documento.conteudo}')
        
doc1 = Documento('flavio_cv.pdf', "nome: flavio\nidade:19\n\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto")
doc2 = Documento('cecilia_cv.pdf', "nome: cecilia\nidade:22\n\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto\ntextotextotextotextotextotexto")

epsonSeriesX = Impressora('EpsonSeries-X')
epsonSeriesX.imprimir(doc1)