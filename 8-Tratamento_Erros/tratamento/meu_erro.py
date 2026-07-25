class MeuErroPersonalizado(Exception):
    
    def __init__(self, *mensagem):
        super().__init__(*mensagem)
        self.mensagem = mensagem
        self.error_type = "Esse e meu erro"