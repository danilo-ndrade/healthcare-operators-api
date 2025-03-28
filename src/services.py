from .db import load_data
import pandas as pd

def search_operators(busca:str):
    df = load_data()

    if df is None:
        return [];

    result = df[df['Razao_Social'].str.contains(busca, case=False, na=False)]

    #transforma os valores em string pois existem inconsistencias nos tipos de dados
    result = result.astype(str)

    result = result.where(pd.notnull(result), "")


    return result.to_dict(orient='records')