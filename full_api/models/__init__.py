from pydantic import BaseModel, Field
from typing import Optional

# Modelo para mensagem de sucesso genérica padrão


class RespostaSucesso(BaseModel):
    mensagem = "Processado com sucesso."
    mensagem: str = Field(mensagem,
                          example=mensagem)

# Modelo para mensagem de Erro


class RespostaErro(BaseModel):
    status: int = Field(..., description="Código da mensagem")
    message: str = Field(..., description="Descrição da mensagem")
    details: str = Field(None, description="Detalhes da mensagem")


# Mensagens de erro padronizadas
DEFAULT_RESPONSES = [
    RespostaErro(status=422, message="Parâmetros da requisição inválidos!", details="1 validation error for Request..."),
    RespostaErro(status=500, message="Erro interno!"),
    RespostaErro(status=404, message="Não encontrado"),
    RespostaErro(status=400, message="Bad Request"),
]

# Para criação de respostas personalizadas

def parse_openapi(responses: list = list()) -> dict:
    responses.extend(DEFAULT_RESPONSES)
    return {exemplo.status: {"content": {"application/json": {"example": exemplo.dict()}}, "model": RespostaErro}
            for exemplo in responses}


# Respostas padrão em formato JSON para rotas (sem personalização pra cada serviço)
DEFAULT_RESPONSES_JSON = parse_openapi()
