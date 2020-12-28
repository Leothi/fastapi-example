from pydantic import Field

from api.models import SuccessResponse


# Validação de campos e construção do Schema no Swagger
# ... Significa obrigatório (required)
class MathResponse(SuccessResponse):
    """Response model to /math"""
    valor: float = Field(...,
                         description="Resultado da operação.", example=4.0)
