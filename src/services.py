from .db import load_data
import pandas as pd
from typing import Optional

def search_operators(
    busca: str,
    ans_number: Optional[bool] = None,
    cnpj: Optional[bool] = None,        
    company_name: Optional[bool] = None  
):
    try:
        df = load_data()
    except Exception as e:
        return str(e)
    
    print(busca, ans_number, cnpj, company_name, 'testeeee')

    # result = df[df['Razao_Social'].str.contains(busca, case=False, na=False)]

    if 'CNPJ' in df.columns:
        df['CNPJ'] = df['CNPJ'].astype(str)
    if 'Registro_ANS' in df.columns:
        df['Registro_ANS'] = df['Registro_ANS'].astype(str)

    if ans_number:
        result = df[df['Registro_ANS'].str.contains(busca, case=False, na=False)]
    elif cnpj:
        print('cnpj')
        result = df[df['CNPJ'].str.contains(busca, case=False, na=False)]
        print(result)
    elif company_name:
        result = df[df['Razao_Social'].str.contains(busca, case=False, na=False)]

    #transforma os valores em string pois existem inconsistencias nos tipos de dados
    result = result.astype(str)

    result = result.where(pd.notnull(result), "")

    return result.to_dict(orient='records')