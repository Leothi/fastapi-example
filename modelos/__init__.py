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
    message: str = Field(..., description="Detalhes da mensagem")
    stacktrace: Optional[str] = Field("", description="Stacktrace do erro")


# Mensagens de erro padronizadas
DEFAULT_RESPONSES = [
    RespostaErro(status=422,
                 message="Parâmetros da requisição inválidos!",
                 stacktrace="Traceback (most recent call last): ..."),
    RespostaErro(status=500,
                 message="Erro interno!",
                 stacktrace="Traceback (most recent call last): ..."),
    RespostaErro(status=404,
                 message="Não encontrado",
                 stacktrace="Traceback (most recent call last): ..."),
    RespostaErro(status=400,
                 message="Bad Request",
                 stacktrace="Traceback (most recent call last): ..."),
]

# Para criação de respostas personalizadas


def parse_openapi(responses: list = list()) -> dict:
    responses.extend(DEFAULT_RESPONSES)
    return {exemplo.status: {"content": {"application/json": {"example": exemplo.dict()}}, "model": RespostaErro}
            for exemplo in responses}


# Respostas padrão em formato JSON para rotas (sem personalização pra cada serviço)
DEFAULT_RESPONSES_JSON = parse_openapi()
