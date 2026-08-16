"""Colcheia simples: ♪Duas colcheias ligadas: ♫Clave de sol: 𝄞"""

class Instrumento:
    def __init__(self, som):
        self._som = som
    
    def tocar(self):
        print(f"{self._som}")
        
class Violao(Instrumento):
    def __init__(self):
        super().__init__("♪♪ ♪♪♪ ♪")

class Piano(Instrumento):
    def __init__(self):
        super().__init__("𝄞 ♫♫ ♫ ♫♫ 𝄞 ♫♫♫")
        
violao = Violao()
violao.tocar()

piano = Piano()
piano.tocar()

