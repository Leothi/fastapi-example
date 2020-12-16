from pydantic import Field

from full_api.models import SuccessResponse

# Validação (de json) de campos e construção do Schema no Swagger
# ... Significa obrigatório (required)


class MensagemResponse(SuccessResponse):
    mensagem_out: str = Field(...,
                              description="Mensagem em upper case.", example="STRING")
