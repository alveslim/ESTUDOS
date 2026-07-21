"""📝 Bloco 1: Variáveis de Classe vs. Instância
Exercício 1: O Contador de Instâncias

Crie uma classe chamada Acesso que rastreie quantas vezes novos objetos foram instanciados a partir dela.
📝 Bloco 1: Variáveis de Classe vs. Instância
Exercício 1: O Contador de Instâncias

Crie uma classe chamada Acesso que rastreie quantas vezes novos objetos foram instanciados a partir dela.

    Use um atributo de classe total_acessos.

    Toda vez que um novo objeto for criado, esse atributo deve aumentar em 1.

    Crie 3 instâncias diferentes e imprima o valor de Acesso.total_acessos.
    Use um atributo de classe total_acessos.

    Toda vez que um novo objeto for criado, esse atributo deve aumentar em 1.

    Crie 3 instâncias diferentes e imprima o valor de Acesso.total_acessos."""

class Acesso:

    acesso = []

    def __init__(self, nome) -> None:
        self.nome = nome
        # adiciona um objeto de fora na lista:
        Acesso.acesso.append(self)
i = 0
obj = Acesso("objeto 1")
ob2 = Acesso("objeto 2")
#print(obj.acesso[1])
print(len(f"Tamanho da lista de objetos instanciados: {Acesso.acesso}")) # Saída: 2 exibindo a quantidade total
for obj in Acesso.acesso:
    i = i + 1
    print(f"{i}: {obj.nome}")

# --------------------------------------------------------------

class Acesso:

    acesso = 0

    def __init__(self, nome) -> None:
        self.nome = nome
        # Soma no acesso toda vez que instanciado:
        Acesso.acesso = Acesso.acesso + self.nome

obj = Acesso(1)
ob2 = Acesso(1)
ob3 = Acesso(2)
print(f"Valor total da soma dos objetos instanciados: {Acesso.acesso}") # Saída: 2

# ---------------------------------------------------------------

class Acesso:

    acesso = 0

    def __init__(self, nome) -> None:
        self.nome = nome
        # Soma no acesso toda vez que instanciado:
        Acesso.acesso += 1
obj = Acesso(1)
ob2 = Acesso(1)
ob3 = Acesso(2)
obj3 = Acesso(10)
print(f"total de objetos que acessou: {Acesso.acesso}")