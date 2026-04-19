#Crie duas funções em python 
#para agendar o desligamento do computador em uma hora e meia hora. 
# cancelar o agendamento do desligamento do computador.

import time 
import os

def agendar_desligamento(tempo):
    time.sleep(tempo)
    print("Desligando o computador...")
    os.system('shutdown /s /t 0') # comando para desligar o computador no windows

def cancelar_desligamento():
    print("Agendamento de desligamento cancelado.")
    os.system('shutdown /a') # comando para cancelar o desligamento no windows

tempo = 10 # 1 hora e meia em segundos
agendar_desligamento(tempo) 
cancelar_desligamento()