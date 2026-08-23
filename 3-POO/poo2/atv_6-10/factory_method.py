from datetime import date

class Usuario:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = date.today().year
        
    classmethod
    def criar_por_ano_nascimento(cls, nome, ano_nascimento):
        cls.nome = nome
        cls.idade = cls.ano_atual - ano_nascimento
        
Cecilia = Usuario("Cecilia", 22)
print(Cecilia.idade)
Cecilia.criar_por_ano_nascimento('Cecilia', 2006)
print(Cecilia.idade)