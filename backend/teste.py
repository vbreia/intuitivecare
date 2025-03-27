from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# Configuração do banco de dados (pegando do ambiente)
DB_NAME = os.getenv("POSTGRES_DB", "postgres")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "123456")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

# Rota de teste
@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}

# Teste de conexão com o banco
@app.get("/test-db")
def test_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return {"status": "Conectado ao banco!", "versão": db_version[0]}
    except Exception as e:
        return {"erro": str(e)}