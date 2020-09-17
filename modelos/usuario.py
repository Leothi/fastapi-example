from pydantic import BaseModel, Field
from typing import List, Dict, Optional

from full_api.modelos import RespostaSucesso


class UserRequest(RespostaSucesso):
    id_: int = Field(..., description="Identificador do usuário", example=1)
    name: str = Field(..., description="Nome do usuário", example="Fulano")
    job: Optional[str] = Field("", description="Trabalho do usuário",
                               example="Pedreiro")


# Job não vai aparecer na response
class UserResponse(BaseModel):
    usuario: UserRequest
