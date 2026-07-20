"""5. Formatando Dados no Getter

O getter não precisa apenas retornar o valor bruto; ele pode transformar o dado para quem está consumindo.

Desafio: Crie uma classe ContaBancaria com o atributo privado _saldo.

    No getter, retorne o saldo formatado como moeda brasileira (ex: R$ 100.00).

    No setter, garanta que o saldo só possa ser alterado se o novo valor for um float ou int."""

class ContaBancaria:
    def __init__(self) -> None:
        self._saldo = float
    
    @property
    def valor(self) -> float:
        return print(f"R${self._saldo}")

    @valor.setter
    def valor(self, valor: float) -> float:
        self._saldo = valor

contaJorge = ContaBancaria()
contaJorge.valor = 100.00
print(contaJorge.valor)