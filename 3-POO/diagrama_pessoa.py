class Pessoa:
    def __init__(self, nome, altura, idade):
        self.nome = nome
        self.altura = altura
        self.idade = idade
    
    def correr(self):
        print(f"{self.nome} está correndo")
    
    def comer (self):
        print(f"{self.nome} está comendo")
        
        