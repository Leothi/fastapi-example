from pydantic import BaseModel, Field
from typing import Optional

from full_api.models import RespostaSucesso


class UserRequest(BaseModel):
    id_: int = Field(..., description="Identificador do usuário", example=1)
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field(
        "", description="Trabalho do usuário", example="Pedreiro")
    password: str = Field(..., description="Senha do usuário",
                          example="swordfish")


# Dessa forma a saída da API não exibe a senha
class UserPassword(BaseModel):
    id_: int = Field(..., description="Identificador do usuário", example=1)
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field("", description="Trabalho do usuário",
                               example="Pedreiro")


class UserResponse(RespostaSucesso):
    usuario: UserPassword
