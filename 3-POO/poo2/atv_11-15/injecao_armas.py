"""njeção de Armas: Crie uma classe Arma com o método atacar(). 
Crie uma classe Guerreiro que receba uma Arma em seu construtor. 
Teste criar armas diferentes (Espada, Machado) e injetá-las no guerreiro."""

class Arma:
    def __init__(self, nome):
        self.arma = nome
    
    def atacar(self):
        print(f"O Guerreiro esta atacando com uma {self.arma}")

class Guerreiro:
    def __init__(self, arma : Arma):
        self.arma = arma

    def usar_arma(self):
        self.arma.atacar()

espada = Arma("espada")
machado = Arma("machado")

guerreiro = Guerreiro(espada)
guerreiro2 = Guerreiro(machado)

guerreiro.usar_arma()
guerreiro2.usar_arma()


