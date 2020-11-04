from pydantic import Field

from full_api.modelos import RespostaSucesso

# Validação (de json) de campos e construção do Schema no Swagger
# ... Significa obrigatório (required)


class MensagemResponse(RespostaSucesso):
    mensagem_out: str = Field(...,
                              description="Mensagem em upper case.", example="STRING")
