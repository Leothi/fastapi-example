from pydantic import Field

from full_api.api.models import SuccessResponse


# Validação de campos e construção do Schema no Swagger
# ... Significa obrigatório (required)
class MathResponse(SuccessResponse):
    valor: float = Field(...,
                         description="Resultado da operação.", example=4.0)
