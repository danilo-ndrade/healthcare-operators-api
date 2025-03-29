from fastapi import APIRouter, HTTPException
from .services import search_operators
from .models import Operator

router = APIRouter()

@router.get("/busca-operadores", response_model=list[Operator])
def search(busca: str):
    try:
        data = search_operators(busca)
        print(len(data))
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))