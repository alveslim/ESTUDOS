"""Desafio: Crie uma classe Produto com o atributo privado __preco. 
Use @property para o getter do preço e a sintaxe @preco.setter para o setter.

O teste final deve ser feito como atributo direto: produto.preco = 150.0 e print(produto.preco)."""

class Produto:
    def __init__(self) -> None:
        self.__preco = None
    
    # 1º: Define o Getter (precisa vir primeiro)
    @property
    def preco(self) -> int:
        return self.__preco

    # 2º: Define o Setter usando @nome_do_getter.setter
    @preco.setter
    def preco(self, preco: int) -> None:
        self.__preco = preco


produto = Produto()
produto.preco = 10       # Chama o @preco.setter
print(produto.preco)     # Chama o @property (getter) -> Imprime 10