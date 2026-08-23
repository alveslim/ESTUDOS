"""O Princípio Aberto/Fechado (Open/Closed Principle - OCP)
é a letra "O" do acrônimo SOLID (um conjunto de boas práticas de programação).

Ele diz que:

    "Entidades de software (classes, módulos, funções, etc.) devem estar 
    abertas para extensão, mas fechadas para modificação."

Em termos práticos: você deve ser capaz de adicionar novas funcionalidades ao 
seu sistema sem precisar alterar o código que já existe e está funcionando. 
Isso evita que você introduza novos bugs em partes do sistema que já foram testadas.

Em Python, geralmente alcançamos isso usando Polimorfismo 
(através de herança ou duck typing) ou Injeção de Dependência.

Vamos ver isso na prática.
❌ O Problema: Violando o Princípio

Imagine que você está criando um sistema para calcular descontos em uma loja. 
A forma mais intuitiva (porém incorreta segundo o OCP) seria usar várias condições if/elif:
"""

class CalculadoraDeDesconto_violando_OCP:
    def calcular(self, tipo_cliente, valor):
        if tipo_cliente == "comum":
            return valor
        elif tipo_cliente == "vip":
            return valor * 0.90  # 10% de desconto
        
from abc import ABC, abstractmethod
# 1. Criamos um "contrato" (Interface) para qualquer tipo de desconto
class RegraDeDesconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass
# 2. Criamos as regras específicas (Fechadas para modificação, testadas e prontas)    
class DescontoComum(RegraDeDesconto):
    def calcular(self, valor):
        return valor
    
class DescontoVip(RegraDeDesconto):
    def calcular(self, valor):
        return valor * 0.90

# 3. A classe principal não precisa mais saber os tipos de cliente!
class CalculadoraDeDesconto:
    def calcular(self, regra: RegraDeDesconto, valor):
        # Ela apenas recebe a regra e executa o cálculo
        return regra.calcular(valor)

# ABERTO PARA EXTENSÃO: Criamos uma nova funcionalidade
class DescontoPremium(RegraDeDesconto):
    def calcular(self, valor):
        return valor * 0.80
    
