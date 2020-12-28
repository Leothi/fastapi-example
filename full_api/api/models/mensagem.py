from pydantic import Field

from api.models import SuccessResponse

# Validação (de json) de campos e construção do Schema no Swagger
# ... Significa obrigatório (required)


class MensagemResponse(SuccessResponse):
    """Response model to /mensagem"""
    mensagem_out: str = Field(...,
                              description="Mensagem em upper case.", example="STRING")
