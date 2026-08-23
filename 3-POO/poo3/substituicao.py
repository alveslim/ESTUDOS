class ConnectionDB:
    def conectar(self):
        print("conectando ao banco")

class SqlRepository(ConnectionDB):
    def select(self):
        print('buscando dados no banco SQL')
        
class NoSqlRepository(ConnectionDB):
    def select(self):
        print('Buscando ddados no banco NOSQL')
        
class DBHandler:
    def alterTable(self):
        print('alterando tabela em SQL')