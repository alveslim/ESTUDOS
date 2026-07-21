class Contabancaria:
    def __init__(self, titular, saldo) -> None:
        self.__titular = titular
        self.__saldo = saldo
        
    def depositar(self, valor):
        
        if valor == 0:
            print("Invalido! Valor tem que ser maior que 0")
        elif valor > 0:
            self.__saldo = self.__saldo + valor
            #print(f"Saldo: {self.__saldo}")
        
    def ver_saldo(self):
        print(f"Saldo do {self.__titular}: {self.__saldo}")
        
conta = Contabancaria("Jorge", 1000)
conta.depositar(100)
conta.ver_saldo()