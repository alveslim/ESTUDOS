class Veiculo:
    
    total_vistoriados = 0
    
    def __init__(self, placa, status="pendente"):
        self.placa = placa
        self.status = status
    
    @classmethod
    def registrar_vistoria(cls):
        cls.total_vistoriados += 1
        print('registrado!')
    
    @classmethod
    def exibir_relatorio_geral(cls):
        print(f'um total de vistoriados: {cls.total_vistoriados}')

class Inspetor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        
    def realizar_vistoria(self, veiculo: Veiculo, status):
        veiculo.status = status
        veiculo.registrar_vistoria()
        print(f'{self.matricula}: Inspetor {self.nome} realizou o veiculo da placa {veiculo.placa}')

fusca = Veiculo('ABC-123')
Richard = Inspetor('Richard', 12343)
Richard.realizar_vistoria(fusca, 'aprovado')
print(fusca.status)