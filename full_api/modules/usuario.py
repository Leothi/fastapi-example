from loguru import logger

from full_api.database.default.sql_alchemy.connector import Connector
from full_api.database.default.mongo.usuario import UsuarioMongoDatabase
from full_api.database.default.sql_alchemy.usuario import UsuarioSQLDatabase


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
