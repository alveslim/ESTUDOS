from abc import ABC, abstractmethod # Criador de classes abstratas
class Pessoa(ABC): # Classe abstrata, nao possui objetos - so pode ser mae (heranca)
    def correr(self):
        print("a pessoa esta correndo de manha")
    
    @abstractmethod # classe filha DEVE criar um metodo trabalhar
    def trabalhar(self):
        pass

class Professor(Pessoa):
    def trabalhar(self):
        print('O professor esta dando aula')

"""p1 = Pessoa() # daria erro
p1.correr"""

p1 = Professor()
p1.trabalhar()
p1.correr()