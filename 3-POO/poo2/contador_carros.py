class Carro:
    total_carros = 0
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
        # Carro.total_carros =+ 2 erro, o numero comtinua 2
        Carro.total_carros += 1
        
    @classmethod
    def exibir_total_carros(cls) -> int:
        print(cls.total_carros)
    
carro = Carro('Fiat', 'Uno')
carro1 = Carro('Honda', 'Fit')
Carro.exibir_total_carros()
