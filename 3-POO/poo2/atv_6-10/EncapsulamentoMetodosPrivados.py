"""Exercício 5: Encapsulamento com Métodos Privados

    Crie uma classe ProcessadorPagamento:

    Crie o método público processar(valor: float, cartão: str).

    Crie métodos privados (iniciando com __) para isolar etapas da operação:

        __validar_cartao(cartao) -> retorna True ou False.

        __conectar_gateway() -> simula um print("Conectando...").

        __executar_cobranca(valor) -> simula um print("Cobrança realizada!").

    O método público processar deve apenas orquestrar essas chamadas privadas."""

class ProcessadorPagamento:
    def __init__(self):
        pass

    def processsar(self, valor: float, cartao: str):
        print("processando...")
        self.__validar_cartao(cartao)
        self.__executar_cobranca(valor)

    def __validar_cartao(self, cartao) -> bool:
        return print(f"Validando cartao {cartao}")

    def __executar_cobranca(self, valor):
        return print(f"Cobranca de R${valor} realizada!")

pagamentoJorge = ProcessadorPagamento()
pagamentoJorge.processsar(10.00, "MasterCard")