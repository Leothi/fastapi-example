from fastapi import APIRouter, Query
from loguru import logger

from api.models.math import MathResponse
from api.modules import math as modulo_math

router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado


@router.get('/dobro', response_model=MathResponse, summary="Retorna o dobro do valor de entrada.")
def router_dobro(valor: float = Query(..., description="Valor para ser dobrado.", example=2.0)) -> float:
    """A partir de um valor de entrada, retorna seu dobro.
    """
    logger.log('LOG ROTA', "Chamada rota /dobro")
    return {"valor": modulo_math.dobro(valor)}


@router.get('/divisao', response_model=MathResponse, summary="Retorna a divisão entre 2 valores.")
def router_divisao(numerador: float = Query(..., description="Numerador.", example=2.0),
                   denominador: float = Query(..., description="Denominador", example=1.0)) -> float:
    """Realiza a divisão de 2 valores.
    """
    logger.log('LOG ROTA', "Chamada rota /divisao")
    return {"valor": modulo_math.divisao(numerador, denominador)}
