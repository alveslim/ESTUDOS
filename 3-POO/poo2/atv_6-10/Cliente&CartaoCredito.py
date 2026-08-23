class CartaoCredito:
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite
        
    def passar_compra(self, valor: float) -> bool:
        if valor <= self.limite:
            return print("Aprovado")
        else:
            return print('Negado')
        
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        
    def fazer_compra(self, cartao: CartaoCredito, valor: float):
        cartao.passar_compra(valor)
        
BlackCard = CartaoCredito(1223, 500.00)
GoldenCard = CartaoCredito(1225, 600.00)
AnaDulce = Cliente('A. Dulce')
AnaDulce.fazer_compra(BlackCard, 500.01)
AnaDulce.fazer_compra(GoldenCard, 500.01)
