class Veiculo:
    def __init__(self, modelo: str, estado: bool = False) -> None:
        self.modelo = modelo
        self.estado = estado
        
    def ligar(self) -> bool:
        if self.estado == True:
            print(f'{self.modelo} já está ligado')
        else:
            self.estado = True
            self.frase = (f"{self.modelo} foi ligado")
    
    def desligar(self) -> bool:
        if self.estado == False:
            print(f'{self.modelo} já está Desligado')
        else:
            self.estado = False
            self.frase = (f"{self.modelo} foi desligado")
            
class Motorista:
    def __init__(self, nome: str):
        self.nome = nome
    
    def dar_partida(self, veiculo: Veiculo):
        veiculo.ligar()
        print(f"{self.nome}: {veiculo.frase}")
    
    def desligar_veiculo(self, veiculo: Veiculo):
        veiculo.desligar()
        print(f"{self.nome}: {veiculo.frase}")

taxi = Veiculo('Fusca')

taxista1 = Motorista('Antonio')
taxista1.dar_partida(taxi)
taxista1.dar_partida(taxi)
taxista1.desligar_veiculo(taxi)
    