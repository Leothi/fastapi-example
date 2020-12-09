from datetime import datetime

from full_api.database import MongoDatabase
from full_api.settings import envs


class UsuarioDatabase(MongoDatabase):
    """Classe banco de dados para Usuário

    :param MongoDatabase: Classe base do banco.
    :type MongoDatabase: class
    """    
    def __init__(self):
        super().__init__(envs.COLLECTION_USER)

    def search(self, id: str) -> dict:
        """Busca um usuário no banco.

        :param id: Id da operação no banco de dados.
        :type id: str
        :return: Dicionário contendo resultado da busca.
        :rtype: dict
        """
        result = self.collection.find_one({'_id': self.str_to_objectid(id)}) or {}
        if result:
            result = self.objectid_dict_to_str(result)
        return result

    def insert(self, name: str, job: str, password: str) -> str:
        """Insere um usuário no banco de dados.

        :param name: Nome do usuário.
        :type name: str
        :param job: Emprego do usuário.
        :type job: str
        :param password: Senha do usuário.
        :type password: str
        :return: Id da operação no banco.
        :rtype: str
        """        
        document = {
            "name": name,
            "job": job,
            "password": password,
            'created_date': datetime.utcnow(),
            'updated_date': datetime.utcnow()
        }
        result = self.collection.insert_one(document)
        return self.objectid_to_str(result.inserted_id)
