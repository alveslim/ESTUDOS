class ClasseQualquer:
    def fazer(self) -> None:
        print("EU vou fazer algo")
    def fazendo(self) -> None:
        print("Estou fazendo algo")
        
class OutraCoisa(ClasseQualquer):
    def preparar(self) -> None:
        print("Estou preparando algo")
    def fazer(self) -> None:
        print("Estou fazendo outra coisa") # sobreescrevendo no primeiro fazer()
        
def fazer_func() -> None:
    print("Vou fazer algo")
        
obj1 = ClasseQualquer()
obj2 = OutraCoisa()
obj3 = OutraCoisa()
obj3.fazendo = fazer_func

obj1.fazer()
obj2.fazer()
obj3.fazendo()