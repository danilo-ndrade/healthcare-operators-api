from .db import load_data
import pandas as pd
from typing import Optional

def search_operators(
    busca: str,
    ans_number: Optional[bool] = None,
    cnpj: Optional[bool] = None,        
    company_name: Optional[bool] = None  
):
    """ Carrega os dados do arquivo CSV """
    try:
        df = load_data()
    except Exception as e:
        return str(e)
    
    """ Converte os campos CNPJ e Registro_ANS para string a 
    fim de evitar erros na hora de fazer a busca no dataframe """
    if 'CNPJ' in df.columns:
        df['CNPJ'] = df['CNPJ'].astype(str)
    if 'Registro_ANS' in df.columns:
        df['Registro_ANS'] = df['Registro_ANS'].astype(str)

    """ Filtra os dados de acordo com o parâmetro de busca """
    if ans_number:
        result = df[df['Registro_ANS'].str.contains(busca, case=False, na=False)]
    elif cnpj:
        result = df[df['CNPJ'].str.contains(busca, case=False, na=False)]
    elif company_name:
        result = df[df['Razao_Social'].str.contains(busca, case=False, na=False)]

    """" Substitui os valores nulos por espaços em branco. 
    Feito para evitar erros que estavam ocorrendo no hora da consulta """
    result = result.where(pd.notnull(result), " ")
    
    """ Converte os valores do dataframe para string a fim de evitar erros """
    result = result.astype(str)

    return result.to_dict(orient='records')