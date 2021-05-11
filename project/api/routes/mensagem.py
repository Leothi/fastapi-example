from fastapi import APIRouter, Query
from loguru import logger

from api.models.mensagem import MensagemResponse
from api.modules import mensagem as modulo_mensagem


router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado


@router.get('/upper', response_model=MensagemResponse, status_code=200, summary="Transforma string para upper case.")
def router_upper(mensagem: str = Query(..., description="Mensagem que será passada para upper case.", example="string")) -> str:
    """A partir de uma string de entrada, transforma para upper case.
    """
    logger.log('LOG ROTA', "Chamada rota /upper")
    return {"mensagem_out": modulo_mensagem.mensagem_upper(mensagem)}
