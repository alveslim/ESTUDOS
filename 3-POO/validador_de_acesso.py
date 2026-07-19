class user:
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.__senha = senha
        
    def __validar_senha_forte(self, password):
        
        if len(password) < 6:
            print("A senha é Invalida \n Por favor, insira uma senha com o mín 6 caracteres")
            self.__senha = None
            return False
        elif len(password) >= 6:
            #print("Senha valida!")
            self.__senha = password
            return True
        
    def criar_conta(self):
        self.__validar_senha_forte(self.__senha)
        print(f"Conta Criada com sucesso!\n"
              f"Nome: {self.nome}\n"
              f"Email: {self.email}\n"
              f"Senha: {self.__senha}\n"
        )
        
usuario = user("jorge", "jorge@gmail.com", "123456")
usuario.criar_conta()