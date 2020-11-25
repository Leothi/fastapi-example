from fastapi import APIRouter, Path

from full_api.models.usuario import (UserBase, UserInsertResponse,
                                     UserSearchResponse)
from full_api.modules import usuario as modulo_usuario

router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado
@router.get('/{insertion_id}/search', summary='Lista o usuário com a id de entrada.', status_code=200, response_model=UserSearchResponse)
def route_search(insertion_id: str = Path(..., description="Id da inserção feita no banco.", example="5fbd6f3adf08221c856a9dac")):
    return {'usuario': modulo_usuario.search(insertion_id)}


@router.post('/add', response_model=UserInsertResponse, status_code=200, summary="Insere um novo usuário no banco de dados.")
def router_add(dados_usuario: UserBase) -> dict:
    """Adiciona um usuário pra teste."""
    insertion_id = modulo_usuario.insert(**dados_usuario.dict())
    return {"_id": insertion_id}

# @router.get('/list', response_model=UserInsertResponse, status_code=200, summary="Cria um novo usuário.")
# def router_list(dados_usuario: UserBase) -> dict:
#     """Lista todos os usuários"""
#     return {"usuarios": modulo_usuario.list}
