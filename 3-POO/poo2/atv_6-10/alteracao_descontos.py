class Produto:
    desconto_padrao = 10 # (10%)
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco =  preco
        
    def calcular_preco_final(self) -> float:
        self.result = self.preco - ((self.preco * self.desconto_padrao) / 100)
        return print(f"{self.nome}: {self.result}")
    
    @classmethod
    def atualizar_desconto(cls, novo_desconto) -> float:
        cls.desconto_padrao = novo_desconto
        print("\n---Desconto Atualizado---\n")
    
PalmaBanana = Produto('Banana', 12.00)
CachosDeUva = Produto('Uvas', 8.00)
PalmaBanana.calcular_preco_final()
CachosDeUva.calcular_preco_final()

Produto.atualizar_desconto(5)
# print(Produto.desconto_padrao)
PalmaBanana.calcular_preco_final()
CachosDeUva.calcular_preco_final()

