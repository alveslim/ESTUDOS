"""3. Propriedade Somente Leitura (Read-Only)

Uma das maiores vantagens do @property é criar atributos que só podem ser lidos, mas nunca alterados 
diretamente de fora.

Desafio: Crie uma classe Retangulo que recebe largura e altura no __init__.

    Crie uma @property chamada area que calcula e retorna largura * altura.

    Não crie um setter para area.

    Tente fazer retangulo.area = 50 no final do código e observe o erro retornado pelo Python."""

class Retangulo:
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura

    @property
    def area(self) -> int:
        return self.largura * self.altura
    
retangulo = Retangulo(10, 5)
print(retangulo.area)