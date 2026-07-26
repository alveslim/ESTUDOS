import random
class ServicoNotificao:
    def enviar_email(self, mensagem: str) -> None:
        print('Enviando Email...')
        print(f'Mensagem: {mensagem}')
        
class Usuario:
    def __init__(self, nome, notificador: ServicoNotificao) -> None:
        self.nome = nome
        self.__notificador = notificador
    def esqueci_senha(self) -> None:
        self.numero = random.randint(1234, 9981)
        self.__notificador.enviar_email(f'Ola {self.nome}, seu código de verificao é: {self.numero}')

servico_email = ServicoNotificao()
Cecilia = Usuario('Cecilia', servico_email)
Cecilia.esqueci_senha()