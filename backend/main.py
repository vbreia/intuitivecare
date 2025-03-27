from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

CSV_PATH = "/data/csvs/Relatorio_cadop.csv"
df_operadoras = pd.read_csv(CSV_PATH, delimiter=";", encoding="utf-8")

@app.get("/")
def home():
    """ Rota inicial para testar a API """
    return {"mensagem": "API funcionando!"}

@app.get("/busca-operadora/")
def busca_operadora(q: str = Query(..., min_length=2)):
    """Busca textual por razão social da operadora"""
    resultados = df_operadoras[df_operadoras['Razao_Social'].str.contains(q, case=False, na=False)]
    
    # Substituir valores NaN e infinitos antes de converter para JSON
    resultados = resultados.fillna("").replace([float("inf"), float("-inf")], "")
    
    return resultados.head(10).to_dict(orient="records")

@app.get("/modalidade/")
def busca_operadora(q: str = Query(..., min_length=2)):
    """Busca textual por modalidade da operadora"""
    resultados = df_operadoras[df_operadoras['Modalidade'].str.contains(q, case=False, na=False)]
    
    # Substituir valores NaN e infinitos antes de converter para JSON
    resultados = resultados.fillna("").replace([float("inf"), float("-inf")], "")
    
    return resultados.head(10).to_dict(orient="records")

@app.get("/bairro/")
def busca_bairro(q: str = Query(..., min_length=2)):
    """Busca textual por bairro da operadora"""
    resultados = df_operadoras[df_operadoras['Bairro'].str.contains(q, case=False, na=False)]
    # Substituir valores NaN e infinitos antes de converter para JSON
    resultados = resultados.fillna("").replace([float("inf"), float("-inf")], "")
    
    return resultados.head(10).to_dict(orient="records")