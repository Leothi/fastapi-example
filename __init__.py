import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from full_api.routes import mensagem, math, usuario, documentacao
from full_api.utils.logger import DEFAULT_FORMAT
from full_api.models import DEFAULT_RESPONSES_JSON
from full_api.modules.middleware import Middleware
from full_api.exceptions import ExceptionHandler

__version__ = '1.0.0'

# Configuração do Logger
logger.configure(
    handlers=[
        {
            "sink": sys.stdout,
            "level": 10,
            "format": DEFAULT_FORMAT
        }
    ]
)

# Criação de Levels
logger.level('REQUEST RECEBIDA', no=37, color="<yellow>")
logger.level('REQUEST FINALIZADA', no=38, color="<yellow>")
logger.level('LOG ROTA', no=39, color="<light-green>")

# Saída para arquivo logger
logger.add("./full_api/teste.log", level=0, format=DEFAULT_FORMAT, rotation='500 MB')
logger.add("./full_api/teste_error.log", level=40, format=DEFAULT_FORMAT, rotation='500 MB')

# Instância API
app = FastAPI(title='API de teste', description="Api para treinamento de FastAPI",
              version=__version__)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(mensagem.router, prefix='/mensagem',
                   tags=['Mensagem'], responses={**DEFAULT_RESPONSES_JSON})
app.include_router(math.router, prefix='/math',
                   tags=['Matemática'], responses={**DEFAULT_RESPONSES_JSON})
app.include_router(usuario.router, prefix='/usuario',
                   tags=['Usuário'], responses={**DEFAULT_RESPONSES_JSON})
app.include_router(documentacao.router)

# Módulos da API
Middleware(app)
ExceptionHandler(app)
