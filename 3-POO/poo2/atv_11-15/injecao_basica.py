import time
VERMELHO = '\033[31m'
VERDE    = '\033[32m'
AZUL     = '\033[34m'
AMARELO = '\033[33m'
RESET    = '\033[0m'

class Motor:
    def __init__(self, potencia: str): 
        self.potencia = potencia
        
    def ligar(self, mensagem: str):
        print(f"{AZUL}Ligando o motor {self.potencia} {mensagem}... VRUM!{RESET}")
        
class Carro:
    def __init__(self, motor: Motor):
        self.motor = motor
        
    def iniciar_corrida(self):
        # O carro usa o motor que foi injetado nele
        self.motor.ligar("para iniciar a corrida")
        
        time.sleep(1.5)
        print(f'{VERMELHO}1{RESET}')
        time.sleep(1.5)
        print(f'{VERMELHO}2{RESET}')
        time.sleep(1.5)
        print(f'{AMARELO}3{RESET}')
        time.sleep(1.5)
        print(f'{VERDE}GOOOOO!!{RESET}')
        
motor_v8 = Motor("V8 5.0")
motor_mil = Motor("1.0 Flex")

mustang = Carro(motor_v8)
celta = Carro(motor_mil)

print("--- Corrida 1 ---")
mustang.iniciar_corrida()

print("\n--- Corrida 2 ---")
celta.iniciar_corrida()