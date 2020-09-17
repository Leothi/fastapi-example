from fastapi import APIRouter

from full_api.modelos.usuario import UserResponse, UserRequest
from full_api.modulos import usuario as modulo_usuario


router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado
@router.post('/add', response_model=UserResponse, response_model_exclude="job", status_code=200, summary="Cria um novo usuário.")
def add_user(dados_usuario: UserRequest) -> dict:
    novo_usuario = modulo_usuario.User(**dados_usuario.dict())
    atributos = novo_usuario.user_attributes()
    return {"usuario": atributos}
