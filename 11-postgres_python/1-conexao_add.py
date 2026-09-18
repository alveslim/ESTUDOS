import psycopg

# Configurações de acesso ao banco
DB_PARAMS = {
    "dbname": "users",
    "user": "flavio",
    "password": "fla3257598",
    "host": "localhost",  # ou o host do container Docker / servidor remoto
    "port": 5433,
}

def consultar_tabela():
    try:
        with psycopg.connect(**DB_PARAMS) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM usuarios;
                    """)
                tabela = cur.fetchall()
                print(tabela)

                for linha in tabela:
                    print(linha)

    
    except psycopg.Error as e:
        print('Erro ao consultar tabelas')

def inserir_usuario(nome: str, email: str, ativo: bool = True):
    # Query parametrizada para evitar SQL Injection
    query = """
        INSERT INTO usuarios (nome, email, ativo)
        VALUES (%s, %s, %s)
        RETURNING id;
    """

    try:
        # Abre a conexão
        with psycopg.connect(**DB_PARAMS) as conn:
            # Abre o cursor para executar comandos
            with conn.cursor() as cur:
                cur.execute(query, (nome, email, ativo))
                novo_id = cur.fetchone()[0]

            # psycopg faz commit automático ao sair do bloco 'with conn' sem erros
            print(f"Registro inserido com sucesso! ID gerado: {novo_id}")

    except psycopg.Error as e:
        print(f"Erro ao inserir dados no PostgreSQL: {e}")



if __name__ == "__main__":
    inserir_usuario("Maria Joao", "maria@exemplo.com", True)
    consultar_tabela()