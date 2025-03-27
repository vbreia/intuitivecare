from fastapi import FastAPI, Query
import psycopg2
import os

app = FastAPI()

# Configuração do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "dbname=postgres user=postgres password=postgres host=db port=5432")

# Função para conectar ao banco
def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.get("/operadoras/")
def search_operadoras(query: str = Query(..., min_length=3)):
    """ Busca textual na lista de operadoras """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM operadoras
        WHERE nome_fantasia ILIKE %s OR razao_social ILIKE %s
        LIMIT 10;
    """, (f"%{query}%", f"%{query}%"))
    result = cur.fetchall()
    cur.close()
    conn.close()
    
    return {"operadoras": result}
