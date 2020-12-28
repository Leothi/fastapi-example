from loguru import logger

from api.database.default.sql_alchemy.connector import Connector
from api.database.default.mongo.usuario import UsuarioMongoDatabase
from api.database.default.sql_alchemy.usuario import UsuarioSQLDatabase


def list_(skip: int = 0, limit: int = None, count: bool = False):
    """Lista todos os documentos do banco.

    :param skip: Valor inicial, defaults to 0
    :type skip: int, optional
    :param limit: Valor final, defaults to None
    :type limit: int, optional
    :param count: Contagem de todos os documentos, defaults to False
    :type count: bool, optional
    :return: Contagem de todas as inserções ou as inserções em si
    :rtype: int ou list
    """    
    with UsuarioMongoDatabase() as db:
        logger.info("Realizando listagem do banco de dados.")
        result = db.list_(skip, limit, count)
    return result


def search(insertion_id: str) -> dict:
    """Realiza busca no banco de dados a partir do id de inserção.

    :param insertion_id: Id de inserção.
    :type insertion_id: str
    :return: JSON com resultado.
    :rtype: dict
    """
    with UsuarioMongoDatabase() as db:
        logger.info("Realizando busca no banco de dados.")
        result = db.search(insertion_id)
    return result


def insert(name: str, job: str, password: str) -> str:
    """Insere um usuário no banco de dados.

    :param name: Nome do usuário.
    :type name: str
    :param job: Emprego do usuário.
    :type job: str
    :param password: Senha do usuário
    :type password: str
    :return: Id de inserção no banco.
    :rtype: str
    """
    with UsuarioMongoDatabase() as db:
        logger.info("Realizando insercao no banco de dados.")
        insertion_id = db.insert(name, job, password)
    return insertion_id


def insert_sql(name: str, job: str, password: str) -> str:
    """Insere um usuário no banco de dados.

    :param name: Nome do usuário.
    :type name: str
    :param job: Emprego do usuário.
    :type job: str
    :param password: Senha do usuário
    :type password: str
    :return: Id de inserção no banco.
    :rtype: str
    """
    with Connector() as connection:
        logger.info("Realizando insercao no banco de dados.")
        usuario = UsuarioSQLDatabase(NAME=name, JOB=job, PW=password)
        usuario.insert(connection)

        resultado = usuario.to_dict()
    return resultado
