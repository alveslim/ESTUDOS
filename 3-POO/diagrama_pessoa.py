class Pessoa:
    def __init__(self, nome, altura, idade):
        self.nome = nome
        self.altura = altura
        self.idade = idade
    
    def correr(self):
        print(f"{self.nome} está correndo")
    
    def comer (self):
        print(f"{self.nome} está comendo")
        
minha_pessoa = Pessoa("Flavio", 1.75, 18)
minha_pessoa.correr()
minha_pessoa.comer()
print(f"{minha_pessoa.nome} tem {minha_pessoa.altura} de altura e {minha_pessoa.idade} anos de idade")