"""Herança com Super: Crie uma classe Funcionario com nome e salario. 
Crie uma classe filha Gerente que além de nome e salário, 
tenha um atributo departamento. 

Use o super().__init__ para aproveitar o construtor da mãe."""

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def info_funcionario(self):
        print(f"O {self.nome} recebe R$ {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento: str):
        super().__init__(nome, salario)
        self.departamento = departamento

    def info_departamento(self):
        print(f"O {self.nome} e do departamento {self.departamento}")

gerente = Gerente("Miguel", 3000.00, "08")
funcionario = Funcionario("Flavio", 1800.00)
funcionario.info_funcionario()
gerente.info_funcionario()
gerente.info_departamento()