from fastapi import APIRouter, Path, Query
from loguru import logger

from api.models.usuario import (UserBase, UserInsertResponse,
                                     UserSearchResponse, UserListResponse)
from api.modules import usuario as modulo_usuario


router = APIRouter()


@router.get('/mongo/list', summary='Lista todas as inserções do banco.',
            status_code=200, response_model=UserListResponse)
def route_mongo_list(skip: int = Query(0, description="Valor inicial de listagem."),
                     limit: int = Query(100, description="Valor final de listagem."),
                     count: bool = Query(None, description='Contagem do total de inserções.', example=False)):
    """Lista todos os documentos do banco."""
    logger.log('LOG ROTA', "Chamada rota /mongo/list")
    return {'usuarios': modulo_usuario.list_(skip=skip, limit=limit, count=count)}


@router.post('/mongo/insert', response_model=UserInsertResponse, status_code=200, summary="Insere um novo usuário no banco de dados.")
def router_mongo_insert(dados_usuario: UserBase) -> dict:
    """Adiciona um usuário pra teste."""
    logger.log('LOG ROTA', "Chamada rota /mongo/insert")
    insertion_id = modulo_usuario.insert(**dados_usuario.dict())
    return {"_id": insertion_id}


@router.get('/mongo/{insertion_id}/search', summary='Lista o usuário com a id de entrada.',
            status_code=200, response_model=UserSearchResponse)
def route_mongo_search(insertion_id: str = Path(..., description="Id da inserção feita no banco.", example="5fbd6f3adf08221c856a9dac")):
    """ Busca um usuário no banco. """
    logger.log('LOG ROTA', "Chamada rota /mongo/search")
    return {'usuario': modulo_usuario.search(insertion_id)}


@router.post('/sql/insert', response_model=UserInsertResponse, status_code=200, summary="Insere um novo usuário no banco de dados.")
def router_sql_insert(dados_usuario: UserBase) -> dict:
    """Adiciona um usuário pra teste."""
    logger.log('LOG ROTA', "Chamada rota /sql/add")
    insertion_id = modulo_usuario.insert_sql(**dados_usuario.dict())
    return {"_id": insertion_id}
