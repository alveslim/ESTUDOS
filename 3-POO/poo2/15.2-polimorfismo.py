class Violino:
    def tocar(self):
        print("Fiiii fiiii fiiii (som de cordas)")

class Bateria:
    def tocar(self):
        print("Tum dum tsss (som de tambores)")

# O Maestro (função) não quer saber qual é o instrumento. 
# Ele só manda tocar!
def maestro_mandar_tocar(instrumento):
    instrumento.tocar() # A mesma ordem gera resultados diferentes!

meu_violino = Violino()
minha_bateria = Bateria()

maestro_mandar_tocar(meu_violino)
maestro_mandar_tocar(minha_bateria)