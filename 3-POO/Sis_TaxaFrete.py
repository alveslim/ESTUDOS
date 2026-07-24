"""🏋️‍♂️ Novo Desafio (Nível Intermediário)Aqui vamos misturar Atributos de Classe, 
Modificação na Instância e uma Lógica de Regra de Negócio dentro do método.

Exercício: Sistema de Taxa de Frete para E-CommerceA Classe e a Taxa Padrão:
Crie uma classe LojaVirtual. Ela
 deve ter um atributo de classe taxa_frete_padrao = 15.0.O 
 Construtor:No __init__, receba o nome da filial e crie um atributo de instância self.nome.
 O Método do Frete:Crie um método calcular_frete(self, peso: float) que retorna o valor do frete calculado pela fórmula:
 
 $$\text{Frete} = \text{peso} \times 2.0 + \text{taxa\_frete}$$
 
 (Dica: use self.taxa_frete_padrao dentro da fórmula para que o objeto procure primeiro se ele tem uma taxa própria ou se usa a da classe!)
 Os Testes:Instancie duas lojas: loja_centro e loja_interior.
 
 Cenário 1: Imprima o frete de um produto de 3kg em ambas as lojas.
 (As duas devem usar a taxa de R$ 15,00).
 Cenário 2 (Reajuste Global): A empresa subiu a taxa padrão da classe LojaVirtual para 20.0. 
 Imprima novamente o frete de 3kg da loja_interior.
 Cenário 3 (Promoção Local): A loja_centro decidiu criar uma promoção própria e definiu sua taxa individual para 5.0.
 Cenário 4 (Novo Reajuste Global): A empresa mudou a taxa da classe para 25.0.
 A Pergunta:No final, qual será o valor do frete de 3kg na loja_centro e na loja_interior? 
 Monte o código e teste sua hipótese!"""