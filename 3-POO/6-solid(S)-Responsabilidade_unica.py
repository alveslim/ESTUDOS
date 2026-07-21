""""class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("acessando banco de dados...")
            print(f"Cadastrar usuario {nome}, idade {idade}")
        else:
            print("dados invalidos")"""
            
class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade) : #1
            self.__registre_user(nome, idade) #2
        else:
            self.__error_handle()
            
    def __validate_input(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
        
    def __registre_user(self, nome: str, idade: int) -> None:
        print("acessando banco de dados...") # 2
        print(f"Cadastrar usuario {nome}, idade {idade}")
        
    def __error_handle(self) -> None:
        print("dados invalidos...")
        
sistema = SistemaCadastral()
sistema.cadastrar("Rafa", 28)