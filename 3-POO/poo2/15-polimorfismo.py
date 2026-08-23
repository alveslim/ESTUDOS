"""A palavra Polimorfismo vem do grego: Poli (Muitas) + Morphos (Formas).

Pense no maestro de uma orquestra. Ele olha para o violinista, aponta a batuta e diz:
"Toque!". O músico passa o arco nas cordas. Depois, ele aponta para o baterista e diz 
o exato mesmo comando: "Toque!". O baterista bate as baquetas nos tambores.

O maestro não precisa saber como o instrumento funciona. Ele só dá a mesma ordem (tocar()) 
e cada instrumento responde da sua própria maneira. Isso é Polimorfismo.

No código, é quando objetos de classes diferentes possuem um método com o mesmo nome, mas fazem 
coisas diferentes quando esse método é chamado."""

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
        # e interessante pq nao fere o principio aberto_fechado, pode extender e alterar e
        # e herdar as outras funcoes.
        
def fazer_func() -> None:
    print("Vou fazer algo")
        
obj1 = ClasseQualquer()
obj2 = OutraCoisa()
obj3 = OutraCoisa()
obj3.fazendo = fazer_func

obj1.fazer()
obj2.fazer()
obj3.fazendo()
# ddd