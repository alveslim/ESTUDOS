class SessaoUsuario:
    # Atributo de Classe: limite global do sistema
    tentativas_maximas = 3


class Autenticador:
    def __init__(self) -> None:
        # Simulando um "banco de dados" de usuários
        self.__banco_usuarios = {
            "rafael": "1234"
        }

    # Método PÚBLICO para criar nova conta
    def cadastrar_usuario(self, usuario: str, senha: str) -> None:
        print(f"--- Tentando cadastrar: {usuario} ---")
        
        # Step 1: Valida os dados de entrada
        if not self.__validar_dados(usuario, senha):
            print("❌ Dados inválidos. Usuário e senha não podem ser vazios.\n")
            return

        # Step 2: Checa se o usuário JÁ EXISTE (usando a busca)
        if self.__buscar_usuario(usuario):
            print("❌ Erro: Este nome de usuário já está cadastrado.\n")
            return

        # Step 3: Se passou nas validações, registra o usuário!
        self.__registrar_usuario(usuario, senha)
        print("✅ Usuário cadastrado com sucesso!\n")

    # Métodos PRIVADOS (Separando as responsabilidades - SRP)
    def __buscar_usuario(self, usuario: str) -> bool:
        # Responsabilidade: Apenas verificar se o usuário existe
        return usuario in self.__banco_usuarios

    def __validar_dados(self, usuario: str, senha: str) -> bool:
        # Responsabilidade: Apenas garantir que os campos não são vazios
        return bool(usuario and usuario.strip()) and bool(senha and senha.strip())

    def __registrar_usuario(self, usuario: str, senha: str) -> None:
        # Responsabilidade: Apenas SALVAR no banco de dados
        self.__banco_usuarios[usuario] = senha
        print(f"💾 [BANCO DE DADOS]: {usuario} foi salvo no sistema!")


# --- TESTANDO O CÓDIGO ---

auth = Autenticador()

# Teste 1: Cadastrar usuário válido
auth.cadastrar_usuario("flavio", "python123")

# Teste 2: Tentar cadastrar o mesmo usuário de novo (vai barrar na busca)
auth.cadastrar_usuario("flavio", "outra_senha")

# Teste 3: Tentar cadastrar com dados em branco
auth.cadastrar_usuario("", "1234")

class SessaoUsuario:
    # Atributo de classe: compartilhado por todo o sistema
    tentativas_maximas = 3


class Autenticador:
    def __init__(self) -> None:
        # Simulando um "banco de dados" simples internamente
        self.__banco_usuarios = {
            "rafael": "1234",
            "flavio": "python123"
        }

    # Método PÚBLICO (Orquestrador)
    def login(self, usuario: str, senha: str) -> None:
        print(f"--- Tentando login para: {usuario} ---")
        
        # Step 1: Busca o usuário
        if not self.__buscar_usuario(usuario):
            print("❌ Falha no login: Usuário não encontrado.\n")
            return # Interrompe o fluxo aqui
            
        # Step 2: Valida a senha
        if not self.__validar_senha(usuario, senha):
            print("❌ Falha no login: Senha incorreta.")
            print(f"⚠️ Atenção: Limite do sistema é de {SessaoUsuario.tentativas_maximas} tentativas.\n")
            return # Interrompe o fluxo aqui

        # Step 3: Se passou nos dois, registra o log de sucesso
        self.__registrar_log(usuario)
        print("✅ Login realizado com sucesso!\n")

    # Métodos PRIVADOS (Apoio e Responsabilidade Única)
    def __buscar_usuario(self, usuario: str) -> bool:
        # Checa se o usuário existe nas chaves do dicionário
        return usuario in self.__banco_usuarios

    def __validar_senha(self, usuario: str, senha: str) -> bool:
        # Compara a senha informada com a senha salva no "banco"
        return self.__banco_usuarios.get(usuario) == senha

    def __registrar_log(self, usuario: str) -> None:
        # Apenas registra o acesso (SRP: isolado da validação)
        print(f"📝 [LOG]: Usuário '{usuario}' autenticado com sucesso no sistema.")


# --- TESTANDO O CÓDIGO ---

auth = Autenticador()

# Teste 1: Usuário que não existe
auth.login("marcos", "1234")

# Teste 2: Usuário existe, mas senha errada
auth.login("rafael", "senha_errada")

# Teste 3: Sucesso!
auth.login("rafael", "1234")