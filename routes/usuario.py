from fastapi import APIRouter

from full_api.models.usuario import UserResponse, UserRequest
from full_api.modules import usuario as modulo_usuario


router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado
@router.post('/add', response_model=UserResponse, status_code=200, summary="Cria um novo usuário.")
def add_user(dados_usuario: UserRequest) -> dict:
    """Adiciona um usuário pra teste."""
    novo_usuario = modulo_usuario.User(**dados_usuario.dict())
    atributos = novo_usuario.user_attributes()
    return {"usuario": atributos}
