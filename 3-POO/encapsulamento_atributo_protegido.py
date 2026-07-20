"""4. Encapsulamento com Atributo Protegido (_) vs Privado (__)

No Python, por convenção da comunidade, costuma-se usar apenas um underline (_valor) para indicar que algo 
é privado/interno, em vez de dois (__valor), evitand do o Name Mangling (mangling de nomes).

Desafio: Reescreva a sua classe original Minhaclasse alterando o atributo de self.__valor para self._valor.

    Implemente a @property e o @valor.setter.

    Adicione um print dentro do getter e do setter indicando quando cada um está sendo chamado."""

class Minhaclasse:
    def __init__(self, valor)-> None:
        self._valor = valor

    @property
    def valor(self) -> type:
        print("calling getter...")
        return print(f"Valor: {self._valor}")
    
    @valor.setter
    def valor(self, valor: type) -> type:
        print("calling setter")
        self._valor = valor

"""-----------------------------------------------------------------------"""

my_class = Minhaclasse(5)
my_class.valor = 10
print(my_class.valor)