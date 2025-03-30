from fastapi import APIRouter, HTTPException
from .services import search_operators
from .models import Operator

router = APIRouter()

@router.get("/busca-operadores", response_model=list[Operator])
def search(busca: str, numero_ans: bool = False, cnpj: bool = False, razao_social: bool = False):
    try:
        data = search_operators(busca, numero_ans, cnpj, razao_social)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))