from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configurações de conexão com o banco de dados

user = 'postgres'
password = 'xxxxxx'
host = 'localhost'  
database = 'blog'
DATABASE_URI = 'postgresql://}{postgres}:{password}@{host}/{database}'

# Criando a engine e a sessão   
engine = create_engine(DATABASE_URI) # Cria a engine de conexão com o banco de dados
Session = sessionmaker(bind=engine)  # Cria a classe de sessão vinculada à engine
session = Session() # Cria uma instância de sessão para interagir com o banco de dados
Base = declarative_base() # Cria a classe base para os modelos de dados, permitindo a definição de tabelas e mapeamento ORM