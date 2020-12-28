from pydantic import BaseModel, Field
from typing import Optional, List, Union, Dict

from api.models import SuccessResponse


class UserBase(BaseModel):
    """Base model de Usuário"""
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field(
        "", description="Trabalho do usuário", example="Pedreiro")
    password: str = Field(..., description="Senha do usuário",
                          example="swordfish")


# Dessa forma a saída da API não exibe a senha
class UserPasswordResponse(BaseModel):
    """Base model de Usuário sem exibir senha"""
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field("", description="Trabalho do usuário",
                               example="Pedreiro")

    
class UserMongoResponse(UserPasswordResponse):
    """Response model to /mongo/search"""
    id: str = Field(..., description="Id da inserção no banco", example=" 5fbd697275d61b32f5e503b5", alias='_id')


class UserListCountResponse(BaseModel):
    """Response model to /mongo/list"""
    total: int = Field(..., description="Contagem do total de inserções.")

    
class UserListResponse(BaseModel):
    """Response model to /mongo/list"""
    usuarios: Union[UserListCountResponse,
                    List[Optional[UserMongoResponse]]]
    class Config:
        schema_extra = {
            "example": {
                "usuarios": [
                    UserMongoResponse(_id="5fd78fe56e13c6e884d97a09",
                                      name="Fulano",
                                      job="Pedreiro").dict(),
                    UserMongoResponse(_id="5fda55c527c3c1ee3d0f2564",
                                      name="Fulano 2",
                                      job="Pedreiro 2").dict(),
                ]
            }
        }


class UserInsertResponse(SuccessResponse):
    """Response model to /mongo/insert"""
    id: str = Field(..., description="Id da inserção no banco", example=" 5fbd697275d61b32f5e503b5", alias='_id')


class UserSearchResponse(SuccessResponse):
    """Response model to /mongo/search"""
    usuario: UserPasswordResponse

