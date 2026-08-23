class MaquininhaCartao:
    def processar_transacao(self, valor: float) -> bool:
        print(f'Processando R${valor:.2f} na maquininha')
        return False
    
class CaixaLoja:
    def __init__(self, maquininha: MaquininhaCartao):
        self.__maquininha = maquininha
        
    def fechar_compra(self, valor_total: float) -> None:
        if self.__maquininha.processar_transacao(valor_total): # <-- if direto e limpo
            print("Compra finalizada com sucesso!!")
        else:
            print("Transação negada!")
            
MaquininhaMini = MaquininhaCartao()
CaixaDB = CaixaLoja(MaquininhaMini)
CaixaDB.fechar_compra(150.00)

"""
sucesso = self.__maquininha.processar_transacao(valor_total)
        if sucesso == True:
            print('Compra finalizada com sucesso!!')
        else:
            print('Transacao negada!')
"""