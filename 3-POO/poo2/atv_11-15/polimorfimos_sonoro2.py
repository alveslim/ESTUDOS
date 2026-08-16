class Instrumento:
    def tocar(self):
        # A mãe tem um comportamento genérico (ou não faz nada)
        print("Fazendo um som genérico...")
        
class Violao(Instrumento):
    # A filha IGNORA o método da mãe e cria o seu próprio
    def tocar(self):
        print("♪♪ ♪♪♪ ♪ (Som de cordas do violão)")

class Piano(Instrumento):
    # A filha também cria sua própria versão do método
    def tocar(self):
        print("𝄞 ♫♫ ♫ ♫♫ 𝄞 (Som de teclas do piano)")
        
# O uso continua idêntico ao seu:
violao = Violao()
violao.tocar()

piano = Piano()
piano.tocar()