class MeuErroPersonalizado(Exception):
    
    def __init__(self, *mensagem):
        super().__init__(*mensagem)
        self.mensagem = mensagem
        self.error_type = "Esse e meu erro"
try:        
    raise MeuErroPersonalizado("Personalizei meu erro")
except Exception as exception:
    print(exception)
    print(exception.error_type)