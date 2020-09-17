from pydantic import BaseModel, Field
from typing import Optional

# Mensagem de sucesso genéricas padrão


class RespostaSucesso(BaseModel):
    mensagem = "Processado com sucesso."
    mensagem: str = Field(mensagem,
                          example=mensagem)


class RespostaErro(BaseModel):
    status: int = Field(..., description="Código da mensagem")
    message: str = Field(..., description="Detalhes da mensagem")
    stacktrace: Optional[str] = Field("", description="Stacktrace do erro")


# Mensagens específicas de erro
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


def parse_openapi(responses: list = list()) -> dict:
    responses.extend(DEFAULT_RESPONSES)
    return {exemplo.status: {"content": {"application/json": {"example": exemplo.dict()}}, "model": RespostaErro}
            for exemplo in responses}


DEFAULT_RESPONSES_JSON = parse_openapi()
