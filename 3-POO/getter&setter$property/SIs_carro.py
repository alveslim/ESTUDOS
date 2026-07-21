class carro:
    def __init__(self, modelo, velocidade) -> None:
        self.modelo = modelo
        self.__velocidade = velocidade
        
    def __injetar_combustivel(self, quantidade):
        print(f"Injetando {quantidade}ml de combustivel...")
        
    def acelerar(self):
        self.__injetar_combustivel(50)
        while self.__velocidade < 50:
            self.__velocidade += 10
            print(f"{self.__velocidade}km/h")
        
skyline = carro("skyline R#4", 0)
skyline.acelerar()