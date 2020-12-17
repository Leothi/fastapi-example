from fastapi import APIRouter, Path
from loguru import logger

from full_api.models.usuario import (UserBase, UserInsertResponse,
                                     UserSearchResponse)
from full_api.modules import usuario as modulo_usuario

router = APIRouter()

# Rota na API
# response_model é o modelo pydantic utilizado
@router.get('/mongo/{insertion_id}/search', summary='Lista o usuário com a id de entrada.', status_code=200, response_model=UserSearchResponse)
def route_mongo_search(insertion_id: str = Path(..., description="Id da inserção feita no banco.", example="5fbd6f3adf08221c856a9dac")):
    logger.log('LOG ROTA', "Chamada rota /mongo/search")
    return {'usuario': modulo_usuario.search(insertion_id)}


@router.post('/mongo/add', response_model=UserInsertResponse, status_code=200, summary="Insere um novo usuário no banco de dados.")
def router_mongo_add(dados_usuario: UserBase) -> dict:
    """Adiciona um usuário pra teste."""
    logger.log('LOG ROTA', "Chamada rota /mongo/add")
    insertion_id = modulo_usuario.insert(**dados_usuario.dict())
    return {"_id": insertion_id}

@router.post('/sql/add', response_model=UserInsertResponse, status_code=200, summary="Insere um novo usuário no banco de dados.")
def router_sql_add(dados_usuario: UserBase) -> dict:
    """Adiciona um usuário pra teste."""
    logger.log('LOG ROTA', "Chamada rota /sql/add")
    insertion_id = modulo_usuario.insert(**dados_usuario.dict())
    return {"_id": insertion_id}

