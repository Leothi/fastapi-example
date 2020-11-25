from pydantic import BaseModel, Field
from typing import Optional

from full_api.models import RespostaSucesso


class UserBase(BaseModel):
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field(
        "", description="Trabalho do usuário", example="Pedreiro")
    password: str = Field(..., description="Senha do usuário",
                          example="swordfish")


# Dessa forma a saída da API não exibe a senha
class UserPassword(BaseModel):
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field("", description="Trabalho do usuário",
                               example="Pedreiro")


class UserInsertResponse(RespostaSucesso):
    id: str = Field(..., description="Id da inserção no banco", example=" 5fbd697275d61b32f5e503b5", alias='_id')


class UserSearchResponse(RespostaSucesso):
    usuario: UserPassword
