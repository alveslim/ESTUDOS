class Passaro:
    def __init__(self, name, cor):
        self.name = name
        self.color = cor
    def voar(self):
        print(f"{self.name} esta voando")
    def cor(self):
        print(f"{self.name} tem a cor da plumagem {self.color}")
    
class Pardal(Passaro):    
    def __init__(self):
        super().__init__(self) 
        self.name = "Pardal"
        self.color = "vermelho"
        
    def alimentando(self):
        print(f"O {self.name} esta se alimentando de sementes...")

class Galinha(Passaro):
    def __init__(self):
        super().__init__(self)
        self.galinha = "galinha"
        
    def voar(self):
        print(f"A {self.name} nao consegue voar")

pardal = Pardal()
pardal.voar()
pardal.alimentando()
pardal.cor()
print("\n=============\n")
galinha = Galinha()
galinha.voar()