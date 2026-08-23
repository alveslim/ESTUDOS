class Quarto:
    quartos_reservados = 0
    capacidade_max = 5
    def __init__(self, numero, ocupado=False):
        self.numero =  numero
        self.ocupado = ocupado
    @classmethod
    def alterar_capacidade(cls, nova_capacidade):
        cls.capacidade_max = nova_capacidade
    def reservar(self) -> bool:
        if self.ocupado == False and self.quartos_reservados < self.capacidade_max:
            self.ocupado = True
            Quarto.quartos_reservados += 1
            return True
        elif self.ocupado == True:
            print('Quarto já está ocupado...')
            return False
        else:
            print('Estamos sem quartos no momento...')
            return False

class Hospede:
    def __init__(self, nome):
        self.nome = nome
    def fazer_reserva(self, quarto: Quarto):
        sucesso = quarto.reservar()
        if sucesso == True:
            print(f"Reserva realizada com sucesso para {self.nome} no quarto {quarto.numero}!")

Quarto1 = Quarto('201')
Quarto2 = Quarto('202')
Cecilia = Hospede('Cecilia')
Leandro = Hospede('Leandro')

Cecilia.fazer_reserva(Quarto1)
Leandro.fazer_reserva(Quarto1)
print(Quarto.quartos_reservados)