"""Exercício 3: Configuração Global vs. Local

Crie uma classe ServidorConfig:

    Defina um atributo de classe chamado ambiente = "Desenvolvimento".

    Instancie dois servidores: servidor_sp e servidor_rj.

    Altere o atributo de classe diretamente na classe para "Homologacao".

    Em seguida, altere o ambiente do servidor_sp para "Producao" sem afetar o servidor_rj.

    Exiba o atributo ambiente das duas instâncias e da classe para validar."""
    
class ServidorConfig:
    
    ambiente = "Desenvolvimento"
    
servidor_rj = ServidorConfig()
servidor_sp = ServidorConfig()

ServidorConfig.ambiente = "Homologacao"
servidor_sp.ambiente = "Producao"
print(ServidorConfig.ambiente)
print(servidor_rj.ambiente)
print(servidor_sp.ambiente)