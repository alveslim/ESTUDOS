class Minhaclasse:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor: int) -> None:
        self.__valor = valor

    @property # nosso atributo ficara "mascarado"
    def getter(self) -> int:
        return self.__valor
    
minhaclasse = Minhaclasse()
minhaclasse.setter(10)
print(minhaclasse.getter) # --> retornando o valor None ditado no init
# L>> o getter vai poder ser chamdo como um atributo