from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

df_operadores = pd.read_csv('./data/Relatorio_cadop.csv', delimiter=';')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/busca-operadores")
def busca_operadores(busca: str = Query(..., description='Termo de busca')):
    result = df_operadores[df_operadores['Razao_Social'].str.contains(busca, case=False)]
    # preencher valores NaN com "", para evitar erros com json
    result = result.where(pd.notnull(result), None)
    return result.to_dict(orient='records')