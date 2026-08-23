# boa convencao para uitilizar herancas

class Animal:
    def alimentar(self):
        print("O animal esta ser alimentando")
        
class Cachorro(Animal): # Funcionamento normal
    def latir(self):
        print('O cachhorro esta latindo')
    def nadar(self):
            print('O cachorro esta nadando')
        
class Peixe(Cachorro): # quebra na substituicao de Liskov
    def nadar(self):
        print('O peixe esta nadando')
        
    def latir(self): # Polimorfismo # Comportamento diferente entre a classe mae e a classe filha
        print('Erro: ')
        raise Exception("Peixa nao late")

def verificar_animal(animal: any):
    animal.nadar()
    
ob1 = Animal()
ob2 = Cachorro()
ob3 = Peixe()
verificar_animal(ob3)
    
"""nemo = Peixe()
nemo.latir()"""