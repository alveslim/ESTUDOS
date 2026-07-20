class Minhaclasse:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor: type) -> None:
        self.__valor = valor

    def getter(self) -> type:
        return self.__valor
    
minhaclasse = Minhaclasse()
minhaclasse.setter(10)
valor = minhaclasse.getter()
print(minhaclasse.getter())
print(valor)