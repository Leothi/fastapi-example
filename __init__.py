import sys
import traceback
import time 
import uuid

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from loguru import logger

from full_api.rotas import mensagem, math, usuario, documentacao
from full_api.excecoes import APIException
from full_api.utils.logging_utils import DEFAULT_FORMAT, log_request
from full_api.modelos import DEFAULT_RESPONSES_JSON


logger.configure(
    handlers=[
        {
        "sink": sys.stdout,
        "level": 38,
        "format": DEFAULT_FORMAT 
        }
    ]
)

logger.level('REQUEST RECEBIDA', no=38, color="<yellow>")
logger.level('REQUEST FINALIZADA', no=39, color="<yellow>")
logger.level('REQUEST ROTA', no=40, color="<light-green>")

logger.add("./full_api/teste.log", format=DEFAULT_FORMAT)

app = FastAPI(title='API de teste')


app.include_router(mensagem.router, prefix='/mensagem',
                   tags=['Mensagem'], responses={**DEFAULT_RESPONSES_JSON})
app.include_router(math.router, prefix='/math',
                   tags=['Matemática'], responses={**DEFAULT_RESPONSES_JSON})
app.include_router(usuario.router, prefix='/usuario',
                   tags=['Usuário'], responses={**DEFAULT_RESPONSES_JSON})
app.include_router(documentacao.router)

# Substituição/criação das exceptions
@app.exception_handler(HTTPException)
async def http_excep(requisicao: Request, exc: HTTPException):
    mensagem = {404: "Não encontrado", 500: "Erro interno", 400: "Bad Request"}
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "mensagem": mensagem[exc.status_code],
            "traceback": traceback.format_exc()
        }        
    )

@app.exception_handler(APIException)
async def camara_exception_handler(requisicao: Request, excecao: APIException):
    return JSONResponse(
        status_code=excecao.status_code,
        content={
            "status": excecao.status_code,
            "mensagem": excecao.mensagem,
            "traceback": traceback.format_exc()
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(requisicao: Request, excecao: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "status": 422,
            "mensagem": "Campo de requisição inválido",
            "traceback": traceback.format_exc()
        }
    )


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id = str(uuid.uuid1())

    log_request("REQUEST RECEBIDA", request.method, id, request.client.host, request.url.path)
    start_time = time.time()
    response = await call_next(request)
    process_time = round(time.time() - start_time, 10)

    log_request("REQUEST FINALIZADA", request.method, id, request.client.host, request.url.path, process_time)
    response.headers["X-Process-Time"] = str("process_time")

    return response
 
