from fastapi import APIRouter, Query

from full_api.models.mensagem import MensagemResponse
from full_api.modules import mensagem as modulo_mensagem


router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado
@router.get('/', response_model=MensagemResponse, status_code=200, summary="Transforma string para upper case.")
def mensagem_upper(mensagem: str = Query(..., description="Mensagem que será passada para upper case.", example="string")) -> str:
    """A partir de uma string de entrada, transforma para upper case.
    """
    return {"mensagem_out": modulo_mensagem.mensagem_upper(mensagem)}
