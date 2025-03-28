from fastapi import APIRouter, HTTPException
from .services import search_operators
from .models import Operator

router = APIRouter()

@router.get("/busca-operadores", response_model=list[Operator])
def search(busca: str):
    result = search_operators(busca)
    if not result:
        raise HTTPException(status_code=404, detail="Nenhum resultado encontrado")
    return result