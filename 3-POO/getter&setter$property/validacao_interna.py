"""2. Validação Interna de Tipos e Valores

Como o Python não bloqueia tipos automaticamente nas type hints, cabe ao setter fazer a validação manual
se quisermos proteger o atributo.

Desafio: Crie uma classe IdadeUsuario com o atributo privado __idade.

    No setter, verifique se o valor recebido é realmente do tipo int e se é maior ou igual a 0.

    Se for uma string ou um número negativo, exiba uma mensagem de erro ou levante um ValueError."""

class IdadeUsuario:
    def __init__(self) -> None:
        self.__idade = None
    
    @property
    def idade(self) -> int:
         return self.__idade
    
    @idade.setter
    def idade(self, idade: int) -> int:
            if not isinstance(idade, int) or isinstance(idade, bool) or idade <= 0:
                raise ValueError("A idade tem deve ser maior que zero e escrita em numeros...")
            else:
                self.__idade = idade

"""--------------testes----------------"""
jorgeIdade = IdadeUsuario()
jorgeIdade.idade = 12
print(jorgeIdade.idade)

#2. Teste inválido (descomente para testar o erro):
# usuario.setter(-5)     # Lança ValueError
# usuario.setter("25")   # Lança ValueError