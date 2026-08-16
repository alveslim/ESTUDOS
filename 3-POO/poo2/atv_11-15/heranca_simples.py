class Passaro:
    def __init__(self, name, cor, tamanhoasa):
        self.name = name
        self.color = cor
        self.tamanhoasa = tamanhoasa
        
    def voar(self):
        print(f"{self.name} esta voando")
    
    def cor(self):
        print(f"{self.name} tem a cor da plumagem {self.color}")
    
    def tamanho_asa(self):
        print(f"tamanho da asa é {self.tamanhoasa}")

########## classes filhas:
        
class Pardal(Passaro):
    def __init__(self):
        super().__init__("Pardal", "Azul", "Grande")
        
    def alimentando(self):
        print(f"O {self.name} esta se alimentando de sementes...")
        
class Galinha(Passaro):
    def __init__(self):
        super().__init__("Galinha", "Marrom", "Pequena")
        
    def voar(self):
        print(f"A {self.name} nao consegue voar")

# acao:

pardal = Pardal()
pardal.voar()
pardal.alimentando()
pardal.cor()
pardal.tamanho_asa()

print("\n=============\n")

galinha = Galinha()
galinha.voar()
galinha.cor()