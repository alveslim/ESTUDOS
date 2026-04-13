# - instalar pip install psycopg2

import psycopg2

conn = psycopg2.connect(
    database = "fliperama",
    user = "postgres",
    password = "xxxxxx", # coloque a senha do seu banco de dados
    host = "localhost",
    port = "5432"
)