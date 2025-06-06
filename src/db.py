import pandas as pd
from .config import CSV_FILE_PATH

""" Carrega os dados do arquivo CSV com pandas. """
def load_data():
    try:
        return pd.read_csv(CSV_FILE_PATH, delimiter=';')
    except Exception as e:
        print(f'Error loading data: {e}')
        return None