from pydantic import Field

from full_api.models import RespostaSucesso


# Validação de campos e construção do Schema no Swagger
# ... Significa obrigatório (required)
class MathResponse(RespostaSucesso):
    valor: float = Field(...,
                         description="Resultado da operação.", example=4.0)
