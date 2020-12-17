from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException


class APIException(Exception):
    """Classe base para criação de Exceções personalizadas da API.

    :param Exception: Classe Python de Exceções.
    """

    def __init__(self, status: int, mensagem: str):
        self.status_code = status
        self.mensagem = mensagem


# Substituição/criação das exceptions
class ExceptionHandler:

    def __init__(self, app: FastAPI):
        app.exception_handler(Exception)(self.exception_handler)
        app.exception_handler(HTTPException)(self.http_excep)
        app.exception_handler(APIException)(self.camara_exception_handler)
        app.exception_handler(RequestValidationError)(self.validation_exception_handler)

    @staticmethod
    async def exception_handler(request: Request, excecao: Exception):
        return JSONResponse(
            status_code=500, content={
                "status": 500,
                "mensagem": 'Internal Server Error'
            }
        )

    @staticmethod
    async def http_excep(requisicao: Request, excecao: HTTPException):
        mensagem = {404: "Não encontrado", 500: "Erro interno", 400: "Bad Request"}
        return JSONResponse(
            status_code=excecao.status_code,
            content={
                "status": excecao.status_code,
                "mensagem": mensagem[excecao.status_code]
            }
        )

    @staticmethod
    async def camara_exception_handler(requisicao: Request, excecao: APIException):
        return JSONResponse(
            status_code=excecao.status_code,
            content={
                "status": excecao.status_code,
                "mensagem": excecao.mensagem
            }
        )

    @staticmethod
    async def validation_exception_handler(requisicao: Request, excecao: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={
                "status": 422,
                "mensagem": "Parâmetros da requisição inválidos!",
                "details": str(excecao)
            }
        )
