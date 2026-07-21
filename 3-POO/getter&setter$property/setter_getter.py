class Minhaclasse:
    def __init__(self) -> None:
        self.__valor = None
    
    def setter(self, valor: type) -> None:
                    # L>> valor: int // serve para nivel de interacao con outro usuario
                    # L>> mesmo definindo como int, pode ser settado minhaclasse.setter("abc12")
                    # LL>> ira printar normalmente

        self.__valor = valor

    def getter(self) -> type:
        return self.__valor
    
minhaclasse = Minhaclasse()
minhaclasse.setter(10)
valor = minhaclasse.getter()
print(minhaclasse.getter())
print(valor)