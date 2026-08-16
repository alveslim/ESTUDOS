class ContaBancaria:
    def __init__(self, saldo: float) -> None:
        self._saldo = saldo
        
    def depositar(self, valor: float):
        self._saldo = self._saldo + valor
        print(f"Valor atual: {self._saldo}")
        
    def sacar(self, valor: float):
        self._saldo = self._saldo - valor
        print(f"Valor atual: {self._saldo}")
        
minhaconta = ContaBancaria(10000.00)
minhaconta.depositar(10.00)
minhaconta._saldo = 10000000.00
minhaconta.depositar(10.00)